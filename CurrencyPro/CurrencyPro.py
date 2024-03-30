import telebot
from telebot import types
from config import keys, TOKEN
from extensions import CryptoConverter, ConvertionExeption

bot = telebot.TeleBot(TOKEN)
ch = 0
@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    chat_id = message.chat.id
    first_name = message.chat.first_name
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard = types.KeyboardButton(text='🤑 Список валют')
    keyboard2 = types.KeyboardButton(text='❓ Помощь')
    markup.add(keyboard, keyboard2)
    if ch == 0:
        bot.send_message(chat_id, f"Привет {first_name} !")
        text = ('Чтобы начать работу введите команду в слудеющем формате: \n*<код валюты> \
<в какую валюту перевести> <количество первой валюты>* \n*Пример запроса: RUB USD 10* \
\nСписок доступных валют - кнопка *"Список валют"*')
    else:
        text = ('Введите следующий запрос:')
    bot.send_message(chat_id, text, parse_mode='Markdown', reply_markup=markup)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = '*Доступные валюты:*'
    for key, item in keys.items():
        text = '\n'.join((text, f'{item[1]} {key} - {item[0]}'))
    text += '\n------------------------------ \n*Пример запроса: RUB USD 10*'
    bot.send_message(message.chat.id, text, parse_mode="Markdown")


@bot.message_handler(content_types=['text'])
def converter(message: telebot.types.Message):
    global ch
    ch = 1

    if message.text == '🤑 Список валют':
        values(message)
        return
    if message.text == '❓ Помощь':
        text = ('Чтобы начать работу введите команду в слудеющем формате: \n*<код валюты> \
<в какую валюту перевести> <количество первой валюты>* \n*Пример запроса: RUB USD 10* \
\nСписок доступных валют - кнопка *"Список валют"*')

        bot.send_message(message.chat.id, text, parse_mode="Markdown")
        return

    try:
        ask = message.text.upper().split(' ')
        if len(ask) != 3:
            raise ConvertionExeption('Количество входных параметров не соответствует')

        quote, base, amoute = ask
        total = CryptoConverter.get_price(quote, base, amoute)

    except ConvertionExeption as e:
        bot.reply_to(message, f'Ошибка пользователя \n{e}')
        start(message)
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду \n{e}')
        start(message)
    else:
        text = f'Курс: {amoute} {keys[quote][1]}{quote} = {total * abs(float(amoute))} {keys[base][1]}{base}'
        bot.reply_to(message, text)
        start(message)


bot.polling(non_stop=True)
