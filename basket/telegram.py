import telebot

# Функція відправки повідомлення телеграм-ботом
def send_message_tg(bot_token, chatid, message):
    # Створення об'єкту бота з використанням bot_token
    bot = telebot.TeleBot(bot_token)
    # Відправка повідомлення в чат, ідентифікатор якого заданий в chatid
    bot.send_message(chatid, message)
