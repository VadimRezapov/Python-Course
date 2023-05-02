import random
# Задача № 0 Создайте кортеж. Запишите в него 10 случайных чисел

# Кортеж в программировании - это неизменяемый список "numbers" во второй строчке это список, а в третье строчке - это кортеж. В кортеже нельзя изментяьь элементы

def example1():
    numbers = [3, 4]
    numbers = tuple(numbers)
    print(numbers)
    print(type(numbers))


def example2():
    numbers = tuple(random.randint(1, 10) for _ in range(10))
    numbers = list(numbers)
    print(numbers)
    print(type(numbers))

# Создайте кортеж, заполненный случайными числами. Напишите метод, который заменяет элемент в кортеже по заданному индексу другим случайным числом.
def change_element(numbers, index):
    return numbers[0:index] + (random.randint(1, 100), ) + numbers[index+1:]


def example3():
    
    numbers = tuple(random.randint(1, 100) for _ in range(10))
    index = 2

    print(numbers)
    numbers = change_element(numbers, index)
    print(numbers)


# На вход подаются два числа. Напишите метод, который вернёт сумму, разность, произведение и частное этих чисел.  Тайминг 47:49

def calculate(n1, n2):
    return n1 + n2, n1 - n2, n1 * n2, n1 / n2 

def example4():
    num_f = 9
    num_s = 3
    res = calculate(num_f, num_s)
    print(res)
    summ, raznost, umnozhenie, delenie = calculate(num_f, num_s)
    print(summ, raznost, umnozhenie, delenie)


# Сгенерируйте список случайных чисел от 1 до 20, состоящий из 10 элементов. Удалите из списка дубликаты уже имеющихся элементов. Определите, сколько элементов было удалено.

def example5():
    numbers = list(random.randint(1,20) for _ in range(10))
    print(numbers)
    length = len(numbers)
    numbers = list(set(numbers))
    print(numbers)
    print(f'Элементов было удалено: {length - len(numbers)}')


# адача 4. Актёров разделили на списки по трём качествам «умные», «красивые», «сильные». На главную роль нужен актёр обладающий всеми тремя качествами. Определите, сколько есть претендентов на главную роль.
# Красивые: Илья Федор Семен Олег Лев Антон Артем Боря Стас Марк Ян
# Умные: Илья Георгий Лев Демьян Антон Владислав Боря Стас Марк Влад
# Сильные: Федор Георгий Олег Демьян Артем Елисей Боря Стас Влад


def example6():
    beuty = set("Илья Федор Семен Олег Лев Антон Артем Боря Стас Марк Ян".split())
    clever = set("Илья Георгий Лев Демьян Антон Владислав Боря Стас Марк Влад".split())
    strong = set("Федор Георгий Олег Демьян Артем Елисей Боря Стас Влад".split())

    top = beuty.intersection(clever). intersection(strong)
    print(top)

example6()
