import telebot
from random import randint

bot = telebot.TeleBot('6097683861:AAGo4dADxVeYlrHelXe6s60p3TrxVN8BKQU')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Узнайте обо мне больше - /help'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['help'])
def help(message):
    mess = "Вот что я могу:\n" \
           "/start - начало\n" \
           "отвечать на ваши вопросы"
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(content_types=['text'])
def answers(message):
    a = 0
    if message.text == 'Привет' or message.text == 'привет' or message.text == 'Прив' or message.text == 'прив' \
            or message.text == 'Hi' or message.text == 'hi' or message.text == 'Hi!' or message.text == 'hi!':
        bot.send_message(message.chat.id, 'Привет', parse_mode='html')
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
            bot.send_message(message.chat.id, 'Если брать во внимание тот факт, что ты находишься где-то там, то я с большей вероятностью нахожусь где-то тут', parse_mode='html')
        elif a == 2:
            bot.send_message(message.chat.id, 'К большому сожалению, не на Мальдивах', parse_mode='html')
        elif a == 3:
            bot.send_message(message.chat.id, 'В твоей голове, в твоём сердце, в твоих мыслях. В данный момент в голосе, который ты слышишь / в буквах, которые ты читаешь', parse_mode='html')
    elif message.text == 'Сколько тебе лет?' or message.text == 'сколько тебе лет?' or message.text == 'Сколько тебе лет' or message.text == 'сколько тебе лет':
        a = randint(1, 3)
        if a == 1:
            bot.send_message(message.chat.id, 'Столько не живут', parse_mode='html')
        elif a == 2:
            bot.send_message(message.chat.id, 'Я не имею права разглашать государственные тайны', parse_mode='html')
        elif a == 3:
            bot.send_message(message.chat.id, 'Мне 100 по эльфийскому времени', parse_mode='html')
    else:
        bot.send_message(message.chat.id, "<b>Моя твоя не понимать</b>", parse_mode='html')


bot.polling(none_stop=True)
