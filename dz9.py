import numpy
import random


def Zadacha1():
    def lIst():
        size = int(input('Из скольки чисел составить список? Введите цифру '))
        numbers = numpy.random.randint(1, 100, size)
        unique_elements = numpy.unique(numbers)
        print(numbers)
        print(unique_elements)
        print(f"Уникальных элементов {len(unique_elements)}")
    lIst()


def Zadacha2():
    def method():
        two_dimensional_array = numpy.random.randint(2, size=(5, 5))
        unique_rows = numpy.unique(two_dimensional_array, axis=0)
        print(two_dimensional_array)
        if unique_rows.shape[0] < two_dimensional_array.shape[0]:
            print("Одинаковык строки")
        else: 
            print("Одинаковых строк нет")



def Zadacha2():
    def lIst():
        size = int(input('Введите первую цифру ')),int(input('Введите вторую цифру '))
        numbers = numpy.random.randint(1, 100, size)
        print(numbers)
        print(f"Максимальное число имеет индекс {numpy.argmax(numbers)}")
        print(f"Минимальное число имеет индекс {numpy.argmin(numbers)}")
        print(f'Элементы главной диагонали массива: {numbers.diagonal()}')

        a = numpy.argmax(numbers)
        x = numpy.floor(a/3).astype(int)
        y = a%3
        print(f'Max = {numbers[x][y]}')

        a = numpy.argmin(numbers)
        x = numpy.floor(a/3).astype(int)
        y = a%3
        print(f'Min = {numbers[x][y]}')

        maxvalue = numpy.max(numbers)
        index_line_max, index_line_max = numpy.where(numbers==maxvalue)
        print (index_line_max[0], index_line_max[0])

        minvalue = numpy.min(numbers)
        index_line_min, index_line_min = numpy.where(numbers==minvalue)
        print (index_line_min[0], index_line_min[0])

    lIst()