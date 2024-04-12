import datetime
import telebot
from telebot import types
import os
import vk_api
from vk_api import VkUpload
import smtplib
from datetime import datetime
import sqlite3
from email.message import EmailMessage
from config import (dict_questions, dict_date_of_birth, TOKEN, TOKEN_VK, about_prog, intro_zoroastri,
                    quize_result, intro, dict_zoroastri, passw_external_app, from_email)


bot = telebot.TeleBot(TOKEN)
user_data = {}
check = 0  # Проверка первичного запуска бота
photo_path = ''
caption = ''
result_quiz: int = 0 # проверяем в базе данных пользователя, если есть присваиваем  результат викторины

@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
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
        analytics_bot(flag=0)
        choice_database(user_id, message=message)
        bot.send_video(message.chat.id, file_logo, None, 'Text')
        text = (f'✋ Привет *{first_name}*! Добро пожаловать в наш телеграмм-бот! \n\n{intro}')
    else:
        text = ('Выберите нужный пункт меню 👇')
    bot.send_message(chat_id, text, parse_mode='Markdown', reply_markup=markup)

@bot.message_handler(commands=['stop'])
def stop(message): #Функция которая происходит по команде /stop
    global check
    bot.send_message(message.chat.id,'📵 Бот остановлен. Для запуска бота введите команду /start',
                     reply_markup=types.ReplyKeyboardRemove())
    check = 0


@bot.message_handler(content_types=['text'])
def quize(message: telebot.types.Message):
    chat_id = message.chat.id
    global check
    if message.text == '❓Викторина':
        analytics_bot(flag=0) # Счетчик обращений. Плюсуем 1 к параметру в базе.
        already_passed(chat_id)

    elif message.text == '📒 По году рождения':
        msg = bot.send_message(message.chat.id, f'{intro_zoroastri}\n\nВведите год вашего рождения \n\n\
👉 *Например: 1978*', parse_mode='Markdown')
        analytics_bot(flag=2)
        bot.register_next_step_handler(msg, totem_year)

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
        question_text = f"🤖 Выберите диапазон вашего дня рождения."
        bot.send_message(chat_id, question_text, reply_markup=inline_db)
        analytics_bot(flag=1)

    elif message.text == 'Программа «Возьми животное под опеку»':
        analytics_bot(flag=3)
        inline_markup = types.InlineKeyboardMarkup(row_width=True)
        inline_prog = types.InlineKeyboardButton('▶️ Подробнее о программе', url='https://moscowzoo.ru/my-zoo/become-a-guardian')
        inline_site = types.InlineKeyboardButton('▶️ Наш сайт', url='https://moscowzoo.ru')
        inline_vk = types.InlineKeyboardButton('▶️ Мы в Telegram', url='https://t.me/Moscowzoo_official')
        inline_tg = types.InlineKeyboardButton('▶️ Мы в VK', url='https://vk.com/moscow_zoo')
        inline_feedback = types.InlineKeyboardButton('✍️ Оставьте ваш отзыв', callback_data='feedback')
        inline_markup.add(inline_prog, inline_site, inline_tg, inline_vk, inline_feedback)
        bot.send_message(message.chat.id, f'{about_prog}', parse_mode='Markdown', reply_markup=inline_markup)

    elif message.text == 'stop' or message.text =='Stop' or message.text == 'стоп' or message.text =='Стоп':
        bot.send_message(message.chat.id, '☝️ Если вы хотите остановить бот, введите команду /stop')

    elif message.text == 'stat':
        text = f"💡 Меню администратора\n\n🖥️ *Статистика бота:*\n- количество активных пользователей\n\
- количество новых подписчиков\n-максимальный, средний, минимальный возраст подписчиков\n\
- сколько раз вызывался каждый пункт меню.твызовов меню бота по датам.\n\n\
📅 Введите дату для формирования аналитики.\n Формат даты (гггг-мм-дд). *Например: 2024-04-10*"

        msg = bot.send_message(chat_id, text, parse_mode='Markdown')
        bot.register_next_step_handler(msg, generating_statistics)

    else:
        bot.send_message(message.chat.id, 'Моя твоя не понимать! 🤷‍♀️', parse_mode='Markdown')
        check = 1
        start(message)
        
def totem_year(message):
    global check
    check = 1
    flag = 0
    chat_id = message.chat.id

    if message.text.isdigit():
        result_temp = int(message.text)

        if abs(result_temp) < 1906:
            now_year = str(datetime.datetime.now())[:4]
            text = f'😜 Вы мстите государству за пенсионную реформу или вам действительно {int(now_year)-result_temp}?'
            bot.send_message(chat_id, text)

        else:
            while flag == 0:
                for key in dict_zoroastri.keys():
                    if result_temp == int(key):
                        with open(f'animals/{dict_zoroastri[key][1]}', 'rb') as photo:
                            bot.send_photo(chat_id, photo, caption=f"{dict_zoroastri[key][0]}",
                                           parse_mode="Markdown")
                        flag = 1
                        choice_database(chat_id, 2, int(message.text), message=message)
                        break
                result_temp -= 32
    else:
        text = f'Возможно, в каком-то летоисчислении это и является годом, но только не в земном.\n\n Напишите цифрами. 🔢'
        bot.send_message(chat_id, text)

    start(message)


def already_passed(chat_id):
    """Проверяем по базе результатов, проходил ли пользователь викторину.
        Если 'ДА', отправляем прошлый результат и спрашиваем о повторном прохождении 'ДА / НЕТ'
        Если 'НЕТ' запускаем викторину.  """
    if result_quiz != 0:
        for i in quize_result.keys():
            if quize_result[i][0][0] <= result_quiz <= quize_result[i][0][1]:
                menu_quiz = types.InlineKeyboardMarkup(row_width=2)
                button_yes = types.InlineKeyboardButton('✅ Да', callback_data='yes')
                button_no = types.InlineKeyboardButton('❌ Нет', callback_data='no')
                menu_quiz.add(button_yes, button_no)
                text = f'Вы уже проходили викторину! \n{quize_result[i][1]} \n\n 👉 *Хотите пройти викторину еще раз?*'
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
                                                            'bd7', 'bd8', 'bd9', 'bd10', 'bd11', 'bd12', 'in_VK',
                                                            'in_m', 'feedback', 'stat_menu'])
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
            msg = bot.send_message(chat_id, '📧 Ваш электронный адрес')
            bot.register_next_step_handler(msg, send_email)

        if call.data == 'feedback':
            msg = bot.send_message(chat_id, 'Напишите ваш отзыв. Это очень важно для нас. 🫶')
            bot.register_next_step_handler(msg, send_feedback)


def send_msg_date_of_birth(chat_id: str, dict_key: str):
    chat_d = chat_id
    '''Отправка фото с текстом. Меню "По дате рождения'''
    inline_send = types.InlineKeyboardMarkup(row_width=True)
    inline_send.add(types.InlineKeyboardButton('📩 Отправить на почту Московского зоопарка', callback_data='in_m'),
                             types.InlineKeyboardButton('💻 Отправить в ВК', callback_data='in_VK'))
    global photo_path, caption
    photo_path = f'animals/{dict_date_of_birth[dict_key][1]}'
    caption = f"👉 {dict_date_of_birth[dict_key][0]}"

    # choice_database(chat_id, 3, 0, dict_key, message=chat_id)
    with open(photo_path, 'rb') as photo:
        bot.send_photo(chat_id, photo, caption=caption, parse_mode="Markdown", reply_markup=inline_send)


@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    """Обработчик ответов викторины"""
    global result_quiz
    chat_id = call.message.chat.id
    # user_id = call.message.from_user.id
    # print('user в обработке', user_id)
    #
    # print('call ', call.message)
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
                        bot.send_photo(chat_id, photo, caption=f"Викторина окончена❗ \n{quize_result[i][1]}", parse_mode="Markdown")

                # поиск в базе результатов ID. Делаем новую запись или обновляем старый результат.

                result_quiz = int(''.join(map(str, {user_info['score']})))
                choice_database(chat_id, 1, message=call.message)

            # Можно сбросить данные пользователя, если викторина окончена
            if chat_id in user_data:
                del user_data[chat_id]


def generating_statistics(message):
    '''Формирование статистики по работе бота. Статистика формируется на конкретный день, который запросил администратор.
    Формат ввода даты проверяется.'''
    now_year = int(datetime.now().strftime("%Y")) # текущий год
    connection = sqlite3.connect('analytics_data.db')
    cursor = connection.cursor()

    try:
        datetime.strptime(message.text, "%Y-%m-%d")
        cursor.execute('SELECT * FROM Data WHERE date = ?', (message.text,))
        quantity = cursor.fetchone()

        cursor.execute('SELECT * FROM Data WHERE date = ?', (message.text,))
        # Новые подписчики за конкретный день
        new_users = cursor.fetchone()[5]

        connection.commit()
        connection.close()

        if quantity:
            amount = quantity[1] + quantity[2] + quantity[3] + quantity[4]    #

            connection = sqlite3.connect('database.db')
            cursor = connection.cursor()
            cursor.execute('SELECT COUNT(*) FROM Users WHERE last_activity = ?', (message.text,))
            activ_user = cursor.fetchone()[0]

            # средний возраст всех подписчиков
            cursor.execute('SELECT * FROM Users')
            select_all = cursor.fetchall()
            avg_all_user = avg_func(select_all)

            # максимальный возраст всех подписчиков
            max_all_user = max(now_year - year[4] for year in select_all if year[4] != 0)

            # минимальный возраст всех подписчиков
            min_all_user = min(now_year - year[4] for year in select_all if year[4] != 0)

            # средний возраст подписчиков за конкретный день
            cursor.execute('SELECT * FROM Users WHERE last_activity = ?', (message.text,))
            select_day = cursor.fetchall()
            avg_day_user = avg_func(select_day)

            # максимальный возраст подписчиков конкретного дня
            max_day_user = max(now_year - year[4] for year in select_day if year[4] != 0)

            # минимальный возраст подписчиков конкретного дня
            min_day_user = min(now_year - year[4] for year in select_day if year[4] != 0)

            text = f'📈 *Статистика за {message.text}*\n\n👨‍👧‍👦️ Активные пользователи - {activ_user}\n\
🏃‍♂️ Новые подписчики - {new_users}\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n↗️ Максимальный возраст подписчиков - {max_day_user}\n\
➡️ Средний возраст подписчиков - {avg_day_user}\n↘️ Минимальный возраст подписчиков - {min_day_user}\n\
➖➖➖➖➖➖➖➖➖➖➖➖➖\n↗️ Максимальный возраст всех подписчиков - {max_all_user}\n➡️ Средний возраст подписчиков - \
{avg_all_user}\n↘️ Минимальный возраст подписчиков - {min_all_user}\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n\
📚 *Количество открытий меню:* \n"Викторина" - {quantity[1]}\n\"По дате рождения" - {quantity[2]}\n"По году рождения" - \
{quantity[3]}\n\"Программа «Возьми животное под опеку»" - {quantity[4]}\n\n * Всего взаимодействий за этот день - {amount}*'

            bot.send_message(message.chat.id, text, parse_mode='Markdown')


        else:
            bot.send_message(message.chat.id, f'❗ *Данных статистики на эту дату нет.*', parse_mode='Markdown')
    except ValueError:
        bot.send_message(message.chat.id, f'❗ *Вы ввели некоректный формат даты.*', parse_mode='Markdown')


def avg_func(avg_all_user):
    now_year = int(datetime.now().strftime("%Y"))
    t = sum(now_year - year[4] for year in avg_all_user if year[4] > 0)
    count = sum(1 for year in avg_all_user if year[4] != 0)
    avg = t / count
    return round(avg)


def analytics_bot(flag=0):
    '''Собираем статистику по пунктам меню
            flag = 0 - статистика по викторине
            flag = 1 - статистика теста "По дате"
            flag = 2 - статистика теста "По году"
            flag = 3 - статистика пункта меню "Программа "'''

    last_activity = datetime.now().strftime("%Y-%m-%d")
    # Устанавливаем соединение с базой данных
    connection = sqlite3.connect('analytics_data.db')
    cursor = connection.cursor()
    # Создаем таблицу Users
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Data (
        date TEXT PRIMARY KEY,
        quiz_quantity INTEGER,
        date_quantity INTEGER,
        year_quantity INTEGER,
        prog_quantity INTEGER,
        new_users INTEGER
        )
        ''')

    cursor.execute('SELECT * FROM Data')
    dates = cursor.fetchall()
    for date in dates: # Если нет статистики текущего дня, добавляется текущая дата.
        if last_activity == date[0]:
            quiz_st = date[1]
            date_st = date[2]
            year_st = date[3]
            prog_st = date[4]
            new_users = date[5]
            break
    else:
        quiz_st = 0
        date_st = 0
        year_st = 0
        new_users = 0
        cursor.execute('INSERT INTO Data (date, quiz_quantity, date_quantity, year_quantity, prog_quantity, new_users) VALUES (?, ?, ?, ?, ?, ?)',
                       (last_activity, 0, 0, 0, 0, 0))


    if flag == 0:  # Поиск пользователя в базе и сохранение последнего результата по викторине
        cursor.execute('UPDATE Data SET quiz_quantity = ?  WHERE date = ?',
                       (quiz_st + 1, last_activity))

    elif flag == 1:
        pass
        cursor.execute('UPDATE Data SET date_quantity = ?  WHERE date = ?',
                       (date_st + 1, last_activity))

    elif flag == 2:
        cursor.execute('UPDATE Data SET year_quantity = ?  WHERE date = ?',
                       (year_st+1, last_activity))

    elif flag == 3:
        cursor.execute('UPDATE Data SET prog_quantity = ?  WHERE date = ?',
                       (prog_st+1, last_activity))
    # Сохраняем изменения и закрываем соединение
    connection.commit()
    connection.close()


# Посмотреть все вхождения user_id. В старте его нет
def choice_database(user_id, val=0, result_year=0, result_date='', message=None):
    first_name = message.chat.first_name
    user_id = message.chat.id

    """ переменная val 0 - первоначальная проверка user в базе данных
                   val 1 - изменение результатов викторины
                   val 2 - изменение года рождения
                   val 3 - изменение даты рождения
    """
    global result_quiz
    last_activity = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Устанавливаем соединение с базой данных
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    # Создаем таблицу Users
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    last_activity TEXT NOT NULL,
    result_quiz INTEGER,
    result_date TEXT NOT NULL,
    result_year TEXT NOT NULL,
    first_name TEXT NOT NULL
    )
    ''')
    if val == 0: # Поиск пользователя в базе и сохранение последнего результата по викторине
        try:
            cursor.execute('SELECT result_quiz, id FROM Users WHERE id = ?', (user_id,))
            results = cursor.fetchone()
            result_quiz = results[0]
        except Exception as e:
            # Если пользователя нет, добавляем его в базу
            cursor.execute('INSERT INTO Users (id, last_activity, result_quiz, result_date, result_year, first_name) VALUES (?, ?, ?, ?, ?, ?)', (user_id, last_activity, 0, ' ', 0, first_name))
            result_quiz = 0
            add_amount_new_user()

    elif val == 1:
        cursor.execute('UPDATE Users SET result_quiz = ?, last_activity = ? WHERE id = ?',
                       (result_quiz, last_activity, user_id))


    elif val == 2:
        cursor.execute('UPDATE Users SET result_year = ?, last_activity = ? WHERE id = ?',
                        (result_year, last_activity, user_id))

    elif val ==3:
        cursor.execute('UPDATE Users SET result_date = ?, last_activity = ? WHERE id = ?',
                        (result_date, last_activity, user_id))
    # Сохраняем изменения и закрываем соединение
    connection.commit()
    connection.close()


def add_amount_new_user():
    """Добавляем нового пользователя к счетчику вновь подписавшихся за текущий день"""
    last_activ = datetime.now().strftime("%Y-%m-%d")
    connection = sqlite3.connect('analytics_data.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Data WHERE date = ?', (last_activ,))
    new_users = cursor.fetchone()[5]
    cursor.execute('UPDATE Data SET new_users = ?  WHERE date = ?',
                   (new_users + 1, last_activ))
    connection.commit()
    connection.close()


def send_feedback(message):
    user_id = message.from_user.id
    '''Сохранение отзыва в файл feedback.txt в формате <user_id>, <feedback>'''
    global check
    with open('feedback.txt', "a", encoding="utf-8") as file:
         feed = f'{user_id}, {message.text}\n'
         file.write(feed)
    check = 1
    start(message)

def send_email(message):
    ''' Фугкция для отправки результата теста на почту зоопарка.
    В настоящее время работает с логином и паролем для внешнего приложения только с моей почтой.
    Для полного функционирования требуется логин и парооль пользователя. '''
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

        bot.send_message(message.chat.id,'📨 Сообщение отправлено на почту Московского зоопарка zoofriends@moscowzoo.ru')
    except Exception as e:
        bot.send_message(message.chat.id,'⛔ Произошла ошибка при отправке сообщения. Повторите попытку')


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
