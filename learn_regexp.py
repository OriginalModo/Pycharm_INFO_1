import calendar
import collections
import copy
import csv
import datetime
import dis
import functools
import itertools
import math
import operator
import random
import re

# text = 'Мама мыла раму'
# # match - ищет последовательность в начале строки
# result = re.match(r'Мама', 'Мама мыла раму')
# print(result[0])                                     # -> Мама    Находит только если pattern в начале
# print(result.group(0), result.group(), result[0])    # -> Мама Мама Мама
# print(result.span(), result.start(), result.end())   # -> (0, 4) 0 4
# result = re.match(r'мыла', 'Мама мыла раму')
# print(result)                                        # -> None    pattern находится НЕ в начале
# print('-'*145)
# # search - ищет первое совпадение с pattern
# result = re.search(r'Мама', 'Мама мыла раму')
# print(result[0])                                     # -> Мама    возвращает только первое даже если больше
# result = re.search(r'мыла', 'Мама мыла раму')
# print(result.group(0))                               # -> мыла    возвращает только первое даже если больше
# result = re.search(r'мыла', 'Мама мыла мыла раму')
# print(result[0])                                     # -> мыла    возвращает только первое даже если больше
# # finditer - ищет все совпадения с pattern. Возвращает итератор
# result = re.finditer(r'мыла', 'Мама мыла мыла раму')
# print([i for i in result])                           # -> ['мыла', 'мыла']
# # re-функции без возврата Match-объекта
# # findall - ищет все совпадения с pattern. Возвращает результирующие строки в виде списка  Работает как search/match
# result = re.findall(r'мыла', 'Мама мыла мыла раму')
# print(result)                                        # -> ['мыла', 'мыла']
# # split - для разделения строки на части по разделителю
# result = re.split(r' ', 'Мама мыла мыла раму', maxsplit=1)
# print(result)                                        # -> ['Мама', 'мыла', 'мыла', 'раму']
# # sub - для замены в строках
# result = re.sub('мыла', '!', 'Мама мыла мыла раму')  # -> Мама ! ! раму
# print(result)


import re
import string
import sys
import time
import timeit


# import numpy
# import pandas as pd


def validate_time(time):
    return re.match(r"2[0-3]|[01]?[0-9]:[0-5][0-9]", time)[0]


# print(validate_time('1:00'))
# print(validate_time('13:1'))
# print(validate_time('12:60'))
# print(validate_time('12:59'))
# print(validate_time('12: 60'))
# print(validate_time('24:00'))
# print(validate_time('00:00'))
# print(validate_time('24o:00'))
# print(validate_time('24:000'))
# print(validate_time(''))
# print(validate_time('09:00'))
# print(validate_time('2400'))
# print(validate_time('foo12:00bar'))
# print(validate_time('010:00'))
# print(validate_time('1;00'))


import re

# Нужно найти весь текст от start до end, текст может быть растянут на несколько строк.
text = """start
Каждое
Слово
На
Новой
Строке
end"""

import re

import re

# text = input()

# Важно Можно использовать rf'' fr'' - строки в заменах
text = r"Мак-адрес моего друга:F0:98:9D:1C:93:F6. Мой мак-адрес: 0F:70:DE:55:60:19."

pattern = re.compile(r"(?:[A-F0-9]{2}:){5}[A-F0-9]{2}")

# print(pattern.findall(text))  # -> <em>Курсив</em> и <strong>Жирный текст</strong>


"(?=...)" "Должно совпасть справа" "Positive Lookahead"
"(?!...)" "НЕ Должно совпасть справа" "Negative Lookahead"
"(?<=...)" "Должно совпасть слева" "Positive Lookbehind"
"(?<!...)" "НЕ Должно совпасть справа" "Negative Lookbehind"

import re
from string import ascii_lowercase
from collections import Counter


def subb(m):
    return m[0] + "o" + m[0]


def translate_to_robber_lang(lst):
    return re.sub(r"(?i)[^aeiou !]", subb, lst)


from functools import reduce
import operator

from collections import defaultdict
from functools import reduce

import re

sett = {"salad", "soup", "main_dish", "drink", "desert"}

from typing import List, Optional
from collections import deque
import re

# Функция-применитель  Посмотри ВСЕ Варианты

from itertools import accumulate
import re

# В dict comprehension прописывать условие k: v Посмотри

from functools import wraps
from typing import Collection

# Пробрасывает Аргументы декоратора дополнительно к аргументам которые передаются при вызове оригинальной функции
from functools import wraps

import decimal
from math import ceil, floor, pow

# contrib = int(input())
# rate = int(input())
# months = int(input())
# print((contrib * float('0.'+str(rate))) + contrib)

# contrib = float(input())
# rate = float(input())
# months = float(input())
import math

import re

# n = int(input())
# lst = input().split()
# lst = [int(i) for i in input().split()]
# res = []
# res_login = []

from string import ascii_lowercase, ascii_uppercase
from itertools import groupby, accumulate, cycle
from functools import reduce
import operator
import heapq
from datetime import date, timedelta, datetime
from calendar import leapdays, isleap, monthrange
from itertools import chain, islice, groupby
from collections import defaultdict, deque, Counter
import re

a_dict = defaultdict(list)
a_dict_2 = defaultdict(list)

# lst = [int(i) for i in input().split()]
# int(input())
# input()
# lst = [float(input()), float(input()), float(input()),]

# Использование __import__   Найти цифры длиной 5 символов
a = 2020
from functools import reduce

# a = '1 2 3'.split()
# c = '1 1'.split()
# n = int(input())
# a = int(input())


# Vitorio Zanzara
# Алекс Глозман
# Анастасия Иванникова
# Олег Галеев

import re

# a, b = [int(i) for i in input().split()]
a, b = [int(i) for i in "1 5".split()]

# a = input()
a = "359"
res_4 = ""

# Vitorio Zanzara
# Алекс Глозман
# Анастасия Иванникова
# Олег Галеев
# Виктор Григорович +


# n = int(input())
# matrix = [list(map(int, input().split())) for _ in range(n)]
# print(matrix)
# matrix = [list(map(int, input().split())) for i in range(int(input()))]
matrix = [[1, 4, 5], [6, 7, 8], [1, 1, 6]]

# n, m = map(int, input().split())
# n, m = [int(input()) for _ in 'aa']
# print(m // n, m % n, sep='\n')


# from datetime import datetime, timedelta
#
#
#
# dt = datetime(year=1, month=1, day=1, minute=0, second=0)
# # delta = timedelta(seconds=int(input())*60)
# delta = timedelta(seconds=3602)
# res = dt + delta
# print(res.hour, res.minute, res.second)

# print(f"The next number for the number {(n:=int(input()))} is {n+True}.")
# print(f"The previous number for the number {(n:=int(input()))} is {n-True}.")

from datetime import datetime, timedelta

# a, b, c, d = [int(input()) for _ in range(4)]
# a, b, c, d = [int(input()) for _ in range(4)]

# Выведите его дробную часть.
a = 17.9
a = "1.79"

# a, b = [int(input()) for _ in 'aa']


# Функции eval() и ast.literal_eval() интерпретируют строки как код Python.
# ast.literal_eval() - обрабатывает только строки, представляющие литералы, более безопасный в применении.
# eval()             - функция способна выполнить любые команды.


# register_check = lambda x: len(__import__('re').findall(r'yes', str(x)))
# register_check = lambda x: len(__import__('re').findall(r'yes', str(x)))


import re

# JavaScript предоставляет встроенный метод parseInt. Его можно использовать следующим образом:
# parseInt("10")              возвращается 10
# parseInt("10 apples") также возвращается 10


# Реализуйте функцию createTemplate, которая принимает строку с тегами, упакованными {{brackets}}в качестве входных
# данных, и возвращает замыкание, которое может заполнять строку данными (плоский объект, где ключами являются имена тегов).

# Пример что должно быть на выходе

# template = create_template("{{name}} likes {{animalType}}")
# template(name="John", animalType="dogs")  # ->  John likes dogs


"aeiouy"
"bcdfghjklmnpqrstvwxzy"

import re
from itertools import pairwise, zip_longest


def sub_fun(m):
    if m[0] == "FIRE":
        return


import re

# a = (1, 2, 3)
# b = (3, 4, 5)

# print(tuple({*a, *b}))
# print(tuple(set(a)+set(b)))

# a = ('John', 'Peter')
# b = (1, 2)
#
# print({key: value for key, value in zip(a, b)})
# print({key: value for key, value in (a, b)})
# print(dict(keys=a, value=b))
# print({key: b[i] for i, key in enumerate(a)})


# class Base:
#     def __init__(self):
#         self.val = 0
#
#     def add_one(self):
#         self.val += 1
#
#     def add_many(self, x):
#         for i in range(x):
#             self.add_one()
#
#
# class Derived(Base):
#     def add_one(self):
#         self.val += 10
#
#
# a = Derived()
# a.add_one()
#
# b = Derived()
# b.add_many(3)
#
# print(a.val)
# print(b.val)


from more_itertools import chunked

from itertools import tee

x = list(range(9, 15))
rez = tee(x, 3)

# for l in rez:
#     print(list(l))

# [9, 10, 11, 12, 13, 14]
# [9, 10, 11, 12, 13, 14]
# [9, 10, 11, 12, 13, 14]

# print([list(i) for i in tee([1, 2, 3], 2)])  # -> [[1, 2, 3], [1, 2, 3]]


import re

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
Используя средства FastAPI разработать сервис с 1 методом,
принимающим на вход CSV-строку (валидация через MIME-тип)
и возвращающим JSON со списком словарей, нормализованных по правилам
* Уровень 3 *
Добавить параметры запроса для сортировки по одному полю
в режимах по убыванию и по возрастанию
(используя сущности FastAPI, Pydantic и стандартные средства типизации)
"""

# Задача Заказчик Открытые Решения

RAW_DATA = """phone, fullname, some_amount, rating_position
+7 993 0965431, Абдуллаев Рамиль Ахмед оглы, 5432, 5
89615421187, Васильев Михаил Борисович, 1577.93, 3
+7 (905) 127-00-01, Филипс    Тревор, 7 311.63, 1
8-987-654-3210, Иванова    Мария Сергеевна, 104, 4
8931 077 2267, Петрова-Васильева     Светлана   Александровна, 35 567.92, 7
955-43-88-102, Крестовоздвиженский    Войцишек  Станислав   Август, 191, 6
7911-631-07-80,    Романов   Борис Анатольевич, 13.2, 2"""

"""
Тестовое задание: бинарная классификация на основе транзакционных аггрегатов
Описание задачи
Клиент приходит в банк и подает заявку на кредит. Необходимо оценить по данным об имеющихся транзакциях клиента выйдет
 ли он в дефолт (просрочка платежа более 90 дней за перый год жизни кредита).

У банка есть исторические данные о транзакциях клиентов и вызревших заявках (с временем жизни более года, чтобы была
 возможность адекватно оценить нашу целевую переменную)

Используя эти данные необходимо построить модель бинарной классификации (Выполнить задания ниже)

Описание данных
Данные:

Application.csv (Таблица заявок)
client_id (id клиента, уникальный ключ таблицы)
app_date (дата заявки)
flag_dr (флаг выхода в дефолт - бинарная переменная (0, 1), целевой признак)
Transaction.csv (Таблица транзакций)
client_id (id клиента)
trans_date (дата транзакции)
amount (сумма транзакции)
category (категория транзакции)
"""

# Task 1
"""Прочитайте данные
Присоедините к заявкам все актуальные на момент заявки транзакции"""

# Task 2
"""
Поисследуйте данные:

Посчитатйте среднее количество транзакций у клиента
Выведите список уникальных категорий транзакций
Посчитайте среднюю сумму транзакций для каждой категории
Постройте график распределения количества транзакций у клиента
Постройте target rate в динамике по месяцам
"""

# Task 3.1
"""
Соберите следующие агрегаты:

Флаг наличия транзакции типа petrol (бинарная)
Количество транзакций типа alcohol
Посчитать отношение суммы трат к сумме поступлений (поступления - income_tranz, траты - все остальное)
Средняя велична последних 3 транзакций типа income_tranz
"""

# Task 3.2

"""
Выведите посчитанные значения для клиентов с id 2851, 463, 1281, 1530, 774, 1816
"""

# Task 4

"""
Разделите выборку на train/test следующим образом:

Train - заявки до июня 2020 включительно
Test - заявки с июля 2020 включительно
"""

# Task 5

"""
Используя полученные фичи, постройте модель логистической регрессии и посчитайте метрику roc auc score на Train и Test выборках
"""

# SOLID - РАСПИСАТЬ ПРИМЕРЫ
# ВСЕ МИНУСЫ С СОБЕСА ПРОЧИТАТЬ!!!


# Миша Горелик  Высокопроизводительные Python-приложения.    # High Performance Python" by Micha Gorelick and Ian Ozsvald
# Марк Лутц  Изучаем Python

# Написать все алгоритмы сортировок


# Матрицы как смотреть вверх, вправо, вниз, влево           # Написать пример
# DIRS = [(-1,0),(0,1),(1,0),(0,-1)] # up right down left


# Float   3.000002    3.9999997   Использовать функцию  linear  solve numpy


# with open('C:\PythonProjects\PythonRussian\input.txt', 'r') as file:
#     text = file.readlines()
# text = [line.strip().split(':') for line in text]
# print(text)


text = """12345
""".strip()

# text = [int(i) for i in text.split()]
#
# with open('C:\PythonProjects\PythonRussian\input.txt', 'r') as file:
#     text = file.read().strip()
#
# text = """AAAA
# BBCD
# BBCC
# EEEC"""
# text = [int(i) for i in text.split()]


# a = re.findall(r'A', text)
# b = re.findall(r'B', text)
# c = re.findall(r'C', text)
# d = re.findall(r'D', text)
# e = re.findall(r'E', text)
# res = [a, b, c, d, e]
#
# a_dict = {}
# for i in res:
#     a_dict[i[0]] = len(i)
# print(a_dict)


# print(a, b, c, d, e)


# text = """AAAA
# BBCD
# BBCC
# EEEC"""


# print(re.search(r'(A)+\1', text).group())
# print(re.search(r'(B)+\1', text).group())
# print(re.search(r'(C)+\1', text).group())
#
#
#
#
#
# # res = [list(i) for i in text.split('\n')]
# res = [i for i in text.split('\n')]
# print(res)
#
# res_2 = []
# for i in res:
#     res_2.append(re.search(r'(B)\1+', i))
# res_3 = [i.span() if i else i for i in res_2]
# res_4 = []
# for i in range(len(res_3)):
#     if res_3[i] and res_3[i+1]:
#         res_4.append(res_3[i])
# print(res_4)


# text = [int(i) for i in text.split()]
#
# with open('C:\PythonProjects\PythonRussian\input.txt', 'r') as file:
#     text = file.read().strip()
#
#
# text = """p=0,4 v=3,-3
# p=6,3 v=-1,-3
# p=10,3 v=-1,2
# p=2,0 v=2,-1
# p=0,0 v=1,3
# p=3,0 v=-2,-2
# p=7,6 v=-1,-3
# p=3,0 v=-1,-2
# p=9,3 v=2,3
# p=7,3 v=-1,2
# p=2,4 v=2,-3
# p=9,5 v=-3,-3"""


# res = text.split('\n')
# # print(res)
#
# val = [list(map(int, i.split(','))) for i in re.findall(r'(?<=p=)(.*?)\s', text)]
# speed = [list(map(int, i.split(','))) for i in re.findall(r'(?<=v=)-?\d+,-?\d+', text)]
# print(val)    # row, col
# print(speed)  # row, col


# matrix = []
# for i in range(7):
#     m = []
#     for j in range(11):
#         m.append([]*11)
#     matrix.append(m)
#
# for i in val:
#     row, col = i
#     matrix[col][row].append(1)


# for i in matrix:
#     print(i)


# matrix = []
# for i in range(7):
#     m = []
#     for j in range(11):
#         m.append('.')
#     matrix.append(m)
#
# for i in val:
#     row, col = i
#     if matrix[col][row] == '.':
#         matrix[col][row] = 1
#     else:
#         matrix[col][row] += 1
#
# for i in matrix:
#     print(i)


# matrix = []
# for i in range(7):
#     m = []
#     for j in range(11):
#         m.append('.')
#     matrix.append(m)


# row, col, row1, col1 = 2, 4, 2, -3
# print('BEFORE')
# matrix[col][row] = 1
# for i in matrix:
#     print(i)
# print(row, col, row1, col1)
# print('AFTER 1')
# matrix[col][row] = '.'
# row, col = row+row1, col+col1
# matrix[col][row] = 1
# for i in matrix:
#     print(i)
# print(row, col, row1, col1)
# print('AFTER 2')
# matrix[col][row] = '.'
# row, col = row+row1, col+col1+7
# matrix[col][row] = 1
# for i in matrix:
#     print(i)
# print(row, col, row1, col1)
# print('AFTER 3')
# matrix[col][row] = '.'
# row, col = row+row1, col+col1
# matrix[col][row] = 1
# for i in matrix:
#     print(i)
# print(row, col, row1, col1)
#
# print('AFTER 3')
# matrix[col][row] = '.'
# row, col = row+row1, col+col1+7
# matrix[col][row] = 1
# for i in matrix:
#     print(i)
# print(row, col, row1, col1)
#
#
# print('AFTER 4')
# matrix[col][row] = '.'
# row, col = (row+row1)%10-1, col+col1
# matrix[col][row] = 1
# for i in matrix:
#     print(i)
# print((row+row1))
# print(row, col, row1, col1)


# matrix = []
# for i in range(7):
#     m = []
#     for j in range(11):
#         m.append('.')
#     matrix.append(m)

# row, col, row1, col1 = 2, 4, 2, -3
# # print('AFTER 1')
# # matrix[col][row] = '.'
#
# matrix[col][row] = 1
# for i in range(9):
#     if abs(col+col1) <= len(matrix) and abs(row+row1) <= len(matrix[0]):
#         if matrix[col][row] == 1:
#             matrix[col][row] = '.'
#         else:
#             matrix[col][row] -=1
#         row, col = row + row1, col + col1
#         matrix[col][row] = 1
#     elif abs(col+col1) > len(matrix) and abs(row+row1) > len(matrix[0]):
#         if matrix[col][row] == 1:
#             matrix[col][row] = '.'
#         else:
#             matrix[col][row] -=1
#         row, col = (row+row1)%10-1, col+col1+len(matrix)
#         matrix[col][row] = 1
#     elif abs(col+col1) > len(matrix):
#         if matrix[col][row] == 1:
#             matrix[col][row] = '.'
#         else:
#             matrix[col][row] -=1
#         row, col = row+row1, col+col1+len(matrix)
#         matrix[col][row] = 1
#     elif abs(row+row1) > len(matrix[0]):
#         if matrix[col][row] == 1:
#             matrix[col][row] = '.'
#         else:
#             matrix[col][row] -=1
#         row, col = row, col = (row+row1)%10-1, col+col1
#         matrix[col][row] = 1
#     elif abs(row + row1) >= len(matrix[0]):
#         if matrix[col][row] == 1:
#             matrix[col][row] = '.'
#         else:
#             matrix[col][row] -= 1
#         row, col = row, col = row + row1, col + col1
#         matrix[col][row] = 1
#
#
# for i in matrix:
#     print(i)
# print(row, col, row1, col1)


# val = [list(map(int, i.split(','))) for i in re.findall(r'(?<=p=)(.*?)\s', text)]
# speed = [list(map(int, i.split(','))) for i in re.findall(r'(?<=v=)-?\d+,-?\d+', text)]
# print(val)    # row, col
# print(speed)  # row, col
# res_1 = list(zip(val, speed))
# print(res_1)
#
# matrix = []
# for i in range(7):
#     m = []
#     for j in range(11):
#         m.append('.')
#     matrix.append(m)
#
# # row, col, row1, col1 = 2, 4, 2, -3
# # print('AFTER 1')
# # matrix[col][row] = '.'
#
#
# # res_1 = [([2, 4], [2, -3]), ([0, 4], [3, -3])]
# # res_1 = [([2, 4], [2, -3])]
# # res_1 = [([10, 3], [-1, 2])]
# for ii, vv in res_1:
#     row, col, row1, col1 = ii[0], ii[1], vv[0], vv[1]
#     matrix[col][row] = 1
#     print(row, col, row1, col1)
#     print(ii,vv)
#     for i in range(1):
#         if abs(col+col1) > len(matrix) and abs(row+row1) > len(matrix[0]):
#             matrix[col][row] = '.'
#             row, col = row + abs(row+row1)-len(matrix[0]), col+col1+len(matrix)
#             matrix[col][row] = 1
#         elif abs(row+row1) == len(matrix[0]) and abs(col+col1) == len(matrix):
#             matrix[col][row] = '.'
#             row, col = abs(row+row1)-len(matrix[0])-1, col+col1+len(matrix)-1
#             matrix[col][row] = 1
#         elif abs(col+col1) > len(matrix):
#             matrix[col][row] = '.'
#             row, col = row + row1, col+col1+len(matrix)
#             matrix[col][row] = 1
#         elif abs(row+row1) == len(matrix[0]):
#             matrix[col][row] = '.'
#             row, col = abs(row+row1)-len(matrix[0])-1, col+col1
#             print(row, col)
#             matrix[col][row] = 1
#         elif abs(row+row1) > len(matrix[0]):
#             matrix[col][row] = '.'
#             row, col = row, col = abs(row+row1)-len(matrix[0]), col+col1
#             matrix[col][row] = 1
#         elif abs(col+col1) == len(matrix):
#
#             # row, col = row + row1, col + col1 + len(matrix) - 1
#             matrix[col][row] = '.'
#
#             # row, col = row + row1, col+col1+len(matrix)-1
#
#             matrix[col][row] = 1
#
#         else:
#             # print(2222)
#             matrix[col][row] = '.'
#             row, col = row + row1, col + col1
#             matrix[col][row] = 1
#
#     print(row, col, row1, col1)
# for i in matrix:
#     print(i)
# # print(row, col, row1, col1)


# Матрицы как смотреть вверх, вправо, вниз, влево
# DIRS = [(-1,0),(0,1),(1,0),(0,-1)] # up right down left


text = [int(i) for i in text.split()]

# with open('C:\PythonProjects\PythonRussian\input.txt', 'r') as file:
#     text = file.read().strip()
# print(len([list(map(int, i.split(','))) for i in text.split('\n')]))

text = """r, wr, b, g, bwu, rb, gb, br"""


# a = 4321
# print(4321//16)
# print(270//16)
# print(16//16)
# print(1//16)


# Пример с числом 4321  в 8 системе счисления
# print(4321-(4321//8*8))                             # 1
# print(4321//8 - ((4321//8//8)*8))                   # 4
# print((4321//8//8) - (4321//8//8//8*8))             # 3
# print((4321//8//8//8) - (4321//8//8//8//8*8))       # 0
# print((4321//8//8//8//8) - (4321//8//8//8//8//8))   # 1
#
#
# print(4321//8)  # -> 540
# print(540//8)   # -> 67
# print(67//8)    # -> 8
# print(8//8)     # -> 1
# print(1//8)     # -> 0


# Пример с числом 4321  в 8 системе счисления    Восьмеричная система (основание 8)
# 4321 / 8 = 540, остаток 1
# 540 / 8 = 67, остаток 4
# 67 / 8 = 8, остаток 3
# 8 / 8 = 1, остаток 0
# 1 / 8 = 0, остаток 1


# Пример с числом 4321  в 16 системе счисления   Шестнадцатеричная система (основание 16)
# 4321 / 16 = 270, остаток 1
# 270 / 16 = 16, остаток 14 (E в шестнадцатеричной системе)
# 16 / 16 = 1, остаток 0
# 1 / 16 = 0, остаток 1


# Пример с числом 4321  в 2 системе счисления    Двоичная система (основание 2)
# 4321 / 2 = 2160, остаток 1
# 2160 / 2 = 1080, остаток 0
# 1080 / 2 = 540, остаток 0
# 540 / 2 = 270, остаток 0
# 270 / 2 = 135, остаток 0
# 135 / 2 = 67, остаток 1
# 67 / 2 = 33, остаток 1
# 33 / 2 = 16, остаток 1
# 16 / 2 = 8, остаток 0
# 8 / 2 = 4, остаток 0
# 4 / 2 = 2, остаток 0
# 2 / 2 = 1, остаток 0
# 1 / 2 = 0, остаток 1


# ВАЖНО   ПЕРЕПИСАТЬ ИСХОДНИКИ Itertools    <-----   <-----   <-----   <-----   <-----

#   Стандартный профилировщик Python:
#  cProfile - расширение C
#  profile  - модуль на чистом Python, интерфейс которого имитируется cProfile




res = ["CALYEAR", "calmonth_ext", "calmonth_ext__txtlg", "SBXXEB022", "SBXXEB022__txtsh", "SBXXEB028"]

# Фильтруем список, оставляя только элементы, не содержащие "__"
filtered_res = [item for item in res if "__" not in item]

print(filtered_res)

# Импорт стандартных библиотек
import datetime
import io
import re
from enum import Enum
from itertools import chain, zip_longest
from typing import Any, Dict, List, Optional, Tuple
from datetime import datetime, timedelta

# Импорт сторонних библиотек
import numpy as np
from numpy import average, median
import pandas as pd
from pandas import DataFrame
import requests

# Импорт собственных модулей
from mymodule import MyClass, my_function

















































































































































































































































































