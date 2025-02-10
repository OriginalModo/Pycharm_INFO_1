# 1) Python — язык программирования со СТРОГОЙ ДИНАМИЧЕСКОЙ ТИПИЗАЦИЕЙ
# СТРОГАЯ ТИПИЗАЦИЯ - означает, что операции между разными типами данных требуют явного их преобразования

# ДИНАМИЧЕСКАЯ ТИПИЗАЦИЯ - при котором переменная связывается с типом в момент присваивания значения,
# а не в момент объявления переменной

# Статический прием типизации данных устанавливает тип переменной в процессе компиляции,
# а динамический — во время работы программы. Статически типизированный язык программирования
# проверяет переменную и присваивает ей тип, который в дальнейшем нельзя изменить

# Интерпретатор -  преобразует исходный код Python в машинные инструкции, которые процессор может понять и выполнить.
# Когда вы запускаете скрипт или программу на Python, интерпретатор считывает код,
# проверяет его синтаксис на ошибки и построчно выполняет инструкции (сверху вниз)

# Компиля́тор — программа, переводящая написанный на языке программирования текст в набор машинных кодов.

# 2) Типы данных ИЗМЕНЯЕМЫЕ(mutable) списки(list), словари(dict), множества(set))
# 2) Типы данных НЕ ИЗМЕНЯЕМЫЕ(immutable) (числа(int), строки(str), кортежи(tuple), frozenset)
# 2) НЕ ИЗМЕНЯЕМЫЕ(immutable) последовательности байтов (бинарные данные, bytes )

# Параметр — это значение, которое принимает функция.
# Аргумент — это значение, которое передается в функцию при ее вызове в программе
# Формальные параметры — это имена аргументов функции, за которыми могут скрываться произвольные значения
# Фактические параметры — это конкретные значения, которые связываются с формальными параметрами при вызове функции

# --- *args и **kwargs ---
# 1) args и kwargs в параметрах функции - общепринятые имена, но можно использовать и другие
# 2) * позволяет распаковать iterable/sequence, а ** распакуют словарь
# 2) Итерируемый объект (iterable) - это объект, который способен возвращать элементы по одному
# 2) Кроме того, это объект, из которого можно получить итератор. Примеры итерируемых объектов:
# все последовательности: список, строка, кортеж
# 2) Последовательность (sequence) - это итерируемый объект, к элементам которого можно обратиться по целочисленному
# индексу, а также можно узнать общее количество элементов (длину последовательности)
# 3) если нет никаких спецсимволов, то аргументы функции можно передавать как позиционно, так и keyword (то есть ключ=значение).
# Важно помнить, что позиционные всегда идут раньше keyword(именованных),
# при этом keyword аргументы между собой не обязаны хранить порядок.
# 4) спецсимвол / в параметрах функции говорит, что все, что ДО него должно передаваться как позиционные аргументы
# 5) спецсимвол * (без указания переменной), говорит о том что все, что ПОСЛЕ него должно передаваться как keyword аргумент
# 6) *args в параметрах функции соберет все позиционные аргументы в кортеж (tuple)
# 7) **kwargs в параметрах функции соберет все keyword (именованные) аргументы в словарь (dict)

#    Оператор is Оператор  ==
# оператор is сравнивает ссылку (не содержимое обьекта)
# == проверяет содержимое обьекта

# Оператор == используется для сравнения значений двух переменных
# Оператор is используется для проверки, являются ли две переменные одним и тем же объектом

# --- ДЕКОРАТОР ---
# ДЕКОРАТОР — это функция, которая принимает другую функцию в качестве аргумента,
# добавляет к ней некоторую дополнительную функциональность и возвращают функцию с измененным поведением.
# Функция -полноправный обьект
# внутренняя функция может захватывать переменные из внешней
# Суть декоратора в том, что мы можем менять поведение декорируемого объекта,
# при этом не меняя его собственную реализацию, его код.

# --- Сборщик мусора (Gargabe Collector, GC) ---
# Сборщик мусора автоматически освобождает память, которая больше не используется.
# Он определяет, что память больше не используется, если на объект нет ссылок
# Сборщик мусора (Gargabe Collector, GC)
# import gc, gc.collect()


# Принципы написания кода
# DRY - don't repeat yourself  - не повторяйся
# YAGNI - You aren't gonna need it  - это не понадобится
# KISS - Keep it simple, stupid  - будь проще
# POLA - Principle Of Least Astonishment  - не удивляй пользователя
# EAFP - Easier to Ask for Forgiveness than Permission  - проще извиниться, чем просить разрешения (сначала действуй)
# LBYL - Look Before You Leap - смотри, прежде чем прыгнуть (сначала спроси)
# Помните, что нет правил без исключений, все принципы и даже дзен - рекомендации, а не неоспоримый закон!

# --- Паттерны ---
# Паттерны в Python – это шаблоны для решения задач, которые часто встречаются в практике программиста.
# Паттерны — это типовые решение для типовых задач.
# Существует три основные разновидности паттернов:
# 1) архитектурные паттерны, 2) паттерны проектирования, 3) идиомы
# ПАТТЕРНЫ ПРОЕКТИРОВАНИЯ:
# 1) Порождающие паттерны — отвечают за процесс создания объектов.
# 2) Структурные паттерны — определяют отношения между объектами, облегчая их взаимодействие
# 3) Поведенческие паттерны — определяют способы коммуникации между объектами

# --- Closure Замыкание ---
# Замыкание(Closure) - Внутренняя функция которая возвращается из внешней и при этом
# использует переменные из внешенго Scope(Область видимости)
# каждое замыкание хранит своё состояние, они не пересекаются
# хранит состояние(данные), предоставляет интерфейс для работы с ними,
# "скрывает" данные и помогает избегать global

#     __main__
# если ты запущен напрямую а не импортирован
# у каждого модуля есть __name__

#  --- lambda ---
# lambda можно написать всё ,то что можно написать после return в обычной функции
# аналог def!!
# можно писать всё что допустимо после return в def
# не выполняется до вызова ()!!!
# значения по умолчанию вычисляются в момент создания функции (аргумент функции)

# Аргумент по умолчанию будет создан 1 раз при интерпретации

# 3)
# Hashable - обьект является Hashable если у него есть Hash и за время жизни обьекта этот Hash никогда не меняется
# Hashable Строки, Числа, Кортежи(если они состоят из неизменяемых обьектов, строк, чисел)
# Hashable != Immutable

# --- Set (Множество) ---
# set - множество, хешсет, неупорядоченный набор hashable объектов, доступ и проверка наличия O(1)
# Элементами множества может быть любой неизменяемый тип данных: числа, строки, кортежи frozenset.
# Изменяемые типы данных не могут быть элементами множества, в частности, нельзя сделать элементом множества список
# (вместо этого используйте неизменяемый кортеж), словарь или другое множество
# frozenset - неизменяемый брат множества

# --- Dict (Словарь) ---
# Dict (Словари)  — это упорядоченные коллекции без повторяющихся элементов,
# где каждый элемент представляет собой пару «ключ-значение»
# dict - словарь, отображение, хеш-мап, ассоциативный массив, коллекция пар ключ-значение,
# где ключом может быть только hashable тип, доступ по ключу и проверка наличия ключа O(1),
# с питона 3.7 хранит порядок вставки
# Значения по ключу могут быть любого типа данных. Чтобы взять значение по ключу,
# необходимо указать ключ в квадратных скобках после имени словаря
# пустой словарь создавать лучше через {},а не dict(), под капотом сразу будет создано 8 элементов
# алгоритм работы словаря и сета: Получаем хеш -} высчитываем позицию в массиве -} если элемента нет
# то действуем соответственно задаче -} если элемент есть то сравниваем ключ == тому что ищем -}
# если ключ не равен искомому то ищем дополнительный бакет
# За скорость словаря и сета мы платим большей памятью и тем, что положить туда можно не любые элементы

# --- List comprehension, Generator expressions ---
# List comprehension = Listcomps (однострочник) киллер фича языка
# Generator expressions - genexp (однострочник) киллер фича языка

# 1) все компсы и генэксп работают по принципу
# [ВЫРАЖЕНИЕ/ПРЕОБРАЗОВАНИЕ for element in ИСТОЧНИК if УСЛОВИЕ]
# читается это слева направо, что важно когда циклов больше 1.
# 2) принцип работы операций у листкомпс и генэксп одинаков, синтаксически различаются скобками
# 3) компсы (листкомпс, сеткомпс, дикткомпс) в результате своей работы формируют
# соответствующую коллекцию и занимают память
# 4) переменные созданные внутри компсов или генэкспа недоступны извне
# 5) генэксп вернет объект, а не коллекцию! при создании объекта он проверит источник,
# что может быть критично, если это какая то функция. Если источник не валидный
# то ошибка упадет при создании генератора, а не при попытке получить значение
# 6) генэксп ленивый, то есть ничего не делает и не занимает память пока не потребуется значение.
# Сгенерировав значение снова засыпает пока опять не попросят новое.
# 7) генэксп одноразовый, при исчерпании начинает бросать исключение, которое мы не увидим,
# если используем генератор в цикле for
# 8) генэксп может потенциально генерировать бесконечные последовательности,
# но он ничего не знает о порядке элементов или о их количестве (нет len)

#  переменные в листкомпс недоступны извне
#  читается слева направо
#  для словаря обязательно указать КЛЮЧ:ЗНАЧЕНИЕ
#  генератор вернет обьект, а не коллецию
#  генератор ленивый, не выполняет действий и не занимает память пока не потребуется (next)
#  генератор проверяет источник при создании!!! чтобы он был iterable
#  генератор одноразовый, если исчерпан то бросает StopIteration
#  цикл for перехватывает StopIteration
#  используйте генэксп вместо компс, кроме случаев когда нужна длина len или индексы

# Лично мое мнение -  если вам не нужна длина, слайсы, индексы, то нужно использовать генэскп,
# не только из-за экономии памяти, но и из-за ленивости, экономии процессорного времени.
# Естественно важно помнить что даже pep-8 и дзен - это не закон, а рекомендации,
# наша конкретная реализация и подход должны диктоваться имеющимися условиями и решаемой задачей.


# Mapping (отображение). В данном контексте отображением мы называем представление
# одних данных (некий пул данных) в виде других путем каких либо преобразований.
# Примеры: map()

# --- yield ---
# yield показывает что функция - генератор
# генератор ленивый (lazy)
# после выполнения yield встает на паузу!
# Оператор yield позволяет приостановить выполнение функции-генератора и сохранить ее текущее состояние
# Это позволяет экономить память и упрощает работу с последовательностями данных.
# END --- yield ---

# --- contextmanager ---
# Контекстные менеджеры в Python — это удобный инструмент для управления ресурсами и обеспечения безопасной работы с ними.
# Для создания своего контекстного менеджера нужно определить класс с двумя специальными методами:
# __enter__() и __exit__().
# Мы также можем создать контекстный менеджер, используя функцию и декоратор contextlib.contextmanager.
# В этом случае функция должна быть генератором, который yield‘ит объект для использования в блоке with.
# Все, что находится до yield, будет выполняться перед входом в блок, а после yield — после выхода из блока.
# END --- contextmanager ---

# Корутины или сопрограммы (англ. coroutine) — это специальные функции, которые могут приостанавливать свое выполнение
# и передавать управление другим корутинам, а затем продолжать с того места, где остановились

# --- LEGB ---
# Буквы в аббревиатуре LEGB обозначают локальную, вложенную, глобальную и встроенную
# (Local, Enclosing, Global и Built-in Scope) области. Поиск идёт сверху-вниз сначала L-E-G-B
# даже для встроенных функций если не нашел переменную, то ошибка  NameError:

# Особенности LEGB:
# 1) сначала поиск идет в локальном пространстве имен, максимально близко к использованию имени и
# далее идет снизу-вверх, изнутри-наружу к глобальному пространству имен
# 2) после локального пространства имен интерпретатор посмотрит в enclosing, то есть в функцию,
# которая содержит текущую (если она есть) и далее проверит глобальное пространство имен
# 3) последним шагом будут проверены имена в модуле builtins (встроенные функции)
# 4) если на любом этапе имя найдено, то далее поиск не идет. Если все этапы неудачны то выбрасывается NameError
# 5) важно понимать что даже если мы используем встроенную функцию, типа max/min/sum/print,
# то интерпретатор сначала проведет поиск по всем скоупам. Вот почему крайне важно НИКОГДА не давать своим переменным,
# функциям, модулям имена встроенных функций или библиотек (самые частые фейлы это имена типа len, list, sum, json, dict)
# END --- LEGB ---

# --- global и nonlocal ---
# global и nonlocal нужны только для изменения значений
# global может создать переменную, nonlocal не может!
# nonlocal ищет только во внешнмх скоупах, но не в глобальном и не builtins
# не используйте global, nonlocal

# Особенности:
# 1) если мы пытаемся изменить какую-то переменную внутри функции, интерпретатор автоматически считает ее локальной,
# слова global/nonlocal нужны как информация интерпретатору, что переменная не локальна
# 2) оба ключевых слова НЕ нужны, если вам нужно только читать переменную, используйте их только для изменения
# 3) оба слова позволяют сразу перейти к поиску в нужном пространстве имен, nonlocal сразу переходит к поиску
# во внешних функциях (в который вложена текущая), global сразу переходит к поиску в глобальном пространстве имен.
# То есть nonlocal сразу идет в букву E, а global в букву G в аббревиатуре LEGB
# 4) global позволяет создать в глобальном пространстве имен переменную, которой там не было.
# Nonlocal работает только с уже существующими переменными
# 5) Nonlocal НЕ ищет в глобальном, а global во вложенных скоупах! Они не взаимозаменяемы
# 6) Есть редкие случаи, когда использование global оправдано,
# но в большинстве случаев и просто как хорошая практика  - не стоит использовать global и nonlocal.
# Стоит отдавать предпочтение независимым, "чистым" функциям.

# Совет: самая хорошая функция которая не влияет ни на что вне себя. Ничего не знает о внешнем мире
# END --- global и nonlocal ---

# --- Стек вызовов --- — это структура данных, которая управляет вызовами функций во время выполнения программы.
# Если программа пытается разместить на стеке больше данных, чем он может вместить, происходит переполнение стека.
# на дне стека есть функция module(ИСПОЛНЯЕТ НАШИ ЗАПРОСЫ) 1) когда мы вызываем функцию она попадает в СТЕК.
# 2) когда функция завершается она снимается со СТЕКА
# ВСЕ ФУНКЦИИ ВНУТРИ СТЕКА ВЫЗОВА ИСПОЛНЯЮТСЯ НО ТОЛЬКО ОДНА ФУНКЦИЯ ВЫПОЛНЯЕТСЯ РЕАЛЬНО(КОТОРАЯ НА ВЕРХУШКЕ СТЕКА)
# А ОСТАЛЬНЫЕ ФУНКЦИИ ЖДУТ СОСЕДА СВЕРХУ ПОКА ОН ИСПОЛНИТСЯ
# СТЕК ВЫЗОВОВ ОТОБРАЖАЕТ ВСЕ ФУНКЦИИ КОТОРЫЕ ИСПОЛНЯЮТСЯ В ДАННЫЙ МОМЕНТ И КТО КОГО ЖДЕТ

# --- Тестирование ---
# Unittest — это модуль стандартной библиотеки Python. Внутри есть фреймворк для создания и запуска тестов.
# С его помощью можно создавать мок-объекты, которые имитируют поведение зависимых компонентов
# и помогают изолировать тестируемый код. Нельзя лишь имитировать внешние сервисы.

# Мок проверяет, что какой-то код выполнился определенным образом. Это может быть вызов функции, HTTP-запрос
# и тому подобное. У мока две задачи: Убедиться в том, что событие произошло — например, функция передала данные
# Отслеживание выполнения какого-то действия — это и есть мокинг

# Моки (mocks) – более продвинутые заглушки, которые позволяют контролировать вызов методов,
# передачу аргументов и проверку ожидаемого поведения тестируемой системы.
# Фейки (fakes) – имитационные объекты, которые имитируют поведение реальных компонентов, но с упрощенной реализацией


#  --- OOP ---
# Объектно-ориентированное программирование (ООП) — это подход,
# при котором программа рассматривается как набор объектов, взаимодействующих друг с другом

# Объе́ктно ориенти́рованное программи́рование(ООП) - это способ решения задач когда все в программе обьекты
# и взаимодействие между ними

# # Обьект - сущность, обьединяющая данные и методы для работы с ними (состояние и поведение)

# Парадигма, в программировании — это совокупность идей и понятий, определяющих стиль написания компьютерных программ

# Парадигмы программирования — это совокупность методов, концепций, принципов, техник и инструментов,
# которые определяют способ организации программы на языке программирования и ход её выполнения.

# Класс - это новый тип данных, обьект - его конкретный представитель
# у любого обьекта есть id (адресс в памяти), значение и тип
# первая потребность для классов - когда не хватает встроенных типов, вторая - разное состояние
# метод - это функция которая принадлежит классу
# self - ссылка на экземпляр класса
# если класс пустой(pass) сравнивает == через is по адресу в памяти (ссылка)

# в Python все обьекты

# Книги ООП: Дасти Филлипс, Марк Лутц

# --- Encapsulation (Инкапсуляция) ---

# Инкапсуляция - Механизм и способ организации классов когда мы данные и методы для работы с ними помещаем в одно место
# но кроме того мы предоставляем пользователю публичный АПИ для взаимодействия с нашим обьектом или классом

# Публичный АПИ - некий интерфейс, публичные методы которые помечаем тем что не ставим _ перед атрибутами и методами

# Инкапсуляция заключается в сборе в одно место (класс) данных и методов для работы с ними и
# предоставлении пользователю публичного интерфейса(API(Публичный интерфейс))
# public(публичный) = без _ , __
# _ - protected(защищенный) знак того, что этот атрибут не предназначен для прямого использования.
# Работа обьекта не гарантируется, при использовании таких атрибутов
# __ - private(приватный) под капотом преобразуется в object._Class__attribute (только для случаев когда начинается с __)
# Name MangLing (Преобразование в не явное)
# Явное лучше неявного!!!
# Публичный АПИ(интерфейс) - это контракт, все методы будут работать, внутренняя же реализация не гарантируется.
# Совет - делать одно _ для врутренних атрибутов и реализаций, не перебарщивать с __ и сеттерами/геттерами

# В питоне применяется нижнее подчеркивание _ для пометки внутренней реализации,
# то есть атрибутов не относящихся к публичному интерфейсу.
# Одно подчеркивание (protected) - это всего лишь сигнал, интерпретатор относится к таким атрибутам как к обычным.
# Два подчеркивания (private) - включает механизм подмены имени Name Mangling,
# который предназначен не для сокрытия данных.
# Инкапсуляция в питоне не подразумевает сокрытия данных (в некоторых языках это одно и то же)
# - все данные доступны для просмотра и изменения. В Python мы не пробуем отобрать у юзера инструменты, мы предупреждаем.

# --- Inheritance (Наследование) ---

# Inheritance - Наследование, это механизм получения доступа к данным и поведению своего предка.
# И расширению (изменению поведения) классов не меняя код
# IS-A является (наследование)
# HAS-A содержит (композиция)
# __ сделано для того чтобы при наследовании не переопределить(изменить) атрибут предка

# Override - Переопределение означает, что в подклассе создается метод с тем же именем, что и в родительском классе
# Override - Переопределение методов — это возможность создавать методы с тем же именем и параметрами,
# но с разной реализацией в классе-наследнике

# любой обьект в Python наследуется от object

# Наследование представляет собой очень мощный и крутой механизм, помогающий писать код красиво,
# структурировано и без дублирования. Достигается это за счет использования трех методик:
# Переопределение (Overriding), Расширение (Extending), Делегирование (Delegation)
# Переопределение метода («Method overriding») — концепция в ООП,
# позволяющая дочернему классу обеспечивать специфическую (свою собственную) реализацию метода,
# уже реализованного в родительском классе.
# Идея Расширение (Extending) заключается в том, что вы можете добавлять в дочерний класс новые атрибуты и методы,
# имеющие отличающиеся имена от атрибутов и методов родительского класса. В результате такого добавления получим,
# что в дочернем классе будут доступны все методы и атрибуты родителя плюс свои собственные,
# то есть более расширенное поведение, чем у его родителя
# # Делегирование - это способ вызова в дочернем(субклассе) метода родительского (базового) класса.
# # Вызывается через использовании функции super()
# Механизм делегирования позволяет «переложить» часть работы на другие объекты.

# --- Множественное наследование ---
# Python позволяет использовать концепцию множественного наследования. Это значит,
# что ваш класс может наследовать атрибуты и методы сразу от нескольких родительских классов.
# Это позволяет создавать более сложные иерархии классов, объединяя функциональность из разных источников
# Книги: Kent Beck (Кент Бек)

# --- MRO (method resolution order) ---
# Аббревиатура MRO – method resolution order (переводится как «порядок разрешения методов»).
# Этот порядок относится не только к поискам методов, но и к прочим атрибутам класса,
# так как методы – это частный случай более общего понятия «атрибут».

# Данная команда возвращает нам список классов ровно в том порядке, в котором Python будет искать методы
# в иерархии класса пока не найдет нужный или не выдаст ошибку.
# Class.mro()   Class.__mro__
# Поиск идёт по алгоритму С3-линеаризации

# --- Polymorphism (Полиморфизм) ---
# Polymorphism (Полиморфизм) в объектно-ориентированном программировании – это возможность обработки разных типов данных,
# т. е. принадлежащих к разным классам, с помощью "одной и той же" функции, или метода

# Это означает, что одна и та же сущность (операция, функция, метод, объект) может использоваться для разных типов.
# Это делает программирование более интуитивным и простым

# Polymorphism - Полиморфизм (Много форм) -  это механизм, позволяющий выполнять один и тот же код по-разному
# Ducktyping (утиная типизация) - наличие поведения для использования в полиморфизме
# Ducktyping - термин пошел после статьи Алекска Мартелли:
# Если что-то выглядит как утка, плавает как утка и крякает как утка, то, скорее всего, это утка

# В ЯП со статической типизацией для полиморфизма важно кто ты (какой тип)
# Для питона важно что ты умеешь (поведение)
# В питоне везде полиморфизм (требуются методы)

# Книги: Лучано Рамальо

# --- Singleton (Одиночка) ---

# Singleton (Одиночка) – ЭТО ПАТТЕРН ПРОЕКТИРОВАНИЯ,
# ЦЕЛЬ КОТОРОГО ОГРАНИЧИТЬ ВОЗМОЖНОСТЬ СОЗДАНИЯ ОБЪЕКТОВ ДАННОГО КЛАССА ОДНИМ ЭКЗЕМПЛЯРОМ.
# Синглтон (Singleton) — это порождающий шаблон проектирования, который обеспечивает,
# что класс имеет только один экземпляр, и предоставляет глобальную точку доступа к нему. Это особенно полезно,
# когда вам нужно точно контролировать доступ к некоторому общему ресурсу, например, базе данных или файлу.

# --- Моносостояние ---
# Инициализируется словарь при создании класса, а не экземпляра класса. При создании экземпляра всем экземплярам
# присваивается ссылка на один и тот же словарь, с которым и работают в итоге все экземпляры
# __shared_attrs = {}  def __init__(self) self.__dict__ = self.__shared_attrs

# Композиция: объект A управляет временем жизни объекта B
# Агрегация: объект А получает ссылку на объект B

# __slots__
# Создатель Python, Guido van Rossum, утверждает,
# что на самом деле он создал __slots__ для более быстрого доступа к атрибутам.
# __slots__ - уменьшить объем в памяти, которое занимает каждый экземпляр объекта.
# После указания __slots__ добавление новых атрибутов в экземпляр класса, кроме уже указанных, невозможно
# Также при использовании __slots__ пропадает возможность получить словарь self.__dict__ с атрибутами
# __slots__ при наследовании
# Чтобы в дочернем классе не пропадала функциональность __slots__ родительского класса,
# нужно просто прописать свой __slots__
# __slots__ - создан для уменьшения памяти, занимаемой обьектами
# но как побочное свойство -не даст добавить объекту новый атрибут

# --- @property ---
# property - это удобный механизм создания геттеров и сеттеров
# У класса (и объекта) есть два основных инструмента взаимодействия — свойства и методы.
# Свойства — это данные, которые лежат внутри объекта.
# Методы — это то, что объект умеет делать или как реагирует на внешние запросы.
# Геттеры и сеттеры являются методами класса, которые используются для получения
# и установки значений атрибутов экземпляра класса, соответственно.

# Возможность установки/получения атрибутов с логикой
# Зарпетить менять атрибут или добавлять новые атрибуты
# __dict__ - это атрибут обьектов в питоне, который хранит состояние
# __setattr__ вызывается при попытке установить атрибут
# @property - это удобный механизм создания геттеров и сеттеров
# в __init__ нужно вызывать setter
# как можно сделать чтобы нельзя было поменять атрибут?
# можно сделать при помощи @property или переопределение __setattr__ просто прописывает условия


# --- Mixin (Миксины, Примеси) ---
# Миксины — это особый вид множественного наследования в Python,
# которые используются для предоставления дополнительной функциональности классам.

# --- Абстрактный класс ---
# Абстрактный класс - это класс, который не предназначен для создания объектов напрямую.
# Он является классом-шаблоном для других классов и определяет абстрактные методы,
# которые должны быть реализованы в дочерних классах.
# Абстрактный класс является абстракцией того, что должны делать его наследники,
# но не определяет, как именно это должно быть сделано
# abc (аббревиатура от Abstract Base Classes) from abc import ABC, abstractmethod
# и вешаем декоратор @abstractmethod на pass функции
# from abc import ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# Класс, который наследует абстрактный класс, должен реализовать все его абстрактные методы, иначе он не будет создан.


# Абстрактный метод - это метод, который объявлен в абстрактном классе, но не имеет реализации.
# Он служит как бы шаблоном для метода, который должен быть реализован в подклассах.

# --- dataclass Python 3.7 ---
# Модуль dataclasses предоставляет декоратор dataclass,
# который позволяет создавать data-классы - подобные позволяют значительно сократить шаблонный код классов
# Dataclass — это функционал, который позволяет легко создавать классы,
# основным предназначением которых является хранение данных. Вот почему их называют классы данных.
# Dataclass предоставляют удобный способ создания классов,
# которые могут быть использованы для хранения и обработки данных.

# Основная идея dataclass заключается в том, что они автоматически генерируют методы для инициализации,
# сравнения и преобразования в строку. Это позволяет значительно упростить код и сделать его более читаемым.
# from dataclasses import dataclass
# @dataclass
# class Customer:
#     name: str
#     balance: int

# --- @classmethod    @staticmethod ---
# 1) LEGB - правило продолжает действовать для простых имен переменных и их поиска
# 2) для self атрибутов поиск идет сначала в объекте, потом в классе, затем у предков OCP(object-class-parent).
# То есть через селф можно достучаться как к обычным методам/атрибутам, так и к классовым, статичным
# 3) если через self пытаться поменять неизменяемый атрибут (строка) класса, то будет создана локальная копия,
# ее не увидят другие объекты класса
# 4) если менять через self изменямый атрибут класса (список), то он изменится для всех объектов класса
# 5) cls - это ссылка на класс (не объект!), питон передает его под капотом. cls = Class
# 6) @classmethod используется для работы с атрибутами класса и с другими методами класса.
# Часто используется для конструирования готовых объектов
# 7) @staticmethod не получает ссылок под капотом, это просто функция связанная контекстом с классом.
# Используется редко и часто завуалированно
# 8) если есть метод где self, cls передаются но нигде не используются это @staticmethod

# --- Dunder methods (Double Underscores) Магические методы ---

# Магические методы - dunder методы, методы которые начинаются и заканчиваются __
# для самописных классов нужно переопеделить магические методы для нужного поведения и действий
# __init__ по умолчанию не ждет аргументов
# __repr__ - для програмистов, возвращает строку, по которой видно (и можно воссоздать) состояние обьекта
# __str__ - для людей, возвращает строку
# если не реализован репр и стр, то будет возвращать адрес в памяти
# __eq__ по умолчанию сравнивает адрес в памяти, в реализации лучше сразу проверить тип
# если определяете метод __eq__ то теряется возможность нахождение hash()
# если методы сравнения не реализованы то падает ошибка
# contains для реализации проверки IN
# bool для самодеельных обьектов всегда вернет True, для изменения поведения нужно написать __bool__
# len вернет ошибку если не переопределить метод __len__
# чтобы обьект стал вызываемым (callable) нужно реализовать __call__, иначе ошибка
# __iter__ возвращает обьект итератор, тот кто реализует итер = Итерабл
# __iter__ = должен вернуть обьект который умеет делать __next__
# __next__ должен вернуть следующий обьект из контейнера, кто его реализует = Итератор, for работает до StorIteration
# Итератор = обьект в нём есть данные и он может по вызову обьекта __next__ данные выдавать
# __getitem__ нужен для функционала [] (аналог списка и словаря)
# __setitem__ для присвоения через [], если не реализовать = ошибка
# если в обьекте не реализован __iter__ то для цикла фор будет использован __getitem__ там ожидается падение IndexError

# Авторы книг: Марк Лутц, Дасти Филлипс, Дэвид Бизли, Кент Бек, Лучано Рамальо
# END --- OOP ---

# -----  S.O.L.I.D принципы -----

# 1) ПРИНЦИП ЕДИНСТВЕННОЙ ОТВЕТСТВЕННОСТИ (Single Responsibility Principle)
# Требует того, чтобы один класс выполнял только одну работу.
# Таким образом, если у класса есть более одной работы, он становится зависимым.
# Изменение поведения одной работы класса приводит к изменению в другой
# «У класса должна быть лишь одна причина для изменения»


# 2) ПРИНЦИП ОТКРЫТОСТИ/ЗАКРЫТОСТИ (Open-Closed Principle)
# Программные сущности (классы, модули, функции) должны быть открыты для расширения, но не модификации.
# Программные сущности (классы, модули, функции) должны быть открыты для расширения, но закрыты для изменений.


# 3) ПРИНЦИП ПОДСТАНОВКИ ЛИСКОВ (Liskov Substitution Principle)
# Главная идея, стоящая за Liskov Substitution Principle в том, что для любого класса клиент
# должен иметь возможность использовать любой подкласс базового класса, не замечая разницы между ними,
# и следовательно, без каких-либо изменений поведения программы при выполнении. Это означает,
# что клиент полностью изолирован и не подозревает об изменениях в иерархии классов

# Проще говоря, это значит, что подкласс, дочерний класс должны соответствовать их родительскому классу или супер классу.

# «Объекты в программе должны быть заменяемы экземплярами их подтипов без ущерба корректности работы программы»


# 4) ПРИНЦИП РАЗДЕЛЕНИЯ ИНТЕРФЕЙСОВ (Interface Segregation Principle)
# Создавайте тонкие интерфейсы, которые ориентированы на клиента. Клиенты не должны зависеть от интерфейсов,
# которые они не используют. Этот принцип устраняет недостатки реализации больших интерфейсов.

# Принцип разделения интерфейсов гласит, что «Ни один клиент не должен зависеть от методов, которые он не использует».

# Принцип разделения интерфейсов предполагает создание небольших интерфейсов, известных как «ролевые интерфейсы»,
# вместо большого интерфейса, состоящего из нескольких методов. Разделяя методы по ролям на более мелкие интерфейсы
# клиенты будут зависеть только от методов, которые имеют к ним отношение.


# 5) ПРИНЦИП ИНВЕРСИИ ЗАВИСИМОСТЕЙ (Dependecy Inversion Principle)
# Зависимость должна быть от абстракций, а не от конкретики. Модули верхних уровней не должны зависеть
# от модулей нижних уровней. Классы и верхних, и нижних уровней должны зависеть от одних и тех же абстракций.
# Абстракции не должны зависеть от деталей. Детали должны зависеть от абстракций.

# Принцип инверсии зависимостей гласит:
# Модуль высокого уровня не должен зависеть от модулей низкого уровня. И то, и другое должно зависеть от абстракций.
# Абстракции не должны зависеть от деталей реализации. Детали реализации должны зависеть от абстракций.

# Если ваш код уже реализует принципы открытости/закрытости и подстановки Лисков,
# он уже будет неявно согласован с принципом инверсии зависимостей


#  ----- ИТОГ S.O.L.I.D -----
# 1) ПРИНЦИП ЕДИНСТВЕННОЙ ОТВЕТСТВЕННОСТИ:
# 1) У класса должна быть всего одна причина для изменения.
# 1) Один класс выполнял только одну работу.


# 2) ПРИНЦИП ОТКРЫТОСТИ/ЗАКРЫТОСТИ:
# 2) Сущности программы (классы, модули, функции и т.п.) должны быть открыты для расширения, но закрыты для изменений.


# 3) ПРИНЦИП ПОДСТАНОВКИ БАРБАРЫ ЛИСКОВ:
# 3) подклассы не должны противоречить надклассам
# 3) функции, которые используют базовый тип, должны иметь возможность использовать подтипы базового типа, не зная об этом.

# 3) Объекты в программе должны быть заменяемы экземплярами их подтипов без ущерба корректности работы программы.
# 3) Проще говоря, это значит, что подкласс, дочерний класс должны соответствовать их родительскому классу или супер классу


# 4) ПРИНЦИП РАЗДЕЛЕНИЯ ИНТЕРФЕЙСОВ:
# 4) Ни один клиент не должен зависеть от методов, которые он не использует.
# 4) слишком «толстые» интерфейсы необходимо разделять на более маленькие и специфические
# 4) «Программные сущности не должны зависеть от методов, которые они не используют»

# 4) «Много интерфейсов, специально предназначенных для клиентов, лучше чем один интерфейс общего назначения»


# 5) ПРИНЦИП ИНВЕРСИИ ЗАВИСИМОСТЕЙ:
# 5) Модуль высокого уровня не должен зависеть от модулей низкого уровня. И то, и другое должно зависеть от абстракций.
# 5) Абстракции не должны зависеть от деталей реализации. Детали реализации должны зависеть от абстракций.

# 5) «Зависимость на Абстракциях. Нет зависимостри на что-то конкретное»


# Абстракция — основной способ борьбы со сложностью в программировании. Она позволяет уйти от деталей реализации
# и сосредоточиться на главном. Хороший пример абстракции — функция сортировки списка.
# Не важно, как она устроена, важно, что она делает то, что нам нужно.



