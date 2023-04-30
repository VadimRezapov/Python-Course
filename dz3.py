# Создайте список. Запишите в него N первых элементов последовательности Фибоначчи.
# 6 –> 1 1 2 3 5 8

from functools import lru_cache
 
def Tast1(): 
    @lru_cache(maxsize=None)
    def fib(n):
        if n < 2:
            return n
        return fib(n-1) + fib(n-2)
 
    num = int(input('Введите число '))
    print ([fib(n) for n in range(num)])


# В списке находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву.
# а –> абрикос, авокадо, апельсин, айва.
def Tast2():
    my_list = []
    my_list.append(input('Введите названия десяти фруктов'))
    count = 0
    while count < 10:
        my_list.append(str(input()))
        count = count+1
    print(my_list)
    check = 'А'
    res = [idx for idx in my_list if idx[0].lower() == check.lower()]
    print(res)


# Создайте скрипт бота, который находит ответы на фразы по ключу в словаре.
# Бот должен, как минимум, отвечать на фразы «привет», «как тебя зовут». 
# Если фраза ему неизвестна, он выводит соответствующую фразу. 

def Tast3():
    data = open('test.txt', encoding='utf-8')
    text = data.readlines()
    data.close()

    phrase = text[0].split(':')

    bot = {}
    bot[phrase[0]] = phrase[1]
    print(bot)

Tast3()