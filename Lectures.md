Функкция round принимает на вход два аргумента. Первый аргумент - это число, а второй аргумент - число знаков после запятой, которые хоим оставить

Цикл while - цикл позволяет выполнить блок кода, пока условие являетя верным. 
Управляющая конструкция: while-else. Блок else выполнятеся, когда основное тело цикла перестает работать самостоятельно. А разве кто-то может прекратить работу цикла? Если вспомнить C#, то да и это конструкция break. 

Функция input(). Для того, чтобы превести число к целочисленному необходимо использовать функицю int. Функция int  отбрасывает дробную часть. Пример: 
c = 5.89
print(c)
n = int(с)
print(n) Вывод будет = 5

Цикл for, функция range()

Цикл for можно использовать со строками, так как у строк есть нумерация, такаяже как и у массивов, начинается с 0: 
for i in 'qwerty' 
print(i)


В python цикл for в основном используется для перебора значений
Пример использования цикла for:
for i in enumeration:
    operator 1
    operator 2
    ...
    operator n

for i in 1, -2, 3, 14, 5:
    print(i)   ответ будет: 1, -2, 3, 14, 5


range выдает значения для диапазона с шагом 1.
Если указано только одно число - от 0 до заданного числа.
Если нужен другой шаг, третьим аргументом можно задать приращение.

Функция len позвоялет узнать размер нашей строки. 
Функция lower позволяет перевести все буквы, находяещиеся в нашей строке, в нижний регистр.
Функция upper позволят поднять все в верхний регистр
Функция replace позволяет поменять сочетание символов в нашей строке.
