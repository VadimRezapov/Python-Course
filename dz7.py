import telebot
import random


# Задача 1 Создайте поьзовательский аналог метода map()

def Zadacha1():

    array = [1, 2, 3, 4, 6]

    def func(element):
        return element * 2
    
    def user_map(func, array):
        new_array = []
        for element in array:
            new_array.append(func(element))
        return new_array
    
    print(user_map(func, array))


# Задача 2. Создайте декоратор, повторяющий функцию заданное количество раз.

def Zadacha2():
    def repeat_func(times):
        def procedure(func):
            def wrapper():
                for _ in range(times):
                    func()
            return wrapper
        return procedure

    @repeat_func(times=6)
    def func():
        print("Hello")

    func()


# Задача 3. Добавьте в telegram-бота игру «Угадай числа».
# Бот загадывает число от 1 до 1000. 
# Когда игрок угадывает его, бот выводит количество сделанных ходов.



def Zadacha3():

    bot = telebot.TeleBot("Token")

    @bot.message_handler(commands=['start'])
    def start(message):
        bot.send_message(message.chat.id, 'Привет! Давай поиграем в игру загадай число от 1 до 1000. Попробуйте угадать его! Введите /play для начала игры.')

    @bot.message_handler(commands=['play'])
    def play(message):
        bot.send_message(message.chat.id, 'Поехали! Я загадал число от 1 до 1000. Введите свой вариант:')

   
        number = random.randint(1, 5)
        tries = 0

        @bot.message_handler(func=lambda m: True)
        def guess(message):
            nonlocal tries
            nonlocal number
            try:
                guess_number = int(message.text)
            except ValueError:
                bot.send_message(message.chat.id, 'Ошибка. Попробуйте еще раз.')
                return
            
            tries += 1

            if guess_number > number:
                bot.send_message(message.chat.id, 'Мое число меньше. Попробуйте еще раз.')
            elif guess_number < number:
                bot.send_message(message.chat.id, 'Мое число больше. Попробуйте еще раз.')
            else:
                bot.send_message(message.chat.id, f'Поздравляю! Вы угадали число за {tries} попыток. Чтобы сыграть еще раз, введите команду /play.')
                tries = 0
                number = random.randint(1, 5)

    @bot.message_handler(commands=['play'])
    def new_game(message):
        play(message)

    bot.polling()


