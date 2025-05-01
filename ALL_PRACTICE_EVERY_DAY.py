import asyncio
import collections
import dataclasses
import functools
import heapq
import itertools
import json
import operator
import random
import sys
import time
import types
import re
from collections import namedtuple
from itertools import count, product
import ctypes
from dataclasses import dataclass, field
from typing import NamedTuple

import more_itertools

#  SyntaxWarning: invalid escape sequence - ошибка связанная с многострочной строкой используем r перед строкой r''' '''



# --- ЗРИ В КОРЕНЬ ПРОСТО ПОСМОТРЕТЬ ---


# Зри в корень 1
"""
value = 100

print_value = lambda: print(value)


value = 200
print_value2 = lambda: print(value)

print_value()       
print_value2()      

my_super_lambda = lambda: no(such(function()))

# --- Вывод ---    Потому что lambda Вычисляется в момент ВЫЗОВА!!!
# 200
# 200
"""




# Зри в корень 2
"""
global value                        # Починили КОД                   
value = 100                         value = 100                 
                                         
def print_value():                  def print_value():                     
    print(value)                        print(value)        
                                                              
def change_value():                 def change_value():                    
    value += 100                        global value                       
    print(value)                        value += 100                       
                                        print(value)     
print_value()                       print_value()       # -> 100                   
change_value()                      change_value()      # -> 200                   
print_value()                       print_value()       # -> 200       
                                
# --- Вывод ---
# 100
# UnboundLocalError: cannot access local variable 'value' where it is not associated with a value
"""




# Зри в корень 3
"""
                                                    # Поменяли чтобы вывод был другой      
value = 100                                         value = 100        
                                                    
def magic():                                        def magic():            
    x = value                                           def invisible():            
                                                            print(value)
    def invisible():                                    return invisible                    
        print(x)                                                     
    return invisible                                          
                                                    
# В момент вызова magic()   value = 100             # Ничего НЕ захватывали внутри                        
run = magic()                                       run = magic()                     
                                                     
value = 200                                         value = 200                   
run()                                               run()         # -> 200     
value = 300                                         value = 300        
run()                                               run()         # -> 300     
                                                    
# --- Вывод ---   Замыкание Запоминает значение
# 100
# 100
"""




# Зри в корень 4
"""
                                                 # Тоже самое если поменяем местами  Объет Функции будет создан 
                                                 # Но выполнение будет в scope  first()  
value = 100                                      value = 100              
                                                        
def first():                                     def first():                  
    def second():                                    length = lambda x: 0  # Если подчеркивает снизу это -  Shadows name              
        print(len(a_list))                           len = length          # Перекрыли len    Shadows built-in name      
        print(len(value))                            a_list = [1, 2, 3]                              
                                                                    
    length = lambda x: 0   # scope  first()          def second():                                                               
    len = length           # scope  first()              print(len(a_list))                                                       
    a_list = [1, 2, 3]     # scope  first()              print(len(value))                                                           
    second()               # scope  first()          second()                                                      
                                                        
first()                                          first()          

# --- Вывод ---
# 0
# 0
"""




# Зри в корень 5
"""
def main(x):
    try:
        return 100 / x
    except Exception:
        return 0
    finally:
        return 100

print(main(0))
print(main(111111))  # Даже если вводим любое число 

# --- Вывод ---  finally  ВЫПОЛНЯЕТСЯ ВСЕГДА!!!   Срабатывает всегда даже при Исключениях
# 100
# 100
"""




# Зри в корень 6
"""
                                             # Чтобы изменить поведение
def count(word: str, counter: dict = {}):    def count(word: str, counter: dict = None):                                               
    for letter in word:                          if counter is None:                           
        if letter in counter:                        counter = {}                                   
            counter[letter] += 1                 for letter in word:                                       
        else:                                        if letter in counter:                   
            counter[letter] = 1                          counter[letter] += 1                                   
    return counter                                   else:                       
                                                         counter[letter] = 1       
count("A")  # -> {'A': 1}                        return counter                               
print(count('BC'))                                                   
                                             count("A")  # -> {'A': 1}          
                                             print(count('BC'))  # -> {'B': 1, 'C': 1}          
                                                                                                        
# --- Вывод ---    Потому что Изменяемый объект в аргументах по умолчанию
# {'A': 1, 'B': 1, 'C': 1}
"""




# Зри в корень 7
"""
name = "Tom"
cat = {"name": 'Tom', "age": 3}

def change_name(name):
    name = 'Jerry'    # Локальная переменная
    return name       # Тут name 'Умирает'      # Будет собрана сборщиком мусора

def change_cat(a_dict):
    a_dict.clear()                        # Разные ссылки  Чистим словарь cat
    a_dict = {"name": "Jerry", "age": 3}  # Разные ссылки  Создали локальную переменную
    return a_dict                         # Тут локальный a_dict 'Умирает'   # Будет собрана сборщиком мусора

change_name(name)
change_cat(cat)

print(name)
print(cat)

# --- Вывод ---     Строка неизменяемая (создаем новый объект при изменении)
# Tom
# {}


#  --- ИЛИ  Другие Выводы ---
name = "Tom"
cat = {"name": 'Tom', "age": 3}

def change_name(name):
    name = 'Jerry'    
    return name       

def change_cat(a_dict):
    a_dict.clear()
    a_dict["name"] = "Jerry"    # Тут поменяли            
    a_dict["age"] = 3           # Тут поменяли    
    return a_dict               

name = change_name(name)  # Чтобы изменить name
cat = change_cat(cat)     # Чтобы изменить cat  clear внутри НЕ нужен
change_cat(cat)

print(name)  # -> JerryJerry
print(cat)   # -> {'name': 'Jerry', 'age': 3}

# --- Вывод ---     Строка неизменяемая (создаем новый объект при изменении)
# Jerry
# {'name': 'Jerry', 'age': 3}
"""




# Зри в корень 8
"""
# Перехватив Исключение МОЖНО поменять содержимое tuple
a_list = [1, 2, 3, 4, 5]
a_tuple = (a_list, 10)

# + Сработал а на = Падает Исключение
try:
    a_tuple[0] += [6]  # += вызывает магический метод у list   Сначала ДОБАВЛЯЕТ элемент а потом ПРИСВАИВАЕТ  2 ЧАСТА
except TypeError:
    print(a_tuple)
    print(a_list)

# --- Вывод ---    Ошибка упала и список ИЗМЕНИЛСЯ   tuple - Нельзя изменять  НО элементы внутри МОЖНО
# ([1, 2, 3, 4, 5, 6], 10)
# [1, 2, 3, 4, 5, 6]


# Интересный пример БЕЗ ОБРАБОТКИ                                                               <-----   <-----
a_list = [1, 2, 3, 4, 5]
a_tuple = (a_list, 10)

a_list += [6]
print(a_list)      # -> [1, 2, 3, 4, 5, 6]  # Так будет работать tuple мы не трогаем
a_tuple[0] += [6]  # TypeError: 'tuple' object does not support item assignment
"""




# Зри в корень 9, 10   НУЖНО ПЕРЕСМОТРЕТЬ ВИДЕО
"""
Если подчеркнуто СЕРЫМ НЕ значит  что ИНТЕРПРЕТАТОР НЕ будет выполнять строчку. Только если она НЕ закоментирована
"""




# Зри в корень 11
"""
# Присваивание: сначала, то что справа а потом слева (в лямбда: если дойдёт до факториала найди где находится и запусти)
factorial = lambda x: 1 if x <= 1 else x * factorial(x - 1)

print(factorial(5))  # -> 120
"""




# Зри в корень 12
"""
# В этом примере мы наблюдаем за оптимизацией строк в CPython.
# При создании нового объекта строки, если на него НЕ осталось ссылок, 
# CPython может оптимизировать выделение памяти, создавая только два уникальных объекта.


# CPython оптимизирует строки, но НЕ стоит на это рассчитывать! (Оптимизация работает, если НЕ осталось ссылок на 
# предыдущие варианты строк) Не сделал 10 объектов а оптимизировал.
# Вместо создания 10 объектов, CPython оптимизирует их до двух.

word = 'Hello from Python Russian'

ids = set()

for e in range(10):
    word = word + str(e)
    ids.add(id(word))

print(len(ids))  # -> 2     # CPython оптимизирует строки, так как старые строки больше НЕ используются



# Как нам сломать оптимизацию? (Будем сохранять ссылки)
# Мы будем сохранять ссылки на старые строки, чтобы CPython НЕ мог их оптимизировать.

word = 'Hello from Python Russian'
a_list = []                 # Список для хранения ссылок на старые строки       <----- 

ids = set()

for e in range(10):
    a_list.append(word)     # Сохраняем ссылку на текущую строку                <-----
    word = word + str(e)    # CPython есть ссылка, значит нельзя оптимизировать
    ids.add(id(word))

print(len(ids))  # -> 10    # Теперь каждая строка уникальна, CPython НЕ может оптимизировать
"""



# Зри в корень 13
"""
# Для строк и чисел Python может кешировать (интернировать) объекты для оптимизации, если они созданы на этапе компиляции.

# Динамические вычисления (например, конкатенация строк или арифметика во время выполнения) могут создавать новые объекты.

# Маленькие целые числа (-5 до 256) всегда кешируются.


# Строки интернируются (кешируются) Python на этапе компиляции, если они состоят из литералов.
main_word = 'python'
second_word = 'python'  # Тот же объект, что и main_word (интернирование)
third_word = 'pyt' + 'hon'  # Конкатенация литералов → оптимизируется в 'python' (интернируется)

# Динамическая конкатенация (с переменной) создаёт новый объект, даже если результат совпадает.
value = 'hon'
last_word = 'pyt' + value  # Новая строка (не интернируется)

print(main_word is second_word, main_word is third_word, main_word is last_word)  # True True False


# Числа вычисляются на этапе компиляции, если состоят из константных выражений.
first_value = 10_000  # 10000
second_value = 100 * 100  # Оптимизируется в 10000 → тот же объект

print(first_value is second_value)  # True (кеширование чисел за пределами -5..256 зависит от реализации)


# Маленькие целые числа (-5 до 256) всегда кешируются.  Они всегда СИНГЛТОНЫ
small_int = 100
another_small_int = int('100')  # Преобразование возвращает кешированный объект 100

print(small_int is another_small_int)  # True (из-за кеширования малых чисел)


--- Из чего состоят строки в Python? ---
Строки в Python состоят из последовательности Unicode-символов и хранятся как неизменяемые (immutable) объекты. <-----

 - Строки в Python — последовательности Unicode.
 
 - Могут храниться как 1, 2 или 4 байта на символ (зависит от содержимого).
 
 - Неизменяемы — любое изменение создаёт новую строку.
 
 - Короткие/ASCII-строки кешируются (интернируются).
 
 - Если нужна изменяемая строка, используется bytearray или list с последующим join.


--- Доказательство [-5, 256] ---
# Несколько способов доказать, что в Python числа от -5 до 256 являются синглтонами (кешируются)

# Тоже самое
res = len([i for i in range(-5, 300) if i is int(str(i))])
res_2 = len([i for i in range(-5, 300) if i is i+0])
print(res)     # -> 262
print(res_2)   # -> 262

# 1. Проверка через id() и повторное создание числа
def is_singleton(num):
    return num is int(str(num))  # или num is num + 0

# Проверяем диапазон
singletons = [i for i in range(-10, 300) if is_singleton(i)]
print("Количестно Кешируемых числей:", len(singletons))       # -> Количестно Кешируемых числей: 262
print("Границы:", min(singletons), "до", max(singletons))     # -> Границы: -5 до 256


# 2. Сравнение адресов в памяти (id)
a = 100
b = 100
print(a is b)  # True (один объект)

c = 1000
d = 1000
print(c is d)  # False (разные объекты, если не в интерактивном режиме)


# 3. Проверка через sys.intern() (для строк не подходит, но для чисел — косвенно)
import sys

def is_cached(num):
    return sys.getrefcount(num) > 3  # Число уже где-то используется  #  (sys.getrefcount не рекомендуется)

print(is_cached(256))  # True (кешируется)
print(is_cached(257))  # True (обычно нет)  # Может давать True даже для 257


# 4. Декомпиляция байт-кода (продвинутый способ)

import dis

def check():
    x = 100
    y = 1000

dis.dis(check)  # LOAD_CONST для 100 берёт значение из кеша, а для 1000 создаёт новый объект.


# Это прямое доказательство, что Python кеширует числа от -5 до 256.
# 5. Чтение исходного кода CPython

#define NSMALLPOSINTS           257  // 0..256
#define NSMALLNEGINTS           5    // -5..-1


Лучшие методы: 1) is int(str(num)), 4) байт-код, 5) исходники CPython.

Ненадёжные методы: 3) sys.getrefcount(), 2) is для чисел вне -5..256 (зависит от реализации).
"""




# Посмотреть 20 способов вывести "Hello World!"
# Каждый из этих способов выводит "Hello World!" разными методами и подходами. 20 СПОСОБОВ
R"""
# 1) Используя функцию print():
print("Hello World!")                

# 2) Используя sys.stdout.write():
import sys
sys.stdout.write("Hello World!")  # Добавляем '\n' для новой строки

# 3) Используя f-строки:
message = "Hello World!"
print(f"{message}")

# 4) Используя форматирование строк:
message = "Hello World!"
print("{}".format(message))

# 5) Используя конкатенацию строк:
print("Hello " + "World!")

# 6) Используя join():
print(" ".join(["Hello", "World!"]))

# 7) Используя lambda-функцию:
hello = lambda: print("Hello World!")
hello()

# 8) Используя класс:
class Greeter:
    def greet(self):
        print("Hello World!")

greeter = Greeter()
greeter.greet()

# 9) Используя обработчик исключений (try-except):
try:
    print("Hello World!")
except Exception as e:
    print(e)

# 10) Используя функцию с возвращаемым значением:
def get_message():
    return "Hello World!"

print(get_message())

# 11) Используя метод __str__() класса:
class HelloWorld:
    def __str__(self):
        return "Hello World!"

hello_instance = HelloWorld()
print(hello_instance)

# 12) Используя генератор:
hello_generator = (word for word in ["Hello", "World!"])
print(" ".join(hello_generator))

# 13) Используя декоратор:
def hello_decorator(func):
    def wrapper():
        print("Hello World!")
    return wrapper

@hello_decorator
def greet():
    pass

greet()

# 14) Используя модуль logging:
import logging
logging.basicConfig(level=logging.INFO)
logging.info("Hello World!")

# 15) Используя функцию map():
list(map(print, ["Hello", "World!"]))

# 16) Используя функцию exec():
exec('print("Hello World!")')

# 17) Используя функцию input() (с имитацией ввода):
input_message = input("Введите сообщение: ") if False else "Hello World!"
print(input_message)

# 18) Используя срезы строк:
message = "Hello World!"
print(message[:5], message[6:])

# 19) Используя многопоточность:
import threading

def print_message():
    print("Hello World!")

thread = threading.Thread(target=print_message)
thread.start()
thread.join()

# 20) Используя asyncio:
import asyncio

async def async_hello():
    print("Hello World!")

asyncio.run(async_hello())
"""




#  X5 Задача что выведет Данный код?    val - являются разными переменными.   Будет выведено  # -> 1
def a():
    val = 1
    def b():
        val = 10
    b()
    print(val)

# a()  # -> 1


# Ответ X5 Задача что выведет Данный код    val - являются разными переменными.    В этом случае замыкания **НЕТ**
"""
def a():
    val = 1  # В функции a создаем переменную val со значением 1

    def b():
        val = 10  # Внутри функции b создаем новую локальную переменную val со значением 10

    b()  # Вызываем функцию b, которая устанавливает свою локальную переменную val в 10
    print(val)  # Здесь мы печатаем значение val из функции a, которое равно 1

a()  # -> 1
"""
### Краткое объяснение X5 Задача что выведет Данный код:
"""
- Переменная `val` в функции `a()` имеет область видимости в этой функции.
- В функции `b()` создается новая локальная переменная `val`, которая не влияет на `val` в `a()`.
- При вызове `b()` выполняется код внутри нее, но `val` в `a()` остается равным `1`.
- Следовательно, когда выполняется `print(val)`, выводится `1`.

Замыкание происходит, когда внутренняя функция ссылается на переменную из внешней функции, и эта внешняя функция
продолжает существовать даже после ее завершения. В данном случае переменная `val` в `b()` 
НЕ ссылается на `val` из `a()`, поэтому замыкания не происходит. Местный `val = 10` в функции `b()` 
просто создает новую локальную переменную, не имея доступа к `val` в функции `a()`
"""




# ПРОСТО ПОСМОТРЕТЬ!!!
"""
# 2 Задачи  компания EdgeЦентр


# ЗАДАЧА 1)

a_list = [1, 2, 3, 4, 5]
res = filter(lambda x: x % 2, a_list)

if any(res):              # потребляет элементы генератора res до первого элемента, который оценивается как True
    for i in res:
        print(i, end=' ') # -> 3 5

for i in res:
    print(i, end=' ')     # Будет пусто потому что Генератор пуст



# ЗАДАЧА 2)

# Редкий случай гонки данных (race condition)     Это корректный пример гонки данных в асинхронном коде.
import asyncio

WORK_COUNTER = 0  # Изначально счетчик равен 0


async def foo():
    global WORK_COUNTER
    if WORK_COUNTER == 0:        # Первая проверка: условие True (0 == 0)
        await asyncio.sleep(.5)  # foo() засыпает на 0.5 сек (передает управление)
        # В этот момент управление переходит к задачам bar()

        WORK_COUNTER += 1        # После пробуждения увеличивает счетчик на 1
        # Но! Это произойдет только после того, как обе bar() проверят условие
    print(f"Foo - Work Counter: {WORK_COUNTER}")  # Выведет 1 (см. объяснение ниже)


async def bar():
    global WORK_COUNTER
    if WORK_COUNTER == 0:        # Условие изначально True (0 == 0)
        await asyncio.sleep(.5)  # bar() тоже засыпает на 0.5 сек
        # Во время сна foo() и другие bar() могут выполняться

        WORK_COUNTER += 2        # После пробуждения увеличивает счетчик на 2
        # Критический момент: обе bar() могут выполнить это ДО того, как foo() изменит счетчик
    print(f"Bar - Work Counter: {WORK_COUNTER}")  # Выведет 3 и 5 (см. объяснение)


async def main():
    # Создаем две асинхронные задачи bar() (они начинают выполняться)
    asyncio.create_task(bar())  # Задача 1
    asyncio.create_task(bar())  # Задача 2
    # Вызываем foo() и ждем его завершения
    await foo()  # Главная корутина ждет завершения foo()


if __name__ == "__main__":
    asyncio.run(main())              # Запускаем event loop
    print(f"Total: {WORK_COUNTER}")  # Итоговый вывод: 5


# Вывод:

# Foo - Work Counter: 1
# Bar - Work Counter: 3
# Bar - Work Counter: 5
# Total: 5


# Итог:
# Гонка данных между foo() и bar() приводит к тому, что обе bar() могут выполнить свои += 2,
# даже если foo() уже изменил счетчик.

# Почему так  Результат: Total: 5.:
# create_task() не гарантирует порядок выполнения, а await foo() не блокирует bar() полностью из-за асинхронности.
# Если bar() успевают проверить WORK_COUNTER == 0 до изменения foo(), они выполнят свои += 2.
"""




# Будет последнее значение выводить 10 раз    ПОСМОТРИ ВНИМАТЕЛЬНО КОД  Обрати внимание на    x   Задача Мебель Детали
# Просто посмотреть в конце будет такое же задание написать
"""
# ВСЕ лямбда-функции ссылаются на одну и ту же переменную a, которая в конце цикла равна 9.
fun = [lambda x: a for a in range(10)]
for f in fun:
    print(f(20), end=' ')  # -> 9 9 9 9 9 9 9 9 9 9


# Используем аргумент по умолчанию a=a . Это позволяет каждой функции сохранить текущее значение a на момент создания.
fun = [lambda x, a=a: a for a in range(10)]
for f in fun:
    print(f(20), end=' ')  # -> 0 1 2 3 4 5 6 7 8 9
"""





# Затраты памяти и времени Python   memory_profiler  ПРОСТО ПОСМОТРЕТЬ!!!   В конце пример profile ПОСМОТРИ!!!
"""
--- Затраты памяти и времени на выполнение append и списковое включение (list comprehensions) memory_profiler ---

#  В общем случае, списковое включение (list comprehension) обычно потребляет меньше памяти,
#  чем использование метода append, потому что оно создает список в одном непрерывном блоке памяти, тогда как метод
#  append может потребовать больше перераспределений памяти, если список растет.

from memory_profiler import memory_usage, profile

# Функция с использованием append
def create_list_append():
    l = []
    for i in range(100_000):
        l.append(i * 2)
    return l

# Функция с использованием спискового включения
def create_list_comprehension():
    return [i * 2 for i in range(100_000)]

# Замер памяти
def memory_usage_test():
    # Замер памяти для append
    append_mem_usage = memory_usage((create_list_append, ))
    print(f"Peak memory usage for append: {max(append_mem_usage) - min(append_mem_usage)} MiB")

    # Замер памяти для спискового включения
    comprehension_mem_usage = memory_usage((create_list_comprehension, ))
    print(f"Peak memory usage for comprehension: {max(comprehension_mem_usage) - min(comprehension_mem_usage)} MiB")

@profile
def profile_memory():
    create_list_append()
    create_list_comprehension()

# Запуск теста
if __name__ == '__main__':
    memory_usage_test()
    profile_memory()

# Выводы Всегда разные проверь сам!!!                                                       <-----   <-----
# Peak memory usage for append:        1.59375 MiB
# Peak memory usage for comprehension: 1.37109375 MiB


# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#   1076     22.1 MiB     22.1 MiB           1   @profile
#   1077                                         def profile_memory():
#   1078     22.4 MiB      0.3 MiB           1       create_list_append()
#   1079     22.4 MiB      0.0 MiB           1       create_list_comprehension()



# Легкий пример как использовать profile                                                      <-----   <-----
from memory_profiler import profile

@profile
def my_function():
    a = [i for i in range(100000)]
    b = [i * 2 for i in a]
    return b

if __name__ == "__main__":
    my_function()

# Line #    Mem usage    Increment  Occurrences   Line Contents
# =============================================================
#   1052     20.9 MiB     20.9 MiB           1   @profile
#   1053                                         def my_function():
#   1054     22.9 MiB      2.0 MiB      100001       a = [i for i in range(100000)]
#   1055     25.1 MiB  -1819.1 MiB      100001       b = [i * 2 for i in a]
#   1056     25.1 MiB      0.0 MiB           1       return b



# Более того даже если мы создадим список без добавления (append), он всеравно будет занимать больше памяти чем кортеж
# Потому что списки хранят дополнитулью информацию о своем текущем состоянии, чтобы эффективно изменять размер <------
# Дополнительная информация занимает мало места (порядка одного дополнительного элемента) однако при использовании
# миллиона списков мы начинаем чувствовать разницу!                                                            <------

import timeit
import sys

# Функции для создания списка и кортежа
def create_list():
    return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def create_tuple():
    return (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# Замер времени
list_time = timeit.timeit(create_list, number=1000000)
tuple_time = timeit.timeit(create_tuple, number=1000000)

# Размеры
list_size = sys.getsizeof(create_list())
tuple_size = sys.getsizeof(create_tuple())

# Вывод результатов
print(f'Время создания списка: {list_time:.3f} секунд')    # ->  Время создания списка:  0.147 секунд
print(f'Время создания кортежа: {tuple_time:.3f} секунд')  # ->  Время создания кортежа: 0.078 секунд
print(f'Размер списка: {list_size} байт')                  # ->  Размер списка:          68 байт
print(f'Размер кортежа: {tuple_size} байт')                # ->  Размер кортежа:         60 байт
"""




# Вычисляем, сколько оперативной памяти используем!   ПРОСТО ПОСМОТРЕТЬ!!!
"""
-- Вычисляем, сколько оперативной памяти используем!--

memit берет данные об использовании ОЗУ от оперативной системы, а asizeof запрашивает у объектов их размер(который может
быть сообщен неверно). Обычно asizeof работает медленнее, чем memit, но asizeof полезна при анализе небольших объектов
Функция memit, вероятно, более подходит для реальных приложений, поскольку измеряет потребление памяти точнее (не на
основе предположений)


# memory_usage позволяет более точно оценить потребление памяти в реальном времени, а asizeof может быть полезен для
# анализа небольших объектов, когда вам нужно измерить их размер более детально.

from pympler.asizeof import asizeof                                                 <-----   <----- Интересный импорт

# Создание списка
my_list = [i for i in range(1000000)]

# Измерение размера объекта
size = asizeof(my_list)
print(f"Size of my_list: {size} bytes")                # -> Size of my_list: 20224368 bytes



from memory_profiler import memory_usage

def my_function():
    return [i for i in range(1000000)]

if __name__ == '__main__':
    # Измерение использования памяти
    mem_usage = memory_usage(my_function)
    print(f"Peak Memory Usage: {max(mem_usage)} MiB")  # -> Peak Memory Usage: 79.70703125 MiB

"""





# Замеры размеров структур Python  ПРОСТО ПОСМОТРЕТЬ!!!
"""
 --- Замеры размеров Python ---

                            -- Примеры Списков deque vs list --                                 <-----
my_list = [1, 2, 3, 4, 5]
print(f'getsizeof list:  {sys.getsizeof(my_list)} байт')           # -> getsizeof list:  104 байт
print(f'asizeof   list:  {asizeof.asizeof(my_list)} байт')         # -> asizeof   list:  264 байт

from collections import deque
my_deque = deque([1, 2, 3, 4, 5])
print(f'getsizeof deque: {sys.getsizeof(my_list)} байт')           # -> getsizeof deque: 104 байт
print(f'asizeof   deque: {asizeof.asizeof(my_deque)} байт')        # -> asizeof   deque: 760 байт



                            -- Примеры Кортежей namedtuple vs tuple --                          <-----
my_tuple = (1, 2, 3, 4, 5)
print(f'getsizeof tuple:       {sys.getsizeof(my_tuple)} байт')    # -> getsizeof tuple:       80 байт
print(f'asizeof   tuple:       {asizeof.asizeof(my_tuple)} байт')  # -> asizeof   tuple:       240 байт

from collections import namedtuple
nt_tuple = namedtuple('nt_tuple', ['a', 'b', 'c', 'd', 'e'])
p = nt_tuple(1, 2, c=3, d=4, e=5)
print(f'getsizeof namedtuple:  {sys.getsizeof(p)} байт')           # -> getsizeof namedtuple:  80 байт
print(f'asizeof   namedtuple:  {asizeof.asizeof(p)} байт')         # -> asizeof   namedtuple:  240 байт


Создание объекта namedtuple накладывает некоторые накладные расходы (например, ХРАНЕНИЕ ИМЕН ПОЛЕЙ), но для 
НЕБОЛЬШИХ ОБЪЕКТОВ эти накладные расходы могут быть минимальными.
Однако в большинстве случаев namedtuple будет занимать больше места в памяти по сравнению с обычным кортежем


                            -- Примеры Словарей OrderedDict vs dict --                          <-----
my_dict = {1: 'a', 2: 'b', 3: 'c'}
print(f'getsizeof dict:         {sys.getsizeof(my_dict)} байт')     # -> getsizeof dict:       224 байт
print(f'asizeof   dict:         {asizeof.asizeof(my_dict)} байт')   # -> asizeof   dict:       488 байт


from collections import OrderedDict
or_dict = OrderedDict({1: 'a', 2: 'b', 3: 'c'})

print(f'getsizeof OrderedDict:  {sys.getsizeof(or_dict)} байт')    # -> getsizeof OrderedDict: 448 байт
print(f'asizeof   OrderedDict:  {asizeof.asizeof(or_dict)} байт')  # -> asizeof   OrderedDict: 712 байт



                            -- Примеры Множества frozenset vs set --                            <-----
my_set = {1, 2, 3, 4, 5}
print(f'getsizeof set:        {sys.getsizeof(my_set)} байт')     # -> getsizeof set:       472 байт
print(f'asizeof   set:        {asizeof.asizeof(my_set)} байт')   # -> asizeof   set:       632 байт


fz_set = frozenset({1, 2, 3, 4, 5})

print(f'getsizeof frozenset:  {sys.getsizeof(fz_set)} байт')    # -> getsizeof frozenset:  472 байт
print(f'asizeof   frozenset:  {asizeof.asizeof(fz_set)} байт')  # -> asizeof   frozenset:  632 байт

# Если list внутри
fz_set = frozenset([1, 2, 3, 4, 5])

print(f'getsizeof frozenset:  {sys.getsizeof(fz_set)} байт')    # -> getsizeof frozenset:  728 байт
print(f'asizeof   frozenset:  {asizeof.asizeof(fz_set)} байт')  # -> asizeof   frozenset:  888 байт

# Если tuple внутри
fz_set = frozenset((1, 2, 3, 4, 5))

print(f'getsizeof frozenset:  {sys.getsizeof(fz_set)} байт')    # -> getsizeof frozenset:  728 байт
print(f'asizeof   frozenset:  {asizeof.asizeof(fz_set)} байт')  # -> asizeof   frozenset:  888 байт



                            -- Примеры Строки/Числа str vs int --                              <-----
my_string = "Hello, World!"

print(f'getsizeof str:  {sys.getsizeof(my_string)} байт')    # -> getsizeof str:  62 байт
print(f'asizeof   str:  {asizeof.asizeof(my_string)} байт')  # -> asizeof   str:  64 байт


my_int = 10000000000000000000000000000

print(f'getsizeof int:  {sys.getsizeof(my_int)} байт')       # -> getsizeof int:  40 байт
print(f'asizeof   int:  {asizeof.asizeof(my_int)} байт')     # -> asizeof   int:  40 байт



# Чем больше строка тем больше размер так же и с другими обьектами

my_string = "a"

print(f'getsizeof str:  {sys.getsizeof(my_string)} байт')    # -> getsizeof str:  50 байт
print(f'asizeof   str:  {asizeof.asizeof(my_string)} байт')  # -> asizeof   str:  56 байт


my_int = 1

print(f'getsizeof int:  {sys.getsizeof(my_int)} байт')       # -> getsizeof int:  28 байт
print(f'asizeof   int:  {asizeof.asizeof(my_int)} байт')     # -> asizeof   int:  32 байт



                            -- Сравнение slots vs no_slots --                                  <-----
                            -- @dataclass(slots=True)  vs  @dataclass() --
from dataclasses import dataclass

@dataclass(slots=True)
class WithSlots:
    value: int

with_slots = WithSlots(10)
print(f'getsizeof WithSlots:  {sys.getsizeof(with_slots)} байт')    # -> getsizeof WithSlots:  40 байт
print(f'asizeof   WithSlots:  {asizeof.asizeof(with_slots)} байт')  # -> asizeof   WithSlots:  72 байт


@dataclass
class NoSlots:
    value: int

no_slots = NoSlots(10)
print(f'getsizeof NoSlots:    {sys.getsizeof(no_slots)} байт')      # -> getsizeof NoSlots:    56 байт
print(f'asizeof   NoSlots:    {asizeof.asizeof(no_slots)} байт')    # -> asizeof   NoSlots:    440 байт
"""



# Замеры ПУСТЫХ обьектом встроенных Python  ПРОСТО ПОСМОТРЕТЬ!!!
"""
 --- Замеры ПУСТЫХ обьектом встроенных Python ---
 
                            -- Примеры list vs [] vs deque() vs heapq --                       <-----
                            
my_list = list()
print(f'getsizeof list():      {sys.getsizeof(my_list)} байт')    # -> getsizeof list():       56 байт
print(f'asizeof   list():      {asizeof.asizeof(my_list)} байт')  # -> asizeof   list():       56 байт
 
my_list = []
print(f'getsizeof []:          {sys.getsizeof(my_list)} байт')    # -> getsizeof []:           56 байт
print(f'asizeof   []:          {asizeof.asizeof(my_list)} байт')  # -> asizeof   []:           56 байт


from collections import deque

my_deque = deque()
print(f'getsizeof deque():     {sys.getsizeof(my_deque)} байт')    # -> getsizeof deque():     760 байт
print(f'asizeof   deque():     {asizeof.asizeof(my_deque)} байт')  # -> asizeof   deque():     760 байт


import heapq

my_heapq = []
heapq.heapify(my_heapq)
print(f'getsizeof heapq:       {sys.getsizeof(my_heapq)} байт')    # -> getsizeof heapq:       56 байт
print(f'asizeof   heapq:       {asizeof.asizeof(my_heapq)} байт')  # -> asizeof   heapq:       56 байт





                            -- Примеры set() vs frozenset() --                                 <-----

my_set = set()
print(f'getsizeof set():       {sys.getsizeof(my_set)} байт')    # -> getsizeof set():         216 байт
print(f'asizeof   set():       {asizeof.asizeof(my_set)} байт')  # -> asizeof   set():         216 байт
  
my_set = frozenset()
print(f'getsizeof frozenset(): {sys.getsizeof(my_set)} байт')    # -> getsizeof frozenset():   216 байт
print(f'asizeof   frozenset(): {asizeof.asizeof(my_set)} байт')  # -> asizeof   frozenset():   216 байт





                            -- Примеры tuple() vs namedtuple() vs () --                        <-----
my_tuple = tuple()
print(f'getsizeof tuple():    {sys.getsizeof(my_tuple)} байт')    # -> getsizeof tuple():      40 байт
print(f'asizeof   tuple():    {asizeof.asizeof(my_tuple)} байт')  # -> asizeof   tuple():      40 байт
print(f'asizeof   ():         {asizeof.asizeof(())} байт')        # -> asizeof   ():           40 байт


from collections import namedtuple

my_tuple = namedtuple('C', '')
nt_tuple = my_tuple()
print(f'getsizeof namedtuple: {sys.getsizeof(nt_tuple)} байт')    # -> getsizeof namedtuple:   40 байт
print(f'asizeof   namedtuple: {asizeof.asizeof(nt_tuple)} байт')  # -> asizeof   namedtuple:   40 байт





                            -- Примеры dict() vs {} vs OrderedDict() vs defaultdict() vs ChainMap() --        <-----
my_dict = dict()
print(f'getsizeof dict():       {sys.getsizeof(my_dict)} байт')      # -> getsizeof dict():       64 байт
print(f'asizeof   dict():       {asizeof.asizeof(my_dict)} байт')    # -> asizeof   dict():       64 байт


my_dict = {}
print(f'getsizeof {{}}:         {sys.getsizeof(my_dict)} байт')      # -> getsizeof {}:           64 байт
print(f'asizeof   {{}}:         {asizeof.asizeof(my_dict)} байт')    # -> asizeof   {}:           64 байт


from collections import OrderedDict
 
my_OrDt = OrderedDict()
print(f'getsizeof OrderedDict:  {sys.getsizeof(my_OrDt)} байт')      # -> getsizeof OrderedDict:  128 байт
print(f'asizeof   OrderedDict:  {asizeof.asizeof(my_OrDt)} байт')    # -> asizeof   OrderedDict:  128 байт


from collections import defaultdict

my_defa = defaultdict(int)     # Все будут весить ОДИНАКОВО!!!
my_defa = defaultdict(str)     # Все будут весить ОДИНАКОВО!!!
my_defa = defaultdict(list)    # Все будут весить ОДИНАКОВО!!!
my_defa = defaultdict(set)     # Все будут весить ОДИНАКОВО!!!
my_defa = defaultdict(dict)    # Все будут весить ОДИНАКОВО!!!
my_defa = defaultdict()        # Все будут весить ОДИНАКОВО!!!
print(f'getsizeof defaultdict():  {sys.getsizeof(my_defa)} байт')    # -> getsizeof defaultdict():  72 байт
print(f'asizeof   defaultdict():  {asizeof.asizeof(my_defa)} байт')  # -> asizeof   defaultdict():  72 байт


from collections import ChainMap
 
my_chain = ChainMap()
print(f'getsizeof ChainMap():  {sys.getsizeof(my_chain)} байт')      # -> ggetsizeof ChainMap():  56 байт
print(f'asizeof   ChainMap():  {asizeof.asizeof(my_chain)} байт')    # -> aasizeof   ChainMap():  536 байт





                            -- Сравнение slots vs no_slots --                                  <-----
                            -- @dataclass(slots=True)  vs  @dataclass() --
                            
from dataclasses import dataclass

@dataclass(slots=True)
class WithSlots:pass

with_slots = WithSlots()
print(f'getsizeof WithSlots:  {sys.getsizeof(with_slots)} байт')    # -> getsizeof WithSlots:  32 байт
print(f'asizeof   WithSlots:  {asizeof.asizeof(with_slots)} байт')  # -> asizeof   WithSlots:  32 байт


@dataclass
class NoSlots:pass

no_slots = NoSlots()
print(f'getsizeof NoSlots:    {sys.getsizeof(no_slots)} байт')      # -> getsizeof NoSlots:    56 байт
print(f'asizeof   NoSlots:    {asizeof.asizeof(no_slots)} байт')    # -> asizeof   NoSlots:    352 байт





                            -- Обычные классы По размеру тоже самое что @dataclass(slots=True)  vs  @dataclass() --
                            -- Сравнение slots vs no_slots --
                            
class WithSlots:__slots__ = ()

with_slots = WithSlots()
print(f'getsizeof WithSlots:  {sys.getsizeof(with_slots)} байт')    # -> getsizeof WithSlots:  32 байт
print(f'asizeof   WithSlots:  {asizeof.asizeof(with_slots)} байт')  # -> asizeof   WithSlots:  32 байт


class NoSlots:pass

no_slots = NoSlots()
print(f'getsizeof NoSlots:    {sys.getsizeof(no_slots)} байт')      # -> getsizeof NoSlots:    56 байт
print(f'asizeof   NoSlots:    {asizeof.asizeof(no_slots)} байт')    # -> asizeof   NoSlots:    352 байт                            





                            -- Примеры int() float() complex() True False str() range(0) bytes() bytearray() vs None -- 
                            -- И пустые объекты Тоже самое 0  ''  0.0  0j  b""  bytearray(b"")  object()  --     <-----
                            
my_int = int()
print(f'getsizeof int():  {sys.getsizeof(my_int)} байт')            # -> getsizeof int():      28 байт
print(f'asizeof   int():  {asizeof.asizeof(my_int)} байт')          # -> asizeof   int():      32 байт
print(f'asizeof   0:      {asizeof.asizeof(0)} байт')               # -> asizeof   0:          32 байт


my_float = float()
print(f'getsizeof float():  {sys.getsizeof(my_float)} байт')        # -> getsizeof float():    24 байт
print(f'asizeof   float():  {asizeof.asizeof(my_float)} байт')      # -> asizeof   float():    24 байт
print(f'asizeof   0.0:      {asizeof.asizeof(my_float)} байт')      # -> asizeof   0.0:        24 байт


my_comp = complex()
print(f'getsizeof complex():  {sys.getsizeof(my_comp)} байт')       # -> getsizeof complex():  32 байт
print(f'asizeof   complex():  {asizeof.asizeof(my_comp)} байт')     # -> asizeof   complex():  32 байт
print(f'asizeof   0j:         {asizeof.asizeof(my_comp)} байт')     # -> asizeof   0j:         32 байт


# True
print(f'getsizeof True:  {sys.getsizeof(True)} байт')               # -> getsizeof True:       28 байт
print(f'asizeof   True:  {asizeof.asizeof(True)} байт')             # -> asizeof   True:       32 байт


# False
print(f'getsizeof False:  {sys.getsizeof(False)} байт')             # -> getsizeof False:      28 байт
print(f'asizeof   False:  {asizeof.asizeof(False)} байт')           # -> asizeof   False:      32 байт


# None  занимает фиксированное количество памяти!!!        Один из самых маленьких объектов по памяти!!!      <-----
print(f'getsizeof None:  {sys.getsizeof(None)} байт')               # -> getsizeof None:       16 байт
print(f'asizeof   None:  {asizeof.asizeof(None)} байт')             # -> asizeof   None:       16 байт


my_str = str()
print(f'getsizeof str():  {sys.getsizeof(my_str)} байт')            # -> getsizeof str():      49 байт
print(f'asizeof   str():  {asizeof.asizeof(my_str)} байт')          # -> asizeof   str():      56 байт
print(f'asizeof   "":     {asizeof.asizeof("")} байт')              # -> asizeof   "":         56 байт


my_range = range(0)
print(f'getsizeof range(0):  {sys.getsizeof(my_range)} байт')       # -> getsizeof range(0):   48 байт
print(f'asizeof   range(0):  {asizeof.asizeof(my_range)} байт')     # -> asizeof   range(0):   48 байт


my_bytes = bytes()
print(f'getsizeof bytes():  {sys.getsizeof(my_bytes)} байт')        # -> getsizeof bytes():    33 байт
print(f'asizeof   bytes():  {asizeof.asizeof(my_bytes)} байт')      # -> asizeof   bytes():    40 байт
print(f'asizeof   b"":      {asizeof.asizeof(b"")} байт')           # -> asizeof   b"":        40 байт


my_b_arr = bytearray()
print(f'getsizeof bytearray():  {sys.getsizeof(my_b_arr)} байт')    # -> getsizeof bytearray():              56 байт
print(f'asizeof   bytearray():  {asizeof.asizeof(my_b_arr)} байт')  # -> asizeof   bytearray():              56 байт
print(f'asizeof   bytearray(b""):  {asizeof.asizeof(bytearray(b""))} байт')  # -> asizeof   bytearray(b""):  56 байт


my_object = object()
print(f'getsizeof object():  {sys.getsizeof(my_object)} байт')      # -> getsizeof object():   16 байт
print(f'asizeof   object():  {asizeof.asizeof(my_object)} байт')    # -> asizeof   object():   0 байт

object() возвращает 0 байт, потому что функция `asizeof` не находит вложенных объектов или атрибутов для учета,
так как `object` не содержит информации.  Сам по себе object() - весит 16 байт
object() - является базовым пустым объектом без дополнительных атрибутов или содержимого.

"""







# type - это тип ВСЕХ типов, для которых НЕ указан явно иной метакласс  ПРОСТО ПОСМОТРЕТЬ!!!
"""
print(type(type))    # -> <class 'type'>
print(type(object))  # -> <class 'type'>
print(type(list))    # -> <class 'type'>
print(type(set))     # -> <class 'type'>
print(type(dict))    # -> <class 'type'>
print(type(bool))    # -> <class 'type'>
print(type(int))     # -> <class 'type'>
print(type(str))     # -> <class 'type'>
print(type(collections.deque))  # -> <class 'type'>

class Bar(object): pass
print(type(Bar))  # -> <class 'type'>
"""



# ПРОСТО ПОСМОТРЕТЬ!!!
# Интересный Пример с обновлением словаря   ПОСМОТРИ ОТВЕТЫ и почему        Словарь в любом случае обновляется!!! <----
# Таким образом, словарь обновляется каждый раз, когда вызывается функция `test2`, независимо от того,
# существует ли ключ `test` или нет.
"""
# Если ключ ЕСТЬ                                # Если ключа НЕТ                    
dct = {'test': 321}                             dct = {'test': 321}                    
                                                     
def test2():                                    def test2():                
    dct.update({'test': 444})                       dct.update({'test': 444})                                
    return 123                                      return 123                
                                                     
print(dct.get('test', test2()))   # -> 444      print(dct.get('TTTTT', test2()))  # -> 123
print(dct)               # -> {'test': 444}     print(dct)               # -> {'test': 444}
"""




# Про ДЕКОРАТОР ПРОСТО ПОСМОТРИ ВСЕ ВАРИАНТЫ!!!                                        <-----       <-----
"""
Сибур Задача  Про декоратор   Посмотри все варианты!!!                                 <-----

# Ошибка вызов пустой функции  TypeError                                # Всё правильно без ОШИБОК!!!
     
def decor(strict=False):                                                def decor(strict=False):
    def real_decor(func):                                                   def real_decor(func):
        @wraps(func)                                                            @wraps(func)
        def wrappper(*args, **kwargs):                                          def wrappper(*args, **kwargs):
            if strict:                                                              if strict:
                return func()                                                           return func()
            return func(*args, **kwargs)                                            return func(*args, **kwargs)
        return wrappper                                                         return wrappper
    return real_decor                                                       return real_decor

# @decor(True) # Тоже самое  НЕ ОБЯЗАТЕЛЬНО ИМЕНОВАННЫМИ ПЕРЕДАВАТЬ     # @decor(False) # Тоже самое    <----
@decor(strict=True)             # Тут   strict=True                     @decor(strict=False)    # Тут   strict=False  
def plus(a):                                                            def plus(a):
    return a+5                                                              return a+5
     
print(plus(5))                                                          print(plus(5))  # -> 10
# -> TypeError: plus() missing 1 required positional argument: 'a'



# Будет ссылка БЕЗ ПЕРЕДАЧИ ПАРАМЕТРОВ в ДЕКОРИРУЕМУЮ ФУНКЦИЮ  БЕЗ ОШИБКИ  ОТРАБОТАЕТ!!!
def decor(strict=False):
    def real_decor(func):
        @wraps(func)
        def wrappper(*args, **kwargs):
            if strict:
                return func()
            return func(*args, **kwargs)
        return wrappper
    return real_decor

@decor                            # НЕ ПЕРЕДАЛИ АРГУМЕНТЫ ОТРАБОТАЕТ БЕЗ ОШИБОК       <-----
def plus(a):
    return a+5

print(plus(5))  # -> <function decor.<locals>.real_decor.<locals>.wrappper at 0x000001C17794EFC0>   #  Важно !!<-----
"""



# Напишите функцию apply_multiple(funcs, value), которая принимает список функций funcs и значение value.  2 Варианта!!!
# Функция должна последовательно применять все функции из списка к значению и вернуть результат.


from functools import reduce, wraps, total_ordering


def apply_multiple(funcs, value):
    pass


def increment(x):
    return x + 1

def double(x):
    return x * 2


# result = apply_multiple([increment, double], 3)
# print(result)  # -> 8



# Напишите функцию apply_multiple(funcs, value), которая принимает список функций funcs и значение value.
# Функция должна последовательно применять все функции из списка к значению и вернуть результат.
f"""
# Обычный Пример                                 #  Через reduce
def apply_multiple(funcs, value):                def apply_multiple(funcs, value):
    for i in funcs:                                  return reduce(lambda v, f: f(v), funcs, value)
        value = i(value)                             # return reduce(lambda x, y: y(x), (el for el in funcs), value)
    return value

def increment(x):                                def increment(x):
    return x + 1                                     return x + 1

def double(x):                                   def double(x):
    return x * 2                                     return x * 2

result = apply_multiple([increment, double], 3)  result = apply_multiple([increment, double], 3)
print(result)  # -> 8                            print(result)  # -> 8
"""



# Напишите Релизацию своего класса имитируещего словарь  через []    Создание собственного класса для реализации словаря








# Ответ Релизация СЛОВАРЯ  Задача с собеседовании   Через  tuple()
# Релизация своего класса имитируещего словарь      Создание собственного класса для реализации словаря
"""
class MyDict:
    def __init__(self):
        self.data = []

    def __setitem__(self, key, value):
        for i, (k, v) in enumerate(self.data):
            if k == key:
                self.data[i] = (key, value)  # Обновляем значение
                return
        self.data.append((key, value))  # Добавляем новый элемент

    def __getitem__(self, key):
        for k, v in self.data:
            if k == key:
                return v  # Возвращаем значение, если ключ найден
        raise KeyError(f"Key {key} not found.")

    def __delitem__(self, key):
        for i, (k, v) in enumerate(self.data):
            if k == key:
                del self.data[i]  # Удаляем элемент с данным ключом
                return
        raise KeyError(f"Key {key} not found.")

    def __contains__(self, key):
        return any(k == key for k, v in self.data)  # Проверяем наличие ключа

    def __len__(self):
        return len(self.data)  # Возвращаем количество элементов в словаре

    def __iter__(self):
        return (k for k, v in self.data)  # Итерирование по ключам

    def items(self):
        return self.data.copy()  # Возвращаем все пары (ключ, значение)

    def keys(self):
        return [k for k, v in self.data]  # Возвращаем список ключей

    def values(self):
        return [v for k, v in self.data]  # Возвращаем список значений

    def clear(self):
        '''Удаляет все элементы из словаря.'''
        self.data.clear()

    def update(self, other):
        '''Обновляет словарь значениями из другого словаря или итерируемого объекта.'''
        for k, v in other.items():
            self[k] = v

    def pop(self, key, default=None):
        '''Удаляет элемент с указанным ключом и возвращает его значение. Если ключ не найден, возвращает значение по умолчанию.'''
        for i, (k, v) in enumerate(self.data):
            if k == key:
                del self.data[i]  # Удаляем элемент
                return v
        if default is not None:
            return default
        raise KeyError(f"Key {key} not found.")

    def popitem(self):
        '''Удаляет и возвращает последнюю добавленную пару (ключ, значение). Если словарь пустой, вызывается исключение KeyError.'''
        if not self.data:
            raise KeyError("popitem(): dictionary is empty")
        return self.data.pop()  # Возвращает и удаляет последний элемент

    def get(self, key, default=None):
        '''Возвращает значение по ключу, если ключ не найден – возвращает значение по умолчанию.'''
        for k, v in self.data:
            if k == key:
                return v
        return default

    def setdefault(self, key, default=None):
        '''Возвращает значение по ключу. Если ключ не найден, добавляет ключ с значением по умолчанию и возвращает его.'''
        if key not in self:
            self[key] = default
        return self[key]

    def items_length(self):
        '''Возвращает длину всех пар (ключ, значение) в словаре.'''
        return len(self.data)

    @classmethod
    def fromkeys(cls, iterable, value=None):
        '''Создает новый экземпляр MyDict с заданными ключами и значением по умолчанию.'''
        new_dict = cls()
        for key in iterable:
            new_dict[key] = value
        return new_dict


# Пример использования
my_dict = MyDict()
my_dict['apple'] = 1
my_dict['banana'] = 2

print(my_dict['apple'])     # Вывод: 1
print('banana' in my_dict)  # Вывод: True
print(len(my_dict))         # Вывод: 2

my_dict['apple'] = 3
print(my_dict['apple'])     # Вывод: 3
my_dict['cherry'] = 5
print(my_dict.items())      # Вывод: [('apple', 3), ('banana', 2), ('cherry', 5)]

del my_dict['banana']
print(my_dict.items())      # Вывод: [('apple', 3), ('cherry', 5)]

# Применение новых методов
my_dict.clear()
print(my_dict.items())      # Вывод: []

my_dict.update({'orange': 4, 'pear': 6})
print(my_dict.items())      # Вывод: [('orange', 4), ('pear', 6)]

value = my_dict.pop('orange')
print(value)  # Вывод: 4
print(my_dict.items())      # Вывод: [('pear', 6)]

last_item = my_dict.popitem()
print(last_item)  # Вывод: ('pear', 6)

# Демонстрация новых методов
print(my_dict.get('pear'))  # Вывод: KeyError
print(my_dict.get('pear', 'default_value'))  # Вывод: default_value

my_dict.setdefault('banana', 10)
print(my_dict.items())  # Вывод: [('banana', 10)]

length = my_dict.items_length()
print(length)           # Вывод: 1

new_dict = MyDict.fromkeys(['key1', 'key2', 'key3'], 'default_value')
print(new_dict.items())  # Вывод: [('key1', 'default_value'), ('key2', 'default_value'), ('key3', 'default_value')]



# Мой вариант на собеседовании ПРОСТОЙ   Через  tuple()

# Тоже самое  Но каждый раз будет создаватся новый список
@dataclass
class MyDict:
    data: list = field(default_factory=list)


class MyDict:
    def __init__(self):
        self.data = []

    def _add(self, key, value):
        if key:
            self.data.append((key, value))

    def _get(self, key):
        for i, (k, v) in enumerate(self.data):
            if key and k == key:
                return v
        raise KeyError


c = MyDict()
c._add(1, 'A')
print(c._get(1))  # -> A
print(c._get(2))  # -> KeyError
"""




# Напишите  Обход в Обратном порядке в цикле for








# Обход в Обратном порядке в цикле for
"""
# Обход в Обратном порядке в цикле for
for i in range(10, -1, -1):
    print(i, end=' ')  # -> 10 9 8 7 6 5 4 3 2 1 0 
    
print([*range(10, 0, -1)])  # -> [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
"""





# Вывести слово кит. Обратный цикл


s = 'информатика'







# Ответ Вывести слово кит. Обратный цикл
"""
s = 'информатика'
print(s[-2:-5:-1])  # -> кит
print(s[-2:-5])     # -> ничего не выведет
"""







# Используйте dis - Библиотека работы с Байт-кодом   import dis







# dis - Библиотека работы с Байт-кодом  from dis import dis
"""
from dis import dis
def func():
   a = 42
   return a
print(dis(func))


import dis
def func2():
    return 42
print(dis.dis(func2))
"""



# Перепиши примеры ниже   Понимание вложенных списков
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]


transposed = []



matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]




# Понимание вложенных списков
"""
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
# Сравни их
print([i for row in matrix for i in row])    # -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print([[i for i in row] for row in matrix])  # -> [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

# ГЕНЕРАТОР  Опустили []
print(i for row in matrix for i in row)    # -> <generator object <genexpr> at 0x000001AF700EB850>
print([i for i in row] for row in matrix)  # -> <generator object <genexpr> at 0x0000025DB01BE500>


# Все результаты будут одинаковые!!!

# Следующее понимание списка будет транспонировать строки и столбцы:
transposed = [[row[i] for row in matrix] for i in range(4)]
print(transposed)          # -> [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# Тоже самое
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)          # -> [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# что, в свою очередь, аналогично:
transposed = []
for i in range(4):
    # следующие 3 строки реализуют вложенный listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)          # -> [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]

# В реальном мире вам следует предпочесть встроенные функции
print(list(zip(*matrix)))  # -> [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
print(list(zip(matrix)))   # -> [([1, 2, 3, 4],), ([5, 6, 7, 8],), ([9, 10, 11, 12],)]  # Без распаковки *  исходный
"""



# Повтори примеры  МОРЖА/Walrus  Разные примеры!!!  Моржовый оператор/Walrus

# Перепиши с Моржом
n = 10
# print(5 <= n < 10 or 101 < n < 201)  # -> False






s = "Hello"
# print(f'Если перевернуть слово "{s}", получится "{s[::-1]}".')






# Напечатайте индекс наименьшего числа в списке.
a = [5, 8, 3, 2, 7, 4, 9]








# Использование МОРЖА/Walrus  Разные примеры!!!  Моржовый оператор/Walrus
"""
# Пример 1

# Без Моржика
n = 10
print(5 <= n < 10 or 101 < n < 201)          # -> # False
# 1 раз обьявляем Моржика := и потом используем
print(5 <= (с := 10) < 10 or 101 < с < 201)  # -> # False
# Переменная создана
print(с)  # -> 10


# Пример 2
print(f'Если перевернуть слово "{(s:="Hello")}", получится "{s[::-1]}".')
# -> Если перевернуть слово "Hello", получится "olleH".
print(s)  # -> Hello


# Пример 3
# match case и Моржик и несколько переменных сразу
match (a := 7), (b := 4):
    case 7, 4:
        print(6)  # -> 6
    case 10, 5:
        print(10)
    case 6, 3:
        print(4)

print(a, b)  # -> 7 4


# Пример 4
# Напечатайте индекс наименьшего числа в списке.
lst = [5, 8, 3, 2, 7, 4, 9]

print(abs(lst.index(min(lst))))                        # -> 3
print((arr := [5, 8, 3, 2, 7, 4, 9]).index(min(arr)))  # -> 3  # Морж классный  <-----
print(min(range(len(lst)), key=lst.__getitem__))       # -> 3


# Пример 5
# Моржика в условии нельзя
print((nn := 10) + 10 if nn % 2 == 0 else nn - 10)  # -> NameError: name 'n' is not defined
print(nn + 10 if (nn := 10) % 2 == 0 else nn - 10)  # -> 20"""





# Морж Примеры ИНТЕРЕСНЫЕ ПОВТОРИТЬ!!!





# Ответ  Морж Примеры ИНТЕРЕСНЫЕ ПОВТОРИТЬ!!!
"""
# Повторно используется только результат `func()`:
result = [y := func(x), y**2, y**3]
Да, можно просто добавить y = func(x) перед объявлением списка, и тогда не нужен оператор walrus, но это одна
дополнительная ненужная строка кода.

# Тоже самое
x = 10
func = lambda x: x*2
result = [y := func(x), y ** 2, y ** 3]
print(result)  # -> [20, 400, 8000]

# Тоже самое
x = 10
func = lambda x: x*2
y = func(x)
result = [y := func(x), y ** 2, y ** 3]
print(result)  # -> [20, 400, 8000]



# МОРЖ СОКРАЩАЕТ ВЫЗОВ ФУНКЦИИ
data = [1, 2, 3]
# `func()` вызывается 2 раза
result = [func(x) for x in data if func(x)]
print(result)  # -> [2, 4, 6]
# `func()` вызывается только 1 раз
result = [y for x in data if (y := func(x))]
print(result)  # -> [2, 4, 6]
"""


# Распарсить JSON-строку  json.loads()

json_string = '{"name": "Alice", "age": 30, "city": "New York"}'










# Пример разбора JSON-строки
# 'json.loads()' для разбора JSON-строки.
"""
json_string = '{"name": "Alice", "age": 30, "city": "New York"}'

import json

data = json.loads(json_string)
print(data)          # -> {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(data['name'])  # -> Alice
"""



# Распарсить JSON-файл  json.load()
# Предположим, у вас есть файл 'data.json' с содержимым:
"""
{
    "employees": [
        {"name": "John", "age": 28},
        {"name": "Anna", "age": 22},
        {"name": "Mike", "age": 32}
    ]
}
"""





# Пример разбора JSON из файла
# json.load()` для разбора JSON-данных из файла
# Предположим, у вас есть файл 'data.json' с содержимым:
"""
{
    "employees": [
        {"name": "John", "age": 28},
        {"name": "Anna", "age": 22},
        {"name": "Mike", "age": 32}
    ]
}

import json

# Открытие файла и разбор JSON
with open('data.json', 'r') as file:
    data = json.load(file)

# Вывод результата
print(data)
print(data['employees'][0]['name'])  # "John"
"""


# Используйте метод 'json.dump()' с отступами  'data.json'  Перепишите пример ниже

data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}








# Пример с 'json.dump()' с отступами
# `json.dump()` сериализует объект Python и записывает его в файл в формате JSON.
"""
import json

# Пример данных для сериализации
data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Запись данных в файл в формате JSON
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

print("Данные успешно записаны в файл data.json")
"""


# Используйте метод 'json.dumps()' с отступами   Перепишите пример ниже

data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}






# Пример с 'json.dumps()' с отступами
# `json.dumps()` сериализует объект Python и возвращает его в виде строкового представления JSON.

"""
import json

data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Сериализация данных в строку JSON с отступами
json_string = json.dumps(data, indent=4)

print("Строка JSON с форматированием:")
print(json_string)
"""


# Перепиши Ниже вариант match case  Кортеж/Список Всё Работает так же как и при обычной распаковке '*'

cmd = [1, "Learning", "Python", 2000.78, 5, 3, 5, 10]








# match case  Кортеж/Список Всё Работает так же как и при обычной распаковке '*'
"""
# Всё Работает так же как и при обычной распаковке '*'

cmd = [1, "Learning", "Python", 2000.78, 5, 3, 5, 10]  # 7 Элементов Список
author, title, price, *_ = cmd   # Так будет работать используем *    *_
author, title, price = cmd       # -> ValueError: too many values to unpack (expected 3)
print(author, title, price)      # -> 1 Learning Python


# Ограничить Размер Кортежа/Списка используем guard if     Можно использовать любые скобки () [] или без скобок
match cmd:
    case [_, str() as author, str(title), float() as price, *_] if len(cmd) >= 7 and len(title) < 10:   # guard
        print(f'Список: {author} {title} {price}')
    case _:  # wildcard
        print(f'Непонятный формат данных')
# -> Список: Learning Python 2000.78 [5, 3, 5, 10]


# Так тоже можно валидировать 
cmd = [1, "Learning", "Python", 2000.78, 5, 3, 5, 10]

match cmd:
    case (int(), str(), str(), float(), *ff):
        print(ff)  # -> [5, 3, 5, 10]
"""



# Перепиши Ниже    match case Словарь  dict '**'

json_data = {'id': 2, 'access': True, 'data': ['26.05.2023', {'login': '1234', 'email': 'xxx@mail.com'}, 2000, 56.4]}

def parse_json(data):
    pass


# print(parse_json(json_data))  # -> ('1234', {'email': 'xxx@mail.com'})
# print(parse_json(json_data))  # -> (True, '26.05.2023')







# match case    Словарь  dict '**'
"""
def parse_json(data):
    match data:
        case {'access': bool() as access, 'data': list([date, *_])}:
            return access, date
    return None

json_data = {'id': 2, 'access': False, 'data': ['26.05.2023', {'login': '1234', 'email': 'xxx@mail.com'}, 2000, 56.4]}
print(parse_json(json_data))  # -> (False, '26.05.2023')

# Другой вариант
def parse_json(data):
    match data:
        case {'access': access, 'data': [_, {'login': login, **kwargs}, *_]} if access:
            return login, kwargs

json_data = {'id': 2, 'access': True, 'data': ['26.05.2023', {'login': '1234', 'email': 'xxx@mail.com'}, 2000, 56.4]}
print(parse_json(json_data))  # -> ('1234', {'email': 'xxx@mail.com'})
"""



# Разделить по Нулям(0) и получить сумму  Merge Nodes in Between Zeros   НАПИШИ ВСЕ ВАРИАНТЫ!!!

head = [0, 3, 1, 0, 4, 5, 2, 0]

def mergeNodes(head):
    pass



# print(mergeNodes(head))  # -> [4, 11]




# Разделить по Нулям(0) и получить сумму  Merge Nodes in Between Zeros
r"""
head = [0, 3, 1, 0, 4, 5, 2, 0]

def mergeNodes(head):
    res = re.sub(r'[,\s\]\[]', '', str(head))
    return [eval('+'.join(i)) for i in re.split(r'0', res) if i]

# Тоже самое но с map
def mergeNodes(head):
    res = ''.join([*map(str, head)]).split('0')
    return [sum(map(int, ' '.join(i).split())) for i in res if i]

print(mergeNodes(head))  # -> [4, 11]


# Решение АРСЕНИЯ Live-coding  если в конце нет нулей
def mergeNodes(head):
    summ, res = 0, []
    for val in head:
        if val != 0:
            summ += val
        else:
            if summ != 0:
                res.append(summ)
            summ = 0
    return res

head = [0, 3, 1, 0, 4, 5, 2]
print(mergeNodes(head))  # -> [4]



# Решение АРСЕНИЯ Live-coding   если в конце нет нулей
def mergeNodes(head):
    summ, res = 0, []
    for val in head:
        if val != 0:
            summ += val
        else:
            if summ != 0:
                res.append(summ)
            summ = 0
    if summ != 0:
        res.append(summ)
    return res
print(mergeNodes(head))  # -> [4, 11]


# ДОПОЛНИТЕЛЬНЫЕ ВАРИАНТЫ РЕШЕНИЯ

# Вариант 1: Использование генераторов и itertools
from itertools import groupby

def mergeNodes(head):
    return [sum(group) for key, group in groupby(head, key=lambda x: x != 0) if key]

head = [0, 3, 1, 0, 4, 5, 2, 0]
print(mergeNodes(head))  # -> [4, 11]



# Вариант 2: С использованием флага для отслеживания между нулями
def mergeNodes(head):
    res = []
    between_zeros = False
    current_sum = 0

    for num in head:
        if num == 0:
            if between_zeros:
                res.append(current_sum)
                current_sum = 0
            between_zeros = True
        else:
            current_sum += num

    return res


head = [0, 3, 1, 0, 4, 5, 2, 0]
print(mergeNodes(head))  # -> [4, 11]



# Вариант 3: Функциональный стиль с reduce
from functools import reduce

def mergeNodes(head):
    def reducer(acc, val):
        sums, current = acc
        if val == 0:
            if current != 0:
                sums.append(current)
            return (sums, 0)
        return (sums, current + val)
    
    sums, _ = reduce(reducer, head, ([], 0))
    return sums

head = [0, 3, 1, 0, 4, 5, 2, 0]
print(mergeNodes(head))  # -> [4, 11]



# Вариант 4: Итеративный подход с двумя указателями
def mergeNodes(head):
    res = []
    left = 0
    
    # Пропускаем начальные нули
    while left < len(head) and head[left] == 0:
        left += 1
    
    right = left
    while right < len(head):
        if head[right] == 0:
            res.append(sum(head[left:right]))
            left = right + 1
        right += 1
    
    return res

head = [0, 3, 1, 0, 4, 5, 2, 0]
print(mergeNodes(head))  # -> [4, 11]



# Вариант 5: С использованием deque
from collections import deque

def mergeNodes(head):
    q = deque(head)
    res = []
    current_sum = 0
    
    while q:
        num = q.popleft()
        if num == 0:
            if current_sum != 0:
                res.append(current_sum)
                current_sum = 0
        else:
            current_sum += num
    
    return res

head = [0, 3, 1, 0, 4, 5, 2, 0]
print(mergeNodes(head))  # -> [4, 11]
"""




# Интересный пример Повтори кстати сам его придумал  a = 'aaaabbсaa' преобразуется в 'a4b2с1a2'

a = 'aaaabbcaa'









# a = 'aaaabbсaa' преобразуется в 'a4b2с1a2'  Считаем символы которые идут подряд
r"""
a = 'aaaabbcaa'

# Придумал сам)
re.sub(r'(\w)\1+|\w', lambda x: f'{x[0][0]}{len(x[0])}', a)  # -> a4b2c1a2
"""






# Так можно разделить легко  Повтори

text = r'17383147371'









# Ответ Так можно разделить легко  Повтори
# Разделит число из тестовых данных на числа, в конце которых стоит единица. 1
r"""
text = r'17383147371'

print(re.findall(r'\d*?1', text))  # -> ['1', '73831', '47371']
print(re.findall(r'\d*1', text))   # -> ['17383147371']          Без ?
"""




# Интересные квантификаторы  жадные НЕ жадные

res = '12345'








# Ответ Интересные квантификаторы  жадные НЕ жадные
r"""
res = '12345'
print(re.search(r'\d{,3}', res).group())  # -> 123
print(re.search(r'\d{3,}', res).group())  # -> 12345
print(re.search(r'\d{3,}?', res).group())  # -> 123

print(re.findall(r'\d{,3}', res))         # -> ['123', '45', '']
print(re.findall(r'\d{3,}', res))         # -> ['12345']
print(re.findall(r'\d{3,}?', res))        # -> ['123']
"""

# Классный пример Повтори   По сути это if...else в Регулярках

text = 'ABC'








# По сути это if...else в Регулярках
"""
# Если находим A значит ищем B иначе ищем C     1 - Номер группы
re.search(r"(A)?(?(1)B|C)", 'ABC')  # -> <re.Match object; span=(0, 2), match='AB'>
re.search(r"(A)?(?(1)B|C)", 'BC')  # -> <re.Match object; span=(1, 2), match='C'>

# Можно и без последнего условия  Шаблон после | необязателен и может быть опущен.
re.search(r"(A)?(?(1)B)", 'ABC')  # -> <re.Match object; span=(0, 2), match='AB'>
re.search(r"(A)?(?(1)B)", 'BC')  # -> <re.Match object; span=(1, 2), match='C'>

# Если находим A значит ищем B иначе ищем C     name - Имя группы
print(re.search(r"(?P<name>A)(?(name)B|C)", 'ABC').group())   # -> AB
print(re.search(r"(?P<name>A)(?(name)BC)", 'ABC').group())    # -> ABC
"""



# Используйте \b \B

text = 'арка чарка аркан баварка знахарка'









# Ответ Используйте \b \B
r"""
text = 'арка чарка аркан баварка знахарка'

# Найти конкретное слово     '\b'
print(re.findall(r'\bарка\b', text))   # -> ['арка']                           <-----

# Найти конкретное слово     '\b'
print(re.findall(r'\Bарка', text))     # -> ['арка', 'арка', 'арка']           <-----

# Найти все слова которые НАЧИНАЮТСЯ с выбранного значения
print(re.findall(r'\bарка', text))     # -> ['арка', 'арка']                  <-----
print(re.findall(r'\bарка\w*', text))  # -> ['арка', 'аркан']                 <-----

# Найти все слова которые ЗАКАНЧИВАЮТСЯ  выбранным значением
print(re.findall(r'арка\b', text))     # -> ['арка', 'арка', 'арка', 'арка']           <-----
print(re.findall(r'\w*арка\b', text))  # -> ['арка', 'чарка', 'баварка', 'знахарка']   <-----


# Сравнение '\B' и '\b'        '\B'  противоположность '\b'
print(re.findall(r'py\B', 'python py3 py2'))  # -> ['py', 'py', 'py']   # В таких найдёт     <-----
print(re.findall(r'py\B', 'py py. py!'))      # -> []                   # В таких НЕ найдёт  <-----

print(re.findall(r'py\b', 'python py3 py2'))  # -> []                   # В таких НЕ найдёт  <-----
print(re.findall(r'py\b', 'py py. py!'))      # -> ['py', 'py', 'py']   # В таких найдёт     <-----
"""





# Используйте re.compile 2 Способа

text = 'ABC123---'






# Использование re.compile 2 Способа
"""
regex = re.compile("[A-Za-z_]"      # letter or underscore             буква или подчеркивание
                   "[A-Za-z0-9_]*"  # letter, digit or underscore      буква, цифра или подчеркивание
                   )
re.findall(regex, 'ABC123---')  # -> ['ABC123']

# Тоже самое
regex.findall('ABC123---')  # -> ['ABC123']
"""



# Использовать flags=re.VERBOSE  (?x)   Можно ставить комменты внутри регулярки  и пробелы не работают

text = '4G22ABC'








# Ответ flags=re.VERBOSE  (?x)   Можно ставить комменты внутри регулярки  и пробелы не работают
r"""
text = '4G22ABC'
test1 = re.findall(r'''[1-9]+    # Любая цифра, кроме 0
                   .           # Любой символ, кроме новой строки
                   \d {2,}     # Любая цифра''', text, flags=re.VERBOSE)
                   
print(test1)                  # -> ['4G22']


pattern = re.compile(r'''(?x)
\d+
''')
print(pattern.findall(text))  # -> ['4', '22']
"""




# Поменяйте местами в регулярке использую Обычные/Именованные группы или Перепишите

text = 'ABC 123'







# Замена по индексу группы: '\1' '\2'    МЕЖДУ/ПЕРЕД/ПОСЛЕ групп можно использовать любые знаки
r"""
text = 'ABC 123'

re.sub(r'(\w+)\s*(\d+)', r'+__\2  \1 !!+',  'ABC 123')                            # -> +__123  ABC !!+   # Поменяли местами
re.sub(r'(?P<ddd>\w+)\s*(?P<dd>\w+)', r'+__\2  \1 !!+',  'ABC 123')               # -> +__123  ABC !!+   # Тоже самое

# Замена по Имени группы:   '\g<name>'
re.sub(r'(?P<first>\w+)\s*(?P<second>\d+)', r'\g<second> \g<first>',  'ABC 123')  # -> 123 ABC   # Поменяли местами


# Интересный момент Посмотри вывод!
text = 'ABC 123'

print(re.sub(r'(\w)\s(\w)', r'\2  ---  \1', text))                      # -> AB1  ---  C23
print(re.sub(r'(?P<s1>\w)\s(?P<s2>\w)', r'\g<s2>  ---  \g<s1>', text))  # -> AB1  ---  C23

# Группы можно использовать как угодно и сколько угодно!
print(re.sub(r'(\w)\s(\w)', r'\2\1  ---  \1\1\1', text))                # -> AB1C  ---  CCC23
"""



# Напишите или Перепишите Обычные/Именованные группы

text = r'ggg wp'








# Обычные/Именованные группы
"""
text = r'ggg wp'
re.search(r'([a-zA-Zа-яА-ЯёЁ])\1\1', text).group()                           # -> ggg
re.search(r'([a-zA-Zа-яА-ЯёЁ])\1', text).group()                             # -> gg

# Тоже самое
re.search(r'(?P<first>[a-zA-Zа-яА-ЯёЁ])(?P=first)', text).group()            # -> gg
re.search(r'(?P<first>[a-zA-Zа-яА-ЯёЁ])(?P=first)(?P=first)', text).group()  # -> ggg

# В findall так НЕ РАБОТАЕТ
re.findall(r'([a-zA-Zа-яА-ЯёЁ])\1', text)                                    # -> ['g']
re.findall(r'([a-zA-Zа-яА-ЯёЁ])\1\1', text)                                  # -> ['g']
"""


# Напишите Обычную группу и  группу БЕЗ Захвата

text = "abc123"








# Группа С захватом ()   Группа БЕЗ захвата   (?:)
r"""
re.findall("([abc])+", "abc")    # -> ['c']     # Группа С захватом
re.findall("(?:[abc])+", "abc")  # -> ['abc']   # Группа БЕЗ захвата   (?:)

# Интересный момент с плюсом + 
print(re.findall(r'(?:\w)(\w+)', text))         # -> ['bc123']
print(re.findall(r'(?:\w)(\w)+', text))         # -> ['3']
"""


# Напишите   Lookahead   Lookbehind

text = '123ABC'








# Lookahead   Lookbehind
# x(?=y) находит x, только если за x следует y             # Positive Lookahead
# x(?!y) находит x, только если за x НЕ следует y          # Negative Lookahead
# (?<=y)x находит x, только если перед x следует y         # Positive Lookbehind
# (?<!y)x находит x, только если перед x НЕ следует y      # Negative Lookbehind
r"""
text = '123ABC'
print(re.findall(r'\d+(?=[A-Z])', text))   # -> ['123']
print(re.findall(r'\d+(?!\d+)', text))     # -> ['123']
print(re.findall(r'(?<=^)\d+', text))      # -> ['123']
print(re.findall(r'(?<!$)[A-Z]+', text))   # -> ['ABC']
"""



# Нужно найти последовательности из 2 одинаковых арабских цифр


text = r'6996966969'








# Ответ Нужно найти последовательности из 2 одинаковых арабских цифр
r"""
text = r'6996966969'

print(re.findall(r'(\d{2})\1', text))    # -> ['96', '69']
print(re.findall(r'([\d]{2})\1', text))  # -> ['96', '69']
"""



# Замените два повторяющиеся слова на одно.


text = 'Нужно удалять удалять повторяющиеся слова слова.'








# Ответ Замените два повторяющиеся слова на одно.
r"""
text = 'Нужно удалять удалять повторяющиеся слова слова.'

print(re.sub(r'([а-яё]+)\s\1', r'\1', text))                   # ->  Нужно удалять повторяющиеся слова.
print(re.sub(r'(?P<name>\w+)\s(?P=name)', r'\g<name>', text))  # ->  Нужно удалять повторяющиеся слова.
"""




# Перепиши ниже Обновление Словаря/Множества

a_dict = {"a": 2}
b_dict = {"b": 3}

a_set = {"a", 2}
b_set = {"b", 3}






# Ответ Обновление Словаря/Множества
"""
# Обновление словаря
a_dict = {"a": 2}
a_dict.update({"b": 10})
print(a_dict)  # -> {'a': 2, 'b': 10}

# Обновление множества
a_set = {"a", 2}
a_set.update({"b": 10})
print(a_set)  # -> {'a': 2, 'b': 10}

a_set.update([1, 2], (3, 4))
print(a_set)  # -> {1, 2, 'b', 3, 4, 'a'}
"""


# Перепиши ниже Обьединение *   Объединения **   |

A = [1, 2, 3]  # list
B = (4, 5, 6)  # tuple
C = {7, 8, 9}  # set

a = {"w": 5, "x": 6}
b = {"y": 7}







# Обьединение *   Объединения **   |

"""
from itertools import chain
# Обьединение *
A = [1, 2, 3]  # list
B = (4, 5, 6)  # tuple
C = {7, 8, 9}  # set
L = [*A, *B, *C]
G = list(chain(A, B, C))
G = [*chain(A, B, C)]    # Тоже самое
print(L)  # -> [1, 2, 3, 4, 5, 6, 8, 9, 7]
print(G)  # -> [1, 2, 3, 4, 5, 6, 8, 9, 7]


# Объединения **
a = {"w": 5, "x": 6}
b = {"y": 7}
c = {"z": 8, **a, **b}
print(c)  # -> {'z': 8, 'w': 5, 'x': 6, 'y': 7}

# Тоже самое
c = {"z": 8}
c = c | a | b
print(c)  # -> {'z': 8, 'w': 5, 'x': 6, 'y': 7}
"""




# Устранить дубликаты и оставить Порядок элементов  fromkeys






# ОТВЕТ  Устранить дубликаты и оставить Порядок элементов  fromkeys
"""
my_lst = [10, 10, 10, 2, 3]
# Порядок НЕ УПОРЯДОЧЕННЫЙ!!!
print(set(my_lst))                         # -> {3, 10, 2}

# Сохраняем порядок
print(dict.fromkeys(my_lst).keys())        # -> dict_keys([10, 2, 3])
print(list(dict.fromkeys(my_lst).keys()))  # -> [10, 2, 3]
"""





# Интересные распаковки ПОВТОРИТЬ!   В конце ПОСМОТРИ Примеры!!!









# Ответ Интересные распаковки ПОВТОРИТЬ!   В конце ПОСМОТРИ Примеры!!!
"""
# слева при распаковке должен стоять кортеж.
*values, = [1, 2, 3, 4, 5]
print(values)         # -> [1, 2, 3, 4, 5]

*values, val_1 = [1, 2, 3, 4, 5]
print(val_1)          # -> 5
print(values, val_1)  # -> [1, 2, 3, 4] 5

*a, b, c = 1, 2
print(a, b, c)  # -> [] 1 2


# ПРОСТО ПОСМОТРЕТЬ!!!                                                                          <-----
# РАБОТАЕТ
a, *b, c = [4, 4]
print(a, b, c)  # -> 4 [] 4

# НЕ ХВАТАЕТ ЗНАЧЕНИЙ
a, *b, c = [4]
print(a, b, c)  # -> ValueError: not enough values to unpack (expected at least 2, got 1)

# Два оператора НЕЛЬЗЯ
a, *b, *c = [4]
print(a, b, c)  # -> SyntaxError: multiple starred expressions in assignment
"""



# Написать решение чтобы каждый раз создавался новый обьект
# default  Аргументы по умолчанию в функциях:
"""
def f(a, L=[]):                       def f(a, L=set()):                    def f(key, value, L={}):
    L.append(a)                             L.add(a)                              L[key] = value
    return L                                return L                              return L
print(f.__defaults__) # -> ([],)      print(f.__defaults__) # -> (set(),)   print(f.__defaults__) # -> ({},)
print(f(1))           # -> [1]        print(f(1))           # -> {1}        print(f(1, 'A'))      # -> {1: 'A'}
print(f.__defaults__) # -> ([1],)     print(f.__defaults__) # -> ({1},)     print(f.__defaults__) # -> ({1: 'A'},)
print(f(2))           # -> [1, 2]     print(f(2))           # -> {1, 2}     print(f(2, 'B'))      # -> {1: 'A', 2: 'B'}
print(f.__defaults__) # -> ([1, 2],)  print(f.__defaults__) # -> ({1, 2},)  print(f.__defaults__) # -> ({1: 'A', 2: 'B'},)
"""









# Способ обойти это - использовать None по умолчанию и явно проверить его в теле функции:
"""
# list                               # set                                   # dict
def f(a, L=None):                    def f(a, L=None):                       def f(key, value, L=None):
    if L is None:                        if L is None:                           if L is None:
        L = []                               L = set()                               L = {}
    L.append(a)                          L.add(a)                                L[key] = value
    return L                             return L                                return L
print(f.__defaults__) # -> (None,)   print(f.__defaults__) # -> (None,)      print(f.__defaults__) # -> (None,)
print(f(1))           # -> [1]       print(f(1))           # -> {1}          print(f(1, 'A'))      # -> {1: 'A'}
print(f.__defaults__) # -> (None,)   print(f.__defaults__) # -> (None,)      print(f.__defaults__) # -> (None,)
print(f(2))           # -> [2]       print(f(2))           # -> {2}          print(f(2, 'B'))      # -> {2: 'B'}
print(f.__defaults__) # -> (None,)   print(f.__defaults__) # -> (None,)      print(f.__defaults__) # -> (None,)
"""


# Напишите функцию с docstring/name. Выведите документацию и название функции










# Ответ docstring/name
'''
def add_numbers(a, b):
    """This function takes in two numbers and returns their sum"""
    return a + b

print(add_numbers.__doc__)   # -> This function takes in two numbers and returns their sum
print(add_numbers.__name__)  # -> add_numbers
'''


# Напишите Итератор  range(10)  iter







# Итератор  range(10)  iter
"""
# Итератор
it = iter([i*i for i in range(10)])


it = iter([i for i in range(10)])
print(*it)    # -> 0 1 2 3 4 5 6 7 8 9
it = iter([i for i in range(10)])
print([*it])  # -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""


# Напишите Функцию-Генератор  range(5) и Обычный генератор








# Функцию-Генератор  range(5) и Обычный генератор
"""
# Генератор
def generate_ints(N):
    for i in range(N):
        yield i

for i in generate_ints(5):
    print(i, end=' ')  # -> 0 1 2 3 4

res = generate_ints(2)
print(next(res))
print(next(res))
print(next(res, 'HEHEHE'))  # -> HEHEHE
print(next(res))            # -> StopIteration

# Тоже самое
generate_ints = (i for i in range(5))
print(generate_ints)               # <generator object <genexpr> at 0x000001790AACC040> 

# Можно сразу в принте написать
print(i for i in range(5))         # <generator object <genexpr> at 0x000001790AACD220>     
"""


# Напишите Конструкцию yield from и ЕЁ аналог










# yield from  - это просто сокращенная форма for item in iterable: yield item
"""
def gen_list1(iterable):
    for i in list(iterable):
        yield i

# эквивалентно

def gen_list2(iterable):
    yield from list(iterable)

print(list(gen_list1('python')))  # -> ['p', 'y', 't', 'h', 'o', 'n']
print([*gen_list2('python')])     # -> ['p', 'y', 't', 'h', 'o', 'n']
"""



# Напишите Функцию-Генератор  range(1, 5) и Обычный генератор  range(1, 5)









# Функцию-Генератор  range(1, 5) и Обычный генератор  range(1, 5)
"""
# Например, такой генератор, как:
def squares(start, stop):
   for i in range(start, stop):
       yield i * i

generator = squares(1, 5)
print([i for i in generator])  # -> [1, 4, 9, 16]



# или эквивалентное выражение генератора (genexp)
generator = (i*i for i in range(1, 5))
print([i for i in generator])  # -> [1, 4, 9, 16]
"""




# Как перевернуть генератор/итератор?

my_list = [1, 2, 3, 4, 5]
my_generator = (x**2 for x in my_list)








# Ответ Как перевернуть генератор/итератор?    reversed(list)
"""
# Что будет на выходе ПОСМОТРИ
my_list = [1, 2, 3, 4, 5]
my_generator = (x**2 for x in my_list)

print(reversed(list(my_generator)))  # -> <list_reverseiterator object at 0x000001C4286F3A00>
print(my_generator)                  # -> <generator object <genexpr> at 0x000001CA17B23850>
print(list(my_generator))            # -> []
"""




# Cоздайте свой Итератор








# Пример создания итератора Iterator:
"""
class SimpleIterator:
    def __iter__(self):
        return self

    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            ret = self.counter
            self.counter += 1
            return ret
        else:
            raise StopIteration

iters = SimpleIterator(4)

print('Функция next:', next(iters))
# Функция next: 0

for i in iters:
   print('Цикл for ... in: ', i)
# Цикл for ... in:  1
# Цикл for ... in:  2
# Цикл for ... in:  3

next(iters)
# StopIteration
"""


# Для создания пользовательского итератора потребуется больше кода:
"""
class Squares(object):
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):  # next in Python 2
        if self.start >= self.stop:
            raise StopIteration
        current = self.start * self.start
        self.start += 1
        return current


iterator = Squares(1, 3)
for i in iterator:
    print(i, end=' ')    # -> 1 4

# Генератор — это итератор В частности, генератор является подтипом итератора.

print(issubclass(collections.abc.Generator, collections.abc.Iterator))  # -> True
print(issubclass(types.GeneratorType, collections.abc.Iterator))        # -> True
"""


# eval vs exec   compile   Можно просто посмотреть





# Ответ eval vs exec   compile   Можно просто посмотреть
"""
Интересный пример
exec("print(aaaa)", globals(), {'aaaa': 42})  # -> 42
eval("print(aaaa)", globals(), {'aaaa': 42})  # -> 42


a = 5
# Возвращает Результат
print(eval('37 + a'))  # -> 42
# Возвращает None
print(exec('37 + a'))  # -> None

# exec Может создать переменную
print(exec('a = 47'))  # -> 47
# eval НЕ Может создать переменную
# print(eval('a = 47'))  # -> SyntaxError: invalid syntax


# eval() НЕ Будет работать!
x = eval('x = 5')  # INVALID; assignment is not an expression.
x = eval('if 1: x = 4')  # INVALID; if is a statement, not an expression.

# exec() Будет работать!
exec('x = 5')
print(x)  # -> 5
x = exec('if 1: x = 4')
print(x)  # -> None


# Выполняет блок кода exec()        # Ошибка eval()
program = '''                       program = '''                            
for i in range(2):                  for i in range(2):                            
    print("Python, sep=' '")            print("Python, sep=' '")                            
'''                                 '''                            
exec(program)                       eval(program)  # -> SyntaxError: invalid syntax                            
# Python, sep=' '                                   
# Python, sep=' '    

# Работает
exec(compile('for i in range(3): print(i, end=" ")', filename='<string>', mode='exec'))   # -> 0 1 2

# compile вызывает исключение, если исходный код содержит операторы или что-либо еще, кроме одного выражения:
# eval(compile('for i in range(3): print(i, end=" ")', filename='<string>', mode='eval'))
# for i in range(3): print(i)
#     ^^^
# SyntaxError: invalid syntax

# Работает
compiled_exec = compile('print("Hello")',  filename='<string>', mode='exec')
exec(compiled_exec)  # -> Hello
compiled_eval = compile('print("Hello")',  filename='<string>', mode='eval')
eval(compiled_eval)  # -> Hello                     
"""

# Напишите Замыкание или Перепишите







# Замыкание
"""
def names():
    all_names = []

    def inner(name: str) -> list:
        all_names.append(name)
        return all_names
    return inner

boys = names()
boys('Vasya')
boys('Sasya')
print(boys.__closure__[0].cell_contents)  # -> ['Vasya', 'Sasya']

# Интересно как работает
print(names()((lambda x: x+5)(2)))        # -> [7]
"""


# Напишите Замыкание lambda или Перепишите








# Замыкание lambda
"""
def pow_(base):
    return lambda value: value ** base

res = pow_(2)
print(res(2))  # -> 4


# Тоже самое но вызов сразу
def pow_(base):
    return lambda x: x**base

print(pow_(2)(3))  # -> 9
"""



# Напишите Замыкание class vs def    Реализация своей функции avg






# Ответ Замыкание class vs def   Реализация своей функции avg
"""
# Замыкание class vs def    Реализация своей функции avg

# Функция НЕЭФФЕКТИВНА              # ЭФФЕКТИВНА                               # Через КЛАСС
def make_averager():                def make_averager():                       class Averager:
    series = []                         total = 0                                  def __init__(self):
                                        count = 0                                      self.series = []
    def averager(new_value):
        series.append(new_value)        def averager(new_value):                   def __call__(self, new_value):
        total = sum(series)                 nonlocal total, count                      self.series.append(new_value)
        return total / len(series)          count +=1                                  total = sum(self.series)
    return averager                         total += new_value                         return total / len(self.series)
                                            return total/count
avg = make_averager()                   return averager                        avg = Averager()
print(avg(10))  # -> 10.0                                                      print(avg(10))  # -> 10.0
print(avg(11))  # -> 10.5                                                      print(avg(11))  # -> 10.5
print(avg(12))  # -> 11.0                                                      print(avg(12))  # -> 11.0                               
 
# __code__ Откомпилированное ТЕЛО ФУНКЦИИ
print(avg.__code__.co_varnames)          # -> ('new_value', 'total')  # Локальные переменные функции
print(avg.__code__.co_freevars)          # -> ('series',)             # Свободные переменные замыкания
print(avg.__closure__[0].cell_contents)  # -> [10, 11, 12]            # Текущее содержимое                           
"""





# Напишите лямбда-функцию с присвоением переменной и без. Сразу вызов







# Ответ lambda
"""
double = lambda x: x * 2
print(double(2))             # -> 4

# Тоже самое сразу вызываем функцию  Оборачиваем в ()
print((lambda x: x * 2)(2))  # -> 4


# Функцию Прибавили
res = lambda: 5
print((lambda x: x+res())(10))  # -> 15

# Можно использовать много +/++++ Разницы НЕТ
print((lambda y: y+2)(3))         # -> 5
print((lambda y: y++2)(3))        # -> 5
print((lambda y: y++++++++2)(3))  # -> 5

# Можно использовать много -/---- Разницы Есть!! четное количество - равно +     НЕ четное количество - равно -
print((lambda x: x-2)(3))     # -> 1
print((lambda x: x--2)(3))    # -> 5
print((lambda x: x---2)(3))   # -> 1
print((lambda x: x----2)(3))  # -> 5
"""





# Написать Lambda function in list comprehensions  Лямбда+ф-строка в Listcomps







# Ответ Lambda function in list comprehensions  Лямбда+ф-строка в Listcomps
"""
Lambda function in list comprehensions  Лямбда+ф-строка в Listcomps:
f = lambda x: x*x
[f(x) for x in range(5)]                # -> [0, 1, 4, 9, 16]
[f"{f(x)}" for x in range(5)]           # -> ['0', '1', '4', '9', '16']  ПРИМЕР с   f-string

[(lambda x: x**2)(i) for i in range(5)] # -> [0, 1, 4, 9, 16]
[i**2 for i in range(5)]                # -> [0, 1, 4, 9, 16]
"""






# Повторите разные сортировки  lambda  и  itemgetter, attrgetter   methodcaller  <---- НЕ ЗАБУДЬ !!!
from operator import itemgetter, attrgetter, methodcaller

ints = list(range(20))






a_dict = {'a': 3, 'b': 2, 'd': 1, 'c': 4}







class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Cat {self.name}, age is {self.age}'

    def greet(self, name, age=None):
        return f"Hello, {name}! Age: {age} {self.name}"


cats = [Cat('Tom', 3), Cat('Angela', 4)]



# methodcaller






# Ответ Повторите разные сортировки  lambda  и  itemgetter, attrgetter   methodcaller
# Ответ Разные Сортировки operator/lambda  Просто перепиши
"""
from operator import attrgetter, itemgetter, methodcaller

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Cat {self.name}, age is {self.age}'
        
    def greet(self, name, age=None):
        return f"Hello, {name}! Age: {age} {self.name}"
        

if __name__ == '__main__':
    ints = list(range(20))
    print(list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, ints)))) # [0, 4, 16, 36, 64, 100, 144, 196, 256, 324]
    print([i ** 2 for i in range(20) if i % 2 == 0])                       # [0, 4, 16, 36, 64, 100, 144, 196, 256, 324]

    a_dict = {'a': 3, 'b': 2, 'd': 1, 'c': 4}
    print(sorted(a_dict.items(), key=lambda x: x[0]))                # -> [('a', 3), ('b', 2), ('c', 4), ('d', 1)]
    print(sorted(a_dict.items(), key=itemgetter(1)))                 # -> [('d', 1), ('b', 2), ('a', 3), ('c', 4)]
    
    # Двойная сортировка в кортеже - Унарный минус работает только с числами!!! Работает как  reverse=True  Но к элементу
    print(sorted(a_dict.items(), key=lambda x: (-x[1], x[0])))       # -> [('c', 4), ('a', 3), ('b', 2), ('d', 1)]
    
    cats = [Cat('Tom', 3), Cat('Angela', 4)]
    print(sorted(cats, key=lambda x: x.age))                         # -> [Cat Tom, age is 3, Cat Angela, age is 4]                    
    print(sorted(cats, key=attrgetter('age')))                       # -> [Cat Tom, age is 3, Cat Angela, age is 4]                    
    print(sorted(cats, key=attrgetter('name')))                      # -> [Cat Angela, age is 4, Cat Tom, age is 3]
    
    greet_method = operator.methodcaller('greet', 'Alice', age=30)   # Тоже самое что и НИЖЕ
    print(greet_method(cats[1]))                                     # -> Hello, Alice! Age: 30 Angela
    print(operator.methodcaller('greet', 'Alice', age=30)(cats[0]))  # -> Hello, Alice! Age: 30 Tom
"""




# Написать Решение с nonlocal и Решение с global   Переписать решение выше чтобы НЕ было ошибки
# Ошибка UnboundLocalError:
"""
# Пример ошибки nonlocal:           Пример ошибки global:
x = 10                              x = 10
def foo():                          def foo():
    x = 10                              print(x)
    def bar():                          x += 1
        print(x)                    foo()
        x += 1                      # UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
    bar()
    print(x)
foo()
# UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
"""








# Ответ
"""
# Решение с nonlocal:                       Решение с global:
x = 10                                      x = 10
def foo():                                  def foo():
    x = 10                                      global x, z    # МОЖЕТ создать z 
    def bar():                                  print(x)
        nonlocal x # не может создать z         x += 1
        print(x)                                z = 100
        x += 1
    bar()
    #print(x)                               foo()    # -> 10
foo()      # -> 10, 11                      print(x) # -> 11   меняет x
print(x)   # -> 10  не меняет x             print(z) # -> 100  СОЗДАЕТ z
"""



# Использовать heapq       Можно найти минимальный или максимальный элемент

h = [20, 10, 1, 2]











# Пример heapq
"""
import heapq
h = [20, 10, 1]
print(h)          # -> [20, 10, 1]
heapq.heapify(h)  # создаем кучу(heap)
print(h)          # -> [1, 10, 20]
print(h[0])       # -> 1
heapq.heappop(h) 
print(h)          # -> [10, 20]
print(h[0])       # -> 10

# Мин/Мах элементы первый параметр сколько элементов нужно вывести
h = [20, 10, 1]
print(heapq.nsmallest(2, h))  # -> [1, 10]
print(heapq.nlargest(2, h))   # -> [20, 10]
"""



# Использовать heapq   Написать    MaxHeap/MinHeap


minheap = [20, 10, 1, 2]






maxheap = [20, 10, 1, 2]





# Ответ Использовать heapq   Написать    MaxHeap/MinHeap     _heapify_max или умножение на -1 или добавить - к числу
"""
import heapq

# MinHeap
minheap = [20, 10, 1, 2]
heapq.heapify(minheap)
print(minheap[0])                     # -> 1
print(heapq.heappop(minheap))         # -> 1


# MaxHeap  через метод _heapify_max
maxheap = [20, 10, 1, 2]
heapq._heapify_max(maxheap)
print(maxheap[0])                     # -> 20
print(heapq.heappop(maxheap))         # -> 20


# MaxHeap   через добавление минуса
maxheap_2 = [20, 10, 1, 2]
res = [-i for i in maxheap_2]
print(res)                            # -> [-20, -10, -1, -2]
heapq.heapify(res)
print(res[0])                         # -> -20
print(heapq.heappop(res))             # -> -20


# MaxHeap   через умножение на -1
maxheap_3 = [20, 10, 1, 2]
res = [i*(-1) for i in maxheap_3]
heapq.heapify(res)
print(res[0])                         # -> -20
print(heapq.heappop(res))             # -> -20
"""



# Написать Рекурсию сумма Входного списка  Проверьте assert








# Пример Рекурсия со Списком(list):
"""
def my_sum(a_list: list) -> int:
   if not a_list:
       return 0
   if len(a_list) == 1:
       return a_list[0]
   return a_list[0] + my_sum(a_list[1:])


if __name__ == '__main__':
    print(my_sum([10, 20, 30]))  # -> 60
    assert my_sum([]) == 0
    assert my_sum([1]) == 1
    assert my_sum([-1]) == -1
    assert my_sum([2, 2]) == 4
    assert my_sum([1, 2, 3]) == 6
"""



# Блок Задач на РЕКУРСИЮ   Кстати если внутри функций назвать list  - Всё будет ОК!
# Затеняются только внутри функции built-in имена

lst = [1, 2, 3]

# 1) Напишите рекурсивную функцию sum




# 2) Напишите рекурсивную функцию count для подсчета элементов в списке.





# 3) Через РЕКУРСИЮ max Найдите наибольшее число в списке.





# Ответы Блок Задач на РЕКУРСИЮ   если внутри функций назвать list  - Всё будет ОК!
# Затеняются только внутри функции built-in имена
"""
lst = [1, 2, 3]

# 1) Напишите РЕКУРСИВНУЮ функцию sum
def sum(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])

print(sum(lst))  # -> 6

# 2) Напишите РЕКУРСИВНУЮ функцию count для подсчета элементов в списке.
def count(list):
    if list == []:
        return 0
    return 1 + count(list[1:])

print(count(lst))  # -> 3

# 3) Через РЕКУРСИВНУЮ функцию max Найдите наибольшее число в списке.
def max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max(list[1:])
    return list[0] if list[0] > sub_max else sub_max

print(max(lst))   # -> 3
"""




# Использовать  from memory_profiler import memory_usage   и   from pympler.asizeof import asizeof







# Ответ Использовать  from memory_profiler import memory_usage   и   from pympler.asizeof import asizeof
"""
from memory_profiler import memory_usage

def my_function():
    return [i for i in range(1000000)]

if __name__ == '__main__':
    # Измерение использования памяти
    mem_usage = memory_usage(my_function)
    print(f"Peak Memory Usage: {max(mem_usage)} MiB")  # -> Peak Memory Usage: 79.70703125 MiB
    
    
from pympler.asizeof import asizeof                                                 <-----   <----- Интересный импорт

# Создание списка
my_list = [i for i in range(1000000)]

# Измерение размера объекта
size = asizeof(my_list)
print(f"Size of my_list: {size} bytes")                # -> Size of my_list: 20224368 bytes
"""




# Использовать __slots__ Написать класс  no_slots/with_slots  Замерить размер структур  asizeof.asizeof/sys.getsizeof











# Ответ Использовать __slots__ Написать класс  no_slots/with_slots  Замерить размер структур  asizeof.asizeof/sys.getsizeof
"""
import sys
from pympler import asizeof

class NoSlots: pass
class WithSlots: __slots__ = ('a', 'b', 'c')

no_slots = NoSlots()
with_slots = WithSlots()

print(sys.getsizeof(with_slots))          # -> 56    # sys.getsizeof не учитывается «содержимое объекта», такое как словарь:
print(sys.getsizeof(no_slots))            # -> 56    # sys.getsizeof не учитывается «содержимое объекта», такое как словарь:
print(sys.getsizeof(no_slots.__dict__))   # -> 296   # Разница в потреблении памяти     БЕЗ __slots__
print(asizeof.asizeof(no_slots.__dict__)) # -> 296   # Разница в потреблении памяти     БЕЗ __slots__
print(asizeof.asizeof(no_slots))          # -> 352   # Разница в потреблении памяти     БЕЗ __slots__
print(asizeof.asizeof(with_slots))        # -> 56    # Разница в потреблении памяти     __slots__
print(no_slots.__dict__)                  # -> {}    Есть __dict__    БЕЗ __slots__



# Демонстрация __slots__ :
class Child:                                                class Child:
    __slots__ = ()  # Нельзя создавать атрибуты                 __slots__ = ('name',)  # Можно создать только указанные
b = Child()                                                 b = Child()
b.name = 'a'                                                b.name = 'a'
# AttributeError: 'Child' object has no attribute 'name'    b.name  # -> a
"""


# Использовать __slots__ в dataclasses







# __slots__ в dataclasses
"""
from dataclasses import dataclass

@dataclass(slots=True)
class Point:
    x: int = 0
    y: int = 0

p = Point()
p.__dict__  # -> AttributeError: 'Point' object has no attribute '__dict__'. Did you mean: '__dir__'?
p.a = 10    # -> AttributeError: 'Point' object has no attribute 'a'
"""


# Напишите Singleton











# Пример Singleton/Одиночка  # id Одинаковые     Гарантируется, что объект всегда будет один и тот же.
"""
# Через from dataclasses import dataclass
@dataclass
class Singleton:
    _instance: 'Singleton' = None
    # _instance: Singleton = None     # Можно даже без кавычек ''


# Через Обычный Класс
class Singleton:
   instance = None

   def __new__(cls, *args, **kwargs):
       if cls.instance is None:
           cls.instance = super().__new__(cls)
       return cls.instance

sing = Singleton()
print(id(sing))         # -> 2796516321616   # id Одинаковые
sing_1 = Singleton()
print(id(sing_1))       # -> 2796516321616   # id Одинаковые
"""

# Пример Обычный класс  # id Разные
"""
class Singleton:
    pass

sing = Singleton()
print(id(sing))        # -> 1742792644624     # id Разные
sing_1 = Singleton()
print(id(sing_1))      # -> 1742792644240     # id Разные
"""



# Напишите Monostate Обычный class/dataclass









# Пример Моносостояние (Аналог Singleton)  # При создании экземпляра всем экземплярам присваивается ссылка на один и тот же словарь
"""
class Monostate:
   _shared_state = {'a': 1, 'b': 2}

   def __init__(self):
       self.__dict__ = self._shared_state
    

mono = Monostate()
print(mono.__dict__)    # -> {'a': 1, 'b': 2}
mono_1 = Monostate()
print(mono_1.__dict__)  # -> {'a': 1, 'b': 2}
mono_1.a = 9999999999
print(mono.__dict__)    # -> {'a': 9999999999, 'b': 2}
print(mono_1.__dict__)  # -> {'a': 9999999999, 'b': 2}
"""

# Тоже самое через dataclass    __post_init__
"""
@dataclass
class Monostate:
    _shared_state: dict = None

    def __post_init__(self):
        if Monostate._shared_state is None:
            Monostate._shared_state = {'a': 1, 'b': 2}
        self.__dict__ = Monostate._shared_state 

mono = Monostate()
print(mono.__dict__)    # -> {'a': 1, 'b': 2}
mono_1 = Monostate()
print(mono_1.__dict__)  # -> {'a': 1, 'b': 2}
mono_1.a = 9999999999
print(mono.__dict__)    # -> {'a': 9999999999, 'b': 2}
print(mono_1.__dict__)  # -> {'a': 9999999999, 'b': 2}
"""

# Пример Monostate Обычный класс  # Смотри на словарь
"""
class Monostate:
    pass

mono = Monostate()
print(mono.__dict__)    # -> {}
mono_1 = Monostate()
print(mono_1.__dict__)  # -> {}
mono_1.a = 9999999999
print(mono.__dict__)    # -> {}
print(mono_1.__dict__)  # -> {'a': 9999999999}
"""

# Пример Monostate dataclass  # Смотри на словарь  Для каждого ЭК свой словарь    <-----
"""
from dataclasses import dataclass, field

@dataclass
class Monostate:
    _shared_state: dict = field(default_factory=lambda: {'a': 1, 'b': 2})

    def __post_init__(self):
        self.__dict__ = self._shared_state


mono = Monostate()
print(mono.__dict__)    # -> {'a': 1, 'b': 2}
mono_1 = Monostate()
print(mono_1.__dict__)  # -> {'a': 1, 'b': 2}
mono_1.a = 9999999999
print(mono.__dict__)    # -> {'a': 1, 'b': 2}
print(mono_1.__dict__)  # -> {'a': 9999999999, 'b': 2}
"""



# Создайте свой Метакласс metaclass








# Ответ Создайте свой Метакласс metaclass
"""
class MyMeta(type):
    def __new__(cls, name, bases, attrs):
        # Модификация атрибутов класса
        attrs['custom_attribute'] = 'This is a custom attribute'
        attrs['hehe'] = '123'
        return super().__new__(cls, name, bases, attrs)

class MyClass(metaclass=MyMeta):
    pass

instance = MyClass()
print(instance.custom_attribute)  # Вывод: This is a custom attribute
print(instance.hehe)              # Вывод: 123
print(instance.__dict__)          # Вывод: {}
print(MyClass.hehe)               # Вывод: 123
print(MyClass.custom_attribute)   # Вывод: This is a custom attribute
"""





# Как создать класс без слова class?  И Создать такой же обычный class и dataclass










# Kласс можно создать без использования ключевого слова class, используя типы type:
# В современном коде лучше использовать types.new_class().                                      <-----
"""
MyClass = type('MyClass', (), {'x': 42, 'foo': lambda self: self.x})
my_ = MyClass()
print(my_.x)       # -> 42 
print(my_.foo())   # -> 42
"""

# Тоже самое что и выше но с ключевым словом class!
"""
class MyClass:
   x = 42
   foo = lambda self: self.x  # Тоже самое что и функция ниже
   
   def foo(self):
       return self.x

my_ = MyClass()
print(my_.x)       # -> 42
print(my_.foo())   # -> 42
"""



# Использовать setattr/delattr/hasattr/getattr


@dataclass
class New:
    name: str = 'Chuck Norris'
    surname: str = 'Sasya'
    number: int = 10






# Использовать setattr/delattr/hasattr/getattr

# getattr(object, name)
# getattr(object, name, default)

# setattr(object, name, value)

# delattr(object, name)
# hasattr(object, name)
"""
from dataclasses import dataclass

@dataclass
class New:
    name: str = 'Chuck Norris'
    surname: str = 'Sasya'
    number: int = 10

setattr(New, 'name', 'SuperSasya')   # установили новый атрибут
delattr(New, 'surname')              # удалили атрибут
hasattr(New, 'surname')              # False
getattr(New, 'name')                 # 'SuperSasya'


getattr(New, 'AAAA', 'HEHE')         # HEHE
getattr(New, 'AAAA')                 # AttributeError: type object 'New' has no attribute 'AAAA'
"""



# Создайте класс с property: Создайте функции для управления получением, установкой и удалением атрибута




class C:
    def __init__(self):
        self._x = None












# __get__, __set__, __delete__
# Дескриптор — это то, как реализован тип Python property
# Функции/методы, связанные методы, property, classmethod и staticmethod все они используют эти специальные методы
# для управления доступом к ним с помощью ТОЧЕЧНОГО ПОИСКА.

# Встроенные объектов дескрипторы: classmethod, staticmethod, property, функции в целом
# свойства с property: Создайте функции для управления получением, установкой и удалением атрибута
'''
class C:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise ValueError
        self._x = value

    @x.deleter
    def x(self):
        del self._x

c = C()
c.x = 10
print(c.x)  # 10


# Примеры встроенных объектов дескрипторов: classmethod, staticmethod, property, функции в целом      <-----
def has_descriptor_attrs(obj):
    return set(['__get__', '__set__', '__delete__']).intersection(dir(obj))

def is_descriptor(obj):
    """obj can be instance of descriptor or the descriptor class"""
    return bool(has_descriptor_attrs(obj))

def has_data_descriptor_attrs(obj):
    return set(['__set__', '__delete__']) & set(dir(obj))

def is_data_descriptor(obj):
    return bool(has_data_descriptor_attrs(obj))



# Мы можем видеть, что это classmethod и staticmethod и функции в целом есть Non-Data-Descriptors:
print(is_descriptor(classmethod), is_data_descriptor(classmethod))    # -> True False
print(is_descriptor(staticmethod), is_data_descriptor(staticmethod))  # -> True False

# Обычные функция  Тоже Non-Data-Descriptors
def foo(): pass
my_func = lambda: 5

print(is_descriptor(foo), is_data_descriptor(foo))                    # -> True False
print(is_descriptor(my_func), is_data_descriptor(my_func))            # -> True False

# Только метод __get__
print(has_descriptor_attrs(classmethod))   # -> {'__get__'}
print(has_descriptor_attrs(staticmethod))  # -> {'__get__'}
# Обычные функции __get__
print(has_descriptor_attrs(foo))           # -> {'__get__'}
print(has_descriptor_attrs(my_func))       # -> {'__get__'}



# Дескриптор данных, @property    Data-Descriptor
# @property
print(is_data_descriptor(property))    # -> True
print(has_descriptor_attrs(property))  # -> {'__get__', '__delete__', '__set__'}
'''

# --- Контейнерные типы данных модуля collections ---


# -- class collections.ChainMap(*maps) --
# Использовать ChainMap

first = {1: 1, 2: 2, 3: 3}
second = {4: 4, 5: 5}








# Ответы ChainMap
"""
from collections import ChainMap

first = {1: 1, 2: 2, 3: 3}
second = {4: 4, 5: 5}

chain = ChainMap(first, second)

print(chain)  # -> ChainMap({1: 1, 2: 2, 3: 3}, {4: 4, 5: 5})
chain[1] = 200
print(chain)  # -> ChainMap({1: 200, 2: 2, 3: 3}, {4: 4, 5: 5})
"""



# -- class collections.Counter([iterable-or-mapping]) --
# Использовать Counter

text = 'hello'






# Ответы Counter
"""
from collections import Counter

counter = Counter('hello')
print(counter)                 # -> Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})
counter.update('world')
print(counter.most_common(3))  # -> [('l', 3), ('o', 2), ('h', 1)]
"""



# -- class collections.OrderedDict([items]) --
# Использовать OrderedDict

first = {1: 1, 2: 2, 3: 3}
second = {2: 2, 1: 1}






# Ответы OrderedDict
"""
from collections import OrderedDict

first = {1: 1, 2: 2, 3: 3}
second = {2: 2, 1: 1}

order1 = OrderedDict(first)
order2 = OrderedDict(second)

print(order1.popitem(last=False))         # -> (1, 1)

print(order1)                             # -> OrderedDict([(2, 2), (3, 3)])
order1.move_to_end(3, last=False)
print(order1)                             # -> OrderedDict([(3, 3), (2, 2)])

# Сравниваем порядок внутри
a_dict = {1: 1, 2: 2}
dict_a = {2: 2, 1: 1}
print(a_dict==dict_a)                     # -> True

order3 = OrderedDict({1: 1, 2: 2})
order4 = OrderedDict({2: 2, 1: 1})
print(order3==order4)                     # -> False
"""



# -- class collections.defaultdict(default_factory=None, /[, ...]) --
# Использовать defaultdict


text = 'hello'








# Ответы defaultdict
"""
from collections import defaultdict

a_dict = defaultdict(list)
for char in 'hello':
    a_dict[char].append(char)

print(a_dict)  # -> defaultdict(<class 'list'>, {'h': ['h'], 'e': ['e'], 'l': ['l', 'l'], 'o': ['o']})


a_dict = defaultdict(int)
for char in 'hello':
    a_dict[char]+=1

print(sorted(a_dict.items(), key=lambda x: x[1], reverse=True))  # -> [('l', 2), ('h', 1), ('e', 1), ('o', 1)]
"""


# -- collections.namedtuple(typename, field_names, *, rename=False, defaults=None, module=None) --
# Использовать namedtuple









# Ответы namedtuple

"""
from collections import namedtuple

Point = namedtuple('Point', 'x y')

tom = ('Tom', 4, 'yellow')
print(tom)       # -> ('Tom', 4, 'yellow')
Cat = namedtuple('Cat', 'name age color')
tom = Cat('Tom', 4, 'yellow')
print(tom)       # -> Cat(name='Tom', age=4, color='yellow')
print(tom.name)  # -> Tom


Point = namedtuple('Point', ['x', 'y'])  # Тоже самое
Point = namedtuple('Point', ('x', 'y'))  # Тоже самое
Point = namedtuple('Point', {'x', 'y'})  # Тоже самое
Point = namedtuple('Point', 'x y')       # Тоже самое  Тут будет работать split  print('x y'.split())  # -> ['x', 'y']
Point = namedtuple('Point', 'x, y')      # Тоже самое
p = Point(11, y=22)
print(p)                # -> Point(x=11, y=22)

# Поддерживает только getattr!!!                            <-----
print(getattr(p, 'x'))  # -> 11
d = {'x': 11, 'y': 22}
print(Point(**d))       # -> Point(x=11, y=22)


# Именованные параметры могут НЕ хранить порядок
C = namedtuple('C', 'a b c')
c = C(a=1, c=2, b=3)
print(c)  # -> C(a=1, b=3, c=2)
"""



# -- class collections.deque([iterable[, maxlen]]) --
# Использовать deque







# Ответы deque
"""
from collections import deque


a_deque = deque([1, 2, 3], maxlen=3)
print(a_deque)     # -> deque([1, 2, 3], maxlen=3)
a_deque.append(4)
print(a_deque)     # -> deque([2, 3, 4], maxlen=3)


a_deque = deque()
a_deque.append(1)
# a_deaue.pop(1)         # -> TypeError: deque.popleft() takes no arguments (1 given)
print(a_deque)
a_deque.appendleft(2)    # -> deque([1])
# a_deaue.popleft(2)     # -> TypeError: deque.popleft() takes no arguments (1 given)
print(a_deque)           # -> deque([2, 1])


# deque НЕ поддерживает pop(1)/popleft(1) с аргументом(Индексом)                            <-----   

b_list = list([1, 2])
b_list.pop(0)
print(b_list)  # -> [2]

b_deque = deque([1, 2])
b_deque.pop(1)      # -> TypeError: deque.pop() takes no arguments (1 given)
b_deque.popleft(1)  # -> TypeError: deque.popleft() takes no arguments (1 given)


# Пример rotate   разворачивает контейнер deque()   Если положительное число вправо Если отрицательное влево 
a_deque = deque([1, 2, 3, 4, 5], maxlen=5)
a_deque.rotate(-1)
print(a_deque)  # -> deque([2, 3, 4, 5, 1], maxlen=5)

a_deque = deque([1, 2, 3, 4, 5], maxlen=5)
a_deque.rotate(1)
print(a_deque)  # -> deque([5, 1, 2, 3, 4], maxlen=5)
"""



# --- Модуль itertools в Python, эффективные итераторы для циклов   - сборник полезных итераторов ---

# --- Бесконечные итераторы   Infinite iterators ---


# itertools.count(start=0, step=1)
# Использовать count








# Ответы count
"""
from itertools import count
for i in count(10):
    if i > 15:
        break
    else:
        print(i, end=' ')  # 10 11 12 13 14 15


# Другой способ ограничить вывод бесконечного итератора - использовать другую функцию из itertools с именем islice().
from itertools import islice, count

for i in islice(count(10), 5):
    print(i, end=' ')  # 10 11 12 13 14
    
    
print(list(islice(count(10), 2, 5)))  # -> [12, 13, 14]
"""



# itertools.cycle(iterable)
# Использовать cycle







# Ответы cycle
"""
from itertools import cycle, islice

for index, value in enumerate(cycle('XYZ')):
    if index > 5:
        break
    print(value, end=' ')
# X Y Z X Y Z


# Пример с islice
for i in islice(cycle([1, 2, 3]), 5):
    print(i, end=' ')  # 1 2 3 1 2 
"""



# itertools.repeat(object[, times])
# Использовать repeat






# Ответы repeat
"""
from itertools import repeat

print(list(repeat(10, 3)))  # -> [10, 10, 10]


# Обычное использование для itertools.repeat() - предоставить поток постоянных значений для map() или zip():

# квадраты элементов списка
print(list(map(pow, range(10), repeat(2))))
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
 
# кубы элементов списка
print(list(map(pow, range(10), repeat(3))))
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

# Интересный пример с zip
fruits = ['apples', 'oranges', 'bananas']

# Initialize inventory to zero for each fruit type.
inventory = dict(zip(fruits, repeat(2)))
print(inventory)  # -> {'apples': 2, 'oranges': 2, 'bananas': 2}

inventory = dict(zip(fruits, repeat(0)))
print(inventory)  # -> {'apples': 0, 'oranges': 0, 'bananas': 0}


# Классный пример 
from itertools import chain, repeat, cycle

fruits = ['apples', 'oranges', 'bananas', 'pineapples','grapes',"berries"]

inventory = list(zip(fruits, chain(repeat(10, 2), cycle(range(1, 3)))))
print(inventory)  # -> [('apples', 10), ('oranges', 10), ('bananas', 1), ('pineapples', 2), ('grapes', 1), ('berries', 2)]
"""



# --- Конечные итераторы    Iterators terminating on the shortest input sequence ---
# --- Итераторы, оканчивающиеся на самой короткой входной последовательности ---


# itertools.accumulate(iterable[, function, *, initial=None])
# Использовать accumulate










# Ответы accumulate
"""
from itertools import accumulate

print(list(accumulate([1, 2, 3, 4, 5])))                # -> [1, 3, 6, 10, 15]
print(list(accumulate([1, 2, 3, 4, 5], initial=100)))   # -> [100, 101, 103, 106, 110, 115]
print(list(accumulate([1, 2, 3, 4, 5], operator.mul)))  # -> [1, 2, 6, 24, 120]
print(list(accumulate([1, 2, 3, 4, 5], operator.sub)))  # -> [1, -1, -4, -8, -13]
"""



# itertools.batched(iterable, n)  Работает с версии Питона 3.12 +
# Использовать batched







# Ответы batched
"""
from itertools import batched
flattened_data = ['roses', 'red', 'violets', 'blue', 'sugar', 'sweet']
unflattened = list(batched(flattened_data, 2))
print(unflattened)  # -> [('roses', 'red'), ('violets', 'blue'), ('sugar', 'sweet')]
"""



# itertools.chain(*iterables)
# Использовать chain

a = [1, 2, [3, 3], [4, 4]]
b, c, d = [1, 2], [1, 2], [1, 2]






# Ответы chain
"""
from itertools import chain
A = [1, 2, 3]  # list
B = (4, 5, 6)  # tuple
C = {7, 8, 9}  # set
D = {'A': '11', 'B': '22'}  # dict

G = list(chain(A, B, C, D))
L = [*chain(A, B, C, D)]    # Тоже самое

print(L)  # -> [1, 2, 3, 4, 5, 6, 8, 9, 7, 'A', 'B']
print(G)  # -> [1, 2, 3, 4, 5, 6, 8, 9, 7, 'A', 'B']

# НЕ распакует вложенные без *
print(list(chain([[1, 2, 3]])))   # -> [[1, 2, 3]]
print(list(chain(*[[1, 2, 3]])))  # -> [1, 2, 3]
"""





# classmethod chain.from_iterable(iterable)
# Использовать chain.from_iterable

a = ['foo', ['one', 'two', [1, 2]]]








# Ответы chain.from_iterable

"""
from itertools import chain

lst = ['foo', ['one', 'two', [1, 2]]]

# Сравнение chain vs chain.from_iterable

# itertools.chain(*iterables)
print(list(chain.from_iterable(lst)))  # -> ['f', 'o', 'o', 'one', 'two', [1, 2]]
print([*chain.from_iterable(lst)])     # -> ['f', 'o', 'o', 'one', 'two', [1, 2]]


# chain.from_iterable(iterable)
print(list(chain(lst)))                 # -> ['foo', ['one', 'two', [1, 2]]]
print([*chain(lst)])                    # -> ['foo', ['one', 'two', [1, 2]]]
"""



# itertools.compress(data, selectors)
# Использовать compress







# Ответы compress
"""
from itertools import compress
print(list(compress('ABCDEF', [1,0,1,0,1,1])))  # -> ['A', 'C', 'E', 'F']        
print([*compress('ABCDEF', [1,0,1,0,1,1])])     # -> ['A', 'C', 'E', 'F']    
"""



# itertools.dropwhile(predicate, iterable)
# Использовать dropwhile

a = [1, 4, 6, 4, 1]







# Ответы dropwhile
"""
from itertools import dropwhile
# Пример 1
print(list(dropwhile(lambda x: x < 5, [1, 4, 6, 4, 1])))  # -> [6, 4, 1]

# Пример 2
def trigger_to_five(x):
    return x > 5

lst = [6, 7, 8, 9, 1, 2, 3, 10]
print(list(dropwhile(trigger_to_five, lst)))  # -> [1, 2, 3, 10]
"""


# itertools.takewhile(predicate, iterable)
# Использовать takewhile


a = [1, 4, 6, 4, 1]










# Ответы takewhile
"""
from itertools import takewhile, dropwhile

print(list(takewhile(lambda x: x < 5, [1, 4, 6, 4, 1])))    # -> [1, 4]

print((list(dropwhile(lambda x: x < 5, [1, 4, 6, 4, 1]))))  # -> [6, 4, 1]
"""



# itertools.filterfalse(predicate, iterable)
# Использовать filterfalse


a = range(1, 5)








# Ответы filterfalse
"""
from itertools import filterfalse

print(list(filterfalse(lambda x: x > 5, [6, 7, 8, 9, 1, 2, 3, 10])))  # -> [1, 2, 3]
print(list(filterfalse(lambda x: x < 5, [6, 7, 8, 9, 1, 2, 3, 10])))  # -> [6, 7, 8, 9, 10]
print(list(filterfalse(lambda x: x % 2 == 0, [6, 7, 8, 9])))          # -> [7, 9]
"""



# itertools.islice(iterable, stop)
# itertools.islice(iterable, start, stop[, step])
# Использовать islice

gen = (i for i in range(5))








# Ответы islice
"""
from itertools import islice
from more_itertools import islice_extended

a_gen = (i for i in range(10))
print(list(itertools.islice(a_gen, None, 5)))  # -> [0, 1, 2, 3, 4]


a_gen = (i for i in range(10))

# Используем islice_extended для отрицательных индексов
print(list(islice_extended(a_gen, None, None, -1)))  # -> [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# print(list(islice(a_gen, None, None, -1)))  # -> ValueError: Step for islice() must be a positive integer or None.


# Используем срезы slice()
print(list([1, 2, 3][slice(None, 2)]))         # -> [1, 2]
print(list([1, 2, 3][slice(None, None, -1)]))  # -> [3, 2, 1]          # Только 3 параметра!!!   <-----
"""


# itertools.pairwise(iterable)
# Использовать pairwise

a = [1, 2, 3]






# Ответы pairwise
"""
from itertools import pairwise
result = pairwise([1, 2, 3])

print(list(result))  # -> [(1, 2), (2, 3)]
"""


# itertools.starmap(function, iterable)
# Использовать starmap

a = [(2, 5, 4), (3, 2, 1), (10, 3, 8)]









# Ответы starmap
"""
from itertools import starmap

x = starmap(max, [(2, 5, 4), (3, 2, 1), (10, 3, 8)])
print(list(x))  # -> [5, 3, 10]


# Пример 1: Важно Понимать отличие примера     map   vs   starmap
def add_plus(a, b):
    return a + b


for item in starmap(add_plus, [(2, 3), (4, 5)]):
    print(item, end=' ')
# 5 9
print()

for item in map(add_plus, [(2, 3)], [(4, 5)]):
    print(item, end=' ')
print()
# (2, 3, 4, 5)
for item in map(add_plus, [2, 3], [4, 5]):
    print(item, end=' ')
# 6 8


# Интересный вариант Присмотрись                                     Важно   <----- 
a = [(2, 5, 4), (3, 2, 1), (10, 3, 8)]  

print([*itertools.starmap(min, a)])                    # -> [2, 1, 3]   
print([*itertools.starmap(lambda x, y, z: x*y+z, a)])  # -> [14, 7, 38]
"""


# itertools.tee(iterable, n=2)
# Использовать tee

a = [1, 2, 3]





# Ответы tee
"""
from itertools import tee

rez = tee([1, 2, 3], 3)
print([list(i) for i in rez])  # -> [[1, 2, 3], [1, 2, 3], [1, 2, 3]]


a = [1, 2, 3]
print(*map(list, itertools.tee(a, 3)))

# Не принимает ИМЕНОВАННЫЕ АРГУМЕНТЫ!!!  tee                                tee(iterable, n=2)
print([list(i) for i in tee(a, n=3)])  # -> TypeError: itertools.tee() takes no keyword arguments
print([list(i) for i in tee(a, 3)])    # -> [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

# Не принимает ПОЗИЦИОННЫЕ аргументы!!!  product                            product(*iterables, repeat=1)
print(*itertools.product(a, repeat=2))   # -> (1, 1) (1, 2) (2, 1) (2, 2)
print(*itertools.product(a, 2))          # -> TypeError: 'int' object is not iterable
"""




# itertools.zip_longest(*iterables, fillvalue=None)     zip(*iterables, strict=False)
# Использовать zip_longest

a = [1, 2]
b = [1, 2, 3]







# Ответы zip_longest
"""
from itertools import zip_longest

rez = zip_longest([1, 2], [1, 2, 3], fillvalue=100)
print(list(rez))  # -> [(1, 1), (2, 2), (100, 3)]


# встроенная функция zip()
rez = zip([1, 2], [1, 2, 3])
print(list(rez))  # -> [(1, 1), (2, 2)]



# zip vs zip_longest
a = [1, 2]
b = [1, 2, 3]

# zip vs zip_longest
print([*itertools.zip_longest(a, b)])      # -> [(1, 1), (2, 2), (None, 3)]
print([*zip(a, b, strict=False)])          # -> [(1, 1), (2, 2)]
print([*zip(a, b, strict=True)])           # -> ValueError: zip() argument 2 is longer than argument 1

# Интересный пример
print(*itertools.zip_longest(a, b, a, b))  # -> (1, 1, 1, 1) (2, 2, 2, 2) (None, 3, None, 3) 
print(*itertools.zip_longest(a, b, a))     # -> (1, 1, 1) (2, 2, 2) (None, 3, None)     
"""



# itertools.groupby(iterable, key=None)
# Повтори from itertools import groupby

res = 'AAAABBBCCDAABBB'









# Пример from itertools import groupby
"""
from itertools import groupby
[k for k, g in groupby('AAAABBBCCDAABBB')] #→ A B C D A B    # -> ['A', 'B', 'C', 'D', 'A', 'B']
[list(g) for k, g in groupby('AAAABBBCCD')]#→ AAAA BBB CC D  # -> [['A', 'A', 'A', 'A'], ['B', 'B', 'B'], ['C', 'C'], ['D']]
"""




# --- Комбинаторные итераторы   Combinatoric iterators ---


# itertools.product(*iterables, repeat=1)
# Использовать product

a = [1, 2]






a, b = [1, 2], [3, 3]






# Ответы product
"""
from itertools import product

print(list(product([1, 2], repeat=2)))  # -> [(1, 1), (1, 2), (2, 1), (2, 2)]
print(list(product([1, 2], repeat=3)))  # -> [(1, 1, 1), (1, 1, 2), (1, 2, 1), (1, 2, 2), (2, 1, 1), (2, 1, 2), (2, 2, 1), (2, 2, 2)]

pairs = ['Aa', 'Bb']
gams = list([x for x in product(*pairs)])
print(gams)  # -> [('A', 'B'), ('A', 'b'), ('a', 'B'), ('a', 'b')]


# Интересный пример
a = [1, 2]
print(list(itertools.product(a, repeat=1)))     # -> [(1,), (2,)]
print(list(itertools.product(a, repeat=2)))     # -> [(1, 1), (1, 2), (2, 1), (2, 2)]

a, b = [1, 2], [3, 3]
print(list(itertools.product(a, b, repeat=1)))  # -> [(1, 3), (1, 3), (2, 3), (2, 3)]
print(list(itertools.product(a, b, repeat=2)))
# [(1, 3, 1, 3), (1, 3, 1, 3), (1, 3, 2, 3), (1, 3, 2, 3), (1, 3, 1, 3), (1, 3, 1, 3), (1, 3, 2, 3), (1, 3, 2, 3), ...


# Не принимает ПОЗИЦИОННЫЕ аргументы!!!
print(*itertools.product(a, repeat=2))   # -> (1, 1) (1, 2) (2, 1) (2, 2)
print(*itertools.product(a, 2))          # -> TypeError: 'int' object is not iterable
"""


# itertools.permutations(iterable, r=None)
# Использовать permutations

a = 'XYZ'








# Ответы permutations
"""
from itertools import permutations

print(list(permutations('XY', 2)))  # -> [('X', 'Y'), ('Y', 'X')]
print(list(permutations('XYZ', 3)))
# [('X', 'Y', 'Z'), ('X', 'Z', 'Y'), ('Y', 'X', 'Z'), ('Y', 'Z', 'X'), ('Z', 'X', 'Y'), ('Z', 'Y', 'X')]
# По дефолту
print(list(itertools.permutations('XYZ')))
# [('X', 'Y', 'Z'), ('X', 'Z', 'Y'), ('Y', 'X', 'Z'), ('Y', 'Z', 'X'), ('Z', 'X', 'Y'), ('Z', 'Y', 'X')]
"""



# itertools.combinations(iterable, r)
# Использовать combinations

a = 'XYZ'







# Ответы combinations
"""
from itertools import combinations

print(list(combinations('XYZ', 2)))  # -> [('X', 'Y'), ('X', 'Z'), ('Y', 'Z')]
print(list(combinations('XYZ', 3)))  # -> [('X', 'Y', 'Z')]
"""



# itertools.combinations_with_replacement(iterable, r)
# Использовать combinations_with_replacement

a = 'XYZ'








# Ответы combinations_with_replacement
"""
from itertools import combinations_with_replacement

print(list(combinations_with_replacement('XYZ', 2)))  # -> [('X', 'X'), ('X', 'Y'), ('X', 'Z'), ('Y', 'Y'), ('Y', 'Z'), ('Z', 'Z')]
print(list(combinations_with_replacement('XYZ', 3)))
# [('X', 'X', 'X'), ('X', 'X', 'Y'), ('X', 'X', 'Z'), ('X', 'Y', 'Y'), ('X', 'Y', 'Z'), ('X', 'Z', 'Z'), ('Y', 'Y', 'Y'),
# ('Y', 'Y', 'Z'), ('Y', 'Z', 'Z'), ('Z', 'Z', 'Z')]
"""



# --- Отличия    combinations  vs  combinations_with_replacement vs  permutations ---

a = 'XYZ'







# Ответ
#  --- Отличия    combinations  vs  combinations_with_replacement vs  permutations ---
"""
from itertools import permutations, combinations, combinations_with_replacement

print(list(permutations('XY', 2)))                    # -> [('X', 'Y'), ('Y', 'X')]
print(list(combinations('XY', 2)))                    # -> [('X', 'Y')]
print(list(combinations_with_replacement('XY', 2)))   # -> [('X', 'X'), ('X', 'Y'), ('Y', 'Y')]
"""





# --- сторонний модуль more-itertools в Python, Больше процедур для работы с итерируемыми объектами, помимо itertools ---



# more_itertools.chunked(iterable, n, strict=False) - Разбейте итерацию на списки длины n
# Использовать chunked


iterable = [1, 2, 3, 4, 5, 6]







# Ответы chunked
"""
from more_itertools import chunked

iterable = [1, 2, 3, 4, 5, 6]
print(list(chunked(iterable, 1)))  # -> [[1], [2], [3], [4], [5], [6]]
print(list(chunked(iterable, 2)))  # -> [[1, 2], [3, 4], [5, 6]]
print(list(chunked(iterable, 3)))  # -> [[1, 2, 3], [4, 5, 6]]
"""



# more_itertools.spy(iterable, n=1) - первые n элементов , и итератор с теми же элементами, что и итерируемый объект.
# Использовать spy


iterable = 'abcdefg'








# Ответы spy
"""
from more_itertools import spy

iterable = 'abcdefg'

head, iterable = spy(iterable, 3)
print(head)             # -> ['a', 'b', 'c']
print(list(iterable))   # -> ['a', 'b', 'c', 'd', 'e', 'f', 'g']

print(spy(iterable))    # -> ([], <itertools.chain object at 0x000002ADE9E0FB20>)    
"""


# more_itertools.first(iterable[, default]) - Возвращает первый элемент iterable или значение по умолчанию , если iterable пуст.
# Использовать first


iterable = [0, 1, 2, 3]






iterable = []







# Ответы first
"""
from more_itertools import first

print(first([0, 1, 2, 3]))        # -> 0
print(first([], 'some default'))  # -> 'some default'
print(first([]))  # -> ValueError: first() was called on an empty iterable, and no default value was provided.
"""



# more_itertools.one(iterable, too_short=ValueError, too_long=ValueError) - Верните первый элемент из iterable
# Использовать one






# Ответы one
"""
from more_itertools import one


it = [1]
print(one(it))   # -> 1

it = ['too', 'many']
print(one(it))   # -> ValueError: Expected exactly one item in iterable, but got 'too', 'many', and perhaps more.

too_long = RuntimeError
one(it, too_long=too_long)  # -> RuntimeError

it = 1
print(one(it))   # -> TypeError: 'int' object is not iterable

it = []
print(one(it))   # -> ValueError: too few items in iterable (expected 1)
"""



# more_itertools.only(iterable, default=None, too_long=ValueError) - Если в iterable есть только один элемент, верните его.
# Использовать only








# Ответы only
"""
from more_itertools import only

print(only([], default='missing'))       # -> 'missing'
print(only([1]))                         # -> 1
print(only([1, 2]))  # -> ValueError: Expected exactly one item in iterable, but got 1, 2, and perhaps more.
print(only([1, 2], too_long=TypeError))  # -> TypeError
"""



# more_itertools.unique_everseen(iterable, key=None) - Создавайте уникальные элементы, сохраняя порядок.
# Использовать unique_everseen








# Ответы unique_everseen
"""
from more_itertools import unique_everseen
from timeit import timeit

print(list(unique_everseen('AAAABBBCCDAABBB')))     # -> ['A', 'B', 'C', 'D']
print(list(unique_everseen('ABBCcAD', str.lower)))  # -> ['A', 'B', 'C', 'D']


iterable = ([1, 2], [2, 3], [1, 2])
print(list(unique_everseen(iterable)))              # [[1, 2], [2, 3]]          # Slow     <-----
print(list(unique_everseen(iterable, key=tuple)))   # [[1, 2], [2, 3]]          # Faster   <-----


#  В основном tuple самый быстрый, можно самому еще потестить варианты
a_list = ([1, 2], [2, 3], [1, 2])
print(timeit('list(unique_everseen(a_list))', globals=globals()))               # ->  3.41782069997862    <-----
print(timeit('list(unique_everseen(a_list, key=tuple))', globals=globals()))    # ->  1.4006470999447629  <-----

a_set = ({1, 2}, {2, 3}, {1, 2})
print(timeit('list(unique_everseen(a_set))', globals=globals()))                 # ->  4.487388600013219   <-----
print(timeit('list(unique_everseen(a_set, key=frozenset))', globals=globals()))  # ->  1.4916451999451965  <-----
"""





#  class more_itertools.islice_extended(iterable, stop)
#  class more_itertools.islice_extended(iterable, start, stop[, step])
#  Расширение этого itertools.islice() поддерживает отрицательные значения для stop , start и Step .


iterable = iter('abcdefgh')









# Ответы islice_extended
"""
from more_itertools import islice_extended


iterable = iter('abcdefgh')
print(list(islice_extended(iterable, None, None, -1)))  # -> ['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
iterable = iter('abcdefgh')
print(list(islice_extended(iterable, -4, -1)))          # -> ['e', 'f', 'g']
"""



# # more_itertools.ilen(iterable) - Возвращает количество элементов в iterable .  Это потребляет итерацию .
# Использовать ilen


a_gen = (i for i in range(10))







# Ответы ilen
"""
from more_itertools import ilen

a_gen = (i for i in range(10))
print(ilen(a_gen))  # -> 10  Генератор/Итератор одноразовый
print(list(a_gen))  # -> []                                                                    <-----

print(len(a_gen))   # -> TypeError: object of type 'generator' has no len()     Обычный len()  <-----
"""






# --- functools — Функции высшего порядка и операции над вызываемыми объектами ---


# functools.reduce(function, iterable[, initializer])
# Напишите from functools import reduce/eval   Используя lambda/operator   eval - НЕ забудь

a = [1, 2, 3, 4]








# Ответ  reduce/eval   lambda/operator
"""
import functools, operator
lst = [1, 2, 3, 4]
print(functools.reduce(operator.add, lst))      # -> 10
print(functools.reduce(lambda x, y: x+y, lst))  # -> 10
# Тоже самое
print(eval('+'.join([str(i) for i in lst])))    # -> 10
print(eval('+'.join(map(str, lst))))            # -> 10
"""


# @functools.cache(user_function)   Написать функцию  factorial
# Использовать cache










# Ответ @functools.cache(user_function)
"""
from functools import cache
@cache
def factorial(n):
    return n * factorial(n-1) if n else 1

print(factorial(10))  # -> 3628800
print(factorial(5))   # -> 120
print(factorial(12))  # -> 479001600
"""




# @functools.lru_cache(user_function)
# @functools.lru_cache(maxsize=128, typed=False)
# Напишите Фибоначчи с кэшем и замер скорости работы timeit   globals=globals()/setup="from __main__ import fibonacci__3"








# Решения Фибоначч с мемоизацией КЭШ  Скорость O(n)  @functools.lru_cache
"""
import timeit
from functools import lru_cache

@__import__('functools').lru_cache(maxsize=None)  #  Так тоже можно импортировать
# @functools.lru_cache(maxsize=None)
def fibonacci__3(n):
    if n < 2:
        return n
    else:
        return fibonacci__3(n - 1) + fibonacci__3(n - 2)

print(fibonacci__3(50))                                                              # -> 12586269025
# Замеры с параметром 50!!!
print(timeit.timeit('fibonacci__3(50)', globals=globals()))                          # -> 0.10358340013772249

# Тоже самое но с setup()
print(timeit.timeit('fibonacci__3(50)', setup="from __main__ import fibonacci__3"))  # -> 0.09871609997935593


# Доп. решение sympy fibonacci
from sympy import fibonacci
print(fibonacci(50))                       # -> 12586269025 

print(__import__('sympy').fibonacci(50))   # -> 12586269025  
"""






# functools.partial(func, /, *args, **keywords)
# Используйте функцию from functools import partial

def multiply(x, y):
    return x * y






# partial функция from functools import partial
"""
from functools import partial

def multiply(x, y):
    return x * y

doubleNum = partial(multiply, 2)
tripleNum = partial(multiply, 3)
res = multiply(10, 2)

print(res)  # 20
print(multiply(10, 2))  # 20
print(doubleNum(20))  # 40
print(tripleNum(20))  # 60

# ИЛИ Сразу вызываем но нужно все аргументы прокидывать
print(partial(multiply, 3, 3)())  # 9
print(partial(multiply, 5, 5)())  # 25
print(partial(multiply, 5)())     # TypeError: multiply() missing 1 required positional argument: 'y'
"""




# @functools.wraps(wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES)
# 1) Написать декоратор, который выводит на экран время работы произвольной функции и используем   from functools import wraps









# Ответ 1)
"""
from functools import wraps
from time import time, perf_counter

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        res = func(*args, **kwargs)
        finish = perf_counter()
        print(f"Время выполнения функции '{func.__name__}': {finish - start:.4f} секунд")
        return res
    wrapper.__name__ = func.__name__   # Тоже самое что   @wraps(func)  Только ручное  
    wrapper.__doc__ = func.__doc__     # Тоже самое что   @wraps(func)  Только ручное
    return wrapper

@timer    # Если навесить еще то будет замерять еще раз     <----
@timer
def example_function(n):
    total = 0
    for i in range(n):
        total += i
    return total
example_function(1000000)  # -> Время выполнения функции 'example_function': 0.0738 секунд
"""


# 1.1) Написать Класс как ДЕКОРАТОР, который выводит на экран время работы произвольной функции:








# Ответ 1.1)
# Класс как ДЕКОРАТОР
"""
from time import perf_counter

class Timer:
    def __init__(self, func):
        self.fn = func

    def __call__(self, *args, **kwargs):
        start = perf_counter()
        print(f"Вызывается функция {self.fn.__name__}")
        result = self.fn(*args, **kwargs)
        finish = perf_counter()
        print(f"Функция {self.fn.__name__} отработала за {finish - start}")
        return result

@Timer
def example_function(n):
    total = 0
    for i in range(n):
        total += i
    return total
example_function(1000000)  # -> Время выполнения функции 'example_function': 0.0738 секунд



# Тоже самое через dataclass        from typing import Callable   - Чтобы указать аннотацию функция

from dataclasses import dataclass, field
from typing import Callable                     # Лучше используем    from collections.abc import Callable 

@dataclass
class Timer:
    func: Callable[[int], str]  # Аннотация типа для функции, принимающей int и возвращающей str

    def __call__(self, *args, **kwargs):
        s = time.perf_counter()
        res = self.func(*args, **kwargs)
        f = time.perf_counter()
        print(f-s)
        return res

@Timer
def plus(a, b):
    return a + b

print(plus(2, 2))
"""



# 1.2) Написать dataclass
# @dataclasses.dataclass(*, init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False, match_args=True,
# kw_only=False, slots=False, weakref_slot=False)










# Ответ 1.2)
# Декорирование класса в Python:

# @dataclasses.dataclass(*, init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False, match_args=True,
# kw_only=False, slots=False, weakref_slot=False)
"""
from dataclasses import dataclass
@dataclass
class InventoryItem:
    name: str
    unit_price: float
    quantity: int = 0

item = InventoryItem(name="HEHE", unit_price=12, quantity=100)
print(item.__dict__)  # -> {'name': 'HEHE', 'unit_price': 12, 'quantity': 100}
"""




# 1.2.1) compare=False   Написать dataclass  В котором Исключить поле из сравнения
# @dataclasses.dataclass(*, init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False, match_args=True,
# kw_only=False, slots=False, weakref_slot=False)










# 1.2.1) Ответ compare=False   Написать dataclass  В котором Исключить поле из сравнения
# @dataclasses.dataclass(*, init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False, match_args=True,
# kw_only=False, slots=False, weakref_slot=False)
"""
from dataclasses import dataclass, field

@dataclass(order=True)
class WorkItem:
    priority: int
    priority_2: int = field(compare=False)  # Это поле не участвует в сравнении
    data: str = field(compare=False)  # Это поле также не участвует в сравнении

# Создаем несколько экземпляров WorkItem
item1 = WorkItem(priority=2, priority_2=5, data="A")
item2 = WorkItem(priority=1, priority_2=10, data="B")
item3 = WorkItem(priority=1, priority_2=20, data="C")

# Сравнение экземпляров
print(item1 > item2)   # True, так как priority 2 > 1
print(item2 < item3)   # False, так как priority 1 == 1, но priority_2 не участвует в сравнении
print(item2 == item3)  # True, так как priority 1 == 1, но при этом priority_2 не учитывается
"""




# 1.3) Сделать по умолчанию пустой список и НЕ пустой  Сравнение __eq__()  уже встроенно в dataclass








# Ответ 1.3)
# Сделать по умолчанию пустой список и НЕ пустой  Сравнение __eq__()  уже встроенно в dataclass
"""
from dataclasses import dataclass, field


@dataclass(order=True, frozen=True)
class Foo:
    n: int
    s: str = 'a'
    ss: str = field(default='AAA')
    items: list[str] = field(default_factory=list)              # <-- и всё это - чтобы по умолчанию был пустой список
    items_2: list[str] = field(default_factory=lambda: [1, 2])  # <-- и всё это - чтобы по умолчанию было [1, 2]
    a_dict: dict = field(default_factory=lambda: {1: 2})
    # a_list: list = field(default=[1, 2])                      # Так будет ошибка
    # a_dict: dict = field(default={3:3})                       # Так будет ошибка
    # ValueError: mutable default <class 'list'> for field a_list is not allowed: use default_factory


f = Foo(1)
f1 = Foo(1)

print(f.__dict__)      # -> {'n': 1, 's': 'a', 'ss': 'AAA', 'items': [], 'items_2': [1, 2], 'a_dict': {1: 2}}
print(f.__eq__(f1))    # -> True
print(f == f1)         # -> True

ff = Foo(11111)
ff1 = Foo(1)
print(ff.__eq__(ff1))  # -> False
print(ff == ff1)       # -> False
print(f >= f1)         # -> True       order=True  Будут работать
f.a = 10               # -> dataclasses.FrozenInstanceError: cannot assign to field 'a'   frozen=True
"""


# 1.4) Использовать Pydantic  по умолчанию пустой список и НЕ пустой









# Ответ 1.4)   Использовать Pydantic  по умолчанию пустой список и НЕ пустой
# Сравните это с пидантиком(Pydantic), в котором, кажется, думают о людях:
"""
from pydantic import BaseModel

class MyDate(BaseModel):
    n: int
    s: str = 'a'
    items: list[str] = []
    items_2: list[str] = [1, 2, 3]

m = MyDate(n=1)
m1 = MyDate(n=1)

print(m.__dict__)    # -> {'n': 1, 's': 'a', 'items': [], 'items_2': [1, 2, 3]}
print(m.dict)        # -> <bound method BaseModel.dict of MyDate(n=1, s='a', items=[], items_2=[1, 2, 3])>

print(m == m1)       # -> True
print(m.__eq__(m1))  # -> True


# Так будет ошибка  <-----   Важно 
mm = MyDate(1)
mm1 = MyDate(1)
"""


# 1.5) Написать  Построители классов данных  dataclass   typing.NamedTuple   namedtuple






# 1.5) Ответ Написать  Построители классов данных  dataclass   typing.NamedTuple   namedtuple
"""
# dataclass                               # typing.NamedTuple                    # namedtuple
from dataclasses import dataclass         from typing import NamedTuple          from collections import namedtuple
     
@dataclass                                class Point(NamedTuple):               Point = namedtuple('Point', ['x', 'y'])
class Point:                                  x: int   
    x: int                                    y: int   
    y: int     
     
p = Point(10, 20)                         p = Point(10, 20)                      p = Point(10, 20)
Point.__doc__ # Point(x: int, y: int)     print(Point.__doc__)  # Point(x, y)    print(Point.__doc__)  # Point(x, y)
print(p)  # Point(x=10, y=20)             print(p.x, p.y)  # 10 20               print(p.x, p.y)  # 10 20

print(Point.__annotations__)               print(Point.__annotations__)                print(Point.__annotations__)
# {'x': <class 'int'>, 'y': <class 'int'>} # {'x': <class 'int'>, 'y': <class 'int'>}  # {}   
"""





# 2) Написать декоратор, который возвращает либо результат, либо экземпляр исключения:










# Ответ 2)
"""
def safe_decorator(func):
   @__import__('functools').wraps(func)
   def wrapper(*args, **kwargs):
       try:
           return func(*args, **kwargs)
       except ZeroDivisionError as e:
           return e
   return wrapper
                                                # Тоже самое Но нацело деление и ошибка другая
@safe_decorator                                 @safe_decorator            
def divide(a, b):                               def divide(a, b):                
    return a / b                                    return a // b                
                                                  
print(divide(10, 0))  # -> division by zero     print(divide(10, 0))  # -> integer division or modulo by zero                                        
print(divide(10, 2))  # -> 5.0                  print(divide(10, 2))  # -> 5                            
"""



# Напишите декоратор с ПАРАМЕТРАМИ/Аргументами   через  ФУНКЦИЮ  и КЛАСС    <-----








# ДЕКОРАТОР С ПАРАМЕТРАМИ - ЭТО ДОБАВЛЕНИЕ ЕЩЕ ОДНОГО УРОВНЯ ВЛОЖЕННОСТИ ДЛЯ ТОГО ЧТОБЫ ПЕРЕДАТЬ КАКОЙ-ТО ПАРАМЕТР А
# ВНУТРИ ЛЕЖИТ ОБЫЧНЫЙ ДЕКОРАТОР.
"""
def typed(type_):  # ->   Добавили уровень вложенности                                                                                              
    def real_decorator(function):  # ->   Внутри обычный декоратор                                                                                              
        @__import__('functools').wraps(function)                                                                                                
        def wrapper(*args):                                                                                             
            for arg in args:                                                                                                
                if not isinstance(arg, type_):                                                                                              
                    raise ValueError(f'Тип должен быть {type_}')                                                                                                
            return function(*args)                                                                                              
        return wrapper                                                                                              
    return real_decorator  # ->   нужно вернуть еще одну функцию как и другие вложенности                                                                                               
                                                                                                
@typed(int)  # @real_decorator                                                                                              
def calculate(a, b, c):                                                                                             
    # Logic                                                                                             
    return a + b + c                                                                                                

@typed(str)  # @real_decorator
def convert(a, b):
    # Logic
    return a + b

if __name__ == '__main__':
    # calculate = typed(int)(calculate) # Под капотом работает так! Ручное декорирование без @             <-----
    print(calculate(2, 2, 2))           
    print(convert('1', 'hello'))            
    # convert = typed(str)(convert)     # Под капотом работает так! Ручное декорирование без @             <-----
    
    
    
# Тоже самое через КЛАСС   Только вешаем Декоратор ЧЕРЕЗ Большую букву 
class Typed:
    def __init__(self, type_):
        self._type = type_
 
    def __call__(self, func):
        @wraps(func)
        def wrapper(*args):
            for arg in args:
                if not isinstance(arg, self._type):
                    raise ValueError(f'Тип должен быть {self._type}')
            return func(*args)
        return wrapper
        
@Typed(int)  # @real_decorator
def calculate(a, b, c):
    # Logic
    return a + b + c
 
@Typed(str)  # @real_decorator
def convert(a, b):
    # Logic
    return a + b
 
if __name__ == '__main__':
    # calculate = Typed(int)(calculate) # Под капотом работает так! Ручное декорирование без @             <-----
    print(calculate(2, 2, 2))
    print(convert('1', 'hello'))
    # convert = Typed(str)(convert)     # Под капотом работает так! Ручное декорирование без @             <-----
"""





# 3) Написать генератор Фибоначчи от a и b.  Вывести первые 10 чисел Фибоначчи










# Ответ 3)
"""
def fibonacci_generator(a, b):
    while True:
        yield a
        a, b = b, a + b

# Пример использования
fib_gen = fibonacci_generator(1, 1)
for _ in range(10):
    print(next(fib_gen), end=' ')  # Выведет первые 10 чисел Фибоначчи              # -> 1 1 2 3 5 8 13 21 34 55
"""


# Дополнительный вопрос Напишите разные варианты ФИБОНАЧЧИ







# Ответ Дополнительный вопрос Напишите разные варианты ФИБОНАЧЧИ
"""
import math

# Формула Бине позволяет вычислить n-е число Фибоначчи за константное время.
def fibonacci_binet(n):
    phi = (1 + math.sqrt(5)) / 2
    return round(phi**n / math.sqrt(5))

print(fibonacci_binet(10))  # Вывод: 55


# Итеративный подход
def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

print(fibonacci_iterative(10))  # Вывод: 55
"""



# 4) Получить из файла текст в юникоде.







# Ответ 4)
"""
def read_unicode_file(file_path):
   with open(file_path, 'r', encoding='utf-8') as f:
       content = f.read()
   return content

# Пример использования
текст = read_unicode_file('path_to_your_file.txt')
print(текст)
"""

# 5) Написать генератор чисел Фибоначчи вида def fib(a=1, b=2):










# Ответ 5)
"""
def fib(a=1, b=2):
    while True:
        yield a
        a, b = b, a + b

# Пример использования
fib_gen = fib()
[print(next(fib_gen), end=' ') for _ in range(10)]
# Выведет первые 10 чисел Фибоначчи начиная с a=1, b=2  # -> 1 2 3 5 8 13 21 34 55 89
"""



# Создать Абстрактный класс  и Унаследоваться от него     from abc import ABC, abstractmethod










# Ответ Создать Абстрактный класс  и Унаследоваться от него     from abc import ABC, abstractmethod
r"""
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

s = Shape()  # -> TypeError: Can't instantiate abstract class Shape with abstract method area

class MyClass(Shape):
    pass

c = MyClass()  # -> TypeError: Can't instantiate abstract class Shape with abstract method area


# Всё работает
class MyClass(Shape):
    def area(self):
        return 1000

c = MyClass()
print(c.area())  # -> 1000



# Интересный момент с \     SyntaxError: unexpected character after line continuation character    <-----
from abc import ABC, abstractmethod

class C(ABC):
    @abstractmethod
    def fff(self):
        pass

class CC(C):

    # def fff(self):
    #     return \     # SyntaxError: unexpected character after line continuation character

    def fff(self):
        return \

c = CC()
print(c.fff())  # -> None
"""




# НАПИСАТЬ Protocol vs ABC





# Ответ Protocol vs ABC
"""
# С ABC (обязательное наследование)                # С Protocol (без наследования)
from abc import ABC, abstractmethod                from typing import Protocol

class Animal(ABC):                                 class Animal(Protocol):
    @abstractmethod                                    def sound(self) -> str: ...
    def sound(self) -> str:
        pass                                       class Dog:  # Просто имеет нужный метод
                                                       def sound(self) -> str:
class Dog(Animal):  # Должен наследовать Animal            return "Гав!"
    def sound(self) -> str:
        return "Гав!"                              # Использование
                                                   def make_sound(animal: Animal) -> None:
# Использование                                        print(animal.sound())
dog = Dog()
print(dog.sound())  # Гав!                         make_sound(Dog())  # Гав!
"""






# Написать Асинхронный код







# Ответ Асинхронный код
"""
import asyncio

async def hello():
    await asyncio.sleep(1)
    print("Hello")

async def world():
    await asyncio.sleep(2)
    print("World")

async def main():
    # asyncio.create_task(hello())
    # asyncio.create_task(world())
    await asyncio.gather(hello(), world())
    # await asyncio.create_task(hello())
    # await asyncio.create_task(world())

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    print(time.time() - start)
    
    
# Названия generator object    coroutine object
def gen():
    x = 10
    print(x)
    yield x

# Не правильное использование
async def example():
    print(100)


print(gen())      # -> <generator object gen at 0x00000208FA74B2A0>

print(example())  # -> <coroutine object example at 0x00000208FA67E080>
# RuntimeWarning: Enable tracemalloc to get the object allocation traceback


# Хороший пример с замером времени БЕЗ БЛОКИРУЮЩЕГО КОДА 3 СЕК   # C БЛОКИРУЮЩИМ КОДОМ  7 СЕК
async def one():                                                 async def one():                                                                               
    print('Start one')                                               print('Start one')                                                                                   
    await asyncio.sleep(1)                                           await asyncio.sleep(1)                                                                                       
    print('Stop one')                                                print('Stop one')                                                                                   
                                                                                                                                 
async def two():                                                 async def two():                                                                               
    print('Start two')                                               print('Start two')                                                                                   
    await asyncio.sleep(2)                                           await asyncio.sleep(2)                                                                                       
    # time.sleep(5)                                                  time.sleep(5)            # Тут   БЛОКИРУЮЩИЙ КОД                                                                 
    print('Stop two')                                                print('Stop two')                                                                                   
                                                                                                                                 
async def three():                                               async def three():                                                                               
    print('Start three')                                             print('Start three')                                                                                       
    await asyncio.sleep(3)                                           await asyncio.sleep(3)                                                                                       
    print('Stop three')                                              print('Stop three')                                                                                   
                                                                                         
async def main():                                                async def main():                                       
    await asyncio.gather(one(), two(), three())                      await asyncio.gather(one(), two(), three())                                                                   
    # asyncio.create_task(one())                                     # asyncio.create_task(one())   
    # asyncio.create_task(two())                                     # asyncio.create_task(two())
    # await asyncio.create_task(three())                             # await asyncio.create_task(three())                                                         
                                                                                         
if __name__ == '__main__':                                       if __name__ == '__main__':                                               
    start = time.time()                                              start = time.time()                                           
    asyncio.run(main())                                              asyncio.run(main())                                           
    print(time.time() - start)  # -> 2.994696855545044               print(time.time() - start)  # -> 7.008123874664307                                                                           
"""




# НАПИШИТЕ gather vs TaskGroup






# ОТВЕТ gather vs TaskGroup
"""
# ПРИМЕР gather
# gather Если одна упадет, остальные работают дальше.                                                                                    
import asyncio                                                           
                                                                         
async def task_success(name, delay):                                                             
    await asyncio.sleep(delay)                                                     
    print(f"{name} завершена успешно")                                                             
                                                                         
async def task_fail(name, delay):                                                         
    await asyncio.sleep(delay)                                                     
    raise Exception(f"{name} сломалась!")                                                                 
                                                                         
async def main_gather():                                                    
    print("Запуск gather с ошибкой")                                                                
    tasks = [                                                            
        asyncio.create_task(task_success("Задача 1", 1)),                                                                     
        asyncio.create_task(task_fail("Задача 2", 2)),                                                                              
        asyncio.create_task(task_success("Задача 3", 3))                                                                             
    ]                                                                               
    results = await asyncio.gather(*tasks, return_exceptions=True)                                                 
    for i, res in enumerate(results):                                                                   
        if isinstance(res, Exception):                                                                                 
            print(f"Задача {i + 1} завершилась с ошибкой: {res}")                         
        else:                                                            
            print(f"Задача {i + 1} успешно завершена")                                                        
    print("Все задачи в gather завершены независимо, ошибки обработаны")                         
                                                                                        
if __name__ == '__main__':                                                                                      
    asyncio.run(main_gather())   
    


# ПРИМЕР TaskGroup
# TaskGroup - отменяет все задачи, если хоть одна сломалась. 
import asyncio                         
              
async def task_success(name, delay):                         
    await asyncio.sleep(delay)                               
    print(f"{name} завершена успешно")                       
              
async def task_fail(name, delay):                            
    await asyncio.sleep(delay)                               
    raise Exception(f"{name} сломалась!")                    
              
async def main_taskgroup():                                  
    print("Запуск TaskGroup с ошибкой")                      
    try:                         
        async with asyncio.TaskGroup() as tg:                
            tg.create_task(task_success("Задача 1", 1))      
            tg.create_task(task_fail("Задача 2", 2))         
            tg.create_task(task_success("Задача 3", 3))      
    except Exception as e:                                   
        print(f"Обработка исключения: {e}")                  
    print("Все задачи в TaskGroup завершены или отменены")   
                                                             
if __name__ == '__main__':                         
    asyncio.run(main_taskgroup())                                                                                                                                                                                
"""




# Как запустить что-то в потоке и вывести результат?   from concurrent.futures import ThreadPoolExecutor







# Ответ  Как запустить что-то в потоке и вывести результат?  from concurrent.futures import ThreadPoolExecutor
"""
from concurrent.futures import ThreadPoolExecutor

fn = lambda: 5
with ThreadPoolExecutor(max_workers=5) as pool:
    future = pool.submit(fn)
    print(future.result())  # -> 5

with ThreadPoolExecutor(max_workers=1) as executor:
    future = executor.submit(pow, 10, 3)
    print(future.result())  # -> 1000.0
"""


# Как запустить что-то в Процессах и вывести результат?   # lambda не сериализуется pickle   ProcessPoolExecutor
# if __name__ == "__main__": для защиты от рекурсии.








# Ответ Как запустить что-то в Процессах и вывести результат?   # lambda не сериализуется pickle   ProcessPoolExecutor
# конструкция if __name__ == "__main__": критически важна не только для multiprocessing, но и для
# concurrent.futures.ProcessPoolExecutor, поскольку он тоже использует механизм порождения процессов (аналогично multiprocessing).
"""
from concurrent.futures import ProcessPoolExecutor

# lambda не сериализуется pickle
fn = lambda: 5

# if __name__ == "__main__": для защиты от рекурсии.
if __name__ == "__main__":
# Создание ProcessPoolExecutor с 4 рабочими процессами
    with ProcessPoolExecutor(max_workers=4) as executor:
        future = executor.submit(fn)
        result = future.result()
        print(result)  # -> 16
# _pickle.PicklingError: Can't pickle <function <lambda> at 0x000001C4AA9B8860>: attribute lookup <lambda> on __main__ failed



# Так будет работать

def task_function(param):
    return param ** 5

if __name__ == "__main__":
# Создание ProcessPoolExecutor с 4 рабочими процессами
    with ProcessPoolExecutor(max_workers=4) as executor:
        future = executor.submit(task_function, 10)
        result = future.result()
        print(result)  # -> 100000
"""





# --- Хорошие задачи PYTHON ---




# Необходимо найти максимальное количество последовательно идущих единиц.  Max Consecutive Ones    НАПИСАТЬ 3 ВАРИАНТА







# ОТВЕТ Необходимо найти максимальное количество последовательно идущих единиц.  Max Consecutive Ones
R"""
# Максимальное количество подряд идущих единиц  Max Consecutive Ones

# ВАРИАНТ 1
# Имеет временную сложность O(n), где n - длина массива, так как мы проходим по массиву только один раз.
# Пространственная сложность O(1), так как используем только константное количество дополнительной памяти.
def findMaxConsecutiveOnes(nums: list) -> int:
    max_count = 0
    current_count = 0

    for num in nums:
        if num == 1:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0

    return max_count


print(findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))  # -> 3
print(findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))  # -> 2



# ВАРИАНТ 2
# Время: O(n) (один проход по массиву).
# Память: O(k), где k — длина максимальной последовательности (в худшем случае O(n)).
def findMaxConsecutiveOnes(nums: list) -> tuple[int, list]:
    max_seq = []
    current_seq = []

    for num in nums:
        if num == 1:
            current_seq.append(num)
            if len(current_seq) > len(max_seq):
                max_seq = current_seq.copy()
        else:
            current_seq = []

    return len(max_seq), max_seq


print(findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))  # -> (3, [1, 1, 1])
print(findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))  # -> (2, [1, 1])



# ВАРИАНТ 3 
# МОЁ РЕШЕНИЕ НЕ ОПТИМАЛЬНОЕ         Сложность: O(n) время, но с большими константами из-за преобразований
def findMaxConsecutiveOnes(nums):
    res = re.sub(r'[\[\]\,\s]', '', str(nums))
    return len(max(res.split('0'), key=len))

print(findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))  # -> 3
print(findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))  # -> 2
"""





# Максимальное количество последовательных единиц II (с возможностью переворота одного нуля)  Max Consecutive Ones II
# НАПИСАТЬ 3 ВАРИАНТА   # YANDEX  (Второй ЗАХОД)





# ОТВЕТ Максимальное количество последовательных единиц II (с возможностью переворота одного нуля)  Max Consecutive Ones II
"""
# ВАРИАНТ 1
# Решение С БИТОВЫМИ ОПЕРАЦИЯМИ  XOR (^) для инвертирования битов
# Время: O(n) - один проход по массиву
# Память: O(1) - константное доп. пространство

# Использует битовую операцию ^ для инвертирования 0/1   x ^ 1 работает как инвертор бита (0→1, 1→0)
# Возвращает len(nums) - l (максимальное окно)
def findMaxConsecutiveOnes(nums: list) -> int:
    l = cnt = 0
    for x in nums:
        cnt += x ^ 1 # Эквивалентно: cnt += 0 if x == 1 else 1
        if cnt > 1:  # Если встретили второй ноль
            cnt -= nums[l] ^ 1
            l += 1
    return len(nums) - l # Длина максимального окна

print(findMaxConsecutiveOnes([1, 0, 1, 1, 0]))     # 4 (можно перевернуть последний 0)
print(findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))  # 4 (можно перевернуть предпоследний 0)
print(findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))  # 6 (уже максимально)
print(findMaxConsecutiveOnes([0, 0, 1, 1, 0]))     # 3 (переворачиваем один из первых нулей)



# ВАРИАНТ 2
# ОПТИМИЗИРОВАННОЕ РЕШЕНИЕ (скользящее окно)
# Время: O(n) - один проход по массиву
# Память: O(1) - константное доп. пространство
def findMaxConsecutiveOnes(nums: list) -> int:
    max_length = 0
    left = 0
    zero_count = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1

        # Если нулей больше одного, двигаем левую границу
        while zero_count > 1:
            if nums[left] == 0:
                zero_count -= 1
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length

print(findMaxConsecutiveOnes([1, 0, 1, 1, 0]))     # 4 (можно перевернуть последний 0)
print(findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))  # 4 (можно перевернуть предпоследний 0)
print(findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))  # 6 (уже максимально)
print(findMaxConsecutiveOnes([0, 0, 1, 1, 0]))     # 3 (переворачиваем один из первых нулей)



# ВАРИАНТ 3
# ВЫВОД ДЛИНА ПОСЛЕДОВАТЕЛЬНОСТЬ
# Временная сложность: O(n) - один проход по массиву
# Пространственная сложность: O(k), где k - длина максимальной последовательности
def findMaxConsecutiveSequence(nums: list) -> tuple[int, list]:
    max_sequence = []
    current_sequence = []
    zero_pos = -1  # Позиция перевернутого нуля

    for i, num in enumerate(nums):
        if num == 1:
            current_sequence.append(1)
        else:
            if zero_pos == -1:  # Первый ноль - переворачиваем
                current_sequence.append(1)
                zero_pos = len(current_sequence) - 1
            else:  # Второй ноль - сбрасываем последовательность
                if len(current_sequence) > len(max_sequence):
                    max_sequence = current_sequence.copy()

                # Начинаем новую последовательность после перевернутого нуля
                current_sequence = current_sequence[zero_pos + 1:] + [1]
                zero_pos = len(current_sequence) - 1

        # Обновляем максимальную последовательность
        if len(current_sequence) > len(max_sequence):
            max_sequence = current_sequence.copy()

    # Проверяем последовательность в конце массива
    if len(current_sequence) > len(max_sequence):
        max_sequence = current_sequence.copy()

    return len(max_sequence), max_sequence


print(findMaxConsecutiveSequence([1, 0, 1, 1, 0]))     # -> (4, [1, 1, 1, 1])
print(findMaxConsecutiveSequence([1, 0, 1, 1, 0, 1]))  # -> (4, [1, 1, 1, 1])
print(findMaxConsecutiveSequence([1, 1, 0, 1, 1, 1]))  # -> (6, [1, 1, 1, 1, 1, 1])
print(findMaxConsecutiveSequence([0, 0, 1, 1, 0]))     # -> (3, [1, 1, 0])
print(findMaxConsecutiveSequence([1, 1, 1]))           # -> (3, [1, 1, 1])
print(findMaxConsecutiveSequence([0, 0, 0]))           # -> (1, [1])
"""



# Максимальное количество последовательных единиц  (разрешено перевернуть не более k нулей)  Max Consecutive Ones III
# ТОЖЕ САМОЕ   Max Consecutive Ones II  Только меняем       while zero_count > 1   на   while zero_count > k   1 ВАРИАНТ







# ОТВЕТ Максимальное количество последовательных единиц  (разрешено перевернуть не более k нулей)  Max Consecutive Ones III
"""
# ВАРИАНТ 1
# Оптимальное решение (метод скользящего окна)
# Временная сложность: O(n), где n - длина массива (каждый элемент обрабатывается дважды в худшем случае)
# Пространственная сложность: O(1) (используем константное количество переменных)
def findMaxConsecutiveOnes(nums: list[int], k: int) -> int:
    max_length = 0
    left = 0
    zero_count = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1

        # Если нулей больше одного, двигаем левую границу
        while zero_count > k:                               # Теперь сравниваем с k вместо 1
            if nums[left] == 0:
                zero_count -= 1
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length


print(findMaxConsecutiveOnes([1,1,1,0,0,0,1,1,1,1,0], 2))                  # 6
print(findMaxConsecutiveOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))  # 10
"""





# Поиск самой длинной подстроки без повторяющихся символов  НАПИШИ 6 ВАРИАНТОВ + ЕЩЕ 5 СО СТРОКОЙ

def lengthOfLongestSubstring(s: str) -> int:
    pass




# print(lengthOfLongestSubstring("bbbbb"))     # -> 1
# print(lengthOfLongestSubstring("abcabcbb"))  # -> 3
# print(lengthOfLongestSubstring("abcb"))      # -> 3
# print(lengthOfLongestSubstring("pwwkew"))    # -> 3
# print(lengthOfLongestSubstring("ckilbkd"))   # -> 5
# print(lengthOfLongestSubstring("dvdf"))      # -> 3





# Ответ Поиск самой длинной подстроки без повторяющихся символов  НАПИШИ 6 ВАРИАНТОВ + ЕЩЕ 5 СО СТРОКОЙ
"""

# ВАРИАНТ 1: Метод скользящего окна с использованием множества баланс между простотой и эффективностью  (O(n))
# O(min(m, n)) по памяти (m - размер алфавита)
            
def lengthOfLongestSubstring(s: str) -> int:                def lengthOfLongestSubstring(s: str) -> tuple[int, str]:                                                
    char_set = set()                                            char_set = set()                        
    left = 0                                                    left = 0                
    max_length = 0                                              max_sub = ""                    
                                                                for right, char in enumerate(s):        
    for right in range(len(s)):                                     while char in char_set:                                
        while s[right] in char_set:                                     char_set.remove(s[left])                                    
            char_set.remove(s[left])                                    left += 1                                        
            left += 1                                               char_set.add(char)                        
        char_set.add(s[right])                                      if right - left + 1 > len(max_sub):                                
        max_length = max(max_length, right - left + 1)                  max_sub = s[left:right+1]                                                        
                                                                       
    return max_length                                           return len(max_sub), max_sub                      
                                                                

# Лучший - Вариант 2, обеспечивает оптимальную производительность O(n) и обрабатывает каждый символ ровно один раз.
# ВАРИАНТ 2: Оптимизированный метод скользящего окна с хэш-мап для больших строк    (O(n))    O(min(m, n)) по памяти

def lengthOfLongestSubstring(s: str) -> int:                     def lengthOfLongestSubstring(s: str) -> tuple[int, str]:                                         
    char_map = {}                                                    last_seen = {}             
    left = 0                                                         start = 0         
    max_length = 0                                                   max_sub = ""             
                                                                     for i, char in enumerate(s): 
    for right in range(len(s)):                                          if char in last_seen and last_seen[char] >= start:                         
        if s[right] in char_map and char_map[s[right]] >= left:              start = last_seen[char] + 1                                                         
            left = char_map[s[right]] + 1                                last_seen[char] = i                                     
        char_map[s[right]] = right                                       if i - start + 1 > len(max_sub):                             
        max_length = max(max_length, right - left + 1)                       max_sub = s[start:i+1]                                                 
                                                                     
    return max_length                                                return len(max_sub), max_sub               
                                                                     
                                                                
# ВАРИАНТ 2: с комментариями УПРОЩЕННЫЙ

def lengthOfLongestSubstring(s: str) -> int:
    char_index = {}  # Словарь для хранения индексов символов
    max_length = 0   # Максимальная длина подстроки
    start = 0        # Начало текущей подстроки

    for i, char in enumerate(s):
        # Если символ уже встречался и его индекс больше или равен началу текущей подстроки
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1  # Обновляем начало подстроки

        char_index[char] = i  # Обновляем индекс текущего символа
        max_length = max(max_length, i - start + 1)  # Вычисляем максимальную длину

    return max_length  # Возвращаем только максимальную длину



# ВАРИАНТ 3: Использование OrderedDict (из collections) если нужно сохранять порядок Сложность: O(n) в среднем случае

from collections import OrderedDict
                                                          # Вариант с двумя указателями (без дополнительной памяти)  
def lengthOfLongestSubstring(s: str) -> int:              def lengthOfLongestSubstring(s: str) -> tuple[int, str]:                                          
    char_dict = OrderedDict()                                 start = 0                          
    max_len = 0                                               max_sub = ""          
    start = 0                                                 for i, char in enumerate(s):          
                                                                  # Проверяем, есть ли текущий символ в текущей подстроке  
    for i, char in enumerate(s):                                  while char in s[start:i]:                              
        if char in char_dict and char_dict[char] >= start:            start += 1                                                      
            start = char_dict[char] + 1                           if i - start + 1 > len(max_sub):                                  
        char_dict[char] = i                                           max_sub = s[start:i+1]                      
        max_len = max(max_len, i - start + 1)                 return len(max_sub), max_sub                                          
    return max_len                                                      
                                                            
                                                            
                                                            
#  лучше не использовать в продакшене (из-за O(n²))
# Вариант 4: Использование списка вместо множества    O(n^2) в худшем случае  O(n) по памяти

                                                      # Вариант со словарём (индексы символов)  
def lengthOfLongestSubstring(s: str) -> int:          def lengthOfLongestSubstring(s: str) -> tuple[int, str]:                                          
    chars = []                                            char_index = {}          
    max_length = 0                                        start = 0              
                                                          max_sub = ""  
    for char in s:                                        for i, char in enumerate(s):              
        if char in chars:                                     if char in char_index and char_index[char] >= start:                      
            chars = chars[chars.index(char)+1:]                   start = char_index[char] + 1                                          
        chars.append(char)                                    char_index[char] = i                      
        max_length = max(max_length, len(chars))              current_sub = s[start:i+1]                                              
                                                              if len(current_sub) > len(max_sub):  
    return max_length                                             max_sub = current_sub                  
                                                          return len(max_sub), max_sub  
                                                        
    
# ВАРИАНТ 5: Использование deque (двусторонней очереди)  Сложность: O(n) в среднем случае   Память: O(min(m, n))

from collections import deque                             from collections import deque                    
                                                         
def lengthOfLongestSubstring(s: str) -> int:              def lengthOfLongestSubstring(s: str) -> tuple[int, str]:                                            
    q = deque()                                               q = deque()
    max_len = 0                                               max_sub = ""
                                                              for char in s:
    for char in s:                                                while char in q:   
        while char in q:                                              q.popleft()          
            q.popleft()                                           q.append(char)     
        q.append(char)                                            if len(q) > len(max_sub):                
        max_len = max(max_len, len(q))                                max_sub = "".join(q)                               
    return max_len                                            return len(max_sub), max_sub
                                                          



print(lengthOfLongestSubstring("bbbbb"))     # -> 1       print(lengthOfLongestSubstring("bbbbb"))     # -> (1, 'b')  
print(lengthOfLongestSubstring("abcabcbb"))  # -> 3       print(lengthOfLongestSubstring("abcabcbb"))  # -> (3, 'abc')  
print(lengthOfLongestSubstring("abcb"))      # -> 3       print(lengthOfLongestSubstring("abcb"))      # -> (3, 'abc')  
print(lengthOfLongestSubstring("pwwkew"))    # -> 3       print(lengthOfLongestSubstring("pwwkew"))    # -> (3, 'wke')  
print(lengthOfLongestSubstring("ckilbkd"))   # -> 5       print(lengthOfLongestSubstring("ckilbkd"))   # -> (5, 'ckilb')  
print(lengthOfLongestSubstring("dvdf"))      # -> 3       print(lengthOfLongestSubstring("dvdf"))      # -> (3, 'vdf')  
"""



# Нахождение самой длинной палиндромной подстроки  НАПИШИ 5 ВАРИАНТОВ   Алгоритм Манакера (O(n) времени и O(n) памяти)
def longestPalindrome(s: str) -> str:
    pass




# print(longestPalindrome("babad"))     # -> bab
# print(longestPalindrome("cbbd"))      # -> bb
# print(longestPalindrome("aaaaa"))     # -> aaaaa






# ОТВЕТ Нахождение самой длинной палиндромной подстроки НАПИШИ 5 ВАРИАНТОВ Алгоритм Манакера (O(n) времени и O(n) памяти)
# Brute Force	                O(n³)	Только для тестирования, tiny strings
# Оптимизированный перебор	    O(n³)	Лучше не использовать
# Динамическое программирование	O(n²)	Для ясности кода, n ≤ 10⁴
# Расширение вокруг центра	    O(n²)	Лучший баланс (n ≤ 10⁵)
# Алгоритм Манакера	            O(n)	Максимальная производительность (n > 10⁵)
"""
# Очень медленный для больших строк    
# ВАРИАНТ 1: Перебор всех подстрок (Bute Force) Сложность: O(n³) - два вложенных цикла O(n²) и проверка палиндрома O(n)

def longestPalindrome(s: str) -> str:
    if not s:
        return ""

    longest = ""
    n = len(s)

    for i in range(n):
        for j in range(i, n):
            substring = s[i:j + 1]
            if substring == substring[::-1] and len(substring) > len(longest):
                longest = substring

    return longest



# ВАРИАНТ 2: Оптимизированный перебор (с ранним прекращением)   В худшем случае O(n³) медленный для больших строк
def longestPalindrome(s: str) -> str:
    if not s:
        return ""
    
    n = len(s)
    longest = s[0]  # минимальный палиндром - первый символ
    
    for i in range(n):
        # Если оставшаяся длина меньше текущего максимального, выходим
        if n - i <= len(longest):
            break
            
        for j in range(n, i, -1):  # идем с конца к началу
            # Если длина текущей подстроки меньше максимальной, пропускаем
            if j - i <= len(longest):
                break
                
            substring = s[i:j]
            if substring == substring[::-1]:
                longest = substring
                break  # нашли максимальный для этого i
    
    return longest    
    
    

# ВАРИАНТ 3: Динамическое программирование (O(n²) времени и O(n²) памяти)

def longestPalindrome(s: str) -> str:
    n = len(s)
    if n < 2:
        return s
    
    # Инициализация таблицы DP
    dp = [[False] * n for _ in range(n)]
    start = 0
    max_len = 1
    
    # Все подстроки длины 1 - палиндромы
    for i in range(n):
        dp[i][i] = True
    
    # Проверяем подстроки длины 2
    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            start = i
            max_len = 2
    
    # Проверяем подстроки длины > 2
    for length in range(3, n+1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i+1][j-1]:
                dp[i][j] = True
                if length > max_len:
                    start = i
                    max_len = length
    
    return s[start:start+max_len]
    


# ВАРИАНТ 4: Расширение вокруг центра (O(n²) времени, O(1) памяти)    достаточно быстро, проще в реализаци

 def longestPalindrome(s: str) -> str:
    def expandAroundCenter(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]
    
    longest = ""
    for i in range(len(s)):
        # Нечетная длина
        palindrome1 = expandAroundCenter(i, i)
        if len(palindrome1) > len(longest):
            longest = palindrome1
        
        # Четная длина
        palindrome2 = expandAroundCenter(i, i+1)
        if len(palindrome2) > len(longest):
            longest = palindrome2
    
    return longest   
    


# ВАРИАНТ 5: Алгоритм Манакера (O(n) времени и O(n) памяти)  макс. производительность! самый быстрый известный алгоритм 

def longestPalindrome(s: str) -> str:
    # Преобразование строки для обработки четных палиндромов
    T = '#'.join('^{}$'.format(s))
    n = len(T)
    P = [0] * n
    center = right = 0
    
    for i in range(1, n-1):
        # Используем зеркальное отражение
        if i < right:
            mirror = 2 * center - i
            P[i] = min(right - i, P[mirror])
        
        # Пытаемся расширить палиндром
        while T[i + P[i] + 1] == T[i - P[i] - 1]:
            P[i] += 1
        
        # Если палиндром выходит за текущий правый край
        if i + P[i] > right:
            center, right = i, i + P[i]
    
    # Находим максимальный палиндром
    max_len, center_index = max((P[i], i) for i in range(n))
    start = (center_index - max_len) // 2
    return s[start:start + max_len]

    
print(longestPalindrome("babad"))     # -> bab
print(longestPalindrome("cbbd"))      # -> bb
print(longestPalindrome("aaaaa"))     # -> aaaaa    
"""







# --- ctypes  Прямое манипулирование памятью в Python ---







# Изменение указателя через ctypes

x = 42






# Ответ Изменение указателя через ctypes
"""
import ctypes

x = 42
ptr = ctypes.addressof(ctypes.c_int(x))  # Получаем указатель
print(ptr)      # -> 2773500981272    id
print(id(x))    # -> 140715386928856
print(x)        # -> 42

# Изменение id через ctypes
new_ptr = ptr + 4  # Сдвиг указателя на 4 байта
print(new_ptr)  # -> 2773500981276    указатель ИЗМЕНИЛСЯ!!!   id + 4

print(id(x))    # -> 140715386928856
print(x)        # -> 42
"""



# Изменить tuple на новое значение чтобы id остался такой как и был # tuple хранит элементы в виде массива указателей
# Однако, так как размеры кортежей разные, копируются только первые элементы.           <-----    <-----


tup1 = (1, 2)
tup2 = (11, 111, 1111, 11111)







# Ответ Изменить tuple на новое значение чтобы id остался такой как и был # tuple хранит элементы в виде массива указателей

"""
# Изменение tuple через ctypes   # Прямое манипулирование памятью в Python
# Однако, так как размеры кортежей разные, копируются только первые элементы.           <-----    <-----

import ctypes

# Создаем два tuple
tup1 = (1, 2)                   
tup2 = (11, 111, 1111, 11111)   

# Печатаем значения и id
print("Before modification:")
print(f"tup1: {tup1}, id: {id(tup1)}")  # -> tup1: (1, 2),                 id: 2723780112000
print(f"tup2: {tup2}, id: {id(tup2)}")  # -> tup2: (11, 111, 1111, 11111), id: 2723780473536

# Вычисляем смещение до данных tuple
offset = (
        ctypes.sizeof(ctypes.c_size_t)  # Размер счетчика ссылок
        + ctypes.sizeof(ctypes.c_void_p)  # Размер указателя на тип объекта
        + ctypes.sizeof(ctypes.c_void_p)  # Размер указателя на длину tuple
)

# Вычисляем размер данных, которые нужно скопировать  БЕЗ НЕГО РАБОТАЕТ ТОЖЕ)
size = ctypes.sizeof(ctypes.c_void_p) * len(tup2)  # Размер одного элемента кортежа (указателя) * количество элементов

# Изменяем длину кортежа tup1
length_offset = ctypes.sizeof(ctypes.c_size_t) + ctypes.sizeof(ctypes.c_void_p)
ctypes.cast(id(tup1) + length_offset, ctypes.POINTER(ctypes.c_ssize_t))[0] = len(tup2)  # Можно использовать c_size_t

# Копируем данные из tup2 в tup1
ctypes.memmove(id(tup1) + offset, id(tup2) + offset, size)

# Печатаем измененные значения
print("After modification:")
print(f"tup1: {tup1}, id: {id(tup1)}")  # -> tup1: (11, 111, 1111, 11111), id: 2723780112000
print(f"tup2: {tup2}, id: {id(tup2)}")  # -> tup2: (11, 111, 1111, 11111), id: 2723780473536
"""




# Изменить frozenset на новое значение чтобы id остался такой как и был  # frozenset использует хэш-таблицу.
# Однако, так как размеры frozenset разные, копируются только первые элементы.           <-----    <-----


fs1 = frozenset([1, 2, 3])
fs2 = frozenset([4, 5, 6, 7, 8])








# Ответ Изменить frozenset на новое значение чтобы id остался такой как и был  # frozenset использует хэш-таблицу.
"""
# Однако, так как размеры frozenset разные, копируются только первые элементы.           <-----    <-----
import ctypes

# Создаем два frozenset
fs1 = frozenset([1, 2, 3])
fs2 = frozenset([4, 5, 6, 7, 8])

# Печатаем значения и id
print("Before modification:")
print(f"fs1: {fs1}, id: {id(fs1)}")  # -> fs1: frozenset({1, 2, 3}),       id: 2241246576224
print(f"fs2: {fs2}, id: {id(fs2)}")  # -> fs2: frozenset({4, 5, 6, 7, 8}), id: 2241247428672

# Вычисляем смещение до данных frozenset
offset = (
    ctypes.sizeof(ctypes.c_size_t)    # Размер счетчика ссылок
    + ctypes.sizeof(ctypes.c_void_p)  # Размер указателя на тип объекта
    + ctypes.sizeof(ctypes.c_void_p)  # Размер указателя на длину frozenset
)

# Изменяем длину frozenset fs1
length_offset = ctypes.sizeof(ctypes.c_size_t) + ctypes.sizeof(ctypes.c_void_p)
ctypes.cast(id(fs1) + length_offset, ctypes.POINTER(ctypes.c_ssize_t))[0] = len(fs2)    # Можно использовать c_size_t

# Копируем данные из fs2 в fs1
ctypes.memmove(id(fs1) + offset, id(fs2) + offset, ctypes.sizeof(ctypes.c_void_p) * len(fs2))

# Печатаем измененные значения
print("After modification:")
print(f"fs1: {fs1}, id: {id(fs1)}")  # -> fs1: frozenset({4, 5, 6, 7, 8}), id: 2241246576224
print(f"fs2: {fs2}, id: {id(fs2)}")  # -> fs2: frozenset({4, 5, 6, 7, 8}), id: 2241247428672
"""




# Изменить str на новое значение чтобы id остался такой как и был


str1 = "hello"
str2 = "world12345"  # Если заменить на такую строку    str2 = "worldworld"   то str1 будет равно    str1 = "world"








# Ответ Изменить str на новое значение чтобы id остался такой как и был

"""
# Изменение str через ctypes   # Прямое манипулирование памятью в Python

import ctypes

# Создаем строки   # Заменяет на новые строки, если str2 = "wwwwwwwwww"  то будет  str1 = "wwwww"
str1 = "hello"
str2 = "world12345"  # Если заменить на такую строку    str2 = "worldworld"   то str1 будет равно    str1 = "world"

print("Before modification:")
print(f"str1: {str1}, id: {id(str1)}")  # -> str1: hello,      id: 3030659487312
print(f"str2: {str2}, id: {id(str2)}")  # -> str2: world12345, id: 3030659487504

# Вычисляем смещение до данных строки
# Внутренняя структура строки в CPython включает:
# - счетчик ссылок (8 байт)
# - указатель на тип объекта (8 байт)
# - длину строки (8 байт)
# - хэш (8 байт)
# - флаги (4 байта)
# - данные строки (зависят от длины и кодировки)

offset = (
        ctypes.sizeof(ctypes.c_size_t)  # Счетчик ссылок
        + ctypes.sizeof(ctypes.c_void_p)  # Указатель на тип объекта
        + ctypes.sizeof(ctypes.c_size_t)  # Длина строки
        + ctypes.sizeof(ctypes.c_size_t)  # Хэш
        + ctypes.sizeof(ctypes.c_int)  # Флаги
)

# Копируем данные из str2 в str1
size = len(str2.encode('utf-8'))  # Размер данных строки в байтах

# Изменяем str1 на "world"                                              #   world   <-----
ctypes.memmove(id(str1) + offset, id(str2) + offset, size)

print("After modification:")
print(f"str1: {str1}, id: {id(str1)}")  # -> str1: world,      id: 3030659487312
print(f"str2: {str2}, id: {id(str2)}")  # -> str2: world12345, id: 3030659487504
"""







# --- Алгоритмы сортировки Python ---



# БЕЗ ФУНКЦИИ  Написать Алгоритм БИНАРНОГО поиска на Python  O(log n)   без конца делит область поиска пополам.


d = [-1, -3, 2, 4, 5, 7, 8, 9]
target = 9







# Ответ БЕЗ ФУНКЦИИ  Написать Алгоритм БИНАРНОГО поиска на Python  O(log n)   без конца делит область поиска пополам.
# Важно отметить, что массив должен быть ОТСОРТИРОВАН для применения бинарного поиска.
"""
d = [-1, -3, 2, 4, 5, 7, 8, 9]                          
n = len(d)                           
                                     
search_v = 9                         
left, right = 0, n-1                  
                                     
while left <= right:                  
    middle = (left + right) // 2                              
    v = d[middle]                    
    if v == search_v:
        # __import__('sys').stdout.write(f'{v} {middle}')  # 9 7   Тоже самое            
        print(v, middle)   # 9 7                                                  
        break            
    elif v < search_v:                  
        left = middle+1                    
    elif v > search_v:                  
        right = middle-1                        
else:
    # __import__('sys').stdout.write('Значение не найдено')  # Тоже самое                     
    print('Значение не найдено')                             
                                                
# 9 7
"""



# ФУНКЦИЮ  Написать Алгоритм БИНАРНОГО поиска на Python  O(log n)   без конца делит область поиска пополам.

d = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
target = 9



def binary_search(arr, target):
    pass




# print(binary_search(d, target))  # -> 8
# __import__('sys').stdout.write(str(binary_search(d, target)))  # -> 8   Тоже самое







# Ответ ФУНКЦИЮ  Написать Алгоритм БИНАРНОГО поиска на Python  O(log n)   без конца делит область поиска пополам.
# Важно отметить, что массив должен быть ОТСОРТИРОВАН для применения бинарного поиска.
"""
d = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
target = 9

def binary_search(arr, target):
    arr = sorted(arr)
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2  # Находим середину

        if arr[mid] == target:
            return mid  # Нашли элемент, возвращаем его индекс
        elif arr[mid] < target:
            left = mid + 1  # Ищем в правой половине
        else:
            right = mid - 1  # Ищем в левой половине

    return -1  # Элемент не найден


print(binary_search(d, target))  # -> 8
__import__('sys').stdout.write(str(binary_search(d, target)))  # -> 8   Тоже самое



# Интересный вариант из книги   High Performance Python                                          <-----
def binary_search(needle, haystack):
    haystack = sorted(haystack)
    imin, imax = 0, len(haystack)
    while True:
        if imin > imax:
            return -1
        midpoint = (imin + imax) // 2
        if haystack[midpoint] > needle:
            imax = midpoint
        elif haystack[midpoint] < needle:
            imin = midpoint + 1
        else:
            return midpoint

print(binary_search(target, d))  # -> 8
__import__('sys').stdout.write(str(binary_search(target, d)))  # -> 8   Тоже самое
"""





# Задача с собеседования
# Написать Quick Sort/Быстрая сортировка   Quicksort обычно работает быстрее, Merge Sort на практике







# Реализация Quick Sort/Быстрая сортировка   Quicksort обычно работает быстрее, Merge Sort на практике
"""
# Вариант 1: Опорный элемент — последний элемент массива
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    left = []
    right = []
    middle = []

    for i in arr:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            middle.append(i)
            
    return quick_sort(left) + middle + quick_sort(right)

# Пример использования
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = quick_sort(arr)
print("Отсортированный массив:", sorted_arr)  # -> Отсортированный массив: [1, 5, 7, 8, 9, 10]
__import__('sys').stdout.write('Отсортированный массив: ' + str(sorted_arr)) # -> Отсортированный массив: [1, 5, 7, 8, 9, 10]


# Вариант 2: Опорный элемент — средний элемент массива
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot_index = len(arr)//2
    pivot = arr[pivot_index]
    left = []
    right = []
    middle = []

    for i in arr:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            middle.append(i)

    return quick_sort(left) + middle + quick_sort(right)


# Пример использования
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = quick_sort(arr)
print("Отсортированный массив:", sorted_arr)  # -> Отсортированный массив: [1, 5, 7, 8, 9, 10]



# Вариант 3: Случайный выбор опорного элемента

import random

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = random.choice(arr)  # Случайный опорный элемент
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

# Пример использования
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = quick_sort(arr)
print("Отсортированный массив:", sorted_arr)  # -> Отсортированный массив: [1, 5, 7, 8, 9, 10]
"""





# 1) Написать Сортировку пузырьком (Bubble Sort)
# Время: O(n²) в худшем и среднем случаях, O(n) в лучшем.  Пространство: O(1)








# 1) Сортировка пузырьком (Bubble Sort)    Время: O(n²) в худшем и среднем случаях, O(n) в лучшем.   Пространство: O(1)
"""
# Тоже самое                                            # Тоже самое
def bubble_sort(arr):                                   def bubble_sort(arr):            
    n = len(arr)                                            n = len(arr)        
    for i in range(n):                                      for i in range(n):            
        swapped = False                                         for j in range(0, n-i-1):            
        for j in range(n-i-1):                                      if arr[j] > arr[j+1]:  # Для обратной сортировки <                  
            if arr[j] > arr[j+1]:                                       arr[j], arr[j+1] = arr[j+1], arr[j]                        
                arr[j], arr[j+1] = arr[j+1], arr[j]         return arr                                        
                swapped = True                                              
        if not swapped:                                             
            break                                               
    return arr                                              


# Пример использования
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print("(Bubble Sort):", sorted_arr)                             # -> (Bubble Sort): [11, 12, 22, 25, 34, 64, 90]
__import__('sys').stdout.write(f'(Bubble Sort): {sorted_arr}')  # -> (Bubble Sort): [11, 12, 22, 25, 34, 64, 90]
"""



# 2) Написать Сортировку выбором (Selection Sort)
# Время: O(n²) во всех случаях.   Пространство: O(1)








# 2) Сортировка выбором (Selection Sort)  Время: O(n²) во всех случаях.   Пространство: O(1)
"""
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:    # if arr[j] > arr[min_index]:   # Для обратной сортировки  >
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Пример использования
arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print("(Selection Sort):", sorted_arr)                             # -> (Selection Sort): [11, 12, 22, 25, 64]
__import__('sys').stdout.write(f'(Selection Sort): {sorted_arr}')  # -> (Selection Sort): [11, 12, 22, 25, 64]
"""



# 3) Написать Сортировку вставками (Insertion Sort)
# Время: O(n²) в худшем случае, O(n) в лучшем.   Пространство: O(1)







# 3) Сортировка вставками (Insertion Sort)    Время: O(n²) в худшем случае, O(n) в лучшем.   Пространство: O(1)
"""
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:   # while j >= 0 and arr[j] < key:   # Для обратной сортировки  >
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Пример использования
arr = [64, 34, 25, 12, 22, 11]
sorted_arr = insertion_sort(arr)
print("(Insertion Sort):", sorted_arr)                             # -> (Insertion Sort): [11, 12, 22, 25, 34, 64]
__import__('sys').stdout.write(f'(Insertion Sort): {sorted_arr}')  # -> (Insertion Sort): [11, 12, 22, 25, 34, 64]
"""



# 4) Написать Быстрая сортировка (Quick Sort)   Quicksort обычно работает быстрее, Merge Sort на практике
# O(n log n) в среднем случае, O(n²) в худшем. Пространство: O(log n) для рекурсии.








# 4) Быстрая сортировка (Quick Sort)   O(n log n) в среднем случае, O(n²) в худшем. Пространство: O(log n) для рекурсии.
"""
def quick_sort(arr):
    match arr:
        case x if len(x) <= 1:
            return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
    # return quick_sort(right) + middle + quick_sort(left)  # Для обратной сортировки

# Пример использования
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = quick_sort(arr)
print("(Quick Sort):", sorted_arr)                             # -> (Quick Sort): [11, 12, 22, 25, 34, 64, 90]
__import__('sys').stdout.write(f'(Quick Sort): {sorted_arr}')  # -> (Quick Sort): [11, 12, 22, 25, 34, 64, 90]

# Придумал свой вариант
def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    pp = lst[len(lst)//2]
    l, r, m = [[] for _ in 'lrm']
    for i in lst:
        match i:
            case i if i < pp:
                l.append(i)
            case i if i > pp:
                r.append(i)
            case _:
                m.append(i)
    return quick_sort(l) + m + quick_sort(r)
"""



# 5) Написать Сортировку слиянием (Merge Sort)
# Время: O(n log n) во всех случаях.    Пространство: O(n)








# 5) Сортировка слиянием (Merge Sort)    Время: O(n log n) во всех случаях.    Пространство: O(n)
"""
                                             # Интересный аналог функции merge_sort       
def merge_sort(arr):                         def merge_sort(lst):                           
    if len(arr) <= 1:                            if len(lst) <= 1:                           
        return arr                                   return lst                       
    mid = len(arr) // 2                          m = len(lst) // 2                           
    left = merge_sort(arr[:mid])                 left, right = lst[:m], lst[m:]                                       
    right = merge_sort(arr[mid:])                return merge(merge_sort(left), merge_sort(right))                                       
    return merge(left, right)                

def merge(left, right):
    result = []
    i = j = 0                                # i, j = 0, 0  # Тоже самое
    while i < len(left) and j < len(right):
        if left[i] < right[j]:               # if l[i] > r[j]:  # Для обратной сортировки
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]          # result.extend(left[i:])  # Тоже самое    # Менять местами можно  result += right[j:]
    result += right[j:]         # result.extend(right[j:]) # Тоже самое    # Менять местами можно  result += left[i:] 
    return result

# Пример использования
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = merge_sort(arr)
print("(Merge Sort):", sorted_arr)                             # -> (Merge Sort): [11, 12, 22, 25, 34, 64, 90]
__import__('sys').stdout.write(f'(Merge Sort): {sorted_arr}')  # -> (Merge Sort): [11, 12, 22, 25, 34, 64, 90]
"""



# 6) Написать Пирамидальная сортировка (Heap Sort)
# Время: O(n log n) во всех случаях.  Пространство: O(1)








# 6) Пирамидальная сортировка (Heap Sort)     Время: O(n log n) во всех случаях.  Пространство: O(1)
"""
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

# Пример использования
arr = [64, 25, 12, 22, 11]
sorted_arr = heap_sort(arr)
print("(Heap Sort):", sorted_arr)                             # -> (Heap Sort): [11, 12, 22, 25, 64]
__import__('sys').stdout.write(f'(Heap Sort): {sorted_arr}')  # -> (Heap Sort): [11, 12, 22, 25, 64]
"""



# 7) Написать Тим-сорт (TimSort)
# Время: O(n log n) в среднем, O(n) в лучшем случае.  Пространство: O(n)








# 7) Тим-сорт (Tim Sort)     Время: O(n log n) в среднем, O(n) в лучшем случае.  Пространство: O(n)
"""
def insertion_sort(arr, left, right):
    '''Сортировка вставками для подмассива arr[left:right+1]'''
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge(left, right):
    '''Слияние двух отсортированных подмассивов'''
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def tim_sort(arr):
    '''Основная функция Тим-сорт'''
    min_run = 32  # Минимальный размер подмассива для сортировки вставками
    n = len(arr)

    # 1. Сортируем подмассивы размером min_run
    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion_sort(arr, start, end)

    # 2. Объединяем отсортированные подмассивы
    size = min_run
    while size < n:
        for left in range(0, n, size * 2):
            mid = left + size - 1
            right = min((left + 2 * size - 1), (n - 1))

            if mid < right:  # Убедимся, что mid < right
                merged = merge(arr[left:mid + 1], arr[mid + 1:right + 1])
                arr[left:left + len(merged)] = merged

        size *= 2
    return arr


# Пример использования
arr = [64, 25, 12, 22, 11]
sorted_arr = tim_sort(arr)
print("(Tim Sort):", sorted_arr)  # Ожидается: (Tim Sort): [11, 12, 22, 25, 64]
__import__('sys').stdout.write(f'(Tim Sort): {sorted_arr}')  # -> (Tim Sort): [11, 12, 22, 25, 64]
"""



# 8) Написать Сортировка Шелла (Shell Sort)
# Время: O(n²) в худшем, O(n log n) в среднем.  Пространство: O(1)







# 8) Сортировка Шелла (Shell Sort)     Время: O(n²) в худшем, O(n log n) в среднем.  Пространство: O(1)
"""
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

# Пример использования
arr = [64, 25, 12, 22, 11]
sorted_arr = shell_sort(arr)
print("(Shell Sort):", sorted_arr)                             # -> (Shell Sort): [11, 12, 22, 25, 64]
__import__('sys').stdout.write(f'(Shell Sort): {sorted_arr}')  # -> (Shell Sort): [11, 12, 22, 25, 64]
"""



# 9) Написать Сортировка битом (Radix Sort)
# Время: O(nk), где k — количество разрядов.  Пространство: O(n + k)








# 9) Сортировка битом (Radix Sort)     Время: O(nk), где k — количество разрядов.  Пространство: O(n + k)
"""
def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for i in range(n - 1, -1, -1):
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max1 = max(arr)
    exp = 1
    while max1 // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10
    return arr

# Пример использования
arr = [64, 25, 12, 22, 11]
sorted_arr = radix_sort(arr)
print("(Radix Sort):", sorted_arr)                             # -> (Radix Sort): [11, 12, 22, 25, 64]
__import__('sys').stdout.write(f'(Radix Sort): {sorted_arr}')  # -> (Radix Sort): [11, 12, 22, 25, 64]
"""



# 10) Написать Сортировка подсчётом (Counting Sort)
# Время: O(n + k), где k — максимальное значение в массиве. Пространство: O(k)








# 10) Сортировка подсчётом (Counting Sort)  Время: O(n + k), где k — максимальное значение в массиве. Пространство: O(k)
"""
Отличие заключается в том, сохраняется ли порядок одинаковых элементов после сортировки.  УСТРОЙЧИВАЯ vs НЕ УСТРОЙЧИВАЯ  

# Первый вариант     УСТРОЙЧИВАЯ(stable)         # Другой Вариант  НЕ УСТРОЙЧИВАЯ(unstable) 
def counting_sort(arr):                          def simple_counting_sort(k, n, A):
    max_val = max(arr)                               C = [0] * k
    count = [0] * (max_val + 1)                      for i in range(n):
    output = [0] * len(arr)                              C[A[i]] += 1
    for num in arr:                                  index = 0
        count[num] += 1                              for i in range(k):
    for i in range(1, len(count)):                       for j in range(C[i]):      
        count[i] += count[i - 1]                             A[index] = i 
    for i in range(len(arr) - 1, -1, -1):                    index += 1       
        output[count[arr[i]] - 1] = arr[i]           return A
        count[arr[i]] -= 1                        
    return output                                # Пример использования 
                                                 arr = [64, 25, 12, 22, 11]     
# Пример использования                           max_val = max(arr) + 1  # максимальное значение + 1  
arr = [64, 25, 12, 22, 11]                       sorted_arr = simple_counting_sort(max_val, len(arr), arr)     
sorted_arr = counting_sort(arr)                  print("(Simple Counting Sort):", sorted_arr) # -> [11, 12, 22, 25, 64]
print("(Counting Sort):", sorted_arr)                             # -> (Counting Sort): [11, 12, 22, 25, 64]
__import__('sys').stdout.write(f'(Counting Sort): {sorted_arr}')  # -> (Counting Sort): [11, 12, 22, 25, 64]      <-----
"""



# 11) Написать Сортировка по ведрам (Bucket Sort):
# Время: O(n + k) для равномерно распределенных данных, где k — количество ведер. Пространство: O(n + k)








# 11) Сортировка по ведрам (Bucket Sort)  O(n + k) для равномерно распределенных данных, k - кол-во ведер. Прос. O(n + k)
"""
def insertion_sort(arr):                                       
    for i in range(1, len(arr)):                               
        key = arr[i]                                           
        j = i - 1                                              
        while j >= 0 and arr[j] > key:                         
            arr[j + 1] = arr[j]                                
            j -= 1                                             
        arr[j + 1] = key                                       
    return arr                                                 
                                                               
                                                               
def bucket_sort(arr):
    if len(arr) == 0:
        return arr
    max_val = max(arr)
    min_val = min(arr)
 
    bucket_count = len(arr)
    bucket_range = (max_val - min_val) / bucket_count
    buckets = [[] for _ in range(bucket_count)]
 
    for num in arr:
        index = int((num - min_val) / bucket_range)
        if index >= bucket_count:
            index = bucket_count - 1
        buckets[index].append(num)
 
    sorted_array = []
    for bucket in buckets:
        # sorted_array.extend(insertion_sort(bucket))  # Тоже самое +=
        sorted_array += insertion_sort(bucket)
 
    return sorted_array


# Пример использования
arr = [64, 25, 12, 22, 11]
sorted_arr = bucket_sort(arr)
print("(Bucket Sort):", sorted_arr)                             # -> (Bucket Sort): [11, 12, 22, 25, 64]
__import__('sys').stdout.write(f'(Bucket Sort): {sorted_arr}')  # -> (Bucket Sort): [11, 12, 22, 25, 64]
"""




# --- Django  Чуть-чуть ---

# Напишите raw-запрос








# Ответ Напишите raw-запрос
"""
people = Person.objects.raw("SELECT id, name FROM hello_person")
"""



# Перепишите lookups

















# Ответ Перепишите lookups
r"""
 Model.objects.all()                                       показать все записи
 Model.objects.filter(budget=1000)                    ==   фильтр на равенство поля
 Model.objects.filter(budget__gt=1000)                 >   фильтр на поле больше значения (great then)
 Model.objects.filter(budget__lt=1000)                 <   фильтр на поле меньше значения
 Model.objects.filter(budget__gte=1000)               >=   фильтр на поле больше либо равно значения
 Model.objects.filter(budget__lte=1000)               <=   фильтр на поле меньше либо равно значения
 Model.objects.exclude(budget=1000)                   !=   фильтр на поле не равно значению
 Model.objects.filter(year__isnull=True)                   фильтр на поле пустое (False - не пустое)
 Model.objects.filter(year__isnull=True, name=’Avatar’)    фильтр на два поля
 Model.objects.exclude(budget=1000).filter(name=’Avatar’)  фильтр на два поля
 Model.objects.filter(name__contains=’Avatar’)             поле содержит значение, чувствителен к регистру
 Model.objects.filter(name__icontains=’Avatar’)            поле содержит значение, НЕ чувствителен к регистру
 Model.objects.filter(name__startswith=’a’)                поле начинается с “a”
 Model.objects.filter(name__endswith=’a’)                  поле заканчивается на “a”
 Model.objects.filter(id__in=[3,5,6])                      выбираются все значения из списка
 
 Movie.objects.all()[:2] # Срезы
 Movie.objects.all()[-1] # ValueError: Negative indexing is not supported.   Отрицательные индексы не поддерживает
 
 # Очень полезные методы   __regex  - чувствительное к регистру       __iregex - НЕчувствительное к регистру
 Model.objects.filter(adv_images__regex=r'^\d\.')[:3]      # фильтрация по регулярному выражению (чувствительно)
 Model.objects.filter(adv_images__iregex=r'^\d\.')[:3]     # фильтрация по регулярному выражению (не чувствительно)
 Model.objects.get(title__regex=r"^(An?|The) +")           # получение одного объекта по регулярному выражению
"""








# Задачи на ORM
"""
class City(models.Model):
   name = models.CharField()


class Person(models.Model):
    name = models.CharField()
    city = models.ForeignKey(City)
    """

# 1)Вывести список людей и городов где они живут?
# 2)Вывести всех людей, живущих в городе N
# 3)Вывести 5 городов с наибольшим населением, упорядочив по убыванию.








# Ответ:
# Вот пример определения моделей с учетом этих деталей:
"""
from django.db import models

class City(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Person(models.Model):
     name = models.CharField(max_length=255)
     city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='people')

     def __str__(self):
         return self.name
"""



# -- Теперь перейдем к выполнению задач --:


# 1. Вывести список людей и городов, где они живут:







# Ответ 1. Вывести список людей и городов, где они живут:
"""
people_with_cities = Person.objects.select_related('city').values('name', 'city__name')
for person in people_with_cities:
    print(f'Человек: {person["name"]}, Город: {person["city__name"]}')
"""



# 2. Вывести всех людей, живущих в городе N:

city_name = 'N'  # укажите название города







# Ответ 2. Вывести всех людей, живущих в городе N:
"""
city_name = 'N'  # укажите название города
people_in_city_n = Person.objects.filter(city__name=city_name)

for person in people_in_city_n:
    print(f'Человек: {person.name}')
"""




# 3. Вывести 5 городов с наибольшим населением, упорядочив по убыванию.
# Для этого нам нужно будет добавить поле для хранения количества людей в каждом городе. Однако, чтобы подсчитать
# это количество динамически, мы можем использовать аннотирование с `Count`.







# Ответ 3. Вывести 5 городов с наибольшим населением, упорядочив по убыванию.
"""
from django.db.models import Count

top_cities = City.objects.annotate(population=Count('people')).order_by('-population')[:5]

for city in top_cities:
    print(f'Город: {city.name}, Население: {city.population}')
"""



# Переписать Класс Q Class Q  Написать Использование  1)OR  2)AND  3)NOT  4)Сложные условия  5)Комбинирование условий


# Первый пример!






# 1)OR  Найдем всех людей, у которых имя "John" ИЛИ фамилия "Doe"




# 2)AND Найдем всех людей, у которых имя "John" И фамилия "Doe"



# 3)NOT Найдем всех людей, у которых имя "John", кроме тех, у кого фамилия "Doe"



# 4)Сложные условия Найдем всех людей, у которых имя "John" И (фамилия "Doe" ИЛИ возраст больше 30)



# 5)Комбинирование условий Найдем всех людей, у которых имя "John", ИЛИ фамилия "Doe", И возраст не меньше 25




# Ответ Класс Q Class Q  Написать Использование  1)OR  2)AND  3)NOT  4)Сложные условия  5)Комбинирование условий

"""
from django.db.models import Q

# Первый пример!
Women.objects.filter(Q(pk__lt=5) | Q(cat_id=2))                                  # | == OR  # |  = Вертикальная черта
Women.objects.filter(Q(pk__lt=5) & Q(cat_id=2))                                  # & == AND # & = Амперсанд
Women.objects.filter(~Q(pk__lt=5) & Q(cat_id=2))                                 # ~ == NOT # ~ = Тильда
Women.objects.filter(~Q(pk__in=[1, 2, 5]) | Q(cat_id=2), title__icontains='pa')

# 1)OR Использование с OR
# Найдем всех людей, у которых имя "John" ИЛИ фамилия "Doe"
people = Person.objects.filter(Q(first_name='John') | Q(last_name='Doe'))

# 2)AND Использование с AND
# Найдем всех людей, у которых имя "John" И фамилия "Doe"
people = Person.objects.filter(Q(first_name='John') & Q(last_name='Doe'))

# 3)NOT Использование NOT
# Найдем всех людей, у которых имя "John", кроме тех, у кого фамилия "Doe"
people = Person.objects.filter(Q(first_name='John') & ~Q(last_name='Doe'))

# 4)Сложные условия
# Найдем всех людей, у которых имя "John" И (фамилия "Doe" ИЛИ возраст больше 30)
people = Person.objects.filter(Q(first_name='John') & (Q(last_name='Doe') | Q(age__gt=30)))

# 5)Комбинирование условий
# Найдем всех людей, у которых имя "John", ИЛИ фамилия "Doe", И возраст не меньше 25
people = Person.objects.filter((Q(first_name='John') | Q(last_name='Doe')) & Q(age__gte=25))
"""



# -- В Django ORM запросы по умолчанию ЛЕНИВЫЕ --

# В Django ORM запросы по умолчанию ЛЕНИВЫЕ. Это означает, что они не выполняются до тех пор, пока не потребуется
# получение данных. Чтобы применить запрос и получить данные, вы можете использовать следующие методы:

# 1. Конвертация в другие структуры данных list(): Преобразует QuerySet в список и выполняет запрос.



# Ответ 1. Конвертация в другие структуры данных list(): Преобразует QuerySet в список и выполняет запрос.
"""
results = list(MyModel.objects.all())
"""


# 2. Использование next() или list(): Если вам нужно только одно значение, вы можете использовать next():



# Ответ 2. Использование next() или list(): Если вам нужно только одно значение, вы можете использовать next():
"""
queryset = MyModel.objects.all()
first_item = next(iter(queryset))  # Возвращает первый элемент, выполняя запрос
"""

# 3. len(): Получает количество объектов в QuerySet и выполняет запрос.



# Ответ 3. len(): Получает количество объектов в QuerySet и выполняет запрос.
"""
count = len(MyModel.objects.all())
"""

# 4. for циклы: Итерирование по QuerySet также выполняет запрос.





# Ответ 4. for циклы: Итерирование по QuerySet также выполняет запрос.
"""
for obj in MyModel.objects.all():
    print(obj)
"""

# 5. get(): Получает единственный объект и выполняет запрос.




# Ответ 5. get(): Получает единственный объект и выполняет запрос.
"""
obj = MyModel.objects.get(id=1)
"""

# 6. Методы get() и filter():
# Вызов get() возвращает конкретный объект, тогда как filter() возвращает QuerySet, который будет выполнен позже.








# Ответ 6. Методы get() и filter():
# Вызов get() возвращает конкретный объект, тогда как filter() возвращает QuerySet, который будет выполнен позже.
"""
single_object = MyModel.objects.get(id=1)                  # Выполняет SQL-запрос
filtered_objects = MyModel.objects.filter(name='example')  # Запрос выполняется при дальнейшей обработке
"""

# 7. first() и last(): Получает первый или последний объект и выполняет запрос.






# Ответ 7. first() и last(): Получает первый или последний объект и выполняет запрос.
"""
first_obj = MyModel.objects.first()
last_obj = MyModel.objects.last()
"""

# 8. exists(): Проверяет наличие объектов и выполняет запрос.





# Ответ 8. exists(): Проверяет наличие объектов и выполняет запрос.
"""
exists = MyModel.objects.filter(condition).exists()
"""

# 9. count(): Возвращает количество объектов в QuerySet и выполняет запрос.





# Ответ 9. count(): Возвращает количество объектов в QuerySet и выполняет запрос.
"""
count = MyModel.objects.all().count()
"""

# 10. aggregate() и annotate(): Эти методы возвращают агрегированные данные и также выполняют запрос.






# Ответ 10. aggregate() и annotate(): Эти методы возвращают агрегированные данные и также выполняют запрос.
"""
from django.db.models import Count, Sum

result = MyModel.objects.aggregate(Count('field_name'))  # Подсчитываем количество

result_aggregate = MyModel.objects.aggregate(total_count=Count('id'), total_sum=Sum('field_name'))
result_annotate = MyModel.objects.annotate(field_name_sum=Sum('field_name'))

print(result_aggregate)  # Выводит агрегированные результаты
for obj in result_annotate:
    print(f'{obj.pk}: {obj.field_name_sum}')
"""

# 11. Пример аннотации: Получаем все объекты MyModel с подсчитанным количеством связанных объектов из RelatedModel.






# Ответ 11. Пример аннотации: Получаем все объекты MyModel с подсчитанным количеством связанных объектов из RelatedModel.
"""
from django.db.models import Count

result = MyModel.objects.annotate(related_count=Count('relatedmodel'))
for obj in result:
    print(f'{obj.pk}: {obj.related_count}')
"""

# 12. values() и values_list(): Эти методы возвращают список словарей или кортежей соответственно, выполняя запрос.








# Ответ 12. values() и values_list(): Эти методы возвращают список словарей или кортежей соответственно, выполняя запрос.
"""
queryset = MyModel.objects.values('id', 'name')           # Возвращает словари с указанными полями
queryset = MyModel.objects.values_list('id', 'name')      # Возвращает список кортежей
queryset = MyModel.objects.values_list('name', flat=True) # Результаты в виде списков
"""

# 13. Срезы: Использование срезов для получения определенного количества объектов.



# Ответ 13. Срезы: Использование срезов для получения определенного количества объектов.
"""
first_five = queryset[:5]  # Выполняет запрос и возвращает первые пять объектов
"""

# 14. Оптимизация запросов: Используйте select_related() и prefetch_related() для оптимизации запросов к связанным объектам.
# Пример использования select_related для один-к-одному и один-ко-многим.








# Ответ 14. Оптимизация запросов: Используйте select_related() и prefetch_related() для оптимизации запросов к связанным объектам.
"""
results = MyModel.objects.select_related('related_model').all()  # Пример использования select_related

results = MyModel.objects.prefetch_related('related_models').all()  # Пример использования prefetch_related
"""

# 15. iterator(): Позволяет итерироваться по QuerySet без загрузки всех объектов в память.





# Ответ 15. iterator(): Позволяет итерироваться по QuerySet без загрузки всех объектов в память.
"""
for obj in MyModel.objects.all().iterator():
    print(obj)
"""

# 16. bulk_create() и bulk_update(): Позволяют выполнять массовые операции создания и обновления объектов.





# Ответ 16. bulk_create() и bulk_update(): Позволяют выполнять массовые операции создания и обновления объектов.
"""
# Пример bulk_create
MyModel.objects.bulk_create([
    MyModel(field1='value1', field2='value2'),
    MyModel(field1='value3', field2='value4'),
])

# Пример bulk_update
MyModel.objects.bulk_update(objects_to_update, ['field1', 'field2'])
"""




# Напиши SQL Задачу с собеседования    НАПИСАТЬ 2 ВАРИАНТА ---







# --- SQL Задача с собеседования    НАПИСАТЬ 2 ВАРИАНТА  ---

"""
Таблицы:
users (пользователи):
    id (INT, PRIMARY KEY)
    name (VARCHAR)
    email (VARCHAR)
    registration_date (DATE)

products (продукты):
    id (INT, PRIMARY KEY)
    name (VARCHAR)
    category (VARCHAR)
    price (DECIMAL)

orders (заказы):
    id (INT, PRIMARY KEY)
    user_id (INT, FOREIGN KEY на users.id)
    product_id (INT, FOREIGN KEY на products.id)
    order_date (DATE)
    quantity (INT)


Первый вариант
Чтобы получить имена пользователей, которые когда-либо делали заказы на продукты, использовать следующий SQL-запрос:

SELECT DISTINCT u.name 
FROM users u
JOIN orders o ON u.id = o.user_id
JOIN products p ON o.product_id = p.id;

### Объяснение:
1. Используем `JOIN` для соединения таблицы `users` с таблицей `orders` по `user_id`.
2. Затем соединяем таблицу `orders` с таблицей `products` по `product_id`.
3. Используем `DISTINCT`, чтобы избежать дублирования имен пользователей, если они сделали несколько заказов.



Второй вариант
**Использование `LEFT JOIN` для получения всех пользователей и их продуктов (если есть):**

SELECT u.name, p.name AS product_name 
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
LEFT JOIN products p ON o.product_id = p.id;

В этом запросе вы получите всех пользователей и, если они сделали заказ, соответствующий продукт.
"""








# Задача SQL                                   С книгами сильный чел   НАПИСАТЬ 2 ВАРИАНТА
# sales
#
#
# id | product | count | year | smth
# 1  | dog     | 1     | 2024
# 2  | dog     | 1     | 2024
# 3  | cat     | 1     | 2024
# 4  | cat     | 1     | 2024
# 5  | cat     | 1     | 2024
#
# Объем продаж по каждому продукту за 2024 год
# product | count
# dog     | 2
# cat     | 3








# Ответ  Задача SQL  С книгами сильный чел   НАПИСАТЬ 2 ВАРИАНТА
"""
Мой вариант

select product, sum(count) AS c 
from sales
where year = '2024'
group by product
having sum(count) > 2;


Второй вариант

SELECT product, COUNT(*) AS c 
FROM sales 
WHERE CAST(year AS CHAR) REGEXP '2024' 
GROUP BY product 
HAVING COUNT(*) > 2;
"""




# Вернуть авторов, которые написали более двух книг      ivi  Иви   НАПИСАТЬ 3 ВАРИАНТА

# CREATE TABLE author (id SERIAL PRIMARY KEY, name TEXT);
# CREATE TABLE book (id SERIAL PRIMARY KEY, title TEXT, publication_date DATE, author_id integer REFERENCES author (id));
# INSERT INTO author(name) VALUES ('Автор 1'), ('Автор 2'), ('Автор 3');
# INSERT INTO book(title, publication_date, author_id) VALUES ('Книга 1', '2017-04-01', 1),
# ('Книга 2', '2018-04-01', 1), ('Книга 3', '2018-05-01', 2);








# -- Ответ Вернуть авторов, которые написали более двух книг          ivi  Иви   НАПИСАТЬ 3 ВАРИАНТА

# CREATE TABLE author (id SERIAL PRIMARY KEY, name TEXT);
# CREATE TABLE book (id SERIAL PRIMARY KEY, title TEXT, publication_date DATE, author_id integer REFERENCES author (id));
# INSERT INTO author(name) VALUES ('Автор 1'), ('Автор 2'), ('Автор 3');
# INSERT INTO book(title, publication_date, author_id) VALUES ('Книга 1', '2017-04-01', 1),
# ('Книга 2', '2018-04-01', 1), ('Книга 3', '2018-05-01', 2);
"""
Мой ответ

SELECT a.name, COUNT(b.id) AS book_count
FROM author AS a
JOIN book AS b ON b.author_id = a.id
GROUP BY a.id, a.name
HAVING COUNT(b.id) > 2;



Вариант 2: Использование подзапроса

SELECT a.id, a.name
FROM author a
WHERE (
    SELECT COUNT(*)
    FROM book b
    WHERE b.author_id = a.id
) > 2;



Вариант 3: Использование CTE (Common Table Expression)   CTE обеспечивают дополнительную гибкость и читаемость кода.

WITH author_counts AS (
    SELECT a.id, a.name, COUNT(b.id) AS book_count
    FROM author a
    JOIN book b ON a.id = b.author_id
    GROUP BY a.id, a.name
)
SELECT id, name
FROM author_counts
WHERE book_count > 2;
"""







# Задача SQL  СИБУР    Исправить код
"""
Исправить код
SELECT  
    C.customer_name,  
    SUM(COALESCE(O.order_amt, 0)) AS total 
FROM Customers AS C 
LEFT JOIN Orders AS O ON C.customer_nbr = O.customer_nbr 
WHERE 
    O.order_date >= '2021-01-01' 
GROUP BY 
    C.customer_name
"""







# Ответ Задача SQL  СИБУР    Исправить код
"""
Исправленный вариант
SELECT  
    C.customer_name,  
    SUM(COALESCE(O.order_amt, 0)) AS total 
FROM Customers AS C 
LEFT JOIN Orders AS O ON C.customer_nbr = O.customer_nbr AND O.order_date >= '2021-01-01' 
GROUP BY 
    C.customer_name;
"""




# Задача SQL  СИБУР   НАПИСАТЬ 2 ВАРИАНТА
#/* Есть таблица t1 <PK, A1, A2, …, AN, T > PK – идентификатор объекта A1, …, AN – это атрибуты T – это время фиксации значения.
#  Напиши SQL, который вернёт последнюю загруженную запись по оси T для каждого PK. */

#  PK A1 A2 A3 A4 T
#  1  1  1  1  1  1
#  1  1  1  1  2  2
#  1  1  1  1  1  3
#  1  2  1  1  2  4
#  1  1  1  1  1  5
#  2  2  3  4  5  3
#
#  Что должно быть на выходе
#  -> PK A1 A2 A3 A4  T
#     1   1  1  1  1  5
#     2   2  3  4  5  3








# Ответ  Задача SQL  СИБУР   НАПИСАТЬ 2 ВАРИАНТА
#/* Есть таблица t1 <PK, A1, A2, …, AN, T > PK – идентификатор объекта A1, …, AN – это атрибуты T – это время фиксации значения.
#  Напиши SQL, который вернёт последнюю загруженную запись по оси T для каждого PK. */
"""
Вариант 1 с использованием подзапроса

SELECT t.*
FROM t1 t
JOIN (
    SELECT PK, MAX(T) AS max_time
    FROM t1
    GROUP BY PK
) AS latest ON t.PK = latest.PK AND t.T = latest.max_time;



Вариант 2 с использованием оконной функции

SELECT PK, A1, A2, A3, A4, T
FROM (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY PK ORDER BY T DESC) as rn
    FROM t1
) AS numbered
WHERE rn = 1;
"""








# --- Задачи с Собеседования Python ---


# 2 Задачи    компания ГК “МТ-Интеграция”
# Задачи  OpenStack   ПОСМОТРИ ТУТ 2 ЗАДАЧИ!!!  АНАГРАММА И ФИЛЬТРАЦИИ СПИСКА СЕРВИСОВ   НАПИШИ ВСЕ ВАРИАНТЫ!!!


# ЗАДАЧА 1  АНАГРАММА   НАПИСАТЬ 5 СПОСОБОВ!


def anagramma(s: str, s1: str) -> bool:
    pass



# print(anagramma('нора', 'рано'))     # -> True
# print(anagramma('нораар', 'раноо'))  # -> False





# ЗАДАЧА 2  ФИЛЬТРАЦИИ СПИСКА СЕРВИСОВ  НАПИСАТЬ 8 СПОСОБОВ!

def is_service_good(lst: list[tuple]):
    pass




# a_res = [(123456, "AuthService", "ERROR"), (1234567, "AuthService", "INFO"), (123456, "Compute", "INFO")]
# EXPECTED_OUTPUT = [(1234567, "AuthService", "INFO"), (123456, "Compute", "INFO")]
#
# print(is_service_good(a_res))  # -> [(123456, 'Compute', 'INFO'), (1234567, 'AuthService', 'INFO')]






# ОТВЕТ 2 Задачи    компания ГК “МТ-Интеграция”
# ОТВЕТ Задачи  OpenStack   ПОСМОТРИ ТУТ 2 ЗАДАЧИ!!!  АНАГРАММА И ФИЛЬТРАЦИИ СПИСКА СЕРВИСОВ   НАПИШИ ВСЕ ВАРИАНТЫ!!!
"""

# Задачи  OpenStack   ПОСМОТРИ ТУТ 2 ЗАДАЧИ!!!    АНАГРАММА  И  ФИЛЬТРАЦИИ СПИСКА СЕРВИСОВ


# ЗАДАЧА 1) АНАГРАММА - это слово или фраза, образованная перестановкой букв другого слова или фразы.
# Примеры АНАГРАММ:  "Кот" → "Ток"    "Апельсин" → "Спаниель"



# Способ 1: Через сортировку                                                                            O(n log n)
def anagramma(s: str, s1: str) -> bool:
    return sorted(s) == sorted(s1)


# Способ 2: Через collections.Counter (быстро и надёжно)                                                O(n)
from collections import Counter

def anagramma(s: str, s1: str) -> bool:
    return Counter(s) == Counter(s1)


# Способ 3: Через defaultdict (альтернатива Counter)  Быстрее обычного словаря (не требует .get()).     O(n)
from collections import defaultdict

def anagramma(s: str, s1: str) -> bool:
    if len(s) != len(s1):
        return False
    counts = defaultdict(int)
    for char in s:
        counts[char] += 1
    for char in s1:
        counts[char] -= 1
        if counts[char] < 0:
            return False
    return True


# Способ 4: Вручную через словарь (без библиотек)                                                       O(n)
def anagramma(s: str, s1: str) -> bool:
    if len(s) != len(s1):
        return False
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    for char in s1:
        if char not in char_count or char_count[char] == 0:
            return False
        char_count[char] -= 1
    return True


# Способ 5: Через массив ASCII (оптимально для английского)  Супербыстрый для ASCII (кириллицу нужно доработать). O(n)
def anagramma(s: str, s1: str) -> bool:
    if len(s) != len(s1):
        return False
    # counts = [0] * 128  # ASCII-таблица (0-127)  # кириллица требует [0] * 1104 для базового Unicode
    # counts = [0] * 1104  # ASCII-таблица (0-127)  # кириллица требует [0] * 1104 для базового Unicode
    counts = [0] * 1114112  # Полная поддержка Unicode
    for c in s:
        counts[ord(c)] += 1
    for c in s1:
        counts[ord(c)] -= 1
        if counts[ord(c)] < 0:
            return False
    return True


print(anagramma('нора', 'рано'))     # -> True
print(anagramma('нораар', 'раноо'))  # -> False





# ЗАДАЧА 2)   ФИЛЬТРАЦИИ СПИСКА СЕРВИСОВ

# ЗАДАЧА фильтрации списка сервисов, оставляя только первую запись для каждого уникального сервиса
# (с учетом сортировки по времени):


# Способ 1: МОЁ РЕШЕНИЕ              O(n²) - из-за вложенного поиска через itertools.chain  НЕ РЕКОМЕНДУЕТСЯ
def is_service_good(lst: list[tuple]):
    res = []
    for i in lst:
        if i[1] not in list(itertools.chain(*res)):
            res.append(i)
    return sorted(res, key=lambda x: x[0])


# Способ 2: Использование set()        O(n log n) - из-за сортировки + O(n) для прохода       Лучший баланс
import itertools
 
def is_service_good(lst: list[tuple]):
    seen_services = set()
    res = []

    for entry in sorted(lst, key=lambda x: x[0]):  # sort by timestamp first
        service = entry[1]
        if service not in seen_services:
            seen_services.add(service)
            res.append(entry)

    return res


# Способ 3: Использование словаря с обновлением   O(n log n) для сортировки + O(n) для прохода   Лучший баланс

def is_service_good(lst: list[tuple]):
    service_dict = {}
    for entry in sorted(lst, key=lambda x: x[0]):
        service = entry[1]
        if service not in service_dict:
            service_dict[service] = entry
    return sorted(service_dict.values(), key=lambda x: x[0])


# Способ 4: Использование groupby из itertools  O(n log n) - две сортировки + O(n) для groupby
 
from itertools import groupby
from operator import itemgetter

def is_service_good(lst: list[tuple]):
    # Сначала сортируем по имени сервиса, затем по времени
    sorted_by_service = sorted(lst, key=itemgetter(1))
    # Берем первую запись для каждого сервиса
    grouped = groupby(sorted_by_service, key=itemgetter(1))
    first_entries = [next(group) for _, group in grouped]
    # Сортируем результат по timestamp
    return sorted(first_entries, key=itemgetter(0))


# Способ 5: Использование OrderedDict    O(n log n) для сортировки + O(n) для прохода

from collections import OrderedDict

def is_service_good(lst: list[tuple]):
    services = OrderedDict()
    for entry in sorted(lst, key=lambda x: x[0]):
        services.setdefault(entry[1], entry)
    return list(services.values())


# Способ 6: Использование множества с фильтрацией  O(n log n) для сортировки + O(n) для прохода
def is_service_good(lst: list[tuple]):
    seen = set()
    return [entry for entry in sorted(lst, key=lambda x: x[0])
            if not (entry[1] in seen or seen.add(entry[1]))]

a_res = [(123456, "AuthService", "ERROR"), (1234567, "AuthService", "INFO"), (123456, "Compute", "INFO")]
EXPECTED_OUTPUT = [(1234567, "AuthService", "INFO"), (123456, "Compute", "INFO")]

print(is_service_good(a_res))  # -> [(123456, 'Compute', 'INFO'), (1234567, 'AuthService', 'INFO')]


# Способ 7: pandas   O(n log n) - зависит от реализации pandas   Для больших данных лучше использовать pandas  (7-8)
import pandas as pd

def is_service_good(lst: list[tuple]):
    df = pd.DataFrame(lst, columns=['timestamp', 'service', 'status'])
    df = df.sort_values('timestamp').drop_duplicates('service', keep='first')
    return [tuple(x) for x in df.to_numpy()]


# Способ 8: Использование pandas с более компактным синтаксисом   O(n log n) - зависит от реализации pandas
import pandas as pd

def is_service_good(lst: list[tuple]):
    return (pd.DataFrame(lst, columns=['time', 'service', 'status'])
              .sort_values('time')
              .drop_duplicates('service')
              .sort_values('time')
              .to_records(index=False)
              .tolist())

a_res = [(123456, "AuthService", "ERROR"), (1234567, "AuthService", "INFO"), (123456, "Compute", "INFO")]
EXPECTED_OUTPUT = [(1234567, "AuthService", "INFO"), (123456, "Compute", "INFO")]

print(is_service_good(a_res))  # -> [(123456, 'Compute', 'INFO'), (1234567, 'AuthService', 'INFO')]
"""





# 4 Задачи    компания Медиалогия  НАПИШИ ВСЕ ВАРИАНТЫ!!!


# ЗАДАЧА 1  РЮКЗАК   НАПИСАТЬ 4 СПОСОБА!

weights = [10, 20, 30, 40]
costs = [20, 10, 30, 40]
max_limit = 40



def knapsack(weights, costs, max_limit):
    pass



# cost, items = knapsack(weights, costs, max_limit)
# print(f"Максимальная стоимость: {cost}")           # ->  Максимальная стоимость: 50
# print(f"Выбранные предметы: {items}")              # ->  Выбранные предметы: [(10, 20), (30, 30)]




# ЗАДАЧА 2  Two Sum тоже самое но НЕ обязательно стоят рядом   НАПИСАТЬ 4 СПОСОБА!

lst = [2, 7, 11, 15, 7]
target = 9

def find_two_sum(nums, target):
    pass



# print(find_two_sum(lst, target))  # -> [0, 1]
# print(find_two_sum(lst, target))  # -> [[0, 1], [0, 4]]





# ЗАДАЧА 3 заменяет нечетные символы в строке на буквы английского алфавита, а остальные оставляет без изменений  3 СПОСОБА
from string import ascii_lowercase

s = 'aaaaaaaaaa'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet = ascii_lowercase


def replace_odd_chars(s):
    pass



# print(replace_odd_chars(s))  # -> aacaeagaia





# ЗАДАЧА 4)  большой JSON-объект без необходимости загружать его полностью в память.   НАПИСАТЬ 4 СПОСОБА!

json_data = [[], 123, 'aaa', {'a': 1}, [1, 2, 3], {'a': 2}, (1, 2), {'a': 1}]

def count_dict_a_1(data):
    pass



# result = count_dict_a_1(json_data)
# print(result)  # -> 2



# ОТВЕТ  4 Задачи    компания Медиалогия  НАПИШИ ВСЕ ВАРИАНТЫ!!!
"""
# ЗАДАЧА 1)  Задача о рюкзаке (или задача о ранце)
# суммарный вес не превышал максимальную грузоподъемность рюкзака, а суммарная стоимость была максимальной.


weights = [10, 20, 30, 40]
costs = [20, 10, 30, 40]
max_limit = 40


# Способ 1: Жадный алгоритм (не всегда дает оптимальное решение)

def knapsack(weights, costs, max_limit):
    n = len(weights)
    # Сортируем предметы по убыванию удельной стоимости (стоимость/вес)
    items = sorted(zip(weights, costs), key=lambda x: x[1] / x[0], reverse=True)

    total_weight = 0
    total_cost = 0
    selected = []

    for weight, cost in items:
        if total_weight + weight <= max_limit:
            selected.append((weight, cost))
            total_weight += weight
            total_cost += cost

    return total_cost, selected


# Способ 2: Динамическое программирование (точное решение)

def knapsack(weights, costs, max_limit):
    n = len(weights)
    # Создаем таблицу для хранения максимальной стоимости для каждого веса
    dp = [[0] * (max_limit + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, max_limit + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + costs[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    # Восстановление выбранных предметов
    w = max_limit
    selected = []
    total_cost = dp[n][max_limit]

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append((weights[i - 1], costs[i - 1]))
            w -= weights[i - 1]

    return total_cost, selected[::-1]


# Способ 3: Метод ветвей и границ (точное решение)

import heapq

class Node:
    def __init__(self, level, weight, cost, bound, items):
        self.level = level
        self.weight = weight
        self.cost = cost
        self.bound = bound
        self.items = items

    # Для сравнения в heapq (чем больше bound, тем выше приоритет)
    def __lt__(self, other):
        return self.bound > other.bound

def bound(node, n, max_limit, weights, costs):
    if node.weight >= max_limit:
        return 0
    bound_value = node.cost
    j = node.level + 1
    total_weight = node.weight

    while j < n and total_weight + weights[j] <= max_limit:
        total_weight += weights[j]
        bound_value += costs[j]
        j += 1

    if j < n:
        bound_value += (max_limit - total_weight) * (costs[j] / weights[j])

    return bound_value

def knapsack(weights, costs, max_limit):
    n = len(weights)
    # Сортируем предметы по убыванию удельной стоимости
    items = sorted(zip(weights, costs), key=lambda x: x[1] / x[0], reverse=True)
    weights = [w for w, _ in items]
    costs = [c for _, c in items]

    # Используем приоритетную очередь
    heap = []
    root = Node(-1, 0, 0, 0, [])
    root.bound = bound(root, n, max_limit, weights, costs)
    heapq.heappush(heap, root)

    max_cost = 0
    best_items = []

    while heap:
        node = heapq.heappop(heap)

        # Если текущая оценка меньше максимальной стоимости, дальше можно не смотреть
        if node.bound <= max_cost:
            continue

        if node.level == n - 1:
            continue

        # Включаем следующий предмет
        next_level = node.level + 1
        next_weight = node.weight + weights[next_level]
        next_cost = node.cost + costs[next_level]
        next_items = node.items + [(weights[next_level], costs[next_level])]

        if next_weight <= max_limit and next_cost > max_cost:
            max_cost = next_cost
            best_items = next_items.copy()

        # Считаем bound для включения предмета
        next_bound = bound(Node(next_level, next_weight, next_cost, 0, next_items),
                          n, max_limit, weights, costs)
        if next_bound > max_cost:
            heapq.heappush(heap, Node(next_level, next_weight, next_cost, next_bound, next_items))

        # Не включаем следующий предмет
        next_bound = bound(Node(next_level, node.weight, node.cost, 0, node.items),
                          n, max_limit, weights, costs)
        if next_bound > max_cost:
            heapq.heappush(heap, Node(next_level, node.weight, node.cost, next_bound, node.items))

    return max_cost, best_items


# Способ 4: Полный перебор (точное решение)

from itertools import combinations


def knapsack(weights, costs, max_limit):
    n = len(weights)
    max_cost = 0
    best_combination = []

    for r in range(1, n + 1):
        for indices in combinations(range(n), r):
            total_weight = sum(weights[i] for i in indices)
            total_cost = sum(costs[i] for i in indices)
            if total_weight <= max_limit and total_cost > max_cost:
                max_cost = total_cost
                best_combination = [(weights[i], costs[i]) for i in indices]

    return max_cost, best_combination


cost, items = knapsack(weights, costs, max_limit)
print(f"Максимальная стоимость: {cost}")           # ->  Максимальная стоимость: 50
print(f"Выбранные предметы: {items}")              # ->  Выбранные предметы: [(10, 20), (30, 30)]




# ЗАДАЧА 2) Two Sum тоже самое но НЕ обязательно стоят рядом

lst = [2, 7, 11, 15, 7]
target = 9


# Способ 1: Использование хэш-таблицы (словаря) — O(n)

def find_two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

print(find_two_sum(lst, target))  # -> [0, 1]



# Способ 2: Вариант с возвратом всех пар (если их несколько) — O(n)

def find_two_sum(nums, target):
    seen = {}
    result = []
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            result.append([seen[complement], i])
        seen[num] = i
    return result

print(find_two_sum(lst, target))  # -> [[0, 1], [0, 4]]


# Способ 3: Решение с двумя указателями (для отсортированного списка) — O(n log n)

def find_two_sum(nums, target):
    nums_sorted = sorted([(num, i) for i, num in enumerate(nums)], key=lambda x: x[0])
    left, right = 0, len(nums_sorted) - 1
    while left < right:
        current_sum = nums_sorted[left][0] + nums_sorted[right][0]
        if current_sum == target:
            return [nums_sorted[left][1], nums_sorted[right][1]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []


print(find_two_sum(lst, target))  # -> [0, 4] (но индексы могут отличаться из-за сортировки)


# Способ 4: менее эффективен для больших списков.  (полный перебор, brute force)    O(n²)

def find_two_sum(nums, target):
    res = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                res.append([i, j])
    return res


print(find_two_sum(lst, target))  # -> [[0, 1], [0, 4]]




# ЗАДАЧА 3)  заменяет нечетные символы в строке на буквы английского алфавита, а остальные оставляет без изменений


import re
from string import ascii_lowercase

s = 'aaaaaaaaaa'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet = ascii_lowercase


# Способ 1:  Простой

def replace_odd_chars(s):
    result = []
    for i in range(len(s)):
        if i % 2 == 0:  # нечетные позиции (индексация с 0)
            # берем соответствующую букву из алфавита
            char = alphabet[i % 26]
            result.append(char)
        else:
            result.append(s[i])

    return ''.join(result)

print(replace_odd_chars(s))  # -> aacaeagaia


# Способ 2:  Через РЕГУЛЯРКУ  (сложный)

def replace_odd_chars_regex(s):
    # Используем регулярное выражение для замены каждого второго символа (начиная с 0)
    # Функция замены будет использовать позицию совпадения для выбора буквы из алфавита
    return re.sub(
        r'(?P<odd>.)?(?P<even>.)?',  # ищем пары символов (1-й и 2-й)
        lambda m: (alphabet[m.start() % 26] if m.group('odd') else '') + (m.group('even') if m.group('even') else ''),
        s
    )


# Способ 3:  Через РЕГУЛЯРКУ   Более простой

def replace_odd_chars_regex(s):
    return re.sub(
        r'(.)',  # ищем каждый символ
        lambda m: alphabet[m.start() % 26] if m.start() % 2 == 0 else m.group(1),
        s
    )

print(replace_odd_chars_regex(s))  # -> aacaeagaia




# ЗАДАЧА 4)  большой JSON-объект без необходимости загружать его полностью в память.

import json
json_data = [[], 123, 'aaa', {'a': 1}, [1, 2, 3], {'a': 2}, (1, 2), {'a': 1}]


# Способ 1: Рекурсивный подход     стоит учитывать ограничение глубины рекурсии   RecursionError          ПРАВИЛЬНЫЙ

def count_dict_a_1(data):
    count = 0
    # Проверяем, является ли текущий элемент искомым словарём
    if isinstance(data, dict) and data == {'a': 1}:
        count += 1
    # Если элемент является списком или кортежем, рекурсивно обходим его элементы
    elif isinstance(data, (list, tuple)):
        for item in data:
            count += count_dict_a_1(item)
    # Если элемент является словарём, рекурсивно обходим его значения
    elif isinstance(data, dict):
        for value in data.values():
            count += count_dict_a_1(value)
    return count

result = count_dict_a_1(json_data)
print(result)  # -> 2


# Способ 2: Итеративный подход с использованием стека (без рекурсии)   избежания ограничений рекурсии     ПРАВИЛЬНЫЙ


# Для очень больших JSON-файлов   эффективный по памяти
def count_dict_a_1(data):
    count = 0
    stack = [data]

    while stack:
        current = stack.pop()
        if isinstance(current, dict):
            if current == {'a': 1}:
                count += 1
            stack.extend(current.values())
        elif isinstance(current, (list, tuple)):
            stack.extend(current)

    return count

result = count_dict_a_1(json_data)
print(result)  # -> 2


# Способ 3: Использование генераторов для ленивого обхода        эффективны по памяти способы (2, 3)      ПРАВИЛЬНЫЙ

# Для очень больших JSON-файлов   эффективный по памяти
def count_dict_a_1(data):
    if isinstance(data, dict):
        yield data
        for value in data.values():
            yield from count_dict_a_1(value)
    elif isinstance(data, (list, tuple)):
        for item in data:
            yield from count_dict_a_1(item)


def count_dict_a_3(data):
    return sum(1 for item in count_dict_a_1(data) if item == {'a': 1})

result = count_dict_a_3(json_data)
print(result)  # -> 2


# Способ 4: Использование object_hook в json.loads (которая все равно загружает весь JSON в память)    НЕ ПРАВИЛЬНЫЙ

# Преобразуем данные в JSON-строку
json_data = json.dumps(json_data)


def count_dict_a_1(json_str):
    count = 0

    def hook(obj):
        nonlocal count
        if isinstance(obj, dict) and obj == {'a': 1}:
            count += 1
        return obj

    json.loads(json_str, object_hook=hook)
    return count

result = count_dict_a_1(json_data)
print(result)  # -> 2
"""





# Полиндром от Санька
# Задача  палиндромом без создания дополнительных строк и с временной сложностью O(n) и пространственной сложностью O(1)



def is_palindrome(s: str) -> bool:
   pass




# # Примеры использования с различными символами
# print(is_palindrome("A man, a plan, a canal: Panama"))  # True
# print(is_palindrome("race a car"))                      # False
# print(is_palindrome("No 'x' in Nixon"))                 # True
# print(is_palindrome("Was it a car or a cat I saw?"))    # True
# print(is_palindrome("!@#$%^&*()"))                      # True, так как пустая строка между символами и игнорируемые символы
# print(is_palindrome("12321"))                           # True
# print(is_palindrome("123456"))                          # False







# Ответ  Полиндром он Санька
# Задача  палиндромом без создания дополнительных строк и с временной сложностью O(n) и пространственной сложностью O(1)
"""

# 1 Вариант

def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1

    while left < right:
        # Пропускаем не буквенные символы слева
        while left < right and not s[left].isalnum():
            left += 1
        # Пропускаем не буквенные символы справа
        while left < right and not s[right].isalnum():
            right -= 1

        # Сравниваем символы, игнорируя регистр
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


# Примеры использования с различными символами
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("race a car"))                      # False
print(is_palindrome("No 'x' in Nixon"))                 # True
print(is_palindrome("Was it a car or a cat I saw?"))    # True
print(is_palindrome("!@#$%^&*()"))                      # True, так как пустая строка между символами и игнорируемые символы
print(is_palindrome("12321"))                           # True
print(is_palindrome("123456"))                          # False



# Вариант 2: Более компактная запись

def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        else:
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
    return True
    
    
# Вариант 3: continue (уменьшает вложенность условий)   
def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        if not s[left].isalnum():
            left += 1
            continue
        if not s[right].isalnum():
            right -= 1
            continue
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True
    
    
# Вариант 4: С предварительным фильтром (но это уже не O(1) по памяти)  Эффективнее (не делает lower() для ненужных символов).
  
# Этот вариант не соответствует требованиям O(1) памяти, но может быть полезен для сравнения. Самый читаемый (питонический стиль).
def is_palindrome(s: str) -> bool:
    filtered = [c.lower() for c in s if c.isalnum()]
    return filtered == filtered[::-1] 
    
    
# Вариант 5: Тоже самое но с map и filter    менее читаемый      эффективнее чем Вариант 6           Но лучше вариант 4
  
# Этот вариант не соответствует требованиям O(1) памяти, но может быть полезен для сравнения
def is_palindrome(s: str) -> bool:
    filtered = list(map(str.lower, filter(str.isalnum, s)))
    return filtered == filtered[::-1]  
    
    
# Вариант 6: Тоже самое но с map и filter  Если могут быть Unicode-символы — лучше 5 вариант.   Но лучше вариант 4
  
# Этот вариант не соответствует требованиям O(1) памяти, но может быть полезен для сравнения
def is_palindrome(s: str) -> bool:
    ff = list(filter(lambda c: c.isalnum(), s.lower()))
    return ff == ff[::-1]
"""





# Задача "Правильная скобочная последовательность"    Valid Braces  Codewars    Мир Танков/World of Tanks

# 2 Раза повторялась задача Попалась и на другом собеседовании!!!

# Write a function called test() that takes a string of parentheses, and determines if the order of the
# parentheses is valid. The function should return true if the string is valid, and false if it's invalid.
# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# "(())((()())())"  =>  true
# "())("            =>  false




# Написать 3 варианта
def is_correct_brackets(text):
    pass



# print(is_correct_brackets('(((())))'))  # True
# print(is_correct_brackets('(((())'))  # False
# print(is_correct_brackets('())))'))  # False
# print(is_correct_brackets('((((){}[]{}[])))'))  # True
# print(is_correct_brackets('(){}[]{}[])))'))  # False
# print(is_correct_brackets('(){}[]{}[]'))  # True







# Ответ Задача "Правильная скобочная последовательность"    Valid Braces  Codewars    Мир Танков/World of Tanks
"""
# Первый Вариант            Квадратичная сложность O(n^2)       Вариант требует создания новых строк и перебора их.                                  
def is_correct_brackets(text):                          
    while '()' in text or '[]' in text or '{}' in text:                                         
        text = text.replace('()', '')                                                            
        text = text.replace('[]', '')                   
        text = text.replace('{}', '')
        # text = text.replace('()', '').replace('[]', '').replace('{}', '')   # Тоже самое вместо 3-х строчек                  
                                                        
    # Возвращаем True, если text с пустой строкой                                     
    return not text                                     


print(is_correct_brackets('(((())))'))  # True
print(is_correct_brackets('(((())'))  # False
print(is_correct_brackets('())))'))  # False
print(is_correct_brackets('((((){}[]{}[])))'))  # True
print(is_correct_brackets('(){}[]{}[])))'))  # False
print(is_correct_brackets('(){}[]{}[]'))  # True



# НЕ только БЫСТРЕЕ по времени выполнения, но и более эффективно использует память.              <-----     <-----
# Второй Вариант            Линейная сложность O(n)            Стек достигает O(n) в худшем случае.
def validBraces(string):
    braces = {"(": ")", "[": "]", "{": "}"}
    stack = []
    for character in string:
        if character in braces.keys():
            stack.append(character)
        else:
            if len(stack) == 0 or braces[stack.pop()] != character:
                return False
    return len(stack) == 0


print(validBraces('(((())))'))  # True
print(validBraces('(((())'))  # False
print(validBraces('())))'))  # False
print(validBraces('((((){}[]{}[])))'))  # True
print(validBraces('(){}[]{}[])))'))  # False
print(validBraces('(){}[]{}[]'))  # True



# Третий Вариант            Квадратичная сложность O(n^2)       Вариант требует создания новых строк и перебора их.
def validBraces(string):
    for _ in string:
        string = string.replace('{}', '').replace('()', '').replace('[]', '')
    return not string


print(validBraces('(((())))'))  # True
print(validBraces('(((())'))  # False
print(validBraces('())))'))  # False
print(validBraces('((((){}[]{}[])))'))  # True
print(validBraces('(){}[]{}[])))'))  # False
print(validBraces('(){}[]{}[]'))  # True


# Ответ ChatGPT
def is_valid(s: str) -> bool:
    # Создаем стек для хранения открывающих скобок
    stack = []
    # Словарь для сопоставления открывающих и закрывающих скобок
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        # Если символ — закрывающая скобка
        if char in mapping:
            # Извлекаем верхнюю скобку из стека, если стек не пуст
            # В противном случае используем символ-знак
            top_element = stack.pop() if stack else '#'
            # Проверяем, соответствует ли открывающая скобка закрывающей
            if mapping[char] != top_element:
                return False
        else:
            # Если это открывающая скобка, добавляем её в стек
            stack.append(char)

    # Если стек пуст, значит все скобки корректны
    return not stack


# Примеры использования
print(is_valid("()"))  # True
print(is_valid("()[]{}"))  # True
print(is_valid("(]"))  # False
print(is_valid("([)]"))  # False
print(is_valid("{[]}"))  # True
________________________________________________________________________________________________________________________
"""



# Создать функцию которая убирает дубликаты           Задача с Live Coding Собеседования


# Написать 3 варианта
def clean_duplicates(lst):
    pass



# print(clean_duplicates([{1: 2}, {1: 2}, {1: 2}]))  # -> [{1: 2}]







# Ответ Создать функцию которая убирает дубликаты           Задача с Live Coding Собеседования
"""
# Первый вариант
def clean_duplicates(lst: list[dict]) -> list[dict]:
    res = []
    for i in lst:
        if i not in res:
            res.append(i)
    return res

print(clean_duplicates([{1: 2}, {1: 2}, {1: 2}]))  # -> [{1: 2}]


# Второй вариант
def clean_duplicates(lst: list[dict]) -> list[dict]:
    res = []
    [res.append(i) for i in lst if i not in res]
    return res

print(clean_duplicates([{1: 2}, {1: 2}, {1: 2}]))  # -> [{1: 2}]


# Третий вариант
def clean_duplicates(lst: list[dict]) -> list[dict]:
    return list([eval(i) for i in set(tuple([str(i) for i in lst]))])

print(clean_duplicates([{1: 2}, {1: 2}, {1: 2}]))  # -> [{1: 2}]


# Интересный вариант              # Тоже самое                       # Тоже самое 
def clean_duplicates(lst):        def clean_duplicates(lst):         def clean_duplicates(lst):            
    res = set()                       res = {str(i) for i in lst}        return [eval(i) for i in {str(j) for j in lst}]    
    for i in lst:                     return [eval(i) for i in res]              
        res.add(str(i))                         
    return [eval(i) for i in res]

print(clean_duplicates([{1: 2}, {1: 2}, {1: 2}]))  # -> [{1: 2}]
________________________________________________________________________________________________________________________
"""



# Yandex-Маркет Задача Отсортировать по двум параметрам. Как я сделал я не знаю

xs = [
    '1_a.txt',
    '2_b.txt',
    '1_c.txt',
    '3_d.txt',
    '1_e.txt',
]








# Ответ  Yandex-Маркет Задача Отсортировать по двум параметрам. Как я сделал я не знаю
r"""
xs = [
    '1_a.txt',
    '2_b.txt',
    '1_c.txt',
    '3_d.txt',
    '1_e.txt',
]


# Функция для извлечения ключа сортировки
def sort_key(item):
    number_part = int(item.split('_')[0])  # Извлекаем числовую часть
    letter_part = item.split('_')[1][0]    # Извлекаем буквенную часть
    return (number_part, letter_part)

# Сортируем список
sorted_xs = sorted(xs, key=sort_key)

# Выводим отсортированный список
print(sorted_xs)  # -> ['1_a.txt', '1_c.txt', '1_e.txt', '2_b.txt', '3_d.txt']


# Тоже инетерсный вариант
def sort_key(item):
    n, s = re.match(r'\d+(?=_)', item).group(), re.search(r'(?<=_)[a-z]', item)[0]
    return int(n), s

print(sorted(xs, key=sort_key))  # -> ['1_a.txt', '1_c.txt', '1_e.txt', '2_b.txt', '3_d.txt']


# МОИ ВАРИАНТЫ

def sub_fun(x):
    return -int(re.sub(r'[^\d]+', '', x)), re.search(r'(?<=_)[a-z]+(?=\.)', x, flags=re.I).group()

def my_func(lst: list) -> list:
    return sorted(lst, key=sub_fun)

print(my_func(xs))  # -> ['3_d.txt', '2_b.txt', '1_a.txt', '1_c.txt', '1_e.txt']

print(sorted(xs, key=lambda x: (-int(x[0]), x[1])))
print(sorted(xs, key=lambda x: (-int(re.sub(r'[^\d]+', '', x)), re.search(r'(?<=_)[a-z]+(?=\.)', x, flags=re.I).group())))
print(sorted(xs, key=sub_fun))
# ['3_d.txt', '2_b.txt', '1_a.txt', '1_c.txt', '1_e.txt']
# ['3_d.txt', '2_b.txt', '1_a.txt', '1_c.txt', '1_e.txt']
# ['3_d.txt', '2_b.txt', '1_a.txt', '1_c.txt', '1_e.txt']

# Через split() хз как улучшить
print(sorted(xs, key=lambda x: (-int(''.join(x.split('.')).split('_')[0]), ''.join(x.split('.')).split('_')[1])))


# Интересный вариат                                     # Тоже самое    
def my_func(x):                                         def my_func(x):
    return -int(x.split('_')[0]), x.split('_')[1]           a, b = x.split('_')                                    
                                                            return -int(a), b        

def get_sorted(lst):
    return sorted(lst, key=my_func)


print(get_sorted(xs))  # -> ['3_d.txt', '2_b.txt', '1_a.txt', '1_c.txt', '1_e.txt']
print(get_sorted(xs))  # -> ['3_d.txt', '2_b.txt', '1_a.txt', '1_c.txt', '1_e.txt']


# Интересный момент с унарным минусом - 
def fun(x):
    a, b = -int(re.search(r'\d(?=_)', x).group()), re.search(r'(?<=_)\w', x)[0]
    return -a, b    

def my_sorted(lst):
    return sorted(lst, key=fun)

print(my_sorted(xs))  # -> ['1_a.txt', '1_c.txt', '1_e.txt', '2_b.txt', '3_d.txt']


# Без унарного минуса будет другой результат
def fun(x):
    a, b = -int(re.search(r'\d(?=_)', x).group()), re.search(r'(?<=_)\w', x)[0]
    return a, b                                                                      # Убрали минус тут
    # return ---a, b      # Можно еще ставить много минусов) с четным и НЕ четным результаты разные будет

def my_sorted(lst):
    return sorted(lst, key=fun)

print(my_sorted(xs))  # -> ['3_d.txt', '2_b.txt', '1_a.txt', '1_c.txt', '1_e.txt']
________________________________________________________________________________________________________________________
"""







# Two Sum Задача с собеседования  YADRO

lst = [2, 7, 9, 10, 11]
target = 9


# Написать 2 варианта range(len(nums)-1), zip  и еще 2 через pairwise, combinations
def twoSum(nums, target):
    pass



# print(twoSum(lst, target))  # -> [[0, 1]]
# print(twoSum(lst, target))  # -> [0, 1]





# Ответ Two Sum Задача с собеседования  YADRO
"""
lst = [2, 7, 9, 10, 11]
target = 9

# Хороший вариант                                     # Тоже самое с МОРЖОМ      
def twoSum(nums, target):                             def twoSum(nums, target):                                  
    res = []                                              res = []                      
    for i in range(len(nums)-1):                          for i in range(len(nums)-1):                                          
        if nums[i] + nums[i+1] == target:                     if sum(((a:=nums[i]), (b:=nums[i+1]))) == target:                                                  
            res.append(nums.index(nums[i]))                       res.append(nums.index(a))                                                  
            res.append(nums.index(nums[i+1]))                     res.append(nums.index(b))                                                      
    return res                                            return res                      
                                                                
print(twoSum(lst, target))  # -> [0, 1]


# Пример 1
from itertools import pairwise
                                                                # Тоже самое но ВЫВОД  [0, 1]  
def twoSum(nums, target):                                       def twoSum(nums, target):                                                                                    
    res = []                                                        res = []                                                                        
    for i, v in enumerate(pairwise(nums)):                          for i, j in itertools.pairwise(nums):                                    
        if sum([v[0], v[1]]) == target:                                 if i+j == target:                                
            res.append([nums.index(v[0]), nums.index(v[1])])                res.append((nums.index(i), nums.index(j)))                                                        
    return res                                                      return [j for i in res for j in i]        
                                                                     
print(twoSum(lst, target))  # -> [[0, 1]]                       print(twoSum(lst, target))  # -> [0, 1]                                    


# Тоже самое slice(1, None, 2) - Принимает только 3 аргумента      Тут создает такие пары  [(2, 7), (9, 10)]
def twoSum(nums, target):                                          lst = [2, 7, 9, 10, 11]     
    res = []
    for i, v in enumerate(zip(nums[slice(None, None, 2)], nums[slice(1, None, 2)])):
        if sum([v[0], v[1]]) == target:
            res.append([i, i + 1])
    return res

print(twoSum(lst, target))  # -> [[0, 1]]


# Тут создает такие пары  [(2, 7), (9, 10)]     lst = [2, 7, 9, 10, 11]     
# Пример 2                                                # Тоже самое                  
def twoSum(nums, target):                                 def twoSum(nums, target):                 
    res = []                                                  res = []
    for i, v in enumerate(zip(nums[::2], nums[1::2])):        for i, (k, v) in enumerate(zip(nums[::2], nums[1::2])):
        if sum([v[0], v[1]]) == target:                           if sum([k, v]) == target:
            res.append([i, i+1])                                      res.append([i, i + 1])
    return res                                                return res

print(twoSum(lst, target))  # -> [[0, 1]]                   print(twoSum(lst, target))  # -> [[0, 1]]


# Пример 3
from itertools import combinations
def twoSum(nums, target):
    res = list(*[i for i in combinations(nums, 2) if sum(i) == target])
    return [i for i, v in enumerate(nums) if v in res]

print(twoSum(lst, target))  # -> [0, 1]


# Ответ ChatGPT
def twoSum(lst, target):
    res = []
    n = len(lst)
    # Ищем все пары индексов
    for i in range(n):
        for j in range(i + 1, n):
            if lst[i] + lst[j] == target:
                res.append((i, j))
    return res

# Пример использования
print(twoSum(lst, target))  # -> [(0, 1)]
________________________________________________________________________________________________________________________
"""



# Релизация своего класса имитируещего СЛОВАРЬ   ML








#  Ответ Релизация своего класса имитируещего СЛОВАРЬ   ML
"""
# Мой вариант на собеседовании ПРОСТОЙ

class MyDict:
    def __init__(self):
        self.data = []

    def _add(self, key, value):
        if key:
            self.data.append((key, value))

    def _get(self, key):
        for i, (k, v) in enumerate(self.data):
            if key and k == key:
                return v
        raise KeyError


c = MyDict()
c._add(1, 'A')
print(c._get(1))  # -> A
print(c._get(2))  # -> KeyError



# Более Правильный вариант Сложный
class MyDict:
    def __init__(self):
        self.data = []

    def __setitem__(self, key, value):
        for i, (k, v) in enumerate(self.data):
            if k == key:
                self.data[i] = (key, value)  # Обновляем значение
                return
        self.data.append((key, value))  # Добавляем новый элемент

    def __getitem__(self, key):
        for k, v in self.data:
            if k == key:
                return v  # Возвращаем значение, если ключ найден
        raise KeyError(f"Key {key} not found.")

    def __delitem__(self, key):
        for i, (k, v) in enumerate(self.data):
            if k == key:
                del self.data[i]  # Удаляем элемент с данным ключом
                return
        raise KeyError(f"Key {key} not found.")

    def __contains__(self, key):
        return any(k == key for k, v in self.data)  # Проверяем наличие ключа

    def __len__(self):
        return len(self.data)  # Возвращаем количество элементов в словаре

    def __iter__(self):
        return (k for k, v in self.data)  # Итерирование по ключам

    def items(self):
        return self.data.copy()  # Возвращаем все пары (ключ, значение)

    def keys(self):
        return [k for k, v in self.data]  # Возвращаем список ключей

    def values(self):
        return [v for k, v in self.data]  # Возвращаем список значений

    def clear(self):
        '''Удаляет все элементы из словаря.'''
        self.data.clear()

    def update(self, other):
        '''Обновляет словарь значениями из другого словаря или итерируемого объекта.'''
        for k, v in other.items():
            self[k] = v

    def pop(self, key, default=None):
        '''Удаляет элемент с указанным ключом и возвращает его значение. Если ключ не найден, возвращает значение по умолчанию.'''
        for i, (k, v) in enumerate(self.data):
            if k == key:
                del self.data[i]  # Удаляем элемент
                return v
        if default is not None:
            return default
        raise KeyError(f"Key {key} not found.")

    def popitem(self):
        '''Удаляет и возвращает последнюю добавленную пару (ключ, значение). Если словарь пустой, вызывается исключение KeyError.'''
        if not self.data:
            raise KeyError("popitem(): dictionary is empty")
        return self.data.pop()  # Возвращает и удаляет последний элемент

    def get(self, key, default=None):
        '''Возвращает значение по ключу, если ключ не найден – возвращает значение по умолчанию.'''
        for k, v in self.data:
            if k == key:
                return v
        return default

    def setdefault(self, key, default=None):
        '''Возвращает значение по ключу. Если ключ не найден, добавляет ключ с значением по умолчанию и возвращает его.'''
        if key not in self:
            self[key] = default
        return self[key]

    def items_length(self):
        '''Возвращает длину всех пар (ключ, значение) в словаре.'''
        return len(self.data)

    @classmethod
    def fromkeys(cls, iterable, value=None):
        '''Создает новый экземпляр MyDict с заданными ключами и значением по умолчанию.'''
        new_dict = cls()
        for key in iterable:
            new_dict[key] = value
        return new_dict


# Пример использования
my_dict = MyDict()
my_dict['apple'] = 1
my_dict['banana'] = 2

print(my_dict['apple'])  # Вывод: 1
print('banana' in my_dict)  # Вывод: True
print(len(my_dict))  # Вывод: 2

my_dict['apple'] = 3
print(my_dict['apple'])  # Вывод: 3
my_dict['cherry'] = 5
print(my_dict.items())  # Вывод: [('apple', 3), ('banana', 2), ('cherry', 5)]

del my_dict['banana']
print(my_dict.items())  # Вывод: [('apple', 3), ('cherry', 5)]

# Применение новых методов
my_dict.clear()
print(my_dict.items())  # Вывод: []

my_dict.update({'orange': 4, 'pear': 6})
print(my_dict.items())  # Вывод: [('orange', 4), ('pear', 6)]

value = my_dict.pop('orange')
print(value)  # Вывод: 4
print(my_dict.items())  # Вывод: [('pear', 6)]

last_item = my_dict.popitem()
print(last_item)  # Вывод: ('pear', 6)

# Демонстрация новых методов
print(my_dict.get('pear'))  # Вывод: KeyError
print(my_dict.get('pear', 'default_value'))  # Вывод: default_value

my_dict.setdefault('banana', 10)
print(my_dict.items())  # Вывод: [('banana', 10)]

length = my_dict.items_length()
print(length)  # Вывод: 1

new_dict = MyDict.fromkeys(['key1', 'key2', 'key3'], 'default_value')
print(new_dict.items())  # Вывод: [('key1', 'default_value'), ('key2', 'default_value'), ('key3', 'default_value')]
________________________________________________________________________________________________________________________
"""




# Задачи с собеседования  X5


# Задача 1

# Есть список чисел. Нужно отсортировать нечетные числа по возрастанию, оставив четные на месте


def sort_array(arr):
    pass





# numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# print(sort_array(numbers))  # -> [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]





# Задача 2

'''Напишите функцию flatten, которая принимает любое кол-во аргументов
и 'разглаживает' их в один список. Все вложенные списки, неважно каких уровней вложенности,
должны разгладиться в один результирующий список'''


# Написать 4 варианта  и написать вариант который НЕ подвержен ограничению рекурсии!
def flatten(*args):
    pass




# print(flatten([1, 2, [2, 3, [4, 4]]]))                  # -> [1, 2, 2, 3, 4, 4]
# print(flatten([1, 2, [2, 3, [4, 4]], [[[[[5, 5]]]]]]))  # -> [1, 2, 2, 3, 4, 4, 5, 5]



# 2 Варианта
def flatten(items):
    pass





# res = [1, 2, [2, 3, [4, 4]]]
# print([*flatten(res)])  # -> [1, 2, 2, 3, 4, 4]
# print(list(flatten(res)))  # -> [1, 2, 2, 3, 4, 4]





# Ответ Задачи с собеседования  X5

r"""
# Задача 1

# Есть список чисел. Нужно отсортировать нечетные числа по возрастанию, оставив четные на месте

def sort_array(arr):
    odds = sorted([i for i in arr if i % 2])
    odd_index = 0
    res = []
    for i in arr:
        if i % 2:
        # if i in odds:  # Тоже самое
            res.append(odds[odd_index])
            odd_index += 1
        else:
            res.append(i)
    return res

numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(sort_array(numbers))  # -> [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]


# Ответ ChatGPT
def sort_array(source_array):
    odds = sorted(filter(lambda i: i % 2 != 0, source_array))
    odds_iter = iter(odds)
    return [next(odds_iter) if i % 2 != 0 else i for i in source_array]

numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(sort_array(numbers))  # -> [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]


# Задача 2

'''Напишите функцию flatten, которая принимает любое кол-во аргументов
и 'разглаживает' их в один список. Все вложенные списки, неважно каких уровней вложенности,
должны разгладиться в один результирующий список'''


# Вариант который НЕ подвержен ограничению рекурсии Python  (Книга Python. Исчерпывающее руководство Дэвид Бизли)
#  1) Избежание переполнения стека  2) Глубокая рекурсия  3) Циклические ссылки      # БУДЕТ РАБОТАТЬ В ЭТИХ СЛУЧАЯХ!
def flatten(items):
    stack = [ iter(items) ]
    while stack:
        try:
            item = next(stack[-1])
            if isinstance(item, list):
                stack.append(iter(item))
            else:
                yield item
        except StopIteration:
            stack.pop()
            
res = [1, 2, [2, 3, [4, 4]]]

print([*flatten(res)])      # -> [1, 2, 2, 3, 4, 4]
print(list(flatten(res)))   # -> [1, 2, 2, 3, 4, 4]   


# Классный вариант  из Книги: Python Книга рецептов   Дэвид Бизли

from collections.abc import Iterable
def flatten(items, ignore_types=(str, bytes)):
    for i in items:
        if isinstance(i, Iterable) and not isinstance(i, ignore_types):                                         
            yield from flatten(i)                                         # Тоже самое   for j in flatten(i):
        else:                                                             #                  yield j    
            yield i

print(list(flatten([1, 2, [2, 3, [4, 4]]])))               # -> [1, 2, 2, 3, 4, 4]
print([*flatten([1, 2, [2, 3, [4, 4]], [[[[[5, 5]]]]]])])  # -> [1, 2, 2, 3, 4, 4, 5, 5]



# Тоже самое  extend                                           # Тоже самое  +=
def flatten(*args):                                            def flatten(*args):
    res = []                                                       res = []
    for i in args:                                                 for i in args:
        if not isinstance(i, list):                                    if isinstance(i, list):
            res.append(i)                                                  res += flatten(*i)
        else:                                                          else:
            res.extend(flatten(*i))                                        res.append(i)
    return res                                                     return res

print(flatten([1, 2, [2, 3, [4, 4]]]))  # -> [1, 2, 2, 3, 4, 4]

# Второй вариант
def flatten(*args):
    res = re.sub(r'[\]\[]', '', str(args))
    return eval(re.sub(r',?\)|\(', lambda x: '[' if x[0] == '(' else ']', res))

print(flatten([1, 2, [2, 3, [4, 4]]]))  # -> [1, 2, 2, 3, 4, 4]

# Интересный вариант
from ast import literal_eval

def flatten(*args):
    res = re.sub(r'[\]\[]', '', str(args))
    res_2 = re.sub(r'\(|,\)', '', res)
    return literal_eval(f"[{res_2}]")
    # return eval(f"[{res_2}]")

print(flatten([1, 2, [2, 3, [4, 4]]]))  # -> [1, 2, 2, 3, 4, 4]

# Интересный вариант
def flatten(*args):
    res = []
    for i in args:
        match i:
            case list():
                res += flatten(*itertools.chain(i))
            case _:
                res.append(i)
    return res

print(flatten([1, 2, [2, 3, [4, 4]]]))  # -> [1, 2, 2, 3, 4, 4]

# Интересный вариант
def flatten(*args):
    try:
        return [*map(int, [i for i in re.findall(r'[^\[\]()]', str(args)) if i not in ' ,'])]
    except:
        print('not good')

print(flatten([1, 2, [2, 3, [4, 4]]]))  # -> [1, 2, 2, 3, 4, 4]


# Так тоже работает
def flatten(*args):
    res = re.sub(r'\[|\]', '', str(args))  # (1, 2, 2, 3, 4, 4,)    # Тут будет вот такая строка с запятой в конце
    return eval(res)

print(flatten([1, 2, [2, 3, [4, 4]]]))                  # -> (1, 2, 2, 3, 4, 4)
print(flatten([1, 2, [2, 3, [4, 4]], [[[[[5, 5]]]]]]))  # -> (1, 2, 2, 3, 4, 4, 5, 5)
________________________________________________________________________________________________________________________
"""



# Задача максимальная последовательность чисел  СБЕР


# Написать 2 варианта

def longest_sequence(lst):
    pass




# arr = [111, 22, 533, 61, 655, 7333, 911, 11, 211, 1, 2, 3, 4, 5]
# print(longest_sequence(arr))  # -> [1, 2, 3, 4, 5]



# Ответ Задача максимальная последовательность чисел  СБЕР
"""
# НОВЫЙ ВАРИАНТ
def longest_sequence(arr):
    if not arr:
        return []

    # Сортируем массив
    arr = sorted(set(arr))  # используем set для удаления дубликатов
    max_length = 0
    current_length = 1
    start_index = 0
    max_start_index = 0

    for i in range(1, len(arr)):
        # Проверяем, является ли текущий элемент последовательным
        if arr[i] == arr[i - 1] + 1:
            current_length += 1
        else:
            # Проверяем, является ли текущая последовательность максимальной
            if current_length > max_length:
                max_length = current_length
                max_start_index = start_index
            
            # Сбрасываем текущую последовательность
            current_length = 1
            start_index = i

    # Проверка последней последовательности
    if current_length > max_length:
        max_length = current_length
        max_start_index = start_index

    return arr[max_start_index:max_start_index + max_length]

# Пример использования
arr = [111, 22, 533, 61, 655, 7333, 911, 11, 211, 1, 2, 3, 4, 5]
print(longest_sequence(arr))  # -> [1, 2, 3, 4, 5]



# Мой вариант                                                   # Такой вариант выведет   ['1', '2', '3', '4'] 
def longest_sequence(arr):                                      def longest_sequence(arr):                                                                                                                                         
    if not arr:                                                     if not arr:                               
        return []                                                       return []                                                   
    res = []                                                        res = []                                      
    for i in range(len(arr)-1):                                     for i in range(len(arr)-1):                                              
        if arr[i] < arr[i+1]:                                           if arr[i] < arr[i+1]:                                      
            res.append(arr[i])                                              res.append(arr[i])                                                        
        else:                                                           else:                                                      
            res.append(arr[i])                                              res.append(arr[i])                                                                                
            res.append('A')                                                 res.append('A')                                                          
    if arr[-1] > res[-1]:                                           res_2 = ' '.join([str(i) for i in res]).split('A')                            
        res.append(arr[-1])                                         return max([i.split() for i in res_2], key=len)   
    res_2 = [i.strip().split() for i in ' '.join(map(str, res)).split('A')]                                                                      
    return [*map(int, max(res_2, key=len))]                                                

arr = [111, 22, 533, 61, 655, 7333, 911, 11, 211, 1, 2, 3, 4, 5]
print(longest_sequence(arr))  # -> [1, 2, 3, 4, 5]


# Еще один вариант МОЙ
def longest_sequence(arr):
    res = []
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            res.append(arr[i])
        else:
            res.append(arr[i])
            res.append('A')
    if arr[-1] > res[-1]:
        res.append(arr[-1])
    res_2 = ' '.join(map(str, res)).split('A')
    return [*map(int, max([i.strip().split() for i in res_2], key=len))]


arr = [111, 22, 533, 61, 655, 7333, 911, 11, 211, 1, 2, 3, 4, 5]
print(longest_sequence(arr))  # -> [1, 2, 3, 4, 5]


# Вариант ChatGPT
def longest_sequence(arr):
    if not arr:
        return []

    max_seq = []
    current_seq = []

    for i in range(len(arr)):
        # Если текущий элемент больше предыдущего
        if i == 0 or arr[i] > arr[i - 1]:
            current_seq.append(arr[i])
        else:
            # Если последовательность прерывается, проверяем и обновляем max_seq
            if len(current_seq) > len(max_seq):
                max_seq = current_seq
            current_seq = [arr[i]]  # Начинаем новую последовательность

    # Проверяем последний текущий сегмент
    if len(current_seq) > len(max_seq):
        max_seq = current_seq
    return max_seq

arr = [111, 22, 533, 61, 655, 7333, 911, 11, 211, 1, 2, 3, 4, 5]
print(longest_sequence(arr))  # -> [1, 2, 3, 4, 5]


# Очень похожий вариант
def longest_sequence(arr):
    max_seq = []
    current_seq = []
    n = len(arr)
    for i in range(n):
        if arr[i] > arr[i-1]:
            current_seq.append(arr[i])
        else:
            if len(current_seq) > len(max_seq):
                max_seq = current_seq
            current_seq = [arr[i]]
    if len(current_seq) > len(max_seq):
        max_seq = current_seq
    return max_seq
    
arr = [111, 22, 533, 61, 655, 7333, 911, 11, 211, 1, 2, 3, 4, 5]
print(longest_sequence(arr))  # -> [1, 2, 3, 4, 5]
"""




# Задача на логику    Сбер

# У Вас есть два шнура (фитиля). Каждый шнур, подожженный с конца, полностью сгорает дотла ровно за один час,
# но при этом горит с неравномерной скоростью. Как при помощи этих шнуров и зажигалки отмерить время в 45 минут?



# Ответ  Задача на логику    Сбер
"""
# Мой ответ
Чтобы рассчитать 30 минут поджигаем с разных сторон Один фитиль
Чтобы Рассчитать 45 минут мы одновременно с первым подожженным с двух сторон поджигаем второй и тушим когда догорел
первый, затем поджигаем остаток второго с двух сторон.


# ChatGPT ответ
Чтобы отмерить 45 минут с помощью двух шнуров, следуйте следующему алгоритму:

1. Зажгите один конец первого шнура и оба конца второго шнура одновременно.
2. Так как второй шнур горит с обеих сторон, он полностью сгорит за 30 минут.
3. Когда второй шнур сгорит, это будет означать, что прошло 30 минут.
4. В этот момент зажгите второй конец первого шнура (который горит с одного конца).
5. Теперь у вас есть первый шнур, горящий с двух концов. Поскольку он уже горел 30 минут и осталась половина шнура,
   при поджигании с другого конца он сгорит за 15 минут (так как будет гореть с обеих сторон).
6. В итоге, с момента, когда второй шнур сгорел, пройдет ещё 15 минут.

Таким образом, в сумме у вас будет 30 минут + 15 минут = 45 минут.
"""




# НАПИШИ 2 ВАРИАНТА   1 - Через функцию  2 - Через Класс
# Создайте декоратор retry, который повторяет выполнение функции заданное количество раз, если она завершилась с ошибкой.
# Если все попытки неудачны, декоратор должен вернуть сообщение об ошибке или выбросить исключение.   Сбер
#
# Условия:
#
# Декоратор принимает два аргумента:
# 1. количество попыток retries;
# 2. время ожидания между попытками delay (в секундах).
#
# Декорируемая функция может принимать любые аргументы и возвращать результат или выбрасывать исключение.
#
# Декоратор должен перехватывать исключения и повторять выполнение функции, если она завершилась с ошибкой.
#
#
# @retry(retries=5, delay=2)
# def unstable_function():
#     if time.time() % 2 > 1.5:
#         raise ValueError("Случайная ошибка")
#     return "Успех!"
# print(unstable_function())
# --------------------------
# Ожидаемый вывод:
#
# Попытка 1 не удалась: Случайная ошибка. Повтор через 2 секунд.
# Попытка 2 не удалась: Случайная ошибка. Повтор через 2 секунд.
# Попытка 3 не удалась: Случайная ошибка. Повтор через 2 секунд.
# Попытка 4 не удалась: Случайная ошибка. Повтор через 2 секунд.
# Функция не отработала корректно







# ОТВЕТ НАПИШИ 2 ВАРИАНТА   1 - Через функцию  2 - Через Класс
# Ответ Создайте декоратор retry, который повторяет выполнение функции заданное количество раз, если она завершилась с
# ошибкой. Если все попытки неудачны, декоратор должен вернуть сообщение об ошибке или выбросить исключение.   Сбер
"""
# Ответ Мой
from functools import wraps
import time

def retry(retries, delay):   # Важно чтобы параметры назывались так же как и в параметрах декорируемой функции   <-----
    def decor(func):         # При передаче их как именованные параметры      ИЛИ TypeError                      <-----
        @wraps(func)
        def wrappper(*args, **kwargs):
            for i in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except ValueError as e:
                    print(f'Попытка {i} не удалась: {e}. Повтор через {delay} секунд.')
                    time.sleep(delay)
            return 'Функция не отработала корректно'
        return wrappper
    return decor


@retry(retries=5, delay=2)  # Важно чтобы параметры назывались так же как и в параметрах декорируемой функции   <-----
def unstable_function():    # При передаче их как именованные параметры      ИЛИ TypeError                      <-----
    if time.time() % 2 > 1.5:
        raise ValueError("Случайная ошибка")
    return "Успех!"

print(unstable_function())


# ТОЖЕ САМОЕ ЧЕРЕЗ КЛАСС
class retry:
    def __init__(self, retries, delay):
        self.retries = retries
        self.delay = delay

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(1, self.retries + 1):
                try:
                    return func(*args, **kwargs)
                except ValueError as e:
                    print(f'Попытка {i} не удалась: {e}. Повтор через {self.delay} секунд.')
                    time.sleep(self.delay)
            return 'Функция не отработала корректно'
        return wrapper
"""




# Задача На ЭК в словаре  Сколько будет объектов в Словаре data?   ЭК - может быть ключом в словаре!
# Интересно работает даже с pass или ...  Хотя функцию создали внутри






# Ответ Задача На ЭК в словаре  Сколько будет объектов в Словаре data?   ЭК - может быть ключом в словаре!
# Интересно работает даже с pass или ...  Хотя функцию создали внутри    ЭК - может быть в set()
"""
class Foo:
    ...


data = {
    Foo(): 1,
    Foo(): 2,
}

print(data)         # -> {<__main__.Foo object at 0x00000295B379A750>: 1, <__main__.Foo object at 0x00000295B38AA410>: 2}

# В сет тоже можно закинуть ЭК
my_set = {Foo(), Foo()}
print(my_set)       # -> {<__main__.Foo object at 0x00000204FB4FD9D0>, <__main__.Foo object at 0x00000204FB4FDA10>}  

# hash Будут Разные
print(hash(Foo()))  # -> 177624230437  # Разные hash
print(hash(Foo()))  # -> 177624099389  # Разные hash

# id Будут Разные
print(id(Foo()))    # -> 2849472269008  # Разные id
print(id(Foo()))    # -> 2849472268944  # Разные id



# Тоже самое  Даже с __hash__  но hash будет 42
class Foo:
    pass

    def __hash__(self):
        return 42        

data = {
    Foo(): 1,
    Foo(): 2,
}

print(data)         # -> {<__main__.Foo object at 0x00000295B41DFC50>: 1, <__main__.Foo object at 0x00000295B5408050>: 2}

# В сет тоже можно закинуть ЭК
my_set = {Foo(), Foo()}
print(my_set)       # -> {<__main__.Foo object at 0x00000204FB4FD9D0>, <__main__.Foo object at 0x00000204FB4FDA10>}  

# hash Будут Одинаковые
print(hash(Foo()))  # -> 42             # Одинаковые hash
print(hash(Foo()))  # -> 42             # Одинаковые hash

# id Будут разные
print(id(Foo()))    # -> 2849472269008  # Разные id
print(id(Foo()))    # -> 2849472268944  # Разные id
"""




# Задача На Объекты в памяти  Просто посмотреть   Важно посмотри когда идет присвоение a=b

"""
a = []                                 a = 1
b = []                                 b = 1
                                        
print(id(a) == id(b))  # -> False      print(id(a) == id(b))  # -> True                         
print(a == b)          # -> True       print(a == b)          # -> True                         
print(a is b)          # -> False      print(a is b)          # -> True 
                        
b = a                                  b = a                                                    <-----   Присвоение
                                       
print(id(a) == id(b))  # -> True       print(id(a) == id(b))  # -> True  
print(a == b)          # -> True       print(a == b)          # -> True                   
print(a is b)          # -> True       print(a is b)          # -> True                   
"""





# Реализовать функцию, которая будет преобразовывать строку (с целочисленным числом)
# в число, не используя стандартные методы преобразования python.


def to_digit(val):
    ...



def string_to_int(value: str) -> int:
    pass


# print(string_to_int("3248"))  # -> 3248




# Ответ Реализовать функцию, которая будет преобразовывать строку (с целочисленным числом)
# в число, не используя стандартные методы преобразования python.
"""
# Мой ответ                                       # Еще один вариант Мой          
def to_digit(val):                                def to_digit(val):                  
    res = {}                                          res = dict(zip(map(str, range(10)), range(10)))              
    res[val] = int(val)                               return res.get(val)                      
    return res[val]                                                  
                                                    
def string_to_int(value: str) -> int:             def string_to_int(value: str) -> int:            
    res = 0                                           res = 0                          
    n = len(value) - 1                                n = len(value) - 1              
    for i in value:                                   for i in value:                                   
        res += to_digit(i) * 10 ** n                      res += to_digit(i) * 10 ** n                
        n -= 1                                            n -= 1                       
    return res                                        return res                             
                                                   
print(string_to_int("3248"))  # -> 3248           print(string_to_int("3248"))  # -> 3248                                        
                                                    
                                                    
 
# Ответ ChatGPT
def string_to_integer(s):
    # Удаляем пробелы в начале и конце строки
    s = s.strip()

    if not s:  # Проверяем пустую строку
        raise ValueError("Пустая строка не может быть преобразована в число.")

    # Переменные для хранения результата и знака числа
    result = 0
    sign = 1
    index = 0

    # Проверка на знак числа
    if s[index] == '-':
        sign = -1
        index += 1
    elif s[index] == '+':
        index += 1

    # Преобразуем каждую цифру в числе
    for char in s[index:]:
        if char < '0' or char > '9':  # Проверяем, является ли символ цифрой
            raise ValueError(f"Недопустимый символ: {char}")

        result = result * 10 + (ord(char) - ord('0'))  # Преобразуем символ в цифру

    return sign * result


print(string_to_integer("123"))     # -> 123
print(string_to_integer("-456"))    # -> -456
print(string_to_integer(" +789 "))  # -> 789
"""




#  Есть список                                              Грузовая кампания
#  words = ['aba', 'bac', 'abb', 'bab', 'bba',
#  'aab', 'abca']
#  Анаграммы - это такие пары слов, в которых одинаковые буквы и одинаковое количество букв, расположенных в разном
#  порядке. В приведенном примере группы анаграмм: (aba, aab), (abb, bab, bba). Напишите такой код, который выведет
#  на консоль первую анаграмму из каждой группы.









# Ответ
# Есть список                                              Грузовая кампания
# words = ['aba', 'bac', 'abb', 'bab', 'bba',
# 'aab', 'abca']
# Анаграммы - это такие пары слов, в которых одинаковые буквы и одинаковое количество букв, расположенных в разном
# порядке. В приведенном примере группы анаграмм: (aba, aab), (abb, bab, bba). Напишите такой код, который выведет
# на консоль первую анаграмму из каждой группы.
"""
# Мой Ответ
from collections import defaultdict

def is_anagramm(lst: list[str]):
    res = defaultdict(list)
    for i in lst:
        res[''.join(sorted(i))].append(i)
    for j in res.values():
        yield j[False]

words = ['aba', 'bac', 'abb', 'bab', 'bba', 'aab', 'abca']
res = is_anagramm(words)

print(*res)  # -> aba bac abb abca



# Ответ ChatGPT
words = ['aba', 'bac', 'abb', 'bab', 'bba', 'aab', 'abca']

# Словарь для группировки анаграмм
anagrams = {}

# Группируем слова по их отсортированной версии
for word in words:
    # Отсортируем буквы в слове и используем это в качестве ключа
    key = ''.join(sorted(word))
    if key not in anagrams:
        anagrams[key] = []
    anagrams[key].append(word)

# Вывод первой анаграммы из каждой группы
for group in anagrams.values():
    print(group[0], end=' ')  # -> aba bac abb abca
    
    
    
# Улучшение Моего варианта ChatGPT

def is_anagramm(lst: list[str]) -> list[str]:
    res = defaultdict(list)
    # Сортируем слова и группируем их анаграммы
    for word in lst:
        res[''.join(sorted(word))].append(word)
    # Возвращаем первые слова из каждой группы анаграмм
    return [words[0] for words in res.values()]

words = ['aba', 'bac', 'abb', 'bab', 'bba', 'aab', 'abca']
print(*is_anagramm(words))  # -> aba abb abca
"""



# Замерить сколько раз вызывается функция       ivi  Иви
# 2 Варианта через функцию  и 1 Вариант через класс







# Ответ Замерить сколько раз вызывается функция      ivi  Иви
"""
from dataclasses import dataclass, field
from typing import Callable                     # Лучше используем    from collections.abc import Callable 
from functools import wraps

# Ответ через функцию                # Ответ ChatGPT через функцию    Интересный пример   <-----  wrapper.my_count += 1
            
def my_count(func):                  def my_count(func):                  
    c = 0                                @wraps(func)          
    @wraps(func)                         def wrapper(*args, **kwargs):                  
    def wrapper(*args, **kwargs):            wrapper.my_count += 1  # Увеличиваем счетчик вызовов  # МОЖНО любое название                                 
        nonlocal c                           print(f"Функция '{func.__name__}' была вызвана {wrapper.my_count} раз(а).")
        c += 1                               return func(*args, **kwargs)  # Вызываем оригинальную функцию                  
        print(c)                         wrapper.my_count = 0  # Инициализируем счетчик вызовов              
        return func(*args, **kwargs)     return wrapper                                      
    return wrapper                                      
                                     
@my_count                            @my_count          
def plus():                          def plus():                       
    ...                                  pass               
                                                 
print(plus())  # -> 1 None           print(plus())  # -> Функция 'plus' была вызвана 1 раз(а). None
print(plus())  # -> 2 None           print(plus())  # -> Функция 'plus' была вызвана 2 раз(а). None
print(plus())  # -> 3 None           print(plus())  # -> Функция 'plus' была вызвана 3 раз(а). None



# Ответ через класс

@dataclass
class MyClass:
    f: Callable
    c: int = 0

    def __call__(self, *args, **kwargs):
        self.c += 1
        print(self.c)
        return self.f(*args, **kwargs)

@MyClass
def plus():
    ...

print(plus())  # -> 1 None
print(plus())  # -> 2 None
print(plus())  # -> 3 None
"""




# Будет последнее значение выводить 10 раз    ПОСМОТРИ ВНИМАТЕЛЬНО КОД  Обрати внимание на    x   Задача Мебель Детали
# Исправить код. Чтобы текущее состояние сохранялось







# Будет последнее значение выводить 10 раз    ПОСМОТРИ ВНИМАТЕЛЬНО КОД  Обрати внимание на    x   Задача Мебель Детали
"""
# ВСЕ лямбда-функции ссылаются на одну и ту же переменную a, которая в конце цикла равна 9.
fun = [lambda x: a for a in range(10)]
for f in fun:
    print(f(20), end=' ')  # -> 9 9 9 9 9 9 9 9 9 9


# Используем аргумент по умолчанию a=a . Это позволяет каждой функции сохранить текущее значение a на момент создания.
fun = [lambda x, a=a: a for a in range(10)]
for f in fun:
    print(f(20), end=' ')  # -> 0 1 2 3 4 5 6 7 8 9
"""




# Задача Заказчик Открытые Решения  Переписать/Написать 4 Варианта
# * Уровень 1 *
# 1.  Распарсить CSV-строку в список словарей, ключи для которых взять из заголовка
#     (built-in СТРОКОВЫМИ средствами)
# 2.  Нормализовать данные в словарях в соответствии с правилами
#     Правила определить, исходя из наблюдаемых в данных отклонениях

RAW_DATA = '''phone, fullname, some_amount, rating_position
+7 993 0965431, Абдуллаев Рамиль Ахмед оглы, 5432, 5
89615421187, Васильев Михаил Борисович, 1577.93, 3
+7 (905) 127-00-01, Филипс    Тревор, 7 311.63, 1
8-987-654-3210, Иванова    Мария Сергеевна, 104, 4
8931 077 2267, Петрова-Васильева     Светлана   Александровна, 35 567.92, 7
955-43-88-102, Крестовоздвиженский    Войцишек  Станислав   Август, 191, 6
7911-631-07-80,    Романов   Борис Анатольевич, 13.2, 2'''






# Ответ Задача Заказчик Открытые Решения
# * Уровень 1 *
# 1.  Распарсить CSV-строку в список словарей, ключи для которых взять из заголовка
#     (built-in СТРОКОВЫМИ средствами)
# 2.  Нормализовать данные в словарях в соответствии с правилами
#     Правила определить, исходя из наблюдаемых в данных отклонениях

RAW_DATA = '''phone, fullname, some_amount, rating_position
+7 993 0965431, Абдуллаев Рамиль Ахмед оглы, 5432, 5
89615421187, Васильев Михаил Борисович, 1577.93, 3
+7 (905) 127-00-01, Филипс    Тревор, 7 311.63, 1
8-987-654-3210, Иванова    Мария Сергеевна, 104, 4
8931 077 2267, Петрова-Васильева     Светлана   Александровна, 35 567.92, 7
955-43-88-102, Крестовоздвиженский    Войцишек  Станислав   Август, 191, 6
7911-631-07-80,    Романов   Борис Анатольевич, 13.2, 2'''


# Первый Вариант
"""
# 1. Разбить строку на строки
lines = RAW_DATA.strip().split('\n')

# 2. Обработать заголовки
headers = [header.strip() for header in lines[0].split(',')]

# 3. Обработать оставшиеся строки
data = []
for line in lines[1:]:
    values = [value.strip() for value in line.split(',')]
    entry = dict(zip(headers, values))
    data.append(entry)

# Результат
print(data)
# [{'phone': '+7 993 0965431', 'fullname': 'Абдуллаев Рамиль Ахмед оглы', 'some_amount': '5432', 'rating_position': '5'},
"""


# Второй Вариант
"""
# 1. Разбить строку на строки
lines = RAW_DATA.strip().split('\n')

# 2. Использовать первую строку как заголовки
headers = [header.strip() for header in lines[0].split(',')]

# 3. Обработать оставшиеся строки и нормализовать данные
data = []
for line in lines[1:]:
    values = [value.strip() for value in line.split(',')]

    # Нормализация данных
    normalized_row = {
        'phone': ''.join(filter(str.isdigit, values[0])),  # Оставляем только цифры
        'fullname': ' '.join(values[1].split()),  # Удаляем лишние пробелы
        'some_amount': float(values[2].replace(' ', '')),  # Удаляем пробелы и преобразуем в float
        'rating_position': int(values[3].strip())  # Преобразуем в int, убирая пробелы
    }

    data.append(normalized_row)

# Результат
print(data)
# [{'phone': '79930965431', 'fullname': 'Абдуллаев Рамиль Ахмед оглы', 'some_amount': 5432.0, 'rating_position': 5},
"""


# Третий Вариант  применение чистых функций, функций высшего порядка синтаксического сахара
"""
# Чистая функция для парсинга CSV-строки
def parse_csv_to_dicts(csv_string):
    lines = csv_string.strip().split('\n')
    header = lines[0].split(',')

    return [
        {header[i].strip(): value.strip() for i, value in enumerate(line.split(','))}
        for line in lines[1:]
    ]


# Чистые функции для нормализации
def normalize_phone(phone):
    return ''.join(filter(str.isdigit, phone))


def normalize_amount(amount):
    try:
        return float(amount.replace(' ', '').replace(',', '.'))
    except ValueError:
        return None


def normalize_rating(rating):
    try:
        return int(rating)
    except ValueError:
        return None


# Объединение нормализации в одну функцию
def normalize_data(entries):
    def normalize_entry(entry):
        return {
            'phone': normalize_phone(entry['phone']),
            'fullname': entry['fullname'],
            'some_amount': normalize_amount(entry['some_amount']),
            'rating_position': normalize_rating(entry['rating_position']),
        }

    # Применяем функцию высшего порядка
    return list(map(normalize_entry, entries))


# Основная функция для обработки данных
def process_csv_data(csv_string):
    parsed_data = parse_csv_to_dicts(csv_string)
    normalized_data = normalize_data(parsed_data)
    return normalized_data


# Вызов основной функции и вывод результата
processed_data = process_csv_data(RAW_DATA)
print(processed_data)
# [{'phone': '79930965431', 'fullname': 'Абдуллаев Рамиль Ахмед оглы', 'some_amount': 5432.0, 'rating_position': 5},
"""


# Четвертый Вариант  применение чистых функций, функций высшего порядка синтаксического сахара
"""
def parse_csv(raw_data):
    # Убираем лишние пробелы и разбиваем строки
    lines = raw_data.strip().split('\n')

    # Извлекаем заголовки и значения
    keys = lines[0].split(', ')
    data = []

    for line in lines[1:]:
        values = line.split(', ')
        # Создаем словарь для каждой строки
        data.append(dict(zip(keys, values)))

    return data


parsed_data = parse_csv(RAW_DATA)

def normalize_phone(phone):
    return ''.join(filter(str.isdigit, phone))  # Сохраняем только цифры

def normalize_name(fullname):
    return ' '.join(fullname.split())  # Убираем лишние пробелы

def normalize_amount(amount):
    amount = amount.replace(' ', '').replace(',', '.')  # Заменяем пробелы и запятые
    return float(amount)

def normalize_rating(rating):
    return int(rating.strip())  # Приводим рейтинг к целому числу

def normalize_data(data):
    return {
        'phone': normalize_phone(data['phone']),
        'fullname': normalize_name(data['fullname']),
        'some_amount': normalize_amount(data['some_amount']),
        'rating_position': normalize_rating(data['rating_position']),
    }

# Применяем нормализацию к каждому элементу в списке словарей
normalized_data = list(map(normalize_data, parsed_data))

# Выводим результат
for item in normalized_data:
    print(item)

# Вывод    
{'phone': '79930965431', 'fullname': 'Абдуллаев Рамиль Ахмед оглы', 'some_amount': 5432.0, 'rating_position': 5}
{'phone': '89615421187', 'fullname': 'Васильев Михаил Борисович', 'some_amount': 1577.93, 'rating_position': 3}
{'phone': '79051270001', 'fullname': 'Филипс Тревор', 'some_amount': 7311.63, 'rating_position': 1}
{'phone': '89876543210', 'fullname': 'Иванова Мария Сергеевна', 'some_amount': 104.0, 'rating_position': 4}
{'phone': '89310772267', 'fullname': 'Петрова-Васильева Светлана Александровна', 'some_amount': 35567.92, 'rating_position': 7}
{'phone': '9554388102', 'fullname': 'Крестовоздвиженский Войцишек Станислав Август', 'some_amount': 191.0, 'rating_position': 6}
{'phone': '79116310780', 'fullname': 'Романов Борис Анатольевич', 'some_amount': 13.2, 'rating_position': 2}
"""




# Попробуй сразу выполнить ВСЁ!!!    Задача Заказчик Открытые Решения
"""
ВАЖНО:
-   можно пользоваться поиском и документацией
-   плюсом будет применение чистых функций, функций высшего порядка
    и синтаксического сахара
-   также при написании web-сервиса будет большим плюсом
    распределение кода по модулям
    
***
ЗАДАЧА
* Уровень 1 *
1.  Распарсить CSV-строку в список словарей, ключи для которых взять из заголовка
    (built-in СТРОКОВЫМИ средствами)
2.  Нормализовать данные в словарях в соответствии с правилами
    Правила определить, исходя из наблюдаемых в данных отклонениях
    
* Уровень 2 *
Используя средства FastAPI разработать сервис с 1 методом,               Можно Использовать Django/DRF
принимающим на вход CSV-строку (валидация через MIME-тип)
и возвращающим JSON со списком словарей, нормализованных по правилам

* Уровень 3 *
Добавить параметры запроса для сортировки по одному полю
в режимах по убыванию и по возрастанию
(используя сущности FastAPI, Pydantic и стандартные средства типизации)  Можно Использовать Django/DRF
"""


RAW_DATA = '''phone, fullname, some_amount, rating_position
+7 993 0965431, Абдуллаев Рамиль Ахмед оглы, 5432, 5
89615421187, Васильев Михаил Борисович, 1577.93, 3
+7 (905) 127-00-01, Филипс    Тревор, 7 311.63, 1
8-987-654-3210, Иванова    Мария Сергеевна, 104, 4
8931 077 2267, Петрова-Васильева     Светлана   Александровна, 35 567.92, 7
955-43-88-102, Крестовоздвиженский    Войцишек  Станислав   Август, 191, 6
7911-631-07-80,    Романов   Борис Анатольевич, 13.2, 2'''






































































































































































































































































































































































































































































































































































































































































































































































































