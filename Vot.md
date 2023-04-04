import telebot


bot = telebot.TeleBot('6097683861:AAGo4dADxVeYlrHelXe6s60p3TrxVN8BKQU')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, {message.from_user.first_name} {message.from_user.last_name}'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['help'])
def help(message):
    mess = "Вот что я могу:\n" \
           "/start - приветствие"
    bot.send_message(message.chat.id, mess, parse_mode='html')


bot.polling(none_stop=True)
