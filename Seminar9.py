import numpy as np

# Задача 1. Проверьте, существует ли связь между данными, приведёнными в таблице.Выполните задание с помощью библиотеки numpy.
def Primer1():
    num_f = [56, 37, 48, 45, 46, 43, 41, 45, 47, 48, 57, 63]
    num_s = [66, 46, 46, 54, 57, 51, 52, 54, 57, 54, 68, 72]
    num_t = [89, 67, 65, 77, 79, 68, 74, 75, 77, 77, 91, 96]


    matrix = [num_f, num_s, num_t]
    result = np.corrcoef(matrix)
    print(result)

#[[1.         0.90175619 0.87896031] 
# [0.90175619 1.         0.98700897] 
# [0.87896031 0.98700897 1.        ]]


def Zadacha1():
    size = 10
    numbers = np.random.randint(10, 100, size)
    print(numbers)

    mean = np.mean(numbers)
    print(f'среднее арифметическое {mean}')

    num = int(input('\nВвведите число: '))
    dist = [np.abs(el - num) for el in numbers]
    print(f'дистанции {dist}')
    min_dist = np.min(dist)
    print(f'минимальное расстояние {np.min(dist)}')
    index_min_dist = dist.index(min_dist)
    print(f'индекс минимального расстояния {dist.index(min_dist)}')

    print(f'ближайший элемент к {num} равен {numbers[index_min_dist]}')



Zadacha1()


#Задача 3. Задайте квадратную матрицу, состоящую из случайных чисел. Найдите самый часто встречающийся элемент в этой матрице.
# def Zadacha3():
