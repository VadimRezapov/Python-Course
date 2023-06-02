## Функции высшего порядка
import time




def example1():
    def our_print():
        def other_print():
            print('123')
        other_print()


    name_func = our_print
    name_func()
    print(type(name_func))


#   Задача 1. Создайте пользовательский аналог метода filter().
def zadacha1():
    def our_filter(func, numbers):
        return (el for el in numbers if func(el))

    def compare_numbers(num):
        return num > 5

    numbers = [1, 14, 6, 10, 3, 2, 5]
    print( list(filter(lambda x: x > 5, numbers)))
    print( list(our_filter(lambda x: x > 5, numbers)))

# Задача 2. Создайте метод, позволяющий замерить время работы других методов.
def zadacha2():
    def stopwatch(func):
        def decorator():
            start_time = time.time()
            func()
            print(f'время выполнения {time.time()- start_time}')
        return decorator

    @stopwatch
    def our_math_str():
        num = '132'
        result = int(num) + int(num*2) + int(num*3)
        print(result)


    def our_marh_int():
        num = '132'
        result = num + num*1000 + num*1000000 + num*1000 + num
        print(result)

        our_math_str()
        our_marh_int()


def example2():
    def stopwatch(func):
        import time
        def decorator():
            start_time = time.time()
            func()
            print(f'время выполнения {time.time() - start_time}')
        return decorator

    @stopwatch
    def our_math_str():
        num = '132'
        result = int(num) + int(num*2) + int(num*3)
        print(result)

    @stopwatch
    def our_math_int():
        num = 132
        result = num + num*1000 + num + num*1000000 + num*1000 + num
        print(result)

    our_math_str()
    our_math_int()


# Задача 3. Создайте декоратор для метода нахождения суммы.

#def zadacha3():
#    def our_format(func):
 #       def decorator(*args):
  #          # print(f'{a} + {b} = ', end='')
   #         for arg in args:
    #            # print( f'{arg} + , end=''()
     #       print('\b\b= ', end='')
      #      func(*args)
       # return decorator

#    @our_format
 #   def sum(a, b):
  #      print(a + b)
#
 #   @our_format
  #  def sum4(a, b, c, d):
   # print(a + b + c + d)
    #
    #sum(3, 51)
    #sum4()





# Задача 4. Создайте декоратор с параметрами.
def zadacha4():
    def greetings(hello):
        def our_greerings(func):
            def decorator():
                name = func()
                print(f'{hello}, {name}')
            return decorator
        return our_greerings

    @greetings('Привет')
    def get_name():
        return input('Как тебя зовут?\n')

    get_name()


# Создание телеграм бота

def zadacha5():
    bot = telebot.TeleBot("")
    
    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(message):
        bot.reply_to(message, "Howdy, how are you doing?")
        

    @bot.message_handler(func=lambda m: True)
    def echo_all(message):
        bot.reply_to(message, message.text)

        bot.polling()
        
zadacha5()