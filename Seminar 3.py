# Задача 0. Дан список, заполненный случайными числами от 0 до 10. Определите, является ли сумма всех элементов чётной.

# Подтянута Библиотека import random 
import random 
import string

def zadacha0():
    length = 7
    #numbers = [0] * length
    #for index in range(length):
    #    numbers[index] = random.randint(0, 10)
    #print(numbers)

    # Решение задачи 0. Дополнительная информация: Создание генератора random.randint(0, 10) for index in range(length)]. Скобки задают типпы данных
    numbers = [random.randint(0, 10) for index in range(length)]
    print(numbers)
    sum = 0 
    for index in range(length):
        sum += numbers[index]
    print(f'Сумма всех элементов равна {sum}')
    if sum % 2 == 0:
        print('Сумма четная')
    else:
        print('Сумма нечетная')


#Задача 1. В списке хранятся сведения о количестве осадков, выпавших за каждый день июня. Определите в какой период выпало больше осадков: в первой или второй половине июня.

def zadachaPrimer():
    days = 30
    numbers = [random.randint(0, 25) for _ in range(days)]
    f_part = numbers[:15]
    s_part = numbers[15:]
    print(numbers)
    f_sum = 0
    s_sum = 0
    for i in range(len(f_part)):
        f_sum += f_part[i]
        s_sum += s_part[i]
    print(f_sum)
    print(s_sum)
    if f_sum > s_sum:
        print('в первой половине больше')
    elif s_sum > f_sum:
        print('во второй половине больше')
    else:
        print('одинаково')

def Task1(length):
    numbers = [random.randint(0, 25) for el in range(length)]
    print(numbers)
    sum1 = sum2 = 0
    for i in range(int(length // 2)):
        sum1 += numbers[i]
    for i in range(int(length // 2), length):
        sum2 += numbers[i]
    if sum1 > sum2: print(f'В первой половине осадков выпало больше: {sum1} > {sum2}')
    else: print(f'Во второй половине осадков выпало больше: {sum1} < {sum2}')
    
#Задача 2. Напишите программу, которая позволит пользователю заполнить анкету, последовательно вводя в программу: - имя; - возраст; - хобби; - любимое животное.
# После окончания ввода, выводится заполненная анкета.
def Task2():
    form = dict(Имя = input('Ваше имя: '), Возраст = input('Ваш возраст: '), Хобби = input('Ваше хобби: '), Любимое_животное = input('Ваше любимое животное: '))
    print()
    for key, value in form.items():
        print("{0}: {1}".format(key,value))

# Задача 3. Напишите скрипт генератора паролей заданной длины, состоящих из латинских букв и чисел.

def Task3(length):
    letters_and_digits = string.ascii_letters + string.digits
    password = ''.join(random.sample(letters_and_digits, length))
    print(password)




#Задача 4. Ручка стоит – 5 рублей, карандаш – 3 рубля, ластик – 4 рубля.
#Кассир последовательно вводит в программу позиции из чека «ручка», «карандаш», «ластик».
#Ввод заканчивается, когда введено слово «стоп». Определите сумму чека.

def task4():
    dict = {'Ручка':5, 'карандаш':3, 'ластик':4}
    sum = 0
    flag = True
    while flag:
        code = input('Введите наименование: ')
        if code in dict:
            sum += dict[code]
        elif code == 'стоп':
            flag = False          
    print(sum)


# Вариан 2 решения задачи 2. Напишите программу, которая позволит пользователю заполнить анкету, последовательно вводя в программу: - имя; - возраст; - хобби; - любимое животное.
# После окончания ввода, выводится заполненная анкета.
def task5():
    name = input("Введите ваше имя: ")
    age = input("Введите ваш возраст: ")
    hobby = input("Введите ваше хобби: ")
    animal = input("Введите ваше любимое животное: ")

    print("\nАнкета заполнена:")
    print("Имя:", name)
    print("Возраст:", age)
    print("Хобби:", hobby)
    print("Любимое животное:", animal)

