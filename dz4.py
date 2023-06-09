# Дано натуральное число N. Напишите метод, который вернёт список простых множителей числа N и количество этих множителей.
# 60 -> 2, 2, 3, 5

def Tast1():
    num = int(input("Введите число: "))
    i = 2  # первое простое число
    lst = []
    old = num
    while i <= num:
        if num % i == 0:
            lst.append(i)
            num //= i
            i = 2
        else:
            i += 1
    print(f"Простые множители числа {old} приведены в списке: {lst}")


# В первом списке находится информация об ассортименте мороженного, во втором списке - информация о том, какое мороженное есть на складе. 
# Выведите названия того товара, который закончился.
# Пример:
# 1 строка файла. «Сливочное», «Бурёнка», «Вафелька», «Сладкоежка»
# 2 строка файла. «Сливочное», «Вафелька», «Сладкоежка»
# Ответ. Закончилось: «Бурёнка»

def Tast2():
    spis_1 = set("«Сливочное», «Бурёнка», «Вафелька», «Сладкоежка»".split())
    spis_2 = set("«Сливочное», «Вафелька», «Сладкоежка»".split())

    lIst = spis_1.difference(spis_2)
    print(f"Закончилась {lIst}")



# Выведите число π с заданной точностью. Точность выводится в виде десятичной дроби.
# 3 -> 3.142

def Tast3():
    from cmath import pi

    N = int(input("Задайте количество знаков после запятой ПИ: "))
    print(f"{pi:.{N+1}}")

Tast3()