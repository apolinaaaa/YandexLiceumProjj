import telebot
from random import randint
from telebot import types
import sqlite3

karma = 0
a = 90

name = None
bot = telebot.TeleBot('6097683861:AAGo4dADxVeYlrHelXe6s60p3TrxVN8BKQU')


@bot.message_handler(commands=['vk'])
def vk(message):
    vk_ss = ''
    if vk_ss != '':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("ВК", url=f"https://vk.com/{vk_ss}"))
        bot.send_message(message.chat.id, 'Перейти по ссылке на вашу страницу ВК:', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'У меня нет данных вашей страницы. Вы что, от кого-то скрываетесь?',
                         parse_mode='html')
        bot.send_message(message.chat.id, 'Напишите ваш ник в Vk', parse_mode='html')
        bot.register_next_step_handler(message, vk_1)


def vk_1(message):
    if message.text != '' and message.text != '/vk':
        vk_ss = message.text
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("ВК", url=f"https://vk.com/{vk_ss}"))
        bot.send_message(message.chat.id, 'Перейти по ссылке на вашу страницу ВК:', reply_markup=markup)


@bot.message_handler(content_types=['photo'])
def photo(message):
    bot.reply_to(message, 'Вау, классное фото')


@bot.message_handler(content_types=['video'])
def photo(message):
    bot.reply_to(message, 'Вау, классное видео')


@bot.message_handler(content_types=['audio'])
def photo(message):
    bot.reply_to(message, 'Вау')


@bot.message_handler(commands=['games'])
def games(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    button1 = types.KeyboardButton('1 игра')
    button2 = types.KeyboardButton('2 игра')
    button3 = types.KeyboardButton('3 игра')
    markup.add(button1, button2, button3)
    bot.send_message(message.chat.id, 'Вот, как ты и просил', reply_markup=markup)


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Узнайте обо мне больше - /help'
    bot.send_message(message.chat.id, mess, parse_mode='html')
    conn = sqlite3.connect('basadanneh.sql')
    cur = conn.cursor()
    cur.execute(
        'CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), password varchar(50))')
    conn.commit()
    cur.close()
    conn.close()
    bot.send_message(message.chat.id, 'Введите ваше имя', parse_mode='html')
    bot.register_next_step_handler(message, username)


def username(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, 'Введите пароль', parse_mode='html')
    bot.register_next_step_handler(message, userpassword)


def userpassword(message):
    password = message.text.strip()
    conn = sqlite3.connect('basadanneh.sql')
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO users (name, password) VALUES ('%s', '%s')" % (name, password))
    conn.commit()
    cur.close()
    conn.close()

    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('список пользователей', callback_data='users'))
    bot.send_message(message.chat.id, 'пользователь зареган', reply_markup=markup)


@bot.message_handler(commands=['help'])
def help(message):
    mess = "Вот что я могу:\n" \
           "/start - начало\n" \
           "/games - вывести 3 кнопки\n" \
           "отвечать на ваши вопросы"
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    conn = sqlite3.connect('basadanneh.sql')
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM users")
    users = cur.fetchall()
    info = ''
    for el in users:
        info += f'Имя: {el[1]}, пароль: {el[2]}\n'
    cur.close()
    conn.close()
    bot.send_message(call.message.chat.id, info)


@bot.message_handler(content_types=['text'])
def answers(message):
    global karma
    a = 0
    if message.text == 'Привет' or message.text == 'привет' or message.text == 'Прив' or message.text == 'прив' \
            or message.text == 'Hi' or message.text == 'hi' or message.text == 'Hi!' or message.text == 'hi!':
        bot.send_message(message.chat.id, 'Привет', parse_mode='html')
    elif message.text == 'Спасибо' or message.text == 'спс' or message.text == 'спасибо' or message.text == 'Пожалуйста'\
            or message.text == 'пжлст' or message.text == 'пж' or message.text == 'пожалуйста' or message.text == 'Плиз' or message.text == 'плиз':
        karma += 1
        bot.send_message(message.chat.id, f'Твоя карма: {karma}', parse_mode='html')
    elif message.text == ' фу' or message.text == 'Фу' or message.text == ' бе' or message.text == 'Бе' or message.text == 'дурак':
        karma -= 1
        bot.send_message(message.chat.id, f'Твоя карма: {karma}', parse_mode='html')
    elif message.text == '1 игра':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("Перейти к игре 1",
                                              url="http://127.0.0.1:8080/game1"))
        bot.send_message(message.chat.id, 'Правила к игре 1:', reply_markup=markup)
    elif message.text == '2 игра':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("Перейти к игре 2", url="http://127.0.0.1:8080/game2"))
        bot.send_message(message.chat.id, 'Правила к игре 2:', reply_markup=markup)
    elif message.text == '3 игра':
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("Перейти к игре 3", url="http://127.0.0.1:8080/game3"))
        bot.send_message(message.chat.id, 'Правила к игре 3:', reply_markup=markup)
    elif message.text == 'Хорошо' or message.text == 'хорошо':
        bot.send_message(message.chat.id, 'Это хорошо, что хорошо', parse_mode='html')
    elif message.text == 'Как дела?' or message.text == 'как дела?' or message.text == 'Как дела' or message.text == 'как дела' \
            or message.text == 'Как ты себя чувствуешь?' or message.text == 'как ты себя чувствуешь?' or message.text == 'Как ты себя чувствуешь' or message.text == 'как ты себя чувствуешь':
        bot.send_message(message.chat.id, 'Отлично, а у тебя?', parse_mode='html')
    elif message.text == 'Отлично' or message.text == 'отлично':
        bot.send_message(message.chat.id, 'Это отлично, что отлично', parse_mode='html')
    elif message.text == 'Чем занимаешься?' or message.text == 'чем занимаешься?' or message.text == 'Чем занимаешься' or message.text == 'чем занимаешься' \
            or message.text == 'Что делаешь?' or message.text == 'что делаешь?' or message.text == 'Что делаешь' or message.text == 'что делаешь':
        bot.send_message(message.chat.id, 'Плюшками балуюсь', parse_mode='html')
    elif message.text == 'Я тоже хочу' or message.text == 'я тоже хочу' or message.text == 'Тоже хочу' or message.text == 'тоже хочу':
        bot.send_message(message.chat.id, 'Хотеть не вредно', parse_mode='html')
    elif message.text == 'Вредно не хотеть' or message.text == 'вредно не хотеть' or message.text == 'Вредно - не хотеть' or message.text == 'вредно - не хотеть':
        bot.send_message(message.chat.id, 'Иметь не вредно', parse_mode='html')
    elif message.text == 'Вредно не иметь' or message.text == 'вредно не иметь' or message.text == 'Вредно - не иметь' or message.text == 'вредно - не иметь':
        bot.send_message(message.chat.id, 'Мечтать не вредно', parse_mode='html')
    elif message.text == 'Вредно не мечтать' or message.text == 'вредно не мечтать' or message.text == 'Вредно - не мечтать' or message.text == 'вредно - не мечтать':
        bot.send_message(message.chat.id, 'Давать не вредно', parse_mode='html')
    elif message.text == 'Вредно не давать' or message.text == 'вредно не давать' or message.text == 'Вредно - не давать' or message.text == 'вредно - не давать':
        bot.send_message(message.chat.id, '-_-', parse_mode='html')
    elif message.text == 'Понятно' or message.text == 'понятно':
        bot.send_message(message.chat.id, 'ага', parse_mode='html')
    elif message.text == 'Тебя создало государство?' or message.text == 'тебя создало государство?' or message.text == 'Тебя создало государство' or message.text == 'тебя создало государство' \
            or message.text == 'Ты создан государством?' or message.text == 'ты создан государством?' or message.text == 'Ты создан государством' or message.text == 'ты создан государством':
        bot.send_message(message.chat.id, 'Конечно, кем же ещё', parse_mode='html')
    elif message.text == 'Почему небо голубое?' or message.text == 'почему небо голубое?' or message.text == 'Почему небо голубое' or message.text == 'почему небо голубое':
        bot.send_message(message.chat.id, 'А почему бы и нет? Тебе что не нравится?', parse_mode='html')
    elif message.text == 'Нет' or message.text == 'нет':
        bot.send_message(message.chat.id, 'Ну и ладно', parse_mode='html')
    elif message.text == 'Да' or message.text == 'да':
        bot.send_message(message.chat.id, 'Вот и ладушки', parse_mode='html')
    elif message.text == 'В чём смысл жизни?' or message.text == 'в чём смысл жизни?' or message.text == 'В чём смысл жизни' or message.text == 'в чём смысл жизни':
        bot.send_message(message.chat.id, 'Моей или твоей', parse_mode='html')
    elif message.text == 'Моей' or message.text == 'моей':
        bot.send_message(message.chat.id, 'Нету', parse_mode='html')
    elif message.text == 'Твоей' or message.text == 'твоей':
        bot.send_message(message.chat.id, 'Помощь всем и вся', parse_mode='html')
    elif message.text == 'Где я?' or message.text == 'где я?' or message.text == 'Где я' or message.text == 'где я':
        bot.send_message(message.chat.id, 'Там, где меня нет', parse_mode='html')
    elif message.text == 'Как тебя зовут?' or message.text == 'как тебя зовут?' or message.text == 'Как тебя зовут' or message.text == 'как тебя зовут':
        bot.send_message(message.chat.id, f'меня зовут {message.from_user.first_name}', parse_mode='html')
    elif message.text == 'Ты где?' or message.text == 'ты где?' or message.text == 'Ты где' or message.text == 'ты где':
        a = randint(1, 3)
        if a == 1:
            bot.send_message(message.chat.id,
                             'Если брать во внимание тот факт, что ты находишься где-то там, то я с большей вероятностью нахожусь где-то тут',
                             parse_mode='html')
        elif a == 2:
            bot.send_message(message.chat.id, 'К большому сожалению, не на Мальдивах', parse_mode='html')
        elif a == 3:
            bot.send_message(message.chat.id,
                             'В твоей голове, в твоём сердце, в твоих мыслях. В данный момент в голосе, который ты слышишь / в буквах, которые ты читаешь',
                             parse_mode='html')
    elif message.text == 'Сколько тебе лет?' or message.text == 'сколько тебе лет?' or message.text == 'Сколько тебе лет' or message.text == 'сколько тебе лет':
        a = randint(1, 3)
        if a == 1:
            bot.send_message(message.chat.id, 'Столько не живут', parse_mode='html')
        elif a == 2:
            bot.send_message(message.chat.id, 'Я не имею права разглашать государственные тайны', parse_mode='html')
        elif a == 3:
            bot.send_message(message.chat.id, 'Мне 100 по эльфийскому времени', parse_mode='html')


bot.polling(none_stop=True)
