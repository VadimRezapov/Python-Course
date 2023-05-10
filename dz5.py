import random

# Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5. Используйте для решения лямбда-функцию.
# 2, 3, 4, 6, 7, 8 -> 6, 7, 8

def Tast1():
    N=int(input('Какое количество чисел сгенерировать? '))
    num=[]
    for i in range(N):
        num.append(random.randint(1,10))
    return print(num), sort(num)

def sort(num):
    arr = list (filter(lambda arr: arr > 5, num))
    return print(arr)



# Дан список случайных чисел. Создайте список, в который попадают числа, описывающие случайную возрастающую последовательность. Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] =>[1, 2, 3] или [2, 7] или [4, 6, 7] и т.д.

def indexes(num: list):
    indexes = [i for i in range(len(num))]      
    result = [] 
    while len(indexes) > 0:  
        index = indexes.pop(random.randint(0, len(indexes)-1))             

        if len(result) == 0 or num[index] > result[-1]:
            result.append(num[index])
        else:
            return result    
    
def Tast2():
    N=int(input('Какое количество чисел сгенерировать? '))
    num=[]
    for i in range(N):
        num.append(random.randint(1,10))
    return print(num), sort(num), indexes(num)

def sort(num):
    flag = True
    while flag:
        result = indexes(num)
        if len(result) > 1:
            print(f'Случайная возрастающая последовательность: {result}')
            flag = False


    
# Задайте список случайных чисел от 1 до 10. Посчитайте, сколько всего совпадающих элементов есть в списке. Удалите все повторяющиеся элементы.
# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадают. 
# Список уникальных элементов [1, 4, 2, 3, 6, 7]

def Tast3():
    N=int(input('Какое количество чисел сгенерировать? '))
    num=[]
    for i in range(N):
        num.append(random.randint(1,10))
    return print(num), sort(num), count(num)

def sort(num):
    arr = list(dict.fromkeys(num))
    print(arr)
    newElement = set(arr)
    print(f'Совпадающих элементов в numbers: {len(num) - len(newElement)}')
    print(f'Множество уникальных элементов: {newElement}')

def count(num):
    counter = {}
    for Elem in num:
        counter[Elem] = counter.get(Elem, 0) + 1
    doubles = {element: count for element, count in counter.items() if count > 1}
    print(doubles)

Tast3()