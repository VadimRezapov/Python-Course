Библиотеки Python:
1. import random - Библиотека позволяет создать случайные числа
2. import telebot
3. import ast
4. import json
 

Семминар 4. Задача номер 4. Для решения создали метод, который будет работать с числами "def calculate(n1, n2):" и делаем возврат значений  "return n1 + n2, n1 - n2, n1 * n2, n1 / n2. Четыре переменные задаются вызовом одного метода благодря кортежам "summ, raznost, umnozhenie, delenie = calculate(num_f, num_s)"

Семминар 4. Задача номер 5. Псевдослучайные числа выбираются с одинаковой вероятностью из конечного набора чисел. Выбранные числа не являются полностью случайными, так как математический алгоритм используется для их выбора, но они достаточно случайны для практических целей. Текущая реализация Random класса основана на измененной версии алгоритма генератора случайных чисел Дональда Е. Кнута.


Замечание к задачам № 5 (Домашная работа)
Во второй задаче ошибка в методе sort():

    resul = indexes(num)
    if len(resul) > 1:
            print(f'Случайная возрастающая последовательность: {result}')
метод indexes() возвращает список только из одной ветви кода. Это значит, что остальные ветви подразумевают возврат None. Значит, в методе sort() подразумевается измерение длины None:

if len(resul) > 1
Метод len() будет работать только с контейнерами. Попадание None вызовет ошибку.

Код, который Вы пушите в гит, должен быть полностью рабочим. Сейчас решение не рабочее, т.к. в решении присутствуют 3 одинаковых метода sort(). Надо или задавать методы разными именами, или пользовать классами и перегрузками.

Функция сама из себя предсталяет целый объект

Ссылка на телеграм проект телеграммм бота t.me/pytshapythonpitoshechka_Bot



## import telebot
## import requests
## import time

## bot = telebot.TeleBot("")

## @bot.message_handler(commands=['start', 'help'])
## def send_welcome(message):
	## bot.reply_to(message, "Howdy, how are you doing?")

## @bot.message_handler(content_types=['text'])
## def text_message(message):
	## print(message)
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
			bot.reply_to(message, 'Ближайшее кафе ищи на карте')
		else:
			bot.reply_to(message, 'Ты уже спрашивал')
	else:
		bot.reply_to(message, 'Что вообще надо от меня?')
		
	
## bot.polling()" ## 



