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
    print(numbers)
    print(type(numbers))

example2()