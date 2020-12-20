import telebot

bot = telebot.TeleBot("1447120422:AAHNBv0chlIqVeKh6JKCVeD43Hb6yD1PJaY")


@bot.message_handler(content_types=['text'])
def send_text(message):
    if 'Назик ' in message.text:
        bot.send_message(message.chat.id, 'Анус бомжа @Kabanchik35')
    elif 'Назар' in message.text:
        bot.send_message(message.chat.id, 'Пидрила йобаная @Kabanchik35')
    elif 'газик' in message.text:
        bot.send_message(message.chat.id, 'Кибер писюн @Kabanchik35')
    elif 'назик' in message.text:
        bot.send_message(message.chat.id, 'вїбав гавна @Kabanchik35')
    elif 'У назара' in message.text:
        bot.send_message(message.chat.id, 'анал вместо шара @Kabanchik35')


bot.polling(none_stop=True)