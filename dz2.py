from math import factorial
from random import randint

# Задача 1. Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
# пусть N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


def Task1():
    
    numb = int(input('Введите число '))
    print(factorial(numb))

# Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.


def Task2():
    print(f'x | y | z | ¬ (X ∧ Y) ∨ Z')
    for x in range(0, 2):
                for y in range(0, 2):    
                    for z in range(0, 2):    
                        print(f'{x} | {y} | {z} | {int(not (x and y) or z)}')


# Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2

def Task3():
    strOne = input('Введите строку: ')
    strTwo = input('Введите значения: ')
    len_one = len(strOne)
    len_two = len(strTwo)
    count = 0
    for i in range(len_one):
        count = 0
        for j in range(len_two):
            if  strOne[i]== strTwo[j]:
                count+=1
        print(f'{strOne[i]}-{count}')


# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Сдвиньте все элементы списка на 2 позиции вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]



def Tast4(n):
    list = []
    for i in range(n):
        list.append(randint(-n, n))
    return list

n = int(input('Введите число N: '))
numbers = Tast4(n)
print(numbers)


