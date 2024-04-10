import datetime
import telebot
from telebot import types
import os
import vk_api
from vk_api import VkUpload
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.message import EmailMessage
from config import (dict_questions, dict_date_of_birth, TOKEN, TOKEN_VK, about_prog, intro_zoroastri,
                    quize_result, intro, dict_zoroastri, passw_external_app, from_email)


bot = telebot.TeleBot(TOKEN)
user_data = {}
check = 0  # Проверка первичного запуска бота
photo_path = ''
caption = ''

@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    chat_id = message.chat.id
    first_name = message.chat.first_name
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard = types.KeyboardButton(text='❓Викторина')
    keyboard1 = types.KeyboardButton(text='🗓️ По дате рождения')
    keyboard2 = types.KeyboardButton(text='📒 По году рождения')
    keyboard3 = types.KeyboardButton(text='Программа «Возьми животное под опеку»')
    markup.add(keyboard)
    markup.add(keyboard1)
    markup.add(keyboard2)
    markup.add(keyboard3)

    path = f'{os.getcwd()}\logo.gif'
    file_logo = open(path, 'rb')
    if check == 0:
        alter_result_quize(chat_id, f"{chat_id}, {'---'}")  # Записываем user в базу данных с результатом викторины '---'
        bot.send_video(message.chat.id, file_logo, None, 'Text')
        text = (f'Привет *{first_name}*! Добро пожаловать в наш телеграмм-бот! \n\n{intro}')
    else:
        text = ('Выберите нужный пункт меню 👇')
    bot.send_message(chat_id, text, parse_mode='Markdown', reply_markup=markup)

@bot.message_handler(commands=['stop'])
def stop(message): #Функция которая происходит по команде /stop
    global check
    bot.send_message(message.chat.id,'Бот остановлен. Для запуска бота введите команду /start',
                     reply_markup=types.ReplyKeyboardRemove())
    check = 0


@bot.message_handler(content_types=['text'])
def quize(message: telebot.types.Message):
    chat_id = message.chat.id
    global check
    if message.text == '❓Викторина':
        already_passed(chat_id)

    elif message.text == '📒 По году рождения':
        mesg = bot.send_message(message.chat.id, f'{intro_zoroastri}\n\nВведите год вашего рождения \n\n\
Например: 1978', parse_mode='Markdown')
        bot.register_next_step_handler(mesg, totem_year)

    elif message.text == '🗓️ По дате рождения':
        # chat_id = message.chat.id
        inline_db = types.InlineKeyboardMarkup(row_width=True)
        inline_db.add(types.InlineKeyboardButton('10 декабря - 09 января', callback_data='bd1'),
                      types.InlineKeyboardButton('10 января - 09 февраля', callback_data='bd2'),
                      types.InlineKeyboardButton('10 февраля - 09 марта', callback_data='bd3'),
                      types.InlineKeyboardButton('10 марта - 09 апреля', callback_data='bd4'),
                      types.InlineKeyboardButton('10 апреля - 09 мая', callback_data='bd5'),
                      types.InlineKeyboardButton('10 мая - 09 июня', callback_data='bd6'),
                      types.InlineKeyboardButton('10 июня - 09 июля', callback_data='bd7'),
                      types.InlineKeyboardButton('10 июля - 09 августа', callback_data='bd8'),
                      types.InlineKeyboardButton('10 августа - 09 сентября', callback_data='bd9'),
                      types.InlineKeyboardButton('10 сентября - 09 октября', callback_data='bd10'),
                      types.InlineKeyboardButton('10 октября - 09 ноября', callback_data='bd11'),
                      types.InlineKeyboardButton('10 ноября - 09 декабря', callback_data='bd12'))
        question_text = f"Выберите диапазон вашего дня рождения."
        bot.send_message(chat_id, question_text, reply_markup=inline_db)

    elif message.text == 'Программа «Возьми животное под опеку»':
        inline_markup = types.InlineKeyboardMarkup(row_width=True)
        inline_prog = types.InlineKeyboardButton('▶️ Подробнее о программе', url='https://moscowzoo.ru/my-zoo/become-a-guardian')
        inline_site = types.InlineKeyboardButton('▶️ Наш сайт', url='https://moscowzoo.ru')
        inline_vk = types.InlineKeyboardButton('▶️ Мы в Telegram', url='https://t.me/Moscowzoo_official')
        inline_tg = types.InlineKeyboardButton('▶️ Мы в VK', url='https://vk.com/moscow_zoo')
        inline_feedback = types.InlineKeyboardButton('▶️ Оставьте ваш отзыв ', callback_data='feedback')
        inline_markup.add(inline_prog, inline_site, inline_tg, inline_vk, inline_feedback)
        bot.send_message(message.chat.id, f'{about_prog}', parse_mode='Markdown', reply_markup=inline_markup)

    elif message.text == 'stop' or message.text =='Stop' or message.text == 'стоп' or message.text =='Стоп':
        bot.send_message(message.chat.id, 'Если вы хотите остановить бот, введите команду /stop')

    else:
        bot.send_message(message.chat.id, 'Моя твоя не понимать!', parse_mode='Markdown')
        check = 1
        start(message)
def totem_year(message):
    global check
    check = 1
    flag = 0
    chat_id = message.chat.id

    if message.text.isdigit():
        data = int(message.text)
        if abs(data) < 1906:
            now_year = str(datetime.datetime.now())[:4]
            text = f'Вы мстите государству за пенсионную реформу или вам действительно {int(now_year)-data}?'
            bot.send_message(chat_id, text)

        else:
            while flag == 0:
                for key in dict_zoroastri.keys():
                    if data == int(key):
                        with open(f'animals/{dict_zoroastri[key][1]}', 'rb') as photo:
                            bot.send_photo(chat_id, photo, caption=f"{dict_zoroastri[key][0]}",
                                           parse_mode="Markdown")
                        flag = 1
                        break
                data -= 32
    else:
        text = f'Возможно, в каком-то летоисчислении это и является годом, но только не в земном.\n\n Напишите цифрами.'
        bot.send_message(chat_id, text)

    start(message)


def already_passed(chat_id: str):
    """Проверяем по базе результатов, проходил ли пользователь викторину.
        Если 'ДА', отправляем прошлый результат и спрашиваем о повторном прохождении 'ДА / НЕТ'
        Если 'НЕТ' запускаем викторину.  """

    last_result = False
    with open('result_quize.txt', 'r', encoding="utf8") as file:
        for line in file:
            if line.startswith(str(chat_id)):
                last_result = line.split(',')[1]

    if last_result.isdigit():
         for i in quize_result.keys():
            if quize_result[i][0][0] <= int(last_result) <= quize_result[i][0][1]:
                menu_quiz = types.InlineKeyboardMarkup(row_width=2)
                button_yes = types.InlineKeyboardButton('Да', callback_data='yes')
                button_no = types.InlineKeyboardButton('Нет', callback_data='no')
                menu_quiz.add(button_yes, button_no)
                text = f'Вы уже проходили викторину! \n{quize_result[i][1]} \n\n *Хотите пройти викторину еще раз?*'
                bot.send_message(chat_id, text, parse_mode='Markdown', reply_markup=menu_quiz)
    else:
        user_data[chat_id] = {'current_question': 1, 'score': 0}  # Начинаем с первого вопроса и 0 баллов
        send_question(chat_id, user_data[chat_id]['current_question'])


def send_question(chat_id, question_number):
    """ Формирование меню ответов на вопрос (Меню 'Викторина')"""
    keyboard = types.InlineKeyboardMarkup(row_width=True)

    for item in dict_questions[question_number]:
        question_text = item
        for val in dict_questions[question_number][item]:
            keyboard.row(telebot.types.InlineKeyboardButton(val[0], callback_data=val[1]))

    question_text = f"Вопрос {question_number}/{len(dict_questions)}. {question_text}"
    bot.send_message(chat_id, question_text, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data in ['yes', 'no', 'bd1', 'bd2', 'bd3', 'bd4','bd5', 'bd6',
                                                            'bd7', 'bd8', 'bd9', 'bd10', 'bd11', 'bd12', 'in_VK', 'in_m', 'feedback'])
def callback_data(call):
    """ Если user уже проходил тест, показываем ему прощлый результат и спрашиваем
        хочет ли он пройти викторину еще раз"""
    chat_id = call.message.chat.id
    if call.message:
        if call.data == 'yes':
            user_data[chat_id] = {'current_question': 1, 'score': 0}  # Начинаем с первого вопроса и 0 баллов
            send_question(chat_id, user_data[chat_id]['current_question'])

        if call.data == 'no':
            global check
            check = 1
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='Выберите нужный пункт меню 👇')

        if call.data == 'bd1':
            send_msg_date_of_birth(chat_id, '10 декабря - 09 января')
        if call.data == 'bd2':
            send_msg_date_of_birth(chat_id, '10 января - 09 февраля')
        if call.data == 'bd3':
            send_msg_date_of_birth(chat_id, '10 февраля - 09 марта')
        if call.data == 'bd4':
            send_msg_date_of_birth(chat_id, '10 марта - 09 апреля')
        if call.data == 'bd5':
            send_msg_date_of_birth(chat_id, '10 апреля - 09 мая')
        if call.data == 'bd6':
            send_msg_date_of_birth(chat_id, '10 мая - 09 июня')
        if call.data == 'bd7':
            send_msg_date_of_birth(chat_id, '10 июня - 09 июля')
        if call.data == 'bd8':
            send_msg_date_of_birth(chat_id, '10 июля - 09 августа')
        if call.data == 'bd9':
            send_msg_date_of_birth(chat_id, '10 августа - 09 сентября')
        if call.data == 'bd10':
            send_msg_date_of_birth(chat_id, '10 сентября - 09 октября')
        if call.data == 'bd11':
            send_msg_date_of_birth(chat_id, '10 октября - 09 ноября')
        if call.data == 'bd12':
            send_msg_date_of_birth(chat_id, '10 ноября - 09 декабря')

        if call.data == 'in_VK':
            send_vk_to_wall(photo_path, caption)

        if call.data == 'in_m':
            mesg = bot.send_message(chat_id, 'Ваш электронный адрес')
            bot.register_next_step_handler(mesg, send_email)

        if call.data == 'feedback':
            mesg = bot.send_message(chat_id, 'Напишите ваш отзыв. Это очень важно для нас. 🫶')
            bot.register_next_step_handler(mesg, send_feedback)




def send_msg_date_of_birth(chat_id: str, dict_key: str):
    '''Отправка фото с текстом. Меню "По дате рождения'''
    inline_send = types.InlineKeyboardMarkup(row_width=True)
    inline_send.add(types.InlineKeyboardButton('Отправить на почту Московского зоопарка', callback_data='in_m'),
                             types.InlineKeyboardButton('Отправить в ВК', callback_data='in_VK'))
    global photo_path, caption
    photo_path = f'animals/{dict_date_of_birth[dict_key][1]}'
    caption = f"{dict_date_of_birth[dict_key][0]}"
    chat_id = chat_id
    with open(photo_path, 'rb') as photo:
        bot.send_photo(chat_id, photo, caption=caption, parse_mode="Markdown", reply_markup=inline_send)


@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    """Обработчик ответов викторины"""
    chat_id = call.message.chat.id
    user_info = user_data.get(chat_id, None)
    if user_info:
        current_question = user_info['current_question']
        user_info['score'] = user_info['score'] + int(call.data)  # Суммируем баллы

        # Переходим к следующему вопросу
        next_question = current_question + 1
        if next_question <= len(dict_questions):  # Если вопросы еще не закончились
            user_data[chat_id] = {'current_question': next_question, 'score': user_info['score']}
            send_question(chat_id, next_question)
        else:
            # Все вопросы заданы, выводим результат
            for i in quize_result.keys():
                if quize_result[i][0][0] < user_info['score'] < quize_result[i][0][1]:

                    with open(f'animals/{quize_result[i][2]}', 'rb') as photo:
                        bot.send_photo(chat_id, photo, caption=f"Викторина окончена! \n{quize_result[i][1]}", parse_mode="Markdown")

                # поиск в базе результатов ID. Делаем новую запись или обновляем старый результат.
                alter_result_quize(chat_id, f"{chat_id},{user_info['score']}")

            # Можно сбросить данные пользователя, если викторина окончена
            if chat_id in user_data:
                del user_data[chat_id]


def alter_result_quize(old_str: str, new_str: str, file='result_quize.txt'):
    """Проверяем юзера в базе данных результатов. Если юзера нет, добавляем в конец файла,
       если есть, переписываем результат"""
    check = 0
    with open(file, "r", encoding="utf-8") as f1, open("%s.bak" % file, "w", encoding="utf-8") as f2:
        for line in f1:
            if line.startswith(str(old_str)):
                line = line.replace(line, new_str)
                check = 1
            f2.write(line)

        if check == 0:
            f2.write('\n')
            f2.write(new_str)

    os.remove(file)
    os.rename("%s.bak" % file, file)


def send_feedback(message):
    global check
    with open('feedback.txt', "a", encoding="utf-8") as file:
         feed = f'{message.chat.id}, {message.text}\n'
         file.write(feed)
    check = 1
    start(message)

def send_email(message):
    try:
        msg = EmailMessage()
        msg['Subject'] = f'Результаты тестирования "Тотемное животное" от {message.chat.first_name}' # тема письма
        msg['From'] =from_email  # от кого
        msg['To'] = message.text  # кому
        msg.set_content(caption)

        with smtplib.SMTP('smtp.mail.ru', 587) as server:  # Specify your SMTP server
            server.starttls()
            server.login(from_email, passw_external_app)
            server.send_message(msg)

        bot.send_message(message.chat.id,'Сообщение отправлено на почту Московского зоопарка zoofriends@moscowzoo.ru')
    except Exception as e:
        bot.send_message(message.chat.id,'Произошла ошибка при отправке сообщения. Повторите попытку')


def send_vk_to_wall(photo_path, caption):
    '''Отправка результата теста в ВК. Работает только с моей стеной.'''
    vk_session = vk_api.VkApi(token=TOKEN_VK)
    caption += ('\n\n Пост был сформирован с помощью телеграмм-бота Московского зоопарка.\
Переходите в в наш телеграмм-бот и узнайте своё тотемное животное https://t.me/MoskvaZooBot')
    vk = vk_session.get_api()
    upload = VkUpload(vk_session)
    photo = upload.photo_wall(photo_path, group_id=None)
    photo_id = f"photo{photo[0]['owner_id']}_{photo[0]['id']}"
    vk.wall.post(from_group=1, attachments=photo_id, message=caption)

bot.polling(non_stop=True)
