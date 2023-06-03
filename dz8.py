#П.1 Напишите бота для техподдержки. Бот должен записывать обращения пользователей в файл.
#П.2 Напишите программу, которая позволяет считывать из файла вопрос, отвечать на него и отправлять ответ обратно пользователю.

import telebot
import requests
import time
def Zadazha12():
    bot = telebot.TeleBot("")

    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(message):
        bot.reply_to(message, "Привет, как ты?")

    @bot.message_handler(content_types=['text'])
    def text_message(message):
        #print(message)
        data = open('fileBot.txt', mode='a', encoding='utf-8')
        text = f'{message.from_user.first_name} {message.from_user.last_name}: {message.text}\n'
        data.write(text)
        data.close()
        if message.text == 'Хочу есть':
            data = open('IdRegistration.txt', mode='r', encoding='utf-8')
            id_list = data.readlines()
            data.close()
            id_list = list(el[:-1] for el in id_list)
            if str(message.from_user.id) not in id_list:
                data = open('IdRegistration.txt', mode='a', encoding='utf-8')
                data.write(f'{message.from_user.id}\n')
                data.close()
                bot.reply_to(message, 'Если нужна ближайшая столовая, то ищи ее на карте')
            else:
                bot.reply_to(message, 'Это уже было, попробуй еще раз')
        else:
            bot.reply_to(message, 'Я не понимаю о чем Вы')
            
        
    bot.polling()