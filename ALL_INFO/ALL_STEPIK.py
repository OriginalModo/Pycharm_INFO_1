"""

 Самое Важное!!!
 Всегда ДУМАТЬ! перед тем, как что-либо сделать, необходимо всё тщательно обдумать

 Радоваться Жизни  Радоваться разным мелочам

 Ценить:         Ценить то что есть и стремиться к лучшему, Ценить сегодняшний день и брать МАКСИМУМ
 Быть проще:     Ко всему относиться Проще и Спокойнее без Волнения
 Слушать Других: Прислушиваться к мнению других людей они могут быть правы  И делать выводы
 Время:          Тайм-менеджмент   Грамотное распределение времени, Контроль Времени, Правильно раставлять Приоритеты
 Уверенность:    Быть уверенным в себе НО Оценивать свои силы!
 Развития:       Развиваться, Учиться, учиться и ещё раз - учиться, Саморазвитие
 Не Надеяться:   Надеяться только на себя
 Контроль:       Быть менее Эмоциональным, Совладать с Эмоциями, Контролировать свои эмоции в любой ситуации
 Внимательность: Быть Внимательным
 Спокойствие:    Быть Спокойнее, Перестать Нервничать , Быть Расслабленным, Не Злиться на себя и на других
 Режим:          Правильный Сон, Пить Воду
 Зарядка:        Бег, Тренировки, Стойка на Голове
 Тельце в тепле: НЕ переохлаждаться

 Молчание золото:  Лучше промолчать, чем сказать и потом жалеть о том, что сказал
 Соломон:          Все пройдёт, и это тоже пройдёт
 Вообще это замечательный подход: осознать, что проблема не такая уж и проблема, и вполне решаема.
 Кто ищет-тот всегда найдет!
 Искать Другие способы
 Не спеши, а то успеешь...   Успеешь, но не туда куда хотел...
 Подумай, нужно ли тебе ЭТО и для Чего
 Надо принимать вещи такими, как они есть, и пользоваться ими с наибольшей для себя выгодой.
 Если научиться принимать вещи как они есть, страдание исчезнет.
________________________________________________________________________________________________________________________

 --- Задачи с Собеседования ---                                       тех. собеседования 1):  32/4
                                                                      тех. собеседования 2):  23/0
________________________________________________________________________________________________________________________

 # Задача на логику    Сбер

 # У Вас есть два шнура (фитиля). Каждый шнур, подожженный с конца, полностью сгорает дотла ровно за один час,
 # но при этом горит с неравномерной скоростью. Как при помощи этих шнуров и зажигалки отмерить время в 45 минут?

 # Ответ
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
________________________________________________________________________________________________________________________

 #  X5 Задача что выведет Данный код?    val - являются разными переменными.

 def a():
     val = 1
     def b():
         val = 10
     b()
     print(val)

 a()  # -> 1


 # Ответ X5 Задача что выведет Данный код    val - являются разными переменными.    В этом случае замыкания **НЕТ**

 def a():
     val = 1  # В функции a создаем переменную val со значением 1

     def b():
         val = 10  # Внутри функции b создаем новую локальную переменную val со значением 10

     b()  # Вызываем функцию b, которая устанавливает свою локальную переменную val в 10
     print(val)  # Здесь мы печатаем значение val из функции a, которое равно 1

 a()  # -> 1

 ### Краткое объяснение:

 - Переменная `val` в функции `a()` имеет область видимости в этой функции.
 - В функции `b()` создается новая локальная переменная `val`, которая не влияет на `val` в `a()`.
 - При вызове `b()` выполняется код внутри нее, но `val` в `a()` остается равным `1`.
 - Следовательно, когда выполняется `print(val)`, выводится `1`.

 Замыкание происходит, когда внутренняя функция ссылается на переменную из внешней функции, и эта внешняя функция
 продолжает существовать даже после ее завершения. В данном случае переменная `val` в `b()`
 НЕ ссылается на `val` из `a()`, поэтому замыкания не происходит. Местный `val = 10` в функции `b()`
 просто создает новую локальную переменную, не имея доступа к `val` в функции `a()`
________________________________________________________________________________________________________________________

 # Будет последнее значение выводить 10 раз    ПОСМОТРИ ВНИМАТЕЛЬНО КОД  Обрати внимание на    x   Задача Мебель Детали

 # ВСЕ лямбда-функции ссылаются на одну и ту же переменную a, которая в конце цикла равна 9.
 fun = [lambda x: a for a in range(10)]
 for f in fun:
     print(f(20), end=' ')  # -> 9 9 9 9 9 9 9 9 9 9


 # Используем аргумент по умолчанию a=a . Это позволяет каждой функции сохранить текущее значение a на момент создания.
 fun = [lambda x, a=a: a for a in range(10)]
 for f in fun:
     print(f(20), end=' ')  # -> 0 1 2 3 4 5 6 7 8 9
________________________________________________________________________________________________________________________

 Задача Заказчик Открытые Решения   Посмотри все варианты! Особенно 2 последних!!!

 * Уровень 1 *
 1.  Распарсить CSV-строку в список словарей, ключи для которых взять из заголовка
     (built-in СТРОКОВЫМИ средствами)
 2.  Нормализовать данные в словарях в соответствии с правилами
     Правила определить, исходя из наблюдаемых в данных отклонениях


 RAW_DATA = '''phone, fullname, some_amount, rating_position
 +7 993 0965431, Абдуллаев Рамиль Ахмед оглы, 5432, 5
 89615421187, Васильев Михаил Борисович, 1577.93, 3
 +7 (905) 127-00-01, Филипс    Тревор, 7 311.63, 1
 8-987-654-3210, Иванова    Мария Сергеевна, 104, 4
 8931 077 2267, Петрова-Васильева     Светлана   Александровна, 35 567.92, 7
 955-43-88-102, Крестовоздвиженский    Войцишек  Станислав   Август, 191, 6
 7911-631-07-80,    Романов   Борис Анатольевич, 13.2, 2'''



 1)  # Первый Вариант

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
 # [{'phone': '+7 993 0965431', 'fullname': 'Абдуллаев Рамиль Ахмед оглы', 'some_amount': '5432', 'rating_position': '5'}



 2)  # Второй Вариант

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



 3)  # Третий Вариант  применение чистых функций, функций высшего порядка синтаксического сахара

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



 4)  # Четвертый Вариант  применение чистых функций, функций высшего порядка синтаксического сахара
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
________________________________________________________________________________________________________________________

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
 @decor(strict=True)             # Тут   strict=True                     @decor(strict=False)
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
________________________________________________________________________________________________________________________

 Сибур Задача

 Интересный Пример с обновлением словаря   ПОСМОТРИ ОТВЕТЫ и почему         Словарь в любом случае обновляется!!! <----
 Таким образом, словарь обновляется каждый раз, когда вызывается функция `test2`, независимо от того,
 существует ли ключ `test` или нет.

 # Если ключ ЕСТЬ                                # Если ключа НЕТ
 dct = {'test': 321}                             dct = {'test': 321}

 def test2():                                    def test2():
     dct.update({'test': 444})                       dct.update({'test': 444})
     return 123                                      return 123

 print(dct.get('test', test2()))   # -> 444      print(dct.get('TTTTT', test2()))  # -> 123
 print(dct)               # -> {'test': 444}     print(dct)               # -> {'test': 444}
________________________________________________________________________________________________________________________

 # Замерить сколько раз вызывается функция      ivi  Иви


 from dataclasses import dataclass, field
 from typing import Callable
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
________________________________________________________________________________________________________________________

 Есть список                                            Грузовая компания
 words = ['aba', 'bac', 'abb', 'bab', 'bba',
 'aab', 'abca']
 Анаграммы - это такие пары слов, в которых одинаковые буквы и одинаковое количество букв, расположенных в разном
 порядке. В приведенном примере группы анаграмм: (aba, aab), (abb, bab, bba). Напишите такой код, который выведет
 на консоль первую анаграмму из каждой группы.


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
________________________________________________________________________________________________________________________

 Реализовать функцию, которая будет преобразовывать строку (с целочисленным числом)
 в число, не используя стандартные методы преобразования python.


 # Мой ответ                                       # Еще один вариант Мой
 def to_digit(val):                                def to_digit(val):
     res = {}                                          res = dict(zip(map(str, range(10)), range(10)))
     res[val] = int(val)                               return res.get(val)
     return res[val]

 def string_to_int(value: str) -> int:            def string_to_int(value: str) -> int:
     res = 0                                          res = 0
     n = len(value) - 1                               n = len(value) - 1
     for i in value:                                  for i in value:
         res += to_digit(i) * 10 ** n                     res += to_digit(i) * 10 ** n
         n -= 1                                           n -= 1
     return res                                       return res

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
________________________________________________________________________________________________________________________

 Создайте декоратор retry, который повторяет выполнение функции заданное количество раз, если она завершилась с ошибкой.
 Если все попытки неудачны, декоратор должен вернуть сообщение об ошибке или выбросить исключение.   Сбер

 Условия:

 Декоратор принимает два аргумента:
 1. количество попыток retries;
 2. время ожидания между попытками delay (в секундах).

 Декорируемая функция может принимать любые аргументы и возвращать результат или выбрасывать исключение.

 Декоратор должен перехватывать исключения и повторять выполнение функции, если она завершилась с ошибкой.


 @retry(retries=5, delay=2)
 def unstable_function():
     if time.time() % 2 > 1.5:
         raise ValueError("Случайная ошибка")
     return "Успех!"
 print(unstable_function())
 --------------------------
 Ожидаемый вывод:

 Попытка 1 не удалась: Случайная ошибка. Повтор через 2 секунд.
 Попытка 2 не удалась: Случайная ошибка. Повтор через 2 секунд.
 Попытка 3 не удалась: Случайная ошибка. Повтор через 2 секунд.
 Попытка 4 не удалась: Случайная ошибка. Повтор через 2 секунд.
 Функция не отработала корректно


 # Ответ Мой
 from functools import wraps
 import time

 def retry(retries, delay):  # Важно чтобы параметры назывались так же как и в параметрах декорируемой функции   <-----
     def decor(func):        # При передаче их как именованные параметры      ИЛИ TypeError                      <-----
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
 def unstable_function():    # При передаче их как именованные параметры  ИЛИ TypeError                          <-----
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
________________________________________________________________________________________________________________________

 # Задача На ЭК в словаре  Сколько будет объектов в Словаре data?   ЭК - может быть ключом в словаре!   Газпром
 # Интересно работает даже с pass или ...  Хотя функцию создали внутри      ЭК - может быть в set()


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
________________________________________________________________________________________________________________________

 # Задача На Объекты в памяти  Просто посмотреть   Важно посмотри когда идет присвоение a=b
 a = []                                 a = 1
 b = []                                 b = 1

 print(id(a) == id(b))  # -> False      print(id(a) == id(b))  # -> True
 print(a == b)          # -> True       print(a == b)          # -> True
 print(a is b)          # -> False      print(a is b)          # -> True

 b = a                                  b = a                                                    <-----   Присвоение

 print(id(a) == id(b))  # -> True       print(id(a) == id(b))  # -> True
 print(a == b)          # -> True       print(a == b)          # -> True
 print(a is b)          # -> True       print(a is b)          # -> True
________________________________________________________________________________________________________________________

 # Yandex-Маркет Задача Отсортировать по двум параметрам. Как я сделал я не знаю

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

 # Интересный вариат                                           # Тоже самое
 def my_func(x):                                               def my_func(x):
     return -int(x.split('_')[0]), x.split('_')[1]                 a, b = x.split('_')
                                                                   return -int(a), b

 def get_sorted(lst):
     return sorted(lst, key=my_func)


 print(get_sorted(xs))  # -> ['3_d.txt', '2_b.txt', '1_a.txt', '1_c.txt', '1_e.txt']
 print(get_sorted(xs))  # -> ['3_d.txt', '2_b.txt', '1_a.txt', '1_c.txt', '1_e.txt']
________________________________________________________________________________________________________________________

 # Создать функцию которая убирает дубликаты           Задача с Live Coding Собеседования

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

 # Two Sum Задача с собеседования  YADRO

 lst = [2, 7, 9, 10, 11]
 target = 9


 # Хороший вариант                                   # Тоже самое с МОРЖОМ
 def twoSum(nums, target):                           def twoSum(nums, target):
     res = []                                            res = []
     for i in range(len(nums)-1):                        for i in range(len(nums)-1):
         if nums[i] + nums[i+1] == target:                   if sum(((a:=nums[i]), (b:=nums[i+1]))) == target:
             res.append(nums.index(nums[i]))                     res.append(nums.index(a))
             res.append(nums.index(nums[i+1]))                   res.append(nums.index(b))
     return res                                          return res

 print(twoSum(lst, target))  # -> [0, 1]


 # Пример 1
 from itertools import pairwise
                                                                  # Тоже самое но ВЫВОД  [0, 1]
 def twoSum(nums, target):                                        def twoSum(nums, target):
     res = []                                                         res = []
     for i, v in enumerate(pairwise(nums)):                           for i, j in itertools.pairwise(nums):
         if sum([v[0], v[1]]) == target:                                  if i+j == target:
             res.append([nums.index(v[0]), nums.index(v[1])])                 res.append((nums.index(i), nums.index(j)))
     return res                                                       return [j for i in res for j in i]

 print(twoSum(lst, target))  # -> [[0, 1]]                        print(twoSum(lst, target))  # -> [0, 1]


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

 # Релизация своего класса имитируещего СЛОВАРЬ    ML
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
________________________________________________________________________________________________________________________

 Задачи с собеседования  X5


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

 print(flatten([1, 2, [2, 3, [4, 4]]]))                  # -> [1, 2, 2, 3, 4, 4]
 print(flatten([1, 2, [2, 3, [4, 4]], [[[[[5, 5]]]]]]))  # -> [1, 2, 2, 3, 4, 4, 5, 5]


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

 print(flatten([1, 2, [2, 3, [4, 4]]]))                  # -> [1, 2, 2, 3, 4, 4]
 print(flatten([1, 2, [2, 3, [4, 4]], [[[[[5, 5]]]]]]))  # -> [1, 2, 2, 3, 4, 4, 5, 5]

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

 print(flatten([1, 2, [2, 3, [4, 4]]]))                  # -> [1, 2, 2, 3, 4, 4]
 print(flatten([1, 2, [2, 3, [4, 4]], [[[[[5, 5]]]]]]))  # -> [1, 2, 2, 3, 4, 4, 5, 5]

 # Интересный вариант
 def flatten(*args):
     try:
         return [*map(int, [i for i in re.findall(r'[^\[\]()]', str(args)) if i not in ' ,'])]
     except:
         print('not good')

 print(flatten([1, 2, [2, 3, [4, 4]]]))                  # -> [1, 2, 2, 3, 4, 4]
 print(flatten([1, 2, [2, 3, [4, 4]], [[[[[5, 5]]]]]]))  # -> [1, 2, 2, 3, 4, 4, 5, 5]


 # Так тоже работает
 def flatten(*args):
     res = re.sub(r'\[|\]', '', str(args))  # (1, 2, 2, 3, 4, 4,)    # Тут будет вот такая строка с запятой в конце
     return eval(res)

 print(flatten([1, 2, [2, 3, [4, 4]]]))                  # -> (1, 2, 2, 3, 4, 4)
 print(flatten([1, 2, [2, 3, [4, 4]], [[[[[5, 5]]]]]]))  # -> (1, 2, 2, 3, 4, 4, 5, 5)
________________________________________________________________________________________________________________________

 Задача максимальная последовательность чисел  СБЕР

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
________________________________________________________________________________________________________________________

 # Задача "Правильная скобочная последовательность"    Valid Braces  Codewars    Мир Танков/World of Tanks

 # 2 Раза повторялась задача Попалась и на другом собеседовании!!!

 # Write a function called test() that takes a string of parentheses, and determines if the order of the
 # parentheses is valid. The function should return true if the string is valid, and false if it's invalid.
 # "()"              =>  true
 # ")(()))"          =>  false
 # "("               =>  false
 # "(())((()())())"  =>  true
 # "())("            =>  false



 # Первый Вариант            Квадратичная сложность O(n^2)       Вариант требует создания новых строк и перебора их.
 def is_correct_brackets(text):
     while '()' in text or '[]' in text or '{}' in text:
         text = text.replace('()', '')
         text = text.replace('[]', '')
         text = text.replace('{}', '')
         # text = text.replace('()', '').replace('[]', '').replace('{}', '')   # Тоже самое вместо 3-х строчек

     # Возвращаем True, если text с пустой строкой
     return not text

 print(is_correct_brackets('(((())))'))          # True
 print(is_correct_brackets('(((())'))            # False
 print(is_correct_brackets('())))'))             # False
 print(is_correct_brackets('((((){}[]{}[])))'))  # True
 print(is_correct_brackets('(){}[]{}[])))'))     # False
 print(is_correct_brackets('(){}[]{}[]'))        # True



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

 print(validBraces('(((())))'))          # True
 print(validBraces('(((())'))            # False
 print(validBraces('())))'))             # False
 print(validBraces('((((){}[]{}[])))'))  # True
 print(validBraces('(){}[]{}[])))'))     # False
 print(validBraces('(){}[]{}[]'))        # True



 # Третий Вариант            Квадратичная сложность O(n^2)       Вариант требует создания новых строк и перебора их.
 def validBraces(string):
     for _ in string:
         string = string.replace('{}', '').replace('()', '').replace('[]', '')
     return not string

 print(validBraces('(((())))'))          # True
 print(validBraces('(((())'))            # False
 print(validBraces('())))'))             # False
 print(validBraces('((((){}[]{}[])))'))  # True
 print(validBraces('(){}[]{}[])))'))     # False
 print(validBraces('(){}[]{}[]'))        # True


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

 # YANDEX  (Второй ЗАХОД)  2 ЗАДАЧИ
 # Максимальное количество последовательных единиц II (с возможностью переворота одного нуля)  Max Consecutive Ones II


 # ЗАДАЧА 1


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



 # ЗАДАЧА 2
 # БИНАРНОЕ ДЕРЕВО С LeetCode




________________________________________________________________________________________________________________________

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
________________________________________________________________________________________________________________________

 # 2 Задачи    компания ГК “МТ-Интеграция”

 # Задачи  OpenStack   ПОСМОТРИ ТУТ 2 ЗАДАЧИ!!!    АНАГРАММА  И  ФИЛЬТРАЦИИ СПИСКА СЕРВИСОВ    ГК “МТ-Интеграция”.


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
________________________________________________________________________________________________________________________

 # 4 Задачи    компания Медиалогия


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
________________________________________________________________________________________________________________________

 # VERME Биржа Смен   ИЧАР С ПРОСТЫМИ ЗАДАЧКАМИ  3 Задачи

 # Какие значения вернет функция print?
 a = [1,2,3]
 b = a
 c = [1,2,3]
 print(a == b)  # -> True
 print(a == c)  # -> True
 print(a is b)  # -> True
 print(a is c)  # -> False

 # Простые задания

 # Задача №1
 # Напишите программу для объединения двух разных словарей. При объединении, если вы
 # найдете одинаковые ключи, вы должны сложить значения этих ключей. Выведите новый словарь
 # Задание:  РЕЗУЛЬТАТ ДОЛЖЕН БЫТЬ ВОТ ТАКОЙ:  {'a': 250, 'b': 200, 'c': 200, 'd': 300}

 d1 = {'a': 50, 'b': 100, 'c':200}
 d2 = {'a': 200, 'b': 100, 'd':300}

 # Способ 1
 res = d1.copy()

 for k, v in d2.items():
     if k in res:
         res[k] += v
     else:
         res[k] = v

 print(res)  # -> {'a': 250, 'b': 200, 'c': 200, 'd': 300}


 # Способ 2   ОЧЕНЬ ИНЕТЕРЕСНЫЙ ПРИМЕР!!!  <-----     (с использованием Counter)
 from collections import Counter

 res = Counter(d1)+Counter(d2)
 print(res)        # -> Counter({'d': 300, 'a': 250, 'b': 200, 'c': 200})
 print(dict(res))  # -> {'a': 250, 'b': 200, 'c': 200, 'd': 300}

 # Сортировка по ключам
 res_sort = Counter(d1) + Counter(d2)
 print(dict(sorted(res_sort.items()))) # -> {'a': 250, 'b': 200, 'c': 200, 'd': 300}

 # Сортировка по значениям (по возрастанию)
 sorted_by_value = dict(sorted(res_sort.items(), key=lambda item: item[1]))
 print(sorted_by_value)                # -> {'b': 200, 'c': 200, 'a': 250, 'd': 300}


 # Способ 3 (с использованием dict comprehension)  ПОРЯДОК БУДЕТ ВСЕГДА РАЗНЫЙ!
 all_keys = set(d1) | set(d2)
 res = {k: d1.get(k, 0) + d2.get(k, 0) for k in all_keys}
 print(res)  # -> {'b': 200, 'd': 300, 'c': 200, 'a': 250}


 # Способ 4 (с использованием defaultdict)
 from collections import defaultdict
 res = defaultdict(int)
 for d in (d1, d2):          # d БУДЕТ СЛОВАРЕМ!!!  d - это переменная, которая поочерёдно становится d1, затем d2
     for k, v in d.items():
         res[k] += v
 print(dict(res))  # -> {'a': 250, 'b': 200, 'c': 200, 'd': 300}


 # Способ 5: Через dict.get() с циклом
 res = {}
 for d in (d1, d2):          # d БУДЕТ СЛОВАРЕМ!!!  d - это переменная, которая поочерёдно становится d1, затем d2
     for k, v in d.items():
         res[k] = res.get(k, 0) + v
 print(res)  # -> {'a': 250, 'b': 200, 'c': 200, 'd': 300}



 # Задача №2
 # Есть произвольный массив чисел, необходимо вывести произведение всех значений, то есть умножить первое значение
 # на второе, затем полученный результат на третье значение и тд
 # Задание:

 from functools import reduce
 import operator, math

 # Способ 1  Использование цикла for
 def mult(lst):
     result = 1
     for num in lst:
         result *= num
     return result

 # Способ 2  Использование встроенной функции reduce и operator.mul
 def mult(lst):
     return reduce(operator.mul, lst, 1)      # ((((1*1)*2)*3)*4)*5) = 120

 # Способ 3  reduce и lambda
 def mult(lst):
     return reduce(lambda x, y: x*y, lst, 1)  # ((((1*1)*2)*3)*4)*5) = 120

 # Способ 4 Использование math.prod (Python 3.8+)
 def mult(lst):
     return math.prod(lst)                    # 1*2*3*4*5 = 120

 a = [1, 2, 3, 4, 5]
 print(mult(a))  # -> 120
________________________________________________________________________________________________________________________

 # ЗАДАЧА ИЗ ПЛОХОГО СОБЕСА  СУММА В СЕКУНДАХ В ЛОГАХ
 from datetime import datetime

 res = [
     '2022-05-20Z logs',
     '2022-05-21Z logs',
     '2022-05-22Z logs',
 ]

 # Извлекаем и парсим даты
 dates = [datetime.fromisoformat(item[:10]) for item in res]
 print(dates)
 # [datetime.datetime(2022, 5, 20, 0, 0), datetime.datetime(2022, 5, 21, 0, 0), datetime.datetime(2022, 5, 22, 0, 0)]

 # Сортируем даты на случай, если они не в хронологическом порядке
 sorted_dates = sorted(dates)

 # Вычисляем разницу между всеми последовательными датами
 total_seconds = 0.0
 for i in range(1, len(sorted_dates)):
     delta = sorted_dates[i] - sorted_dates[i-1]
     total_seconds += delta.total_seconds()

 # Вычисляем общую разницу между первой и последней датой
 full_delta = sorted_dates[-1] - sorted_dates[0]
 full_seconds = full_delta.total_seconds()

 print(f"\nОбщая сумма всех интервалов: {total_seconds} секунд")
 # Общая сумма всех интервалов: 172800.0 секунд

 print(f"Прямая разница от первой до последней даты: {full_seconds} секунд")
 # Прямая разница от первой до последней даты: 172800.0 секунд

 print(f"Это соответствует {full_seconds/86400:.1f} дням")
 # Это соответствует 2.0 дням
________________________________________________________________________________________________________________________

 # компания вроде DOG  2 задачи  FizzBuzz  и Code review  Django

 # Задание 1) FizzBuzz  компания вроде DOG

 n => [1...n]
 i % 3 => Fizz
 i % 5 => Buzz
 i % 3,5 => FizzBuzz


 # i % 15 == 0 действительно эквивалентно i % 3 == 0 and i % 5 == 0


 # Моя версия садо-мазо
 def fizzbuzz(n: int) -> None:
     for i in range(True, n + True):
         if i % 3 == 0 and i % 5 == 0:  # Тоже самое  i % 15 == 0
             # __import__('sys').stdout.write(f'FizzBuzz ')
             print('FizzBuzz', end=' ')
         elif i % 3 == 0:
             # __import__('sys').stdout.write(f'Fizz ')
             print('Fizz', end=' ')
         elif i % 5 == 0:
             # __import__('sys').stdout.write(f'Buzz ')
             print('Buzz', end=' ')
         else:
             # __import__('sys').stdout.write(f'{i} ')
             print(str(i), end=' ')

 fizzbuzz(15)
 # 1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz
 print()

 # Короткая версия (для любителей однострочников):
 fizzbuzz = lambda n: ['FizzBuzz' if i % 15 == 0 else 'Fizz' if i % 3 == 0 else 'Buzz' if i % 5 == 0 else str(i) for i in range(1, n + 1)]
 # i % 15 == 0 действительно эквивалентно i % 3 == 0 and i % 5 == 0
 fizzbuzz = lambda n: ['FizzBuzz' if i % 3 == 0 and i % 5 == 0 else 'Fizz' if i % 3 == 0 else 'Buzz' if i % 5 == 0 else str(i) for i in range(1, n + 1)]
 print(*fizzbuzz(15))
 # 1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz



 # Задание 2 Code review  Django  ПРОСТО ПОСМОТРЕТЬ

 Вот основные проблемы в этом коде:

 Уязвимость безопасности:
  - Хеш кода SHA256 не использует соль, что делает его уязвимым к атакам по радужным таблицам.
  - Соль - случайные данные, добавляемые перед хешированием. Соль в криптографии

 Проблемы с кодом:
  - Синтаксическая ошибка в методе isActive() (лишнее двоеточие в условии)
  - Неправильное сравнение времени в isActive() (используется tz_created() без определения)

 Логирование чувствительных данных:
  - Вывод кода и его хеша в консоль (print)

 Проблемы с производительностью:
  - Нет ограничения на количество запросов кода для одного IP/номера

 Нет обработки ошибок:
  - Нет обработки ошибок при отправке SMS

 Хрупкость:
  - Жестко закодированный отправитель SMS ('hellodoc')

 Потенциальная race condition:
 - Между проверкой can_send_sms и сохранением кода

 Нет очистки:
  - Старых/неактивных кодов в базе данных

 # модель с одноразовыми кодами
 class PhoneAuth(Base):
     phone = models.TextField()  # Проблема: Лучше использовать CharField с max_length
     code = models.TextField()   # Проблема: Хранение хеша без соли, уязвимость безопасности
     ip_address = models.TextField(null=True)  # Проблема: Лучше GenericIPAddressField
     is_active = models.BooleanField(default=True)

     objects: Manager()  # Проблема: Отсутствует импорт Manager

     @staticmethod
     def get_phone_auth_for_number(phone, code) -> PhoneAuth:
         return PhoneAuth.objects.filter(phone=phone, code=code, is_active=True).first()

     @staticmethod
     def get_last_auth_for_number(phone, ip):
         date = datetime.now() - timedelta(hours=constants.IP_ADDRESS_BAN_HOURS)
         result = PhoneAuth.objects.filter(phone=phone, ip_address=ip).order_by('-created').first()
         count_from_ip = PhoneAuth.objects.filter(ip_address=ip, created__gte=date).count()

         return result, count_from_ip

     @staticmethod
     def delete_by_phone(phone):
         PhoneAuth.objects.filter(phone=phone, is_active=True).update(is_active=False)

     def deactivate(self):
         self.is_active = False
         self.save()

     def isActive(self):
         return to_timestamp(datetime.utcnow()) - to_timestamp(
             self.tz_created()) <= constants.PHONE_CONF_CODE_LIFE_SECONDS and self.is_active:
             # Проблема 1: Лишнее двоеточие в конце
             # Проблема 2: Метод tz_created() не определен
             # Проблема 3: Нет обработки случая, когда tz_created() = None

 # апи отправки кода по смс
 class Phone(views.APIView):
     authentication_classes = (BaseAppAuthentication, UserNotRequiredAuthentication)

     class PhoneRegisterParams(serializers.Serializer):
         phone = serializers.CharField(max_length=12, min_length=10)

         def validate_phone(self, phone):
             success, result = validate_phone(phone)
             if success:
                 return result
             else:
                 raise serializers.ValidationError(result)

     def post(self, request):
         data = Phone.PhoneRegisterParams(data=request.data)

         if not data.is_valid():
             return response_error(BadRequestParams.init_dev_err(data.errors))

         phone = data.validated_data['phone']
         print(phone)  # Проблема: Логирование конфиденциальных данных
         ip = get_client_ip(request)
         err = can_send_sms(phone, ip)
         if err:
             return response_error(err)

         code = random.randrange(MIN_VER_INT, MAX_VER_INT)
         sms_text = 'Ваш код %s' % code
         sms = SMSMessage(**dict(text=sms_text, phone=phone))
         sms.save()
         print(code)  # Проблема: Логирование кода подтверждения

         hash_code = hashlib.sha256()
         hash_code.update(unicode(code))  # Проблема 1: unicode() не существует в Python 3
                                         # Проблема 2: Нет соли для хеширования
         hash_code = hash_code.hexdigest()
         print(hash_code)  # Проблема: Логирование хеша кода

         PhoneAuth.delete_by_phone(phone)  # Проблема: Потенциальная race condition с can_send_sms

         phone_auth = PhoneAuth(**dict(phone=phone, code=hash_code, ip_address=ip))
         phone_auth.save()

         send_sms.delay(sms.id)

         return response(HTTP_200_OK)

 # фоновая задача отправки смс
 @shared_task
 def send_sms(object_id):
     sms = SMSMessage.get_sms(object_id)
     phone = sms.phone
     if phone:
         message = sms.text
         phone = sms.phone  # Проблема: Дублирование присваивания

         data = {
             'login': settings.SMSC_LOGIN,  # Проблема: Логин в открытом виде
             'psw': md5(settings.SMSC_PASSWORD).hexdigest(),  # Проблема: Устаревший MD5
             'charset': 'utf-8',
             'mes': message.encode('utf-8'),
             'phones': phone,
             'sender': 'hellodoc'  # Проблема: Жестко закодированное значение
         }

         url = 'https://smsc.ru/sys/send.php'
         print(data)  # Проблема: Логирование учетных данных
         if not settings.DEBUG:
             response = requests.post(url, params=data)
             sms.error = response  # Проблема: Нет обработки ошибок запроса

         sms.is_delivered = True  # Проблема: Помечаем как доставленное до фактической доставки
         sms.save()
________________________________________________________________________________________________________________________

 # компания Молочные Коровки


 - Есть три сервиса. Фронт и два бэкэнда.
 Один бэк это апишка для фронта. Второй бэк это CPU-bound сервис (считает один запрос 5 минут).
 Как правильно связать все три сервиса (включая фронт), чтобы получить лучший флоу для клиента, который нажимает
 кнопку "посчитать" и ждёт результат.

 Такую архитектуру используют многие SaaS-платформы для тяжелых вычислений (например, рендеринг видео, ML-предсказания).
 Отражает best practices для работы с долгими CPU-bound задачами в веб-приложениях

 [Frontend]
   │ POST /api/calculate
   ↓
 [API] → [Queue (RabbitMQ/Kafka)] → [CPU Worker]
   │ 202 Accepted                     │
   │ ↑                                ↓
   └────────────────────────────── [DB/Redis]
                                       │
 [Frontend] ← polling/WS ←─────────────┘


 1) Фронт отправляет запрос в API бэкенд
 Как:
 - POST-запрос на эндпоинт типа /api/calculate с параметрами задачи (например, { "data": "..." }).

 Зачем:
 - Клиент инициирует процесс, но не должен зависеть от времени выполнения.

 2) API бэкенд ставит задачу в очередь (RabbitMQ, Kafka, Redis Queue) и сразу возвращает фронту 202 Accepted + task_id

 Как:

 - API генерирует уникальный task_id (UUID или хеш).
 - Пишет сообщение в очередь (например, RabbitMQ/Kafka):

 json
 {
   "task_id": "123e4567-e89b-12d3-a456-426614174000",
   "data": "..."
 }

 - Возвращает фронту:

 json
 {
   "status": "accepted",
   "task_id": "123e4567-e89b-12d3-a456-426614174000",
   "check_status_url": "/api/tasks/123e4567-e89b-12d3-a456-426614174000"
 }

 Зачем:

 - Клиент получает мгновенный ответ (без ожидания 5 минут).
 - Задача гарантированно попадает в очередь (даже если CPU-сервис перегружен).

 3) CPU-bound бэкенд забирает задачу из очереди, обрабатывает (5 минут) и сохраняет результат в БД/кеш

 Как:

 - Воркер CPU-сервиса подписан на очередь (например, через channel.basic_consume в RabbitMQ).
 - Получив задачу, начинает вычисления.
 - Важно:
   - Обновляет статус в БД (например, "in_progress").
   - Сохраняет результат в хранилище (БД/Redis):

     json
     {
       "task_id": "123e4567-e89b-12d3-a456-426614174000",
       "status": "completed",
       "result": { ... },
       "timestamp": "2024-02-20T12:00:00Z"
     }

 Зачем:

 - Очередь развязывает API и CPU-сервис.
 - Результат сохраняется даже при падении фронта.


 4) Фронт периодически (через polling/WebSocket) запрашивает API бэкенд по task_id

 Polling:

 - Фронт каждые N секунд (например, 5) дергает GET /api/tasks/{task_id}.
 - API проверяет статус в БД и возвращает:

 json
 {
   "status": "in_progress", // или "completed", "failed"
   "progress": 50, // опционально
   "result": null // или результат
 }

 WebSocket:

 - Фронт открывает WS-соединение к API.
 - API подписывается на события из БД/очереди и推送лет обновления.

 Зачем:

 - Клиент видит прогресс (например, прогресс-бар).
 - Нет риска таймаутов.



 5) Когда результат готов — API бэкенд отдаёт его фронту

 Как:

 - Когда статус становится "completed", API забирает результат из БД/кеша.
 - Для polling: фронт получает его в следующем запросе.
 - Для WebSocket: API отправляет сообщение:

 json
 {
   "event": "task_completed",
   "task_id": "123e4567-e89b-12d3-a456-426614174000",
   "result": { ... }
 }

 Зачем:

 - Клиент получает результат только когда он готов.

 Почему так?

 - Не блокируем HTTP-соединения
 - CPU-bound сервис масштабируется независимо
 - Клиент видит статус обработки
________________________________________________________________________________________________________________________

 # МТС  компания    3 ЗАДАЧИ посмотреть

 # ЗАДАЧА 1
 # Присваивание d2 = d1 не создаёт новый словарь, а копирует ссылку. Изменения в d2 влияют на d1.

 d1 = {1:1, 2:2, 3:3}
 d2 = d1                             # d2 — это ссылка на d1, а не копия
 d2[1]=0                             # меняем d1 через d2
 print(d1)  # -> {1: 0, 2: 2, 3: 3}
 print(d2)  # -> {1: 0, 2: 2, 3: 3}


 # ЗАДАЧА 2
 # f1 меняет переданный список, т.к. работает с его элементами.
 # f2 не меняет исходный список, т.к. переназначает локальную переменную.

 def f1(my_list):
     my_list[0] = 123            # меняет переданный список
 def f2(my_list):
     my_list = [4, 5, 6]         # создаёт локальную переменную, не меняя исходный список
 l1 = [1, 2, 3]
 l2 = [1, 2, 3]
 f1(l1)                          # изменяет l1
 print(l1)  # -> [123, 2, 3]
 f2(l2)                          # НЕ изменяет l2
 print(l2)  # -> [1, 2, 3]


 # ЗАДАЧА 3
 # Если аргумент по умолчанию (L=[]) изменяется, он сохраняет состояние между вызовами.
 # При передаче своего списка (l) изменения применяются к нему.

 l = [1, 2, 3]
 def f(a, L=[]):
     L.append(a)                 # изменяет один и тот же список L при каждом вызове
     return L
 f(4)
 f(5)
 tmp_l = f(6)
 print(tmp_l)  # -> [4, 5, 6]
 f(7, l)                         # передаём внешний список l
 f(8, l)
 f(9, l)
 print(l)      # -> [1, 2, 3, 7, 8, 9]
________________________________________________________________________________________________________________________

 # Задачи тестовое задание 16 штук   компания СОГАЗ   (2 Задачи не хватает 12, 13)
 
 
 # ЗАДАЧА 1
 # Напишите функцию на Python без регулярок находим сумму всех чисел
 
 
 # ОТВЕТ Напишите функцию на Python без регулярок находим сумму всех чисел
 
 # Напишите функцию на Python без регулярок находим сумму всех чисел
 
 # Решение с регуляркой
 def sum_numbers_in_string(s: str) -> int:
     return sum(map(int, re.findall(r'\d+', s)))
 
 # ВАРИАНТ 1: Если нужны только положительные целые числа
 def sum_numbers_in_string(s):
     current_number = ''
     total = 0
 
     for char in s:
         if char.isdigit():
             current_number += char
         else:
             if current_number:
                 total += int(current_number)
                 current_number = ''
 
     # Добавляем последнее число, если строка заканчивается цифрой
     if current_number:
         total += int(current_number)
 
     return total
 
 # ВАРИАНТ 2: С обработкой отрицательных чисел
 def sum_numbers_in_string(s):
     current_number = ''
     total = 0
     sign = 1  # 1 для положительных, -1 для отрицательных
 
     for char in s:
         if char.isdigit():
             current_number += char
         elif char == '-' and not current_number:
             sign = -1
         else:
             if current_number:
                 total += sign * int(current_number)
                 current_number = ''
                 sign = 1
 
     if current_number:
         total += sign * int(current_number)
 
     return total
 
 # ВАРИАНТ 3: С использованием генератора и isdigit()
 def sum_numbers_in_string(s):
     total = 0
     num_str = ''
 
     for char in s + ' ':  # Добавляем пробел для обработки последнего числа
         if char.isdigit():
             num_str += char
         elif num_str:
             total += int(num_str)
             num_str = ''
 
     return total
 
 # ВАРИАНТ 4: С обработкой чисел с плавающей точкой
 def sum_numbers_in_string(s):
     total = 0.0
     num_str = ''
     has_decimal = False
 
     for char in s + ' ':  # Добавляем пробел для обработки последнего числа
         if char.isdigit():
             num_str += char
         elif char == '.' and not has_decimal and num_str:
             num_str += char
             has_decimal = True
         elif num_str:
             total += float(num_str)
             num_str = ''
             has_decimal = False
 
     return int(total) if total.is_integer() else total
 
 from itertools import groupby
 
 # ВАРИАНТ 5: Функциональный стиль с группировкой цифр
 def sum_numbers_in_string(s):
     total = 0
     for is_digit, group in groupby(s, key=lambda x: x.isdigit()):
         if is_digit:
             total += int(''.join(group))
     return total
 
 
 print(sum_numbers_in_string("abc123xyz45"))              # -> 168  # (123 + 45)
 print(sum_numbers_in_string("7 chocolates, 3 candies"))  # -> 10   # (7 + 3)
 print(sum_numbers_in_string("1a2b3c"))                   # -> 6    # (1 + 2 + 3)
 
 
 
 # ЗАДАЧА 2
 # Что выведет данный код?
 
 m = [[1, 2, 3], [4,5,6], [7,8,9]]
 t = list(zip(*m))
 
 # print(list(map(list, t)))  # -> ???
 # print(t)                   # -> ???
 
 
 
 
 
 # ЗАДАЧА 2 Что выведет данный код?
 
 # Это транспонированная матрица, где строки стали столбцами, а столбцы — строками.
 m = [[1, 2, 3], [4,5,6], [7,8,9]]
 t = list(zip(*m))
 print(list(map(list, t)))  # -> [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
 print(t)                   # -> [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
 
 
 
 
 
 # ЗАДАЧА 3
 # Что выведет данный код?
 
 class Y:
     def __init__(self, x):
         self.x = x
 
     def caclucate(self):
         return self.x * 2 + 1  # Формула: 2x + 1
 
 class Z(Y):
     def __init__(self, x, y):
         super().__init__(x)
         self.y = y
 
     def caclucate(self):
         return super().caclucate() + self.y  # (2x + 1) + y
 
 class X(Z):
     def __init__(self, x, y, z):
         super().__init__(x, y)
         self.z = z
 
     def caclucate(self):
         return self.z - super().caclucate()  # z - ((2x + 1) + y)
 
 a = Y(3)
 b = Z(2, 4)
 c = X(2, 1, 7)
 
 # print(a.caclucate())  # -> ???
 # print(b.caclucate())  # -> ???
 # print(c.caclucate())  # -> ???
 
 
 
 
 
 # ОТВЕТ ЗАДАЧА 3 Что выведет данный код?
 
 # Каждый класс переопределяет метод caclucate()
 class Y:
     def __init__(self, x):
         self.x = x
 
     def caclucate(self):
         return self.x * 2 + 1  # Формула: 2x + 1
 
 class Z(Y):
     def __init__(self, x, y):
         super().__init__(x)
         self.y = y
 
     def caclucate(self):
         return super().caclucate() + self.y  # (2x + 1) + y
 
 class X(Z):
     def __init__(self, x, y, z):
         super().__init__(x, y)
         self.z = z
 
     def caclucate(self):
         return self.z - super().caclucate()  # z - ((2x + 1) + y)
 
 a = Y(3)
 b = Z(2, 4)
 c = X(2, 1, 7)
 
 print(a.caclucate())  # -> 7   # 3 * 2 + 1 = 7
 print(b.caclucate())  # -> 9   # (2*2 + 1) + 4 = 5 + 4 = 9
 print(c.caclucate())  # -> 1   # 7 - ((2*2 + 1) + 1) = 7 - 6 = 1
 
 
 
 
 
 # ЗАДАЧА 4
 # Какой из принципов в коде нарушен и как его исправить?
 
 class EmailSender:
     def send(self, message):
         print(f"Sending email: {message}")
 
 class MessageService:
     def __init__(self, email_sender):
         self.email_sender = email_sender
 
     def send_message(self, message):
         self.email_sender.send(message)
 
 
 
 # ОТВЕТ ЗАДАЧА 4 Какой из принципов в коде нарушен и как его исправить?
 
 # Нарушен принцип Dependency Inversion (DIP).   DIP (Dependency Inversion Principle) – Принцип инверсии зависимостей
 # Исправить: Зависить от абстракции (интерфейса), а не от конкретного класса EmailSender.
 from abc import ABC, abstractmethod
 
 class MessageSender(ABC):
     @abstractmethod
     def send(self, message):
         pass
 
 class EmailSender(MessageSender):
     def send(self, message):
         print(f"Sending email: {message}")
 
 class MessageService:
     def __init__(self, sender: MessageSender):
         self.sender = sender
 
     def send_message(self, message):
         self.sender.send(message)
         
         
 # Теперь можно легко добавить новые отправители:
 
 class SmsSender(MessageSender):
     def send(self, message):
         print(f"Sending SMS: {message}")
 
 sms_sender = SmsSender()
 service = MessageService(sms_sender)
 service.send_message("Hi via SMS!")  # -> Sending SMS: Hi via SMS!
 
 # Вывод:
 # Принцип Dependency Inversion (DIP) соблюдается, так как:
 # - MessageService зависит от абстракции (MessageSender), а не от конкретного класса.
 # - Новые реализации (SmsSender, PushSender) можно добавлять без изменения MessageService.
 # Код стал гибким и соответствует SOLID особенно принципу DIP.
 
 
 
 
 # ЗАДАЧА 5
 # На фреймворке fastapi  напишите код который будет принимать в запросе json содержащий name weight и будет создавать
 # товар в базе после чего возвращать {result: true}  с кодом 201 Created
 
 
 
 
 # ОТВЕТ ЗАДАЧА 5 На фреймворке fastapi  напишите код который будет принимать в запросе json содержащий name weight и
 # будет создавать товар в базе после чего возвращать {result: true}  с кодом 201 Created
 
 Если нужен минималистичный API           -> FastAPI.
 Если нужен полноценный бэкенд с админкой -> Django + DRF.
 
 
 # FastAPI более лаконичен и не требует ORM (можно использовать SQLAlchemy напрямую).
 from fastapi import FastAPI, status, Depends
 from pydantic import BaseModel
 from sqlalchemy import create_engine, Column, Integer, String
 from sqlalchemy.ext.declarative import declarative_base
 from sqlalchemy.orm import sessionmaker, Session
 
 # Настройка базы данных
 SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
 engine = create_engine(SQLALCHEMY_DATABASE_URL)
 SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
 
 Base = declarative_base()
 
 # Модель товара в базе данных
 class ProductDB(Base):
     __tablename__ = "products"
     
     id = Column(Integer, primary_key=True, index=True)
     name = Column(String, index=True)
     weight = Column(Integer)
 
 # Создаем таблицы (в реальном проекте лучше использовать миграции)
 Base.metadata.create_all(bind=engine)
 
 app = FastAPI()
 
 # Pydantic модель для входящих данных
 class ProductCreate(BaseModel):
     name: str
     weight: int
     
 # Pydantic модель для ответа
 class ProductResponse(BaseModel):
     result: bool
 
 # Зависимость для получения сессии базы данных
 def get_db():
     db = SessionLocal()
     try:
         yield db
     finally:
         db.close()
 
 @app.post("/products/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
 def create_product(product: ProductCreate, db: Session = Depends(get_db)):
     # Создаём товар в базе данных
     db_product = ProductDB(name=product.name, weight=product.weight)
     db.add(db_product)
     db.commit()
     db.refresh(db_product)
     
     return {"result": True}
 
 
 
 # Django + DRF требует больше кода, но дает больше "из коробки" (админка, миграции, аутентификация).
 # ТОЖЕ САМОЕ Django+DRF
 
 1. Сначала определим модель Product в models.py:
 from django.db import models
 
 class Product(models.Model):
     name = models.CharField(max_length=255)
     weight = models.FloatField()
 
     def __str__(self):
         return self.name
         
         
 # 2. Затем создадим сериализатор (если используем Django REST Framework) в serializers.py:
 from rest_framework import serializers
 from .models import Product
 
 class ProductSerializer(serializers.ModelSerializer):
     class Meta:
         model = Product
         fields = ['name', 'weight']
         
         
 # 3. Напишем представление (view) в views.py:
 # Вариант с Django REST Framework (рекомендуется):
 
 from rest_framework.views import APIView
 from rest_framework.response import Response
 from rest_framework import status
 from .models import Product
 from .serializers import ProductSerializer
 
 class CreateProductView(APIView):
     def post(self, request):
         serializer = ProductSerializer(data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response({"result": True}, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
 # 4. Напишем представление (urls) в urls.py:
 from django.urls import path
 from .views import CreateProductView
 
 urlpatterns = [
     path('products/', CreateProductView.as_view(), name='create_product'),
 ]
 
 Не забудьте выполнить миграции (python manage.py makemigrations и python manage.py migrate) после создания модели.
 
 
 
 
 
 # ЗАДАЧА 6
 # В базе данных имеется visitors с полями id, first_time (первый визит) и count (общее количество запросов).
 # Напишите к этой таблице три SQL запроса:
 # 1) Вывод id всех посетилей, количество визитов которых более 5
 # 2) Вывод всех id посетилей, зашедших на сайт зимой 2022 года
 # 3) Вывод пяти дней 2023 года, в которые визиты совершались чаще всего, с количеством визитов в каждый такой день
 
 
 
 
 
 
 # ОТВЕТ ЗАДАЧА 6
 
 1. Вывод id всех посетителей, количество визитов которых более 5
 
 SELECT id
 FROM visitors
 WHERE count > 5;
 
 
 2. Вывод всех id посетителей, зашедших на сайт зимой 2022 года (декабрь 2021, январь и февраль 2022)
 
 SELECT DISTINCT id
 FROM visitors
 WHERE first_time BETWEEN '2021-12-01' AND '2022-02-28';
 
 
 3. Вывод пяти дней 2023 года с наибольшим количеством визитов (и количеством визитов в каждый такой день)
 Проблема: В таблице нет данных о каждом визите.  Неточный, но единственно возможный с данными таблицы   
 
 SELECT DATE(first_time) AS day, SUM(count) AS total_visits
 FROM visitors
 WHERE first_time BETWEEN '2023-01-01' AND '2023-12-31'
 GROUP BY DATE(first_time)
 ORDER BY total_visits DESC
 LIMIT 5;
 
 
 
 
 # ЗАДАЧА 7
 # Опишите струтуру реляционной бд в которой будет хранится лекарства и категории этих лекарст. Одно лекарство при
 # этом может быть привязано к нескольким категориям одновременно. Пропишите только имена таблиц и полей типы полей.
 # Иную информацию прописывать не нужно
 
 
 
 
 
 
 # ОТВЕТ ЗАДАЧА 7
 
 Таблицы:
 
 # MEDICINES – хранит информацию о лекарствах.
 
 MEDICINES (
     id INT,
     name VARCHAR,
     description TEXT,
     manufacturer VARCHAR,
     price DECIMAL,
     created_at DATETIME,
     updated_at DATETIME
 )
 
 # CATEGORIES – содержит категории лекарств.
 
 CATEGORIES (
     id INT,
     name VARCHAR,
     description TEXT,
     created_at DATETIME,
     updated_at DATETIME
 )
 
 # MEDICINE_CATEGORY – связывает лекарства и категории (многие-ко-многим).
 
 MEDICINE_CATEGORY (
     medicine_id INT NOT NULL,
     category_id INT NOT NULL,
     created_at DATETIME,
     PRIMARY KEY (medicine_id, category_id),
     FOREIGN KEY (medicine_id) REFERENCES MEDICINES(id),
     FOREIGN KEY (category_id) REFERENCES CATEGORIES(id)
 )
 
 
 
 
 # ЗАДАЧА 8
 # Какие есть NoSQL базы данных?
 
 
 
 
 # ОТВЕТ ЗАДАЧА 8
 
 Типы NoSQL баз данных
 
 ДОКУМЕНТООРИЕНТИРОВАННЫЕ (хранят данные в формате JSON/BSON, XML):
 
 - MongoDB (наиболее популярная)
 - CouchDB, Firebase Firestore, RavenDB
 - Elasticsearch (поисковая система на основе документов, поддерживает полнотекстовый поиск)
 
 КЛЮЧ-ЗНАЧЕНИЕ (простая структура, высокая скорость):
 
 - Redis (также поддерживает сложные структуры)
 - DynamoDB (AWS), Riak, etcd
 
 КОЛОНОЧНЫЕ (оптимизированы для аналитики и больших данных):
 
 - Cassandra (распределённая, отказоустойчивая)
 - HBase (на основе Hadoop)
 - ClickHouse (OLAP, аналитика в реальном времени)
 
 ГРАФОВЫЕ (эффективны для работы со связями):
 
 - Neo4j (наиболее известная)
 - ArangoDB (мультимодельная, поддерживает и документы, и графы)
 - Amazon Neptune
 
 IN-MEMORY (работают в ОЗУ, очень быстрые):
 
 - Redis (поддерживает персистентность)
 - Memcached (простой кеш, без персистентности)
 
 
 Когда использовать?
  - Гибкость схемы                        -> MongoDB, CouchDB
  - Высокая скорость доступа              -> Redis, Memcached
  - Большие объемы данных + аналитика     -> Cassandra, ClickHouse
  - Сложные связи (соцсети, рекомендации) -> Neo4j
  - Масштабируемость и отказоустойчивость -> Cassandra, DynamoDB
  - Полнотекстовый поиск и анализ текстов -> Elasticsearch
  
  
 Когда НЕ выбирать NoSQL?
  - Нужны транзакции (ACID).
  - Нужны сложные JOIN-запросы.
  - Данные жестко структурированы (лучше SQL).
 
 
 
 
 # ЗАДАЧА 9
 # В каких форматах происходит передача и хранение данных при взаимодействии с NoSQL-хранилищами с которыми вы также
 # знакомы. Укажите названия хранилищ и соответствующие им форматы данных
 
 
 
 
 # ОТВЕТ ЗАДАЧА 9
 
 MongoDB       - BSON (бинарный JSON)
 Redis         - строки, хэши, списки, множества (бинарно-безопасные)
 Cassandra     - JSON, BSON, строки, бинарные данные (через CQL)
 Elasticsearch - JSON
 DynamoDB      - JSON (через SDK), бинарные данные
 Couchbase     - JSON, бинарные данные
 RocksDB       - ключ-значение (бинарные данные)
 Neo4j         - JSON (Cypher-запросы), графовые структуры
 ClickHouse    - бинарные (столбцовое хранение, сжатие), JSON, CSV, Parquet, Avro, ORC, Protobuf (через коннекторы)
 
 
 
 
 # ЗАДАЧА 10
 # Какие методы REST вы знаете?  Какие из них ИДЕМПОТЕНТНЫЕ а какие нет.
 
 
 
 
 
 
 # ОТВЕТ ЗАДАЧА 10
 
 GET     - получение ресурса.
 POST    - создание ресурса или выполнение операции.                      НЕ ИДЕМПОТЕНТЕН
 PUT     - полное обновление ресурса (или создание, если не существует).   
 PATCH   - частичное обновление ресурса.                                  НЕ ИДЕМПОТЕНТЕН
 DELETE  - удаление ресурса.
 HEAD    - аналогичен GET, но возвращает только заголовки (без тела).
 OPTIONS - получение информации о доступных методах для ресурса.
 
 
 PATCH НЕ всегда НЕИДЕМПОТЕНТНЫЙ (зависит от логики), а DELETE считается идемпотентным, даже если ресурс уже удалён. 
 PATCH Обычно неидемпотентный, но может быть идемпотентным, если логика обновления детерминирована
 (например, замена поля { "status": "completed" }).
 Если PATCH применяет операции типа { "increment": 1 }, то он неидемпотентный.
 
 
 
 Идемпотентность методов
 Идемпотентный метод – это метод, который при многократном выполнении с одними и теми же данными даёт одинаковый результат
 (не изменяет состояние сервера после первого вызова).
 
 Метод	 Идемпотентный?	 Безопасный?         Описание
 GET	     Да	             Да (только чтение)  Получение ресурса. Не изменяет сервер.                   
 POST     Нет	         Нет                 Создание ресурса. Каждый вызов может создавать новый объект.       
 PUT	     Да	             Нет                 Полное обновление (или создание). Повторные запросы не меняют результат.       
 PATCH	 Нет (обычно)    Нет                 Частичное обновление. Зависит от текущего состояния ресурса.       
 DELETE	 Да	             Нет                 Удаление ресурса. После первого удаления дальнейшие запросы не изменяют состояние.       
 HEAD	 Да	             Да                  Как GET, но без тела ответа. Только заголовки.   
 OPTIONS	 Да	             Да                  Информация о доступных методах для ресурса.   
 
 
 
 
 # ЗАДАЧА 11
 # Исправить структуру RESTful API чтобы соответствовала стандарту REST
 # get     /item/id
 # get     /items/list
 # add     /items/new/id
 # edit    /item/id
 # delete  /items/id
 
 
 
 
 
 # ОТВЕТ ЗАДАЧА 11
 
 GET    /items/{id}       - получение одного элемента
 GET    /items            - получение списка элементов
 POST   /items            - создание нового элемента (id обычно генерируется сервером)
 PUT    /items/{id}       - полное обновление элемента
 PATCH  /items/{id}       - частичное обновление элемента
 DELETE /items/{id}       - удаление элемента
 
 
 
 
 
 # ЗАДАЧА 14
 # Что в терминале Linux значит   >>   <<   &&
 
 
 
 
 # ОТВЕТ ЗАДАЧА 14
 
 >> - добавление вывода в конец файла (без перезаписи).
 << - передача текста в команду (here-document).
 && - выполнить следующую команду, только если предыдущая успешна.
 
 Кратко:
 >> - дописать в файл.
 << - многострочный ввод.
 && - "и тогда".
 
 
 
 
 # ЗАДАЧА 15
 # Почему при помощи git revert может быть невозможно откатить merge?
 # Каким образом можно откатить merge?
 
 
 
 
 
 # ОТВЕТ ЗАДАЧА 15
 
 Проблемы с git revert для merge:
 
  - Конфликты изменений, если последующие коммиты зависят от merge.
  - Нужно указывать правильный родительский коммит (-m 1 или -m 2).
 
 Как откатить merge:
 
  - git revert -m 1 <merge-commit> — откат к состоянию до merge (выбирает первую ветку).
  - Или использовать git reset --hard <commit-before-merge> (если merge не опубликован).
 
 Кратко: revert с -m, или reset если можно переписать историю.
 
 
 
 
 # ЗАДАЧА 16
 # С каким типами ошибок в Git Вам обычно приходилось сталкиватся (точные название не обязательно но можно, важно указать
 # суть каждого типа ошибок)?
 # Каким образом каждая из этих ошибок решается?
 
 
 
 
 
 # ОТВЕТ ЗАДАЧА 16
 Краткий список ошибок в Git и их решений
 1) Конфликты слияния
  - Суть: Git не может сам объединить изменения.
  - Решение: Ручное исправление -> git add -> git commit.
 
 2) Отмена изменений
  - Суть: Файлы изменены/удалены, но не закоммичены.
  - Решение:
     - Отмена правок: git restore <file> (или git checkout -- <file>).
     - Восстановление удалённых: git restore <file>.
 
 3) Ошибочный коммит
  - Суть: Неправильные изменения/сообщение в коммите.
  - Решение:
    - Последний коммит: git commit --amend.
    - Старые коммиты: git rebase -i.
 
 4) Потерянные коммиты
  - Суть: Удаление ветки или reset --hard.
  - Решение: Найти через git reflog, восстановить (git checkout <hash>).
 
 5) Пуш не в ту ветку
  - Суть: Изменения в main вместо feature-ветки.
  - Решение: Откат (git revert/reset), пуш в нужную ветку.
 
 6) Неотслеживаемые файлы
  - Суть: Новые файлы не в индексе.
  - Решение: git add <file> или git add ..
 
 7) Игнорируемые файлы в Git
  - Суть: Git следит за файлами из .gitignore.
  - Решение: git rm --cached <file>.
 
 8) Отсоединённая ветка
  - Суть: Локальная ветка не связана с origin.
  - Решение: git branch -u origin/<branch>.
 
 9) Жёсткий reset (потеря изменений)
 - Суть: reset --hard удаляет незакоммиченное.
 - Решение: Восстановить через git reflog (если коммит был).
 
 10) Пустые коммиты
 - Суть: Коммит без изменений.
 - Решение: Удалить (git reset) или разрешить (--allow-empty).
 
 
 Итог:
 
 Конфликты       - ручное исправление.
 Отмена          - restore/checkout.
 Потеря коммитов - reflog.
 Ошибочный пуш   - revert/reset.
 
 
 Главные инструменты для исправления ошибок:
 
 git reflog                      - спасает при потере коммитов.
 git restore / git reset         - отмена изменений.
 git commit --amend и rebase -i  - правка истории.
 git stash                       - временное сохранение правок.
________________________________________________________________________________________________________________________

 Ozon младший-разработчик сети

 1) Сколько бит в ipv4?   IPv4 - 32 бита (4 байта, форма: 192.168.1.1).
 2) Сколько максимум хостов мб в сети с маской /24?  Максимум хостов в /24 - 254 (256 адресов − 2 служебных).
 3) Какой командой посмотреть запущенные процессы в Linux?
 - ps aux     - список процессов.
 - top / htop - мониторинг в реальном времени.
 - pstree     - процессы в виде дерева.
________________________________________________________________________________________________________________________

 СБЕР  ЛИГАЛ     2 ЗАДАЧИ

 ЗАДАЧА 1) Разные способы вывести СПИСОК в обратном порядке в Python


 # Вариант 1) Разворот списка через индексы (вариант с СОБЕСЕДОВАНИЯ)                    - O(n)
 lst = [1, 'a', 'b', 2]
 n = len(lst)
 for i in range(len(lst) // 2):
     lst[i], lst[n-1-i] = lst[n-1-i], lst[i]
 print(lst)                  # -> [2, 'b', 'a', 1]

 # Вариант 2) Разворот списка через отрицательные индексы (вариант с СОБЕСЕДОВАНИЯ)      - O(n)
 lst = [1, 'a', 'b', 2]
 for i in range(len(lst)//2):
     lst[i], lst[-i-1] = lst[-i-1], lst[i]
 print(lst)                  # -> [2, 'b', 'a', 1]

 # Вариант 3) Используя метод reverse()                                                  - O(n)
 lst = [1, 'a', 'b', 2]
 lst.reverse()
 print(lst)                  # -> [2, 'b', 'a', 1]

 # Вариант 4) Используя срез [::-1]                                                      - O(n)
 lst = [1, 'a', 'b', 2]
 print(lst[::-1])            # -> [2, 'b', 'a', 1]

 # Вариант 5) Используя функцию reversed()                                               - O(n)
 lst = [1, 'a', 'b', 2]
 print(list(reversed(lst)))  # -> [2, 'b', 'a', 1]

 # Вариант 6) Через цикл for (итерируясь с конца)                                        - O(n)
 lst = [1, 'a', 'b', 2]
 reversed_lst = []
 for item in lst[::-1]:
     reversed_lst.append(item)  # append() - O(1), но создание среза lst[::-1]   - O(n)
 print(reversed_lst)         # -> [2, 'b', 'a', 1]

 # Вариант 7) Используя insert() с перебором исходного списка                            - O(n²)
 lst = [1, 'a', 'b', 2]
 reversed_lst = []
 for item in lst:
     reversed_lst.insert(0, item)  # insert(0) - O(n) для каждого элемента → итого O(n²)
 print(reversed_lst)         # -> [2, 'b', 'a', 1]



 ЗАДАЧА 2) Преобразует список чисел в строку с диапазонами

 lst = [1, 3, 2, 8, 5, 6, 7, 10]


 # Вариант 1) сортировка + однопроходный анализ    O(n log n)
 def list_to_ranges(lst: list[int]) -> str:
     if not lst:
         return ""

     lst = sorted(set(lst))  # Удаляем дубликаты и сортируем  #  O(n log n) (из-за сортировки)
     ranges = []
     start = lst[0]
     prev = start

     for num in lst[1:]:  # Проход по списку O(n)
         if num == prev + 1:
             prev = num
         else:
             if start == prev:
                 ranges.append(str(start))
             else:
                 ranges.append(f"{start}-{prev}")
             start = num
             prev = num

     # Добавляем последний диапазон
     if start == prev:
         ranges.append(str(start))
     else:
         ranges.append(f"{start}-{prev}")

     return ", ".join(ranges)


 # Вариант 2) C группировкой последовательных чисел (используя itertools.groupby)  O(n log n)
 from itertools import groupby

 def list_to_ranges(lst: list[int]) -> str:
     if not lst:
         return ""

     lst = sorted(set(lst))
     ranges = []

     for _, group in groupby(enumerate(lst), key=lambda x: x[1] - x[0]):
         group = list(group)
         start = group[0][1]
         end = group[-1][1]
         ranges.append(f"{start}-{end}" if start != end else str(start))

     return ", ".join(ranges)


 # Вариант 3) С двумя указателями  O(n log n)
 def list_to_ranges(lst: list[int]) -> str:
     if not lst:
         return ""

     lst = sorted(set(lst))
     ranges = []
     i = 0
     n = len(lst)

     while i < n:
         start = lst[i]
         while i < n - 1 and lst[i + 1] == lst[i] + 1:
             i += 1
         end = lst[i]
         ranges.append(f"{start}-{end}" if start != end else str(start))
         i += 1

     return ", ".join(ranges)

 print(list_to_ranges(lst))  # -> "1-3, 5-8, 10"
________________________________________________________________________________________________________________________

 X5 Задача КАКАЯ ПОСЛЕДОВАТЕЛЬНОСТЬ ВЫВОДА БУДЕТ и что вместо ???  какая аннотация

 import asyncio
 import typing as t

 async def func1():
     print('func1 started')  # 4 - выполняется при запуске task1
     return 42               # 7 - возвращает результат (будет получен в await task1)


 async def func2():
     print('func2 started')  # 5 - выполняется при запуске task2
     raise Exception()       # 8 - вызывает исключение (будет получено в await task2)

 async def main():
     print('main started')   # 1 - вход в основную корутину

     # Создаем корутины, но они еще не выполняются
     coroutine1: t.Coroutine = func1()  # просто создает объект корутины
     coroutine2 = func2()               # создает объект корутины
     print('coroutines created')  # 2 - корутины созданы, но не запущены

     # Создаем задачи - теперь они добавлены в event loop и будут выполняться
     task1 = asyncio.create_task(coroutine1)  # 3 - задача планируется на выполнение
     task2 = asyncio.create_task(coroutine2)  # задача планируется на выполнение
     print('tasks created')  # 3 - задачи созданы и добавлены в event loop

     # Даем время на выполнение задач (event loop получает управление)
     await asyncio.sleep(0.1)  # переключает контекст на выполнение задач
     print('main woke up')   # 6 - main() продолжает выполнение после sleep

     # Ожидаем результаты выполнения задач
     res1 = await task1      # получаем результат func1() (уже выполнен к этому моменту)
     print(f'res1 is {res1}')  # 9 - выводим результат первой задачи

     try:
         res2 = await task2  # получаем исключение из func2()
         print(f'res2 is {res2}')  # этот код не выполнится из-за исключения
     except Exception:
         print("Exception from task2")  # 10 - обрабатываем исключение


 asyncio.run(main())  # запускает event loop и корутину main()
________________________________________________________________________________________________________________________

 2 ЗАДАЧИ X5


 # ЗАДАЧА 1 ДОПОЛНИТЬ КОД

 some_arr = [{"1": 1}]
 some_arr = some_arr*  3

 assert some_arr == [{"1": 1}, {"1": 1}, {"1": 1}]

 some_arr[0]["1"] = 2

 assert some_arr == [{"1": 2}, {"1": 2}, {"1": 2}]

 some_arr[1] = "test"

 assert some_arr == [{"1": 2}, 'test', {"1": 2}]

 some_arr = some_arr.append("1")

 assert some_arr == None


 КРАТКО ПОЧЕМУ ТАКОЙ ОТВЕТ:
 - some_arr * 3 создает список с тремя одинаковыми ссылками на один и тот же словарь {"1": 1}.
 - Изменение some_arr[0]["1"] меняет исходный словарь, поэтому изменение видно во всех элементах списка.
 - Присваивание some_arr[1] = "test" заменяет ссылку на словарь строкой, не затрагивая другие элементы.
 - append() модифицирует список на месте и возвращает None, поэтому some_arr становится None.



 ЗАДАЧА 2  НАПИСАТЬ СВОЙ КОНТЕКСТНЫЙ МЕНЕДЖЕР  2 ВАРИАНТА!!!

 # ВАРИАНТ 1: Класс с методами __enter__ и __exit__

 # Класс, если нужна сложная логика (например, управление состоянием).
 class MyContextManager:
     def __init__(self, name):
         self.name = name
         print(f"Инициализация контекстного менеджера для {self.name}")

     def __enter__(self):
         print(f"Вход в контекст для {self.name}")
         # Можно вернуть объект, который будет связан с as-переменной
         return self

     def __exit__(self, exc_type, exc_val, exc_tb):
         print(f"Выход из контекста для {self.name}")
         if exc_type is not None:
             print(f"Произошло исключение: {exc_val}")
         # Если вернуть True, исключение будет подавлено
         return False


 # Пример использования
 with MyContextManager("тестовый ресурс") as cm:
     print(f"Выполняем операции внутри контекста с {cm.name}")
     # Если раскомментировать следующую строку, будет видна обработка исключения
     raise ValueError("Ошибка в контексте")


 # ВАРИАНТ 2: Декоратор @contextmanager

 # Декоратор @contextmanager, если контекстный менеджер простой и лаконичный.
 from contextlib import contextmanager

 @contextmanager
 def my_context_manager(name):
     print(f"Подготовка ресурса {name}")
     resource = f"Ресурс: {name}"
     try:
         yield resource  # это значение будет присвоено as-переменной
     except Exception as e:
         print(f"Обработка исключения: {e}")
         raise
     finally:
         print(f"Освобождение ресурса {name}")

 # Пример использования
 with my_context_manager("данные") as res:
     print(f"Используем {res} внутри контекста")
________________________________________________________________________________________________________________________

 2 ЗАДАЧИ МТС FULLSTACK  1) Правильная скобочная последовательность  2) Палиндром (перевернуть число МАТЕМАТИЧЕСКИ)


 # ЗАДАЧА 2) Палиндром.  Реализовать функцию, проверяющую число на полиндромность (слева-направо одинаковое).


 # ВАРИАНТ 1) перевернуть число МАТЕМАТИЧЕСКИ
 def is_palindrome(integer: int) -> bool:
     if integer < 0:
         return False  # Отрицательные числа не могут быть палиндромами
     original = integer
     reversed_num = 0
     while integer > 0:
         reversed_num = reversed_num * 10 + integer % 10
         integer = integer // 10
     return original == reversed_num

 print(is_palindrome(12321))  # -> True
 print(is_palindrome(12345))  # -> False


 # ВАРИАНТ 2) ОБЫЧНЫЙ
 def is_palindrome(integer: int) -> bool:
     str_num = str(integer)
     # return str_num == str_num[::-1]
     return str_num == str_num[slice(None, None, -True)]

 print(is_palindrome(12321))  # -> True
 print(is_palindrome(12345))  # -> False
________________________________________________________________________________________________________________________


 # ВК HR ВОПРОСЫ  ПРОСТО ПОСМОТРЕТЬ


 # ВОПРОСЫ 1)

 Клауд:

 Какие механизмы есть в СУБД для отказоустойчивости?

 - Репликация (синхронная/асинхронная) - копирование данных на несколько узлов.
 - Транзакции и ACID - гарантируют целостность данных даже при сбоях.
 - Журналирование (WAL - Write-Ahead Logging) - изменения сначала записываются в лог, что позволяет восстановить данные.
 - Кластеризация - автоматический переход на резервный узел при отказе основного (например, в PostgreSQL с Patroni).
 - Шардирование - распределение данных для уменьшения последствий отказа одного узла.

 Что означает буква D в аббревиатуре ACID?

 D - Durability (Долговечность) - гарантия, что после подтверждения транзакции (COMMIT) изменения сохранятся даже
 при сбое системы (например, благодаря записи на диск).

 Какими инструментами можно найти процесс, активно потребляющий ресурсы в Linux?

 top / htop          - интерактивные мониторы процессов.
 ps aux --sort=-%cpu - вывод процессов с сортировкой по CPU.
 vmstat 1            - статистика по CPU, памяти, I/O.
 iotop               - мониторинг процессов, нагружающих диск.
 glances             - расширенный мониторинг системы.

 Какими инструментами можно узнать нагрузку на диски в Linux?

 iostat -x 1                  - статистика загрузки дисков (await, %util).
 dstat                        - комбинированная статистика (CPU, disk, network).
 sar -d 1 (из пакета sysstat) - история нагрузки на диски.
 iotop                        - какие процессы активно пишут/читают.

 Какими инструментами можно проверить сетевые настройки linux из cli?

 ip a / ifconfig                  - список интерфейсов и их IP.
 ip route / route -n              - таблица маршрутизации.
 ss -tulnp / netstat -tulnp       - открытые порты и процессы.
 ping, traceroute, mtr            - проверка доступности и маршрута.
 nslookup / dig                   - DNS-запросы.
 nmcli (если есть NetworkManager) - управление соединениями.

 Что быстрее: синхронная или асинхронная запись в файл?

 Асинхронная запись быстрее, так как данные сначала попадают в буфер (кеш), а запись на диск происходит позже.
 Синхронная запись медленнее, потому что ОС ждёт подтверждения записи на диск перед завершением операции (например, fsync()).

 В чём разница между списком и картежом в Python?

  - Список (list) – изменяемый (можно добавлять, удалять элементы), [1, 2, 3].
  - Кортеж (tuple) – неизменяемый (после создания нельзя изменить), (1, 2, 3). Кортежи занимают меньше памяти и работают быстрее.

 Какова сложность поиска в словаре по значению?

  - Поиск по значению (dict.values()) имеет сложность O(n), так как требует перебора всех элементов.
  - Поиск по ключу – O(1) (хеш-таблица).

 Почему использование модуля "threading" неэффективно для масштабирования процессорных вычислений?

  - Из-за GIL (Global Interpreter Lock) в CPython: только один поток выполняет Python-код одновременно.
  - Для CPU-задач лучше использовать multiprocessing (параллелизм) или асинхронность (asyncio для I/O).

 Что такое "MRO" и "name mangling" в Python?

 MRO (Method Resolution Order) – порядок поиска методов при наследовании (алгоритм C3, можно посмотреть через ClassName.__mro__).
 Name mangling – автоматическое преобразование имён вида __var в _ClassName__var для избежания коллизий в наследовании.

 Работал ли с виртуальными системами? Касался ли вообще?
 Давненько Virtual Box, Песочницы, WMWareWorkstation.



 # ВОПРОСЫ 2)

 ArenadataDB:

 1. Можно ли заменить символ в строке и почему?
 Нет, строки в Python неизменяемы (immutable). Можно создать новую строку с заменой.

 2. Чем корутина отличается от генератора?
 Генератор производит значения (yield), корутина может и потреблять (send()), и выполнять асинхронные операции (await).
 В Python корутины - это расширение генераторов

 3. Какие примитивы синхронизации есть в AsyncIO?
  - asyncio.Lock      - блокировка для критических секций.
  - asyncio.Event     - уведомление между задачами.
  - asyncio.Semaphore - ограничение числа одновременных задач.
  - asyncio.Condition - ожидание изменения состояния.
  - asyncio.Queue     - потокобезопасная очередь.

 4. Как написать новый Dunder-метод?
 Определить метод в классе с двойными подчёркиваниями
 Их нельзя переопределять произвольно, только те, что поддерживаются Python.

 5. Что быстрее асинхронная или синхронная запись в файл, почему?
 Синхронная запись обычно быстрее для одного файла, так как нет накладных расходов на event loop.
 Асинхронная запись (например, через aiofiles) полезна при множестве одновременных операций (например, веб-сервер)
 На самом деле, асинхронность не ускоряет сам диск, но позволяет выполнять другие задачи во время ожидания.

 6. Что делает метод type?
 Как функция: возвращает тип объекта: type(42)  # <class 'int'>
 Как метакласс: создаёт новый класс:  MyClass = type('MyClass', (Base,), {'x': 42})
 type - это метакласс по умолчанию для всех классов в Python.

 7. В чем разница между мягкой и жесткой ссылкой? soft/hard link
 Жёсткая ссылка (hard link) - это дополнительное имя для файла в файловой системе (inode). Удаление одной ссылки
 не удаляет данные, пока есть другие ссылки.
 Мягкая ссылка (symbolic link, symlink) - это ярлык, указывающий на путь. Если оригинал удалён, symlink становится "битым".

 8. Зачем в питоне использовать замыкание?
 Сохраняет состояние между вызовами (альтернатива ООП). Используется в декораторах, callback-ах, фабриках функций.
________________________________________________________________________________________________________________________

 # ВК  ЗАДАЧИ  МНОГО ЗАДАЧ!!!


 # ЗАДАЧА 0 (Разогрев) Написать декоратор с параметрами

 import time
 from functools import wraps

 def retry(max_retries):
     def decorator(func):
         @wraps(func)
         def wrapper(*args, **kwargs):
             last_exception = None
             for attempt in range(max_retries):
                 try:
                     return func(*args, **kwargs)
                 except Exception as e:
                     last_exception = e
                     print(f"Attempt {attempt + 1} failed. Retrying...")
                     time.sleep(1)  # Небольшая задержка перед повторной попыткой
             print(f"All {max_retries} attempts failed")
             raise last_exception  # Пробрасываем последнее исключение
         return wrapper
     return decorator

 # Пример использования
 @retry(3)
 def risky_function():
     import random
     if random.random() < 0.7:  # 70% вероятность ошибки
         raise ValueError("Something went wrong!")
     return "Success!"


 # Запустим 10 раз, чтобы увидеть ошибки
 for _ in range(10):
     try:
         print(risky_function())
     except ValueError as e:
         print(f"Error: {e}")



 # ЗАДАЧА 1 Написать код

 # Требования:
 # Уведомления высылаются регулярно и приходят из разных источников.
 # Уведомления отправляются в разные каналы.
 #
 #
 # John,email, name@example.com, some content
 # {"name":"Alice", “type”: “telegram”, "id":"@alice", “content”:”some content”}


 # ОТВЕТ ЗАДАЧА 1 Написать код

 import json
 from abc import ABC, abstractmethod

 # Абстрактный класс для уведомлений
 class Notification(ABC):
     def __init__(self, name, content):
         self.name = name
         self.content = content

     @abstractmethod
     def send(self):
         pass

 # Email уведомление
 class EmailNotification(Notification):
     def __init__(self, name, email, content):
         super().__init__(name, content)
         self.email = email

     def send(self):
         print(f"Sending email to {self.name} ({self.email}): {self.content}")
         # Здесь должна быть реальная логика отправки email
         return True

 # Telegram уведомление
 class TelegramNotification(Notification):
     def __init__(self, name, chat_id, content):
         super().__init__(name, content)
         self.chat_id = chat_id

     def send(self):
         print(f"Sending Telegram message to {self.name} ({self.chat_id}): {self.content}")
         # Здесь должна быть реальная логика отправки в Telegram
         return True

 # Фабрика для создания уведомлений
 class NotificationFactory:
     @staticmethod
     def create_notification(data):
         if isinstance(data, str):
             # Обработка CSV-подобной строки "John,email,name@example.com,some content"
             parts = [part.strip() for part in data.split(',')]
             if len(parts) >= 4 and parts[1].lower() == 'email':
                 return EmailNotification(parts[0], parts[2], ','.join(parts[3:]))

         elif isinstance(data, dict):
             # Обработка JSON-подобного словаря
             if data.get('type', '').lower() == 'telegram':
                 return TelegramNotification(
                     data.get('name', ''),
                     data.get('id', ''),
                     data.get('content', '')
                 )
             elif data.get('type', '').lower() == 'email':
                 return EmailNotification(
                     data.get('name', ''),
                     data.get('id', ''),
                     data.get('content', '')
                 )

         return None

 # Менеджер уведомлений
 class NotificationManager:
     def __init__(self):
         self.notifications = []

     def add_notification(self, data):
         notification = NotificationFactory.create_notification(data)
         if notification:
             self.notifications.append(notification)

     def send_all(self):
         results = []
         for notification in self.notifications:
             results.append(notification.send())
         self.notifications = []
         return results

 # Пример использования
 if __name__ == "__main__":
     manager = NotificationManager()

     # Добавляем уведомления из разных источников
     manager.add_notification('John,email, name@example.com, some content')
     manager.add_notification(json.loads('{"name":"Alice", "type": "telegram", "id":"@alice", "content":"some content"}'))

     # Отправляем все уведомления
     manager.send_all()



 # ЗАДАЧА 2 ЧТО НЕ ТАК В КОДЕ ПРОСТО ПОСМОТРЕТЬ

 # Разработчик написал разовый скрипт для отправки уведомлений и уволился.
 # Этот код качественный? Что тебе в нем не нравится?

 # Jhon,email, name@example.com, some content
 # Jack,telegram, 12345678, some content

 def send_notifications(params):
    csv_file = open(os.path.dirname(file) + "/list.csv", newline="")
    f = csv.reader(csv_file, delimiter=",", quotechar="\")
    for row in f:
        if not params["skip_email"] and row[1] == "email":
            print(f"EMAIL: {row[2]}. Hello, {row[0]}! {row[3]}.")
        elif not params["skip_telegram"] and row[1] == "telegram":
            print(f"TELEGRAM: {row[2]}. Hello, {row[0]}! {row[3]}.")

 if name == "main":
    send_notifications(params)


 # ОТВЕТ ЗАДАЧА 2 ЧТО НЕ ТАК В КОДЕ ПРОСТО ПОСМОТРЕТЬ

 1) Утечка ресурсов: Файл не закрывается (csv_file), лучше использовать with open()
 3) Синтаксическая ошибка: quotechar="\" - незакрытая кавычка и неэкранированный обратный слэш
 4) Отсутствие проверки существования файла: Нет обработки случая, когда файл не существует
 5) Жестко закодированный путь: os.path.dirname(file) + "/list.csv" - проблема с конкатенацией путей
 6) Неясные зависимости: Непонятно, откуда берутся переменные file и params
 7) Магические числа: Использование индексов (row[0], row[1] и т.д.) вместо именованных констант
 8) Отсутствие обработки ошибок: Нет try-except для обработки возможных ошибок
 9) Опечатка в __name__: if name == "main" вместо if __name__ == "__main__"
 10) Использование print: Для логирования лучше использовать модуль logging
 11) Хардкод значений: "email" и "telegram" лучше вынести в Enum или константы
 12) Отсутствие валидации данных: Нет проверки формата и полноты данных в CSV
 13) Проблемы с пробелами: В данных есть пробелы (, name@example.com,), но нет .strip()
 14) Смешение ответственности: Функция и читает файл, и отправляет уведомления
 15) Нет тестов: Код не модульный и не тестируемый
 16) Плохая расширяемость: Добавление нового типа уведомления требует модификации кода
 17) Нет документации: Отсутствуют docstring и комментарии
 18) Проблемы с кодировкой: Файл открывается без указания кодировки
 19) Уязвимости безопасности: Нет проверки входящих данных (например, email)
 20) Отсутствие аннотаций типов. Нет type hints

 # "ЗОЛОТАЯ СЕРЕДИНА" между качеством и простотой для данной задачи. НО ДЛЯ production-системы можно сделать лучше.

 import csv
 import logging
 import re
 from enum import Enum, auto
 from pathlib import Path
 from typing import Dict, List, Optional, TypedDict

 # Настройка логирования
 logging.basicConfig(level=logging.INFO)
 logger = logging.getLogger(__name__)


 class NotificationType(Enum):
     EMAIL = auto()
     TELEGRAM = auto()

     @classmethod
     def from_string(cls, value: str) -> Optional['NotificationType']:
         normalized = value.strip().upper()
         for member in cls:
             if member.name == normalized:
                 return member
         return None


 class NotificationConfig(TypedDict):
     skip_email: bool
     skip_telegram: bool


 class MessageTemplates:
     EMAIL = "EMAIL: {address}. Hello, {name}! {message}."
     TELEGRAM = "TELEGRAM: {address}. Hello, {name}! {message}."


 class InvalidDataError(Exception):
     pass


 def is_valid_email(email: str) -> bool:
     return bool(re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email.strip()))


 def is_valid_telegram_id(tg_id: str) -> bool:
     return tg_id.strip().isdigit()


 def read_recipients(csv_path: Path) -> List[Dict[str, str]]:
     '''Читает CSV файл и возвращает список получателей.'''
     recipients = []

     with open(csv_path, newline="", encoding="utf-8") as csv_file:
         # Проверяем есть ли заголовок
         sample = csv_file.read(1024)
         csv_file.seek(0)
         has_header = csv.Sniffer().has_header(sample)

         reader = csv.DictReader(
             csv_file,
             fieldnames=["name", "type", "address", "message"],
             skipinitialspace=True
         )

         if has_header:
             next(reader)  # Пропускаем строку заголовка

         for row in reader:
             recipients.append({k: v.strip() for k, v in row.items()})

     return recipients


 def validate_recipient(recipient: Dict[str, str]) -> None:
     '''Проверяет валидность данных получателя.'''
     if not all(recipient.values()):
         raise InvalidDataError("Missing required fields")

     notification_type = NotificationType.from_string(recipient["type"])
     if notification_type is None:
         raise InvalidDataError(f"Invalid notification type '{recipient['type']}'")

     if notification_type == NotificationType.EMAIL and not is_valid_email(recipient["address"]):
         raise InvalidDataError(f"Invalid email format '{recipient['address']}'")

     if notification_type == NotificationType.TELEGRAM and not is_valid_telegram_id(recipient["address"]):
         raise InvalidDataError(f"Invalid Telegram ID '{recipient['address']}'")


 def send_notification(recipient: Dict[str, str], config: NotificationConfig) -> None:
     '''Отправляет одно уведомление.'''
     notification_type = NotificationType.from_string(recipient["type"])

     handlers = {
         NotificationType.EMAIL: (
             lambda cfg: not cfg["skip_email"],
             MessageTemplates.EMAIL
         ),
         NotificationType.TELEGRAM: (
             lambda cfg: not cfg["skip_telegram"],
             MessageTemplates.TELEGRAM
         ),
     }

     if notification_type in handlers:
         should_send, template = handlers[notification_type]
         if should_send(config):
             logger.info(template.format(**recipient))


 def send_notifications(config: NotificationConfig, csv_path: str) -> None:
     '''
     Send notifications to recipients based on data from CSV file.

     Args:
         config: Dictionary with notification settings:
             - skip_email: bool - whether to skip email notifications
             - skip_telegram: bool - whether to skip telegram notifications
         csv_path: Path to CSV file with recipient data

     CSV file format:
         name, type, address, message
     '''
     try:
         csv_path = Path(csv_path).resolve()
         logger.info(f"Processing notifications from file: {csv_path}")

         if not csv_path.exists():
             raise FileNotFoundError(f"CSV file not found at {csv_path}")

         recipients = read_recipients(csv_path)

         for row_num, recipient in enumerate(recipients, start=1):
             try:
                 validate_recipient(recipient)
                 send_notification(recipient, config)
             except InvalidDataError as e:
                 logger.warning(f"Row {row_num}: {str(e)}, skipping")
             except Exception as e:
                 logger.error(f"Row {row_num}: Error processing recipient - {str(e)}")
                 continue

     except FileNotFoundError as e:
         logger.error(str(e))
     except csv.Error as e:
         logger.error(f"CSV parsing error: {str(e)}")
     except Exception as e:
         logger.error(f"Unexpected error: {str(e)}")
     else:
         logger.info("Notifications processing completed successfully")


 if __name__ == "__main__":
     config: NotificationConfig = {
         "skip_email": False,
         "skip_telegram": False
     }
     send_notifications(config, csv_path="list.csv")



 # ЗАДАЧА 3 ЗА СКОЛЬКО ОРАБОТАЕТ АСИНХРОННЫЙ КОД И КАКИЕ БУДУТ ПРИНТЫ

 import asyncio

 async def fetch_data(delay):
     print(f"Inside function before {delay} sleep...")
     await asyncio.sleep(delay)
     print(f"Inside function after {delay} sleep...")
     return delay

 async def main():
     await fetch_data(1)
     await fetch_data(2)
     await fetch_data(3)

 asyncio.run(main())


 # ОТВЕТ ЗАДАЧА 3 ЗА СКОЛЬКО ОРАБОТАЕТ АСИНХРОННЫЙ КОД И КАКИЕ БУДУТ ПРИНТЫ

 # ВЫПОЛНЕНИЕ БУДЕТ ЗА 6 СЕКУНД   Работает ПОСЛЕДОВАТЕЛЬНО, а НЕ ПАРАЛЛЕЛЬНО(асинхронно).

 # Использование await перед каждой функцией в исходном коде заставляет их выполняться ПОСЛЕДОВАТЕЛЬНО, а НЕ ПАРАЛЛЕЛЬНО.
 # Коротко: await блокирует текущую корутину, пока операция не завершится → выполнение становится последовательным.


 import asyncio

 async def fetch_data(delay):
     print(f"Inside function before {delay} sleep...")
     await asyncio.sleep(delay)
     print(f"Inside function after {delay} sleep...")
     return delay

 async def main():
     await fetch_data(1)
     await fetch_data(2)
     await fetch_data(3)

 asyncio.run(main())

 # ВЫВОД
 # Inside function before 1 sleep...
 # Inside function after 1 sleep...
 # Inside function before 2 sleep...
 # Inside function after 2 sleep...
 # Inside function before 3 sleep...
 # Inside function after 3 sleep...


 # РАБОТАЕТ 3 СЕКУНДЫ  ПАРАЛЛЕЛЬНО(асинхронно), нужно использовать asyncio.gather() или asyncio.create_task().

 import asyncio

 # asyncio.create_task() (КОНТРОЛЬ над задачами)            # asyncio.gather()  (рекомендуется для простых случаев)
 async def fetch_data(delay):                               async def fetch_data(delay):
     print(f"Inside function before {delay} sleep...")          print(f"Inside function before {delay} sleep...")
     await asyncio.sleep(delay)                                 await asyncio.sleep(delay)
     print(f"Inside function after {delay} sleep...")           print(f"Inside function after {delay} sleep...")
     return delay                                               return delay

 async def main():                                          async def main():
     # Создаем задачи (они запускаются сразу)                   # Запускаем все корутины параллельно
     task1 = asyncio.create_task(fetch_data(1))                 await asyncio.gather(
     task2 = asyncio.create_task(fetch_data(2))                     fetch_data(1),
     task3 = asyncio.create_task(fetch_data(3))                     fetch_data(2),
                                                                    fetch_data(3)
     # Ждем завершения всех задач                               )
     await task1
     await task2
     await task3

 asyncio.run(main())                                        asyncio.run(main())

 # ВЫВОД                                                    # ВЫВОД
 # Inside function before 1 sleep...                        # Inside function before 1 sleep...
 # Inside function before 2 sleep...                        # Inside function before 2 sleep...
 # Inside function before 3 sleep...                        # Inside function before 3 sleep...
 # Inside function after 1 sleep...                         # Inside function after 1 sleep...
 # Inside function after 2 sleep...                         # Inside function after 2 sleep...
 # Inside function after 3 sleep...                         # Inside function after 3 sleep...



 # ЗАДАЧА 4 НАПИСАТЬ ТЕСТЫ ДЛЯ ФУНКЦИИ

 def division(a, b):
     return a / b


 # ОТВЕТ ЗАДАЧА 4 НАПИСАТЬ ТЕСТЫ ДЛЯ ФУНКЦИИ

 import pytest

 def test_division_normal_cases():
     # Тестирование нормальных случаев
     assert division(10, 2) == 5.0
     assert division(9, 3) == 3.0
     assert division(1, 2) == 0.5
     assert division(0, 5) == 0.0
     assert division(-10, 2) == -5.0
     assert division(-9, -3) == 3.0


 def test_division_float_result():
     # Тестирование случаев с дробным результатом
     assert division(5, 2) == 2.5
     assert division(1, 3) == pytest.approx(0.333333, rel=1e-6)


 def test_division_by_zero():
     # Тестирование деления на ноль
     with pytest.raises(ZeroDivisionError):
         division(10, 0)

     with pytest.raises(ZeroDivisionError):
         division(0, 0)


 def test_division_invalid_input():
     # Тестирование неверного ввода (не числа)
     with pytest.raises(TypeError):
         division("10", 2)

     with pytest.raises(TypeError):
         division(10, "2")

     with pytest.raises(TypeError):
         division("a", "b")



 # ЗАДАЧА 5 НАПИСАТЬ СОБСТВЕННЫЙ КОНТЕКСТНЫЙ МЕНЕДЖЕР (НАПИШИ 2 ВАРИАНТА)

 class HybridContext:
     def __init__(self):
         pass


 def __enter__(self):
     return self


 def __exit__(self, exc_type, exc_val, exc_tb):


 with HybridContext(127.0.1.1) as e:
     ...


 # ОТВЕТ ЗАДАЧА 5 НАПИСАТЬ СОБСТВЕННЫЙ КОНТЕКСТНЫЙ МЕНЕДЖЕР (НАПИШИ 2 ВАРИАНТА)

 # ВАРИАНТ 1 Собственная реализация контекстного менеджера

 # Исключения подавляются, так как метод __exit__ возвращает True.
 class HybridContext:
     def __init__(self, ip_address):
         self.ip_address = ip_address

     def __enter__(self):
         print(f"Подключение к {self.ip_address}")
         return self

     def __exit__(self, exc_type, exc_val, exc_tb):
         print(f"Отключение от {self.ip_address}")
         if exc_type is not None:
             print(f"Произошла ошибка: {exc_val}")
         return True  # Подавляем исключения


 # Использование
 with HybridContext("127.0.1.1") as e:
     print(F"Выполнение кода внутри контекста")
     # raise Exception("Тестовая ошибка")  # Раскомментируйте для теста обработки ошибок

 # ВЫВОД
 # Подключение к 127.0.1.1
 # Выполнение кода внутри контекста
 # Отключение от 127.0.1.1



 # ВАРИАНТ 2 Реализация с использованием contextlib
 from contextlib import contextmanager

 @contextmanager
 def hybrid_context(ip_address):
     print(f"Подключение к {ip_address}")
     try:
         yield ip_address
     except Exception as e:
         print(f"Произошла ошибка: {e}")
         # return True  # Чтобы было подавление исключений
     finally:
         print(f"Отключение от {ip_address}")

 # Использование
 with hybrid_context("127.0.1.1") as ip:
     print(f"Выполнение кода внутри контекста с IP {ip}")
     # raise Exception("Тестовая ошибка")  # Раскомментируйте для теста обработки ошибок

 # ВЫВОД
 # Подключение к 127.0.1.1
 # Выполнение кода внутри контекста с IP 127.0.1.1
 # Отключение от 127.0.1.1
________________________________________________________________________________________________________________________

 # ЗАДАЧА Integer to Roman (leetcode)    SmartKit  Ритейл-Процессинг


 # Все варианты работают за O(1) по времени и O(1) по памяти (так как используют фиксированный объем дополнительной памяти)

 # Вариант 4 (жесткое кодирование) - самый быстрый на реальных данных, так как не содержит циклов и рекурсии.
 # Остальные варианты чуть медленнее из-за циклов, но разница незначительна для ограниченного диапазона входных чисел.


 # ВАРИАНТ ЧЕРЕЗ  библиотеку pip install roman
 import roman

 def intToRoman(num: int) -> str:
     try:
         return roman.toRoman(num)
     except roman.InvalidRomanNumeralError:
         return "Invalid number (must be 1-3999)"

 print(intToRoman(3749))  # -> MMMDCCXLIX
 print(intToRoman(58))    # -> LVIII
 print(intToRoman(1994))  # -> MCMXCIV


 # ВАРИАНТ 1  Жадный алгоритм с фиксированными значениями
 def intToRoman(num: int) -> str:
     values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
     symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
     roman = []
     for i in range(len(values)):
         while num >= values[i]:
             roman.append(symbols[i])
             num -= values[i]
     return ''.join(roman)


 # ВАРИАНТ 2  Использование списка кортежей
 def intToRoman(num: int) -> str:
     val_symbols = [
         (1000, 'M'),
         (900, 'CM'),
         (500, 'D'),
         (400, 'CD'),
         (100, 'C'),
         (90, 'XC'),
         (50, 'L'),
         (40, 'XL'),
         (10, 'X'),
         (9, 'IX'),
         (5, 'V'),
         (4, 'IV'),
         (1, 'I')
     ]
     roman = []
     for val, symbol in val_symbols:
         while num >= val:
             roman.append(symbol)
             num -= val
         if num == 0:
             break
     return ''.join(roman)


 # ВАРИАНТ 3  Использование словаря
 def intToRoman(num: int) -> str:
     val_to_roman = {
         1000: 'M',
         900: 'CM',
         500: 'D',
         400: 'CD',
         100: 'C',
         90: 'XC',
         50: 'L',
         40: 'XL',
         10: 'X',
         9: 'IX',
         5: 'V',
         4: 'IV',
         1: 'I'
     }
     roman = []
     for val in sorted(val_to_roman.keys(), reverse=True):
         while num >= val:
             roman.append(val_to_roman[val])
             num -= val
     return ''.join(roman)


 # ВАРИАНТ 4 Жесткое кодирование для каждой цифры  # Очень быстрое решение (O(1) по времени, так как нет циклов).
 def intToRoman(num: int) -> str:
     thousands = ["", "M", "MM", "MMM"]
     hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
     tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
     ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

     return (
         thousands[num // 1000] +
         hundreds[(num % 1000) // 100] +
         tens[(num % 100) // 10] +
         ones[num % 10]
     )


 # ВАРИАНТ 5  Рекурсивный подход
 def intToRoman(num: int) -> str:
     val_symbols = [
         (1000, 'M'),
         (900, 'CM'),
         (500, 'D'),
         (400, 'CD'),
         (100, 'C'),
         (90, 'XC'),
         (50, 'L'),
         (40, 'XL'),
         (10, 'X'),
         (9, 'IX'),
         (5, 'V'),
         (4, 'IV'),
         (1, 'I')
     ]
     for val, symbol in val_symbols:
         if num >= val:
             return symbol + intToRoman(num - val)
     return ""  # для num = 0

 print(intToRoman(3749))  # -> MMMDCCXLIX
 print(intToRoman(58))    # -> LVIII
 print(intToRoman(1994))  # -> MCMXCIV
________________________________________________________________________________________________________________________













 # --- SQL Задача с собеседования ---

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


 # Первый вариант
 Чтобы получить имена пользователей, которые когда-либо делали заказы на продукты, использовать следующий SQL-запрос:

 SELECT DISTINCT u.name
 FROM users u
 JOIN orders o ON u.id = o.user_id
 JOIN products p ON o.product_id = p.id;

 ### Объяснение:
 1. Используем `JOIN` для соединения таблицы `users` с таблицей `orders` по `user_id`.
 2. Затем соединяем таблицу `orders` с таблицей `products` по `product_id`.
 3. Используем `DISTINCT`, чтобы избежать дублирования имен пользователей, если они сделали несколько заказов.



 # Второй вариант
 **Использование `LEFT JOIN` для получения всех пользователей и их продуктов (если есть):**

 SELECT u.name, p.name AS product_name
 FROM users u
 LEFT JOIN orders o ON u.id = o.user_id
 LEFT JOIN products p ON o.product_id = p.id;

 В этом запросе вы получите всех пользователей и, если они сделали заказ, соответствующий продукт.
________________________________________________________________________________________________________________________

 # Задача SQL                                   С книгами сильный чел
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


 # Мой вариант

 select product, sum(count) AS c
 from sales
 where year = '2024'
 group by product
 having sum(count) > 2;


 # Второй вариант

 SELECT product, COUNT(*) AS c
 FROM sales
 WHERE CAST(year AS CHAR) REGEXP '2024'
 GROUP BY product
 HAVING COUNT(*) > 2;
________________________________________________________________________________________________________________________

 Вернуть авторов, которые написали более двух книг      ivi  Иви
 CREATE TABLE author (id SERIAL PRIMARY KEY, name TEXT);
 CREATE TABLE book (id SERIAL PRIMARY KEY, title TEXT, publication_date DATE, author_id integer REFERENCES author (id));
 INSERT INTO author(name) VALUES ('Автор 1'), ('Автор 2'), ('Автор 3');
 INSERT INTO book(title, publication_date, author_id) VALUES ('Книга 1', '2017-04-01', 1),
 ('Книга 2', '2018-04-01', 1), ('Книга 3', '2018-05-01', 2);



 # Мой ответ

 SELECT a.name, COUNT(b.id) AS book_count
 FROM author AS a
 JOIN book AS b ON b.author_id = a.id
 GROUP BY a.id, a.name
 HAVING COUNT(b.id) > 2;



 #  Вариант 2: Использование подзапроса

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
________________________________________________________________________________________________________________________

 # Задача SQL  СИБУР    Исправить код

 # Исправить код
 SELECT
     C.customer_name,
     SUM(COALESCE(O.order_amt, 0)) AS total
 FROM Customers AS C
 LEFT JOIN Orders AS O ON C.customer_nbr = O.customer_nbr
 WHERE
     O.order_date >= '2021-01-01'
 GROUP BY
     C.customer_name


 # Ответ
 SELECT
     C.customer_name,
     SUM(COALESCE(O.order_amt, 0)) AS total
 FROM Customers AS C
 LEFT JOIN Orders AS O ON C.customer_nbr = O.customer_nbr AND O.order_date >= '2021-01-01'
 GROUP BY
     C.customer_name;
________________________________________________________________________________________________________________________

 Задача SQL  СИБУР

 /* Есть таблица t1 <PK, A1, A2, …, AN, T > PK – идентификатор объекта A1, …, AN – это атрибуты T – это время фиксации значения.
  Напиши SQL, который вернёт последнюю загруженную запись по оси T для каждого PK. */

 PK A1 A2 A3 A4 T
 1  1  1  1  1  1
 1  1  1  1  2  2
 1  1  1  1  1  3
 1  2  1  1  2  4
 1  1  1  1  1  5
 2  2  3  4  5  3

 Что должно быть на выходе
 -> PK A1 A2 A3 A4  T
    1   1  1  1  1  5
    2   2  3  4  5  3


 # Ответ
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
________________________________________________________________________________________________________________________

 ВК  2 задачи в одной (ДВА В ОДНОМ)

 goods (id, title, type, price)

 1) Нужно получить количество товаров каждого типа с ценой товара больше 15.

 -- Эти запросы подсчитают все товары с price > 15, независимо от того, есть ли NULL в title или нет.
 SELECT type, COUNT(*) AS goods_count  SELECT type, COUNT(id) AS goods_count  SELECT type, COUNT(1) AS goods_count
 FROM goods                            FROM goods                             FROM goods
 WHERE price > 15                      WHERE price > 15                       WHERE price > 15
 GROUP BY type;                        GROUP BY type;                         GROUP BY type;

 -- Если title НЕ содержит NULL значений    -- Если title содержит NULL значений
 SELECT type, COUNT(title) AS goods_count   SELECT type, COUNT(title) AS goods_count
 FROM goods                                 FROM goods
 WHERE price > 15                           WHERE price > 15 AND title is not NULL
 GROUP BY type;                             GROUP BY type;


 2) Нужно получить количество товаров каждого типа с ценой товара больше 15. Показать нужно только количество меньше 5.

  -- Эти запросы подсчитают все товары с price > 15, независимо от того, есть ли NULL в title или нет.
 SELECT type, COUNT(*) AS goods_count  SELECT type, COUNT(id) AS goods_count  SELECT type, COUNT(1) AS goods_count
 FROM goods                            FROM goods                             FROM goods
 WHERE price > 15                      WHERE price > 15                       WHERE price > 15
 GROUP BY type                         GROUP BY type                          GROUP BY type
 HAVING COUNT(*) < 5;                  HAVING COUNT(id) < 5;                  HAVING COUNT(1) < 5;

 -- Вариант 1 (использование алиаса)        -- Вариант 2 (использование агрегатной функции)
 SELECT type, COUNT(title) AS goods_count   SELECT type, COUNT(title) AS goods_count
 FROM goods                                 FROM goods
 WHERE price > 15                           WHERE price > 15
 GROUP BY type                              GROUP BY type
 HAVING goods_count < 5;                    HAVING COUNT(title) < 5;


 # Все 4 варианта (COUNT(*), COUNT(1), COUNT(id), COUNT(title)) дадут одинаковый результат, если:
 id является PRIMARY KEY (значит не может быть NULL)
 title не содержит NULL значений

 # Разбор вариантов COUNT(*), COUNT(1), COUNT(id), COUNT(title)
 COUNT(*) - считает все строки в группе, включая NULL.  COUNT(*) будет наиболее предпочтительным вариантом.
 COUNT(1) - эквивалентен COUNT(*), потому что 1 - это не-NULL константа, и она учитывается для каждой строки.
 COUNT(id) - считает только строки, где id не NULL (если id - PRIMARY KEY, разницы с COUNT(*) нет).
 COUNT(title) - считает только не-NULL значения title
________________________________________________________________________________________________________________________



________________________________________________________________________________________________________________________
 --- END  Задачи с Собеседования ---
________________________________________________________________________________________________________________________



 # Задача "Расстановка скобок в коде"
 def validBraces(string):
     braces = {')': '(', '}': '{', ']': '['}
     stack = []
     for i, v in enumerate(string, start=1):
         if v in braces.values():
             stack.append((v, i))
         if v in braces and (not stack or braces[v] != stack.pop()[0]):
             return i
     return stack.pop()[1] if stack else 'Success'

 print(validBraces('([](){([])})'))  # Success
 print(validBraces('()[]}'))         # 5


 # Вроде правильный вариант но не проходил все Тесты
 def validBraces(string):
     s = string
     for _ in string:
         string = string.replace('{}', '').replace('()', '').replace('[]', '')
     return 'Success' if not string else len(s)

 print(validBraces('([](){([])})'))  # Success
 print(validBraces('()[]}'))         # 5
 print(validBraces('{{[()]]'))       # 5
________________________________________________________________________________________________________________________

 # Задача "Высота дерева"

 # Вариант 1
 from functools import lru_cache

 @lru_cache(maxsize=None)
 def count(data, i):
     return (data[i] == -1 and 1 or count(data, data[i]) + 1)

 num, data = 10, (9, 7, 5, 5, 2, 9, 9, 9, 2, -1)
 print(max(count(data, i) for i in range(num)))   # -> 4


 # Вариант 2
 n = 10
 s = [9, 7, 5, 5, 2, 9, 9, 9, 2, -1]

 def countd(i):
     if d[i] == - 1:
         d[i] = countd(s[i]) + 1
     return d[i]

 d = [-1] * (len(s)) + [0]
 [countd(i) for i in range(len(s))]
 print(max(d))                                      # -> 4

________________________________________________________________________________________________________________________

 # Максимум в скользящем окне    # Sliding Window Maximum

 # Скользящее окно – это фиксированный отрезок данных, который шаг за шагом перемещается по последовательности,
 # обрабатывая каждый участок (например, считая среднее).

 Данные: [1, 2, 3, 4, 5], окно = 3.

 Шаги:
 [1, 2, 3] → считаем
 [2, 3, 4] → считаем
 [3, 4, 5] → считаем


 # Вариант с exec
 exec('''def convert(iterable, m):
     t = [iterable[x:] for x in range(m)]
     result = [max(i) for i in zip(*t)]
     return result

 print(convert([2, 7, 3, 1, 5, 2, 6, 2], 3))  # -> [7, 7, 5, 5, 6, 6]
 ''')

 # Вариант zip
 def convert(iterable, m):
     t = [iterable[x:] for x in range(m)]
     result = [max(i) for i in zip(*t)]
     return result

 print(convert([2, 7, 3, 1, 5, 2, 6, 2], 3))   # -> [7, 7, 5, 5, 6, 6]


 # Вариант Обычный
 def convert2(listi, m):
     listo = []
     n = len(listi)
     for i in range(n-m+1):
         listo.append(max(listi[i:3+i]))
     return listo

 print(convert2([2, 7, 3, 1, 5, 2, 6, 2], 3))  # -> [7, 7, 5, 5, 6, 6]
________________________________________________________________________________________________________________________

 Задача на программирование: небольшое число Фибоначчи    Посмотри тесты в конце!!!    Важно!!! <-----    <-----

 # Скорость O(1)                      # Скорость O(1)
 def fibonacci__1(n):                 import math
     if n == 0:
         return 0                     def fibonacci__2(n):
     elif n == 1:                         phi = (1 + math.sqrt(5)) / 2
         return 1                         return round((phi**n - (1 - phi)**n) / math.sqrt(5))

     a, b = 0, 1
     for _ in range(2, n + 1):
         a, b = b, a + b
     return b

 n = 7                                 n = 7
 print(fibonacci__1(n))  # -> 13       print(fibonacci__2(n))   # -> 13


 # Решения с мемоизацией КЭШ  Скорость O(n)   НО С ОЧЕНЬ БОЛЬШИМИ ЧИСЛАМИ НЕ БУДЕТ РАБОТАТЬ!!! ЛУЧШЕ ВЫБРАТЬ fibonacci__1
 # @__import__('functools').lru_cache(maxsize=None)  #  Так тоже можно импортировать
 @functools.lru_cache(maxsize=None)
 def fibonacci__3(n):
     if n < 2:
         return n
     else:
         return fibonacci__3(n - 1) + fibonacci__3(n - 2)

 n = 7
 print(fibonacci__3(n))  # -> 13


 # Простая функция  if/else                               # Простая функция  match/case     <-----  Посмотри тесты в конце!!!
 def fibonacci__0(n):                                     def fib(n):
     if n < 2:                                                match n:
         return n                                                 case 0 | 1:
     else:                                                            return n
         return fibonacci__0(n - 1) + fibonacci__0(n - 2)         case _:
                                                                    return fib(n - 1) + fib(n - 2)
 n = 7                                                    n = 7
 print(fibonacci__0(n))  # -> 13                          print(fibonacci__0(n))  # -> 13


 # Замеры с параметром 50!!!
 print(timeit.timeit('fibonacci__1(50)', globals=globals()))                          # -> 2.737594800069928
 print(timeit.timeit('fibonacci__2(50)', globals=globals()))                          # -> 1.235288399970159
 print(timeit.timeit('fibonacci__3(50)', globals=globals()))                          # -> 0.10358340013772249

 # Замер простой функции с параметром ТОЛЬКО 10!!!
 print(timeit.timeit('fibonacci__0(10)', globals=globals()))                          # -> 16.955934199970216
 # Замер match case простой функции с параметром ТОЛЬКО 10!!!
 print(timeit.timeit('fib(10)', globals=globals()))                                   # -> 24.523009299999103


 # Тоже самое но с setup()
 print(timeit.timeit('fibonacci__1(50)', setup="from __main__ import fibonacci__1"))  # -> 2.7405860000289977
 print(timeit.timeit('fibonacci__2(50)', setup="from __main__ import fibonacci__2"))  # -> 1.2412337001878768
 print(timeit.timeit('fibonacci__3(50)', setup="from __main__ import fibonacci__3"))  # -> 0.09871609997935593

 # Замер простой функции с параметром ТОЛЬКО 10!!!
 print(timeit.timeit('fibonacci__0(10)', setup="from __main__ import fibonacci__0"))  # -> 16.960932299960405

 # Замер match case простой функции с параметром ТОЛЬКО 10!!!
 print(timeit.timeit('fib(10)', setup="from __main__ import fib"))                    # -> 24.574260200140998


 times = {
     'fibonacci__1': round(timeit.timeit('fibonacci__1(50)', globals=globals()), 3),
     'fibonacci__2': round(timeit.timeit('fibonacci__2(50)', globals=globals()), 3),
     'fibonacci__3': round(timeit.timeit('fibonacci__3(50)', globals=globals()), 3),
     'Default': round(timeit.timeit('fibonacci__0(10)', globals=globals()), 3),
     'Default match case': round(timeit.timeit('round(fib(10), 2)', globals=globals()), 3),
 }

 # Оценим время, за которое они завершили исполнение!   Странно match case очень долго работает
 print(sorted(times.items(), key=lambda x: x[1]))
 # [('fibonacci__3', 0.104), ('fibonacci__2', 1.225), ('fibonacci__1', 2.692), ('Default', 17.286), ('Default match case', 25.659)]
________________________________________________________________________________________________________________________


________________________________________________________________________________________________________________________


________________________________________________________________________________________________________________________


________________________________________________________________________________________________________________________


________________________________________________________________________________________________________________________


________________________________________________________________________________________________________________________


________________________________________________________________________________________________________________________


________________________________________________________________________________________________________________________


________________________________________________________________________________________________________________________


________________________________________________________________________________________________________________________


 --- Интересные решения ---

 На вход подается 5 чисел, что нам нужно с ними сделать, запоминаем:
 - Первое число умножить на второе число
 - К результату прибавить третье число
 - Из результата вычесть четвертое число
 - То что получилось поделить на пятое число

 # Входные данные [a = 5, b = 14, c = 8.0, d = 6, e = 3]

  # Тоже самое
 a = float(input())  # 5
 b = float(input())  # 14
 c = float(input())  # 8.0
 d = float(input())  # 6
 e = float(input())  # 3
 print((((a*b)+c)-d)/e)                                     # -> 24.0


 # Тоже самое
 res = float(input())
 for op in ('mul', 'add', 'sub', 'truediv'):
     res = getattr(res, f'__{op}__')(float(input()))
 print(res)                                                 # -> 24.0


 # Тоже самое
 n1, n2, n3, n4, n5 = (float(input()) for _ in range(5))
 print((n1 * n2 + n3 - n4) / n5)                            # -> 24.0
 -----------------------------------------------------------------------------------------------------------------------

 # Сумма чисел
 total = 0
 while (number := input()) != 'конец':
     total += int(number)
 print(total)
 -----------------------------------------------------------------------------------------------------------------------

 # На вход программе подается некоторое количество слов, а далее текст "сколько" и слово, количество которого считаем
 res = []
 while True:
     m = input()
     if m == 'сколько':
         print(res.count(input()))
         break
     else:
         res.append(m)
 -----------------------------------------------------------------------------------------------------------------------

 # Моржа :=  Можно оборачивать в скобки () и Лучше всегда его оборачивать
 #  у "моржа" самый низкий приоритет:   приоритет присваивания самый низкий   :=     Поэтому оборачиваем в ()   (a:=1)

 # str.format
 print('Если перевернуть слово "{0}", получится "{1}".'.format((s := 'Hello'), s[::-1]))  # Тут смотри моржа
 # f-строка
 print(f'Если перевернуть слово "{(s:="Hello")}", получится "{s[::-1]}".')                # Тут смотри моржа
 # -> Если перевернуть слово "Hello", получится "olleH".
 -----------------------------------------------------------------------------------------------------------------------

 # Сразу применить в ф-строке несколько +_  можно без ()
 s = 5000                                  s = 345
 s1 = 756                                  s1 = 786
 print(f'{(s-s1):+_}')  # -> +4_244        print(f'{s-s1:+_}')  # -> -441
 -----------------------------------------------------------------------------------------------------------------------

 # Поменяйте местами минимальный и максимальный элемент
 lst = [1, 2, 3, 4, 5]
 mx, mn = lst.index(max(lst)), lst.index(min(lst))
 lst[mx], lst[mn] = lst[mn], lst[mx]
 print(*lst)  # -> 5 2 3 4 1
 -----------------------------------------------------------------------------------------------------------------------

 # Ход ладьи   может ли ладья попасть с первой клетки на вторую одним ходом.
 x1, y1, x2, y2 = [3, 5, 7, 2]
 if (-1 <= x1 - x2 <= 1) and (-1 <= y1 - y2 <= 1):
     print(f'ДА')
 else:
     print(f'НЕТ')
 -----------------------------------------------------------------------------------------------------------------------

 # Необходимо сравнить первое число со вторым и вывести <=>
 a, b = [4, 6]
 print('>' if a > b else '<' if a < b else '=')  # -> <
 -----------------------------------------------------------------------------------------------------------------------

 # Калькулятор
 # lst = input().split()
 # x, y = input().split()
 # symbol = input()

 x, y = '7.0', '0'
 symbol = '/'
 try:
     print(float(eval(x + symbol + y)))
 except:
     print("Некорректная операция")  # -> Некорректная операция
 -----------------------------------------------------------------------------------------------------------------------

 # Классный пример c моржом и pass внутри

 psw = 'Password'                                      psw = 'Password'
 while (enter := input('Введите пароль: ')) != psw:    for i in iter(input, psw):
     pass                                                  pass
 print('Вход в систему')                               print('Вход в систему')


 # Можно через ; делать
 # Тоже самое           # Тоже самое
 a, b = 15, 45          a, b = 15, 45
 c = 0                  c = 0
 while a <= b:          while a <= b:
     a *= 3                 a *= 3; b *= 2; c += 1   # Вот тут ;
     b *= 2             print(c)  # -> 3
     c += 1
 print(c)  # -> 3
 -----------------------------------------------------------------------------------------------------------------------



 --- else в Циклах while и for ---
 # Важно else в циклах while и for!!!  <-----                                      <-----

 # else НЕ срабатывает в цикле while           # else срабатывает в цикле while    <-----           <-----
 c = 0                                         c = 0
 while c < 5:                                  while c < 5:
     c += 1                                        c += 1
     if c == 4:                                    if c == 100:
         break                                         break
 else:                                         else:
     print('Цикл while отработал полностью')        print('Цикл while отработал полностью')  # -> Цикл while отработал полностью



 # else НЕ срабатывает в цикле for            # else срабатывает в цикле for       <-----           <-----
 c = 0                                        c = 0
 for i in range(5):                           for i in range(5):
     c += 1                                       c += 1
     if c == 4:                                   if c == 100:
         break                                        break
 else:                                        else:
     print('Цикл for отработал полностью')        print('Цикл for отработал полностью')  # -> Цикл for отработал полностью
 -----------------------------------------------------------------------------------------------------------------------


 # Необходимо реализовать игру в "Города"  Следующее слово начинается на букву, которой оканчивалось предыдущее.
 lst = ['Гжижевск', 'Королевыьъ', 'Вайфаеград']

 res = []
 for i, v in enumerate(lst):
     if i == 0:
         continue
     if lst[i-1][-1].lower() in "ыьъ":
         if lst[i-1][-2].lower() == lst[i][0].lower():
             res.append(True)
             continue
     if lst[i-1][-1].lower() == lst[i][0].lower():
         res.append(True)
         continue
     else:
         res.append(False)

 print('ДА' if all(res) else 'НЕТ')  # -> НЕТ
 -----------------------------------------------------------------------------------------------------------------------

 -- enumerate vs range(len(lst)) --

 # Тоже самое                       # Тоже самое                           # Внутри enumerate Кортежи (индекс, значение)
 lst = ['a', 'b', 'c', 'd']         lst = ['a', 'b', 'c', 'd']             lst = ['a', 'b', 'c', 'd']

 for i, v in enumerate(lst):        for i in range(len(lst)):              for i in enumerate(lst):
     print(f'{i}={v}', end='  ')        print(f'{i}={lst[i]}', end='  ')       print(f'{i}', end='  ')
 # -> 0=a  1=b  2=c  3=d            # -> 0=a  1=b  2=c  3=d                # -> (0, 'a')  (1, 'b')  (2, 'c')  (3, 'd')
 -----------------------------------------------------------------------------------------------------------------------

 # Лесенка из чисел и выводится на экран.            # Вывод
 n = 3
 for i in range(1, n+1):                             # 1
     a = ''                                          # 1 2
     for j in range(1, i+1):                         # 1 2 3
         a += str(j)+' '
     print(a.strip())
 -----------------------------------------------------------------------------------------------------------------------


 # За раз можно взять только одну гантель.                        # За раз можно взять только одну гантель.
 l, target = sorted([1, 2, 4, 8, 16, 32, 64], reverse=True), 255  target = 255
 arr = []                                                         res = []
 res = target                                                     for x in [64, 32, 16, 8, 4, 2, 1]:
 while target != 0:                                                   while 1 <= x <= target: target -= x; res.append(x)
     for el in l:                                                 print(res)  # -> [64, 64, 64, 32, 16, 8, 4, 2, 1]
         if el <= target:
             res -= el
             arr.append(el)
             break
     target -= el
 print(arr)  # -> [64, 64, 64, 32, 16, 8, 4, 2, 1]


 # Моё решение
 # За раз можно взять только одну гантель.
 target = 255
 dumbbells = (1, 2, 4, 8, 16, 32, 64)

 res = []
 c = 0
 for i in dumbbells[::-1]:
     while sum(res) < target or i < target:
         if c + i <= target:
             res.append(i)
             c += i
             continue
         else:
             break
 print(res)  # -> [64, 64, 64, 32, 16, 8, 4, 2, 1]
 -----------------------------------------------------------------------------------------------------------------------

 # Сколько дней в каком-нибудь месяце.

 from calendar import monthrange
 days = monthrange(2023, 4)[1]
 print(days)  # -> 30
 days = monthrange(2023, 4)
 print(days)  # -> (5, 30)
 -----------------------------------------------------------------------------------------------------------------------

 # Достать значения
 lst = [
     {
      'id': 1, 'name': 'fruits',
      'list': ['apples', 'bananas', 'oranges']
     },
 ]

 print([list(i.items())[-1][-1] for i in lst])  # -> [['apples', 'bananas', 'oranges']]
 print([list(s.items())[2][1] for s in lst])    # -> [['apples', 'bananas', 'oranges']]
 -----------------------------------------------------------------------------------------------------------------------

 # Интересный момент с fromkeys При создании можно указать любой словарь даже НЕ пустой
 a_dict = dict.fromkeys('abc', 1)
 print(a_dict)  # -> {'a': 1, 'b': 1, 'c': 1}

 a_dict = {}.fromkeys('abc', 1)
 print(a_dict)  # -> {'a': 1, 'b': 1, 'c': 1}

 a_dict = {1: 2}.fromkeys('abc', 1)
 print(a_dict)  # -> {'a': 1, 'b': 1, 'c': 1}
 -----------------------------------------------------------------------------------------------------------------------

 # dict comprehensions только key
 a_dict = {k: k*2 for k in range(5)}
 print(a_dict)  # -> {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}
 -----------------------------------------------------------------------------------------------------------------------

 # Необходимо вывести все индексы неуникальных слов(встречающихся более 1-го раза)
 lst = ['к', 'п', 'р', 'н', 'г', 'о', 'л', 'о', 'к', 'а', 'п', 'н',]
 print([i for i, v in enumerate(lst) if lst.count(v) > 1])  # -> [0, 1, 3, 5, 7, 8, 10, 11]
-----------------------------------------------------------------------------------------------------------------------

 # Объединить все элементы Разные способы
 lst = [{1, 2}, frozenset({3, 4}), {5, 6}, frozenset({8, 7}), {9, 10}, frozenset({11, 12})]
 print(frozenset(chain.from_iterable(lst)))           # -> frozenset({1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12})
 print(frozenset(set.union(*lst)))                    # -> frozenset({1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12})
 print(frozenset({elem for i in lst for elem in i}))  # -> frozenset({1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12})
 -----------------------------------------------------------------------------------------------------------------------

 # Несколько Переменных и проверок сразу  match  case

 # Срабатывает                           # Срабатывает                           # НЕ Срабатывает
 a, b = 1, '1'                           a, b = 1, '1'                           a, b = 1, 1000

 match a, b:                             match a, b:                             match a, b:
     case int() as x, str() as y:            case int(a), str(b):                    case int(a), str(b):
         print('Integer and String')             print('Integer and String')             print('Integer and String')
     case _:                                 case _:                                 case _:
         print('a != int or b != str')           print('a != int or b != str')           print('a != int or b != str')

 # -> Integer and String                 # -> Integer and String                 # -> a != int or b != str
 -----------------------------------------------------------------------------------------------------------------------

 # Вам необходимо перебрать его и для каждого типа данных, кроме str
 lst = [1, 5.6, '3', [1, 2], (4, 7), {'a': 4}, True]

 for e in lst:
     match e:
         case str():
             continue                                                       # Можно даже так        <-----
         case _:
             print(f'{type(e)}', end=' ')

 # -> <class 'int'> <class 'float'> <class 'list'> <class 'tuple'> <class 'dict'> <class 'bool'>
 -----------------------------------------------------------------------------------------------------------------------

 # отвечает тем же сообщением, что написали ему или s1
 s = 'Как дела?'                                   s = 'Как дела?'
 s1 = 'Пока не родила'                             s1 = 'Пока не родила'

 match s, s1:                                      match s == s1:
     case x, y if x == y:                              case True:
         print('полное соответствие')                      print('полное соответствие')
     case _:                                           case _:
         print(s1)                                         print(s1)
 -----------------------------------------------------------------------------------------------------------------------

 # 2 новых списка. В первом 'облачность' =  'ясно' и 'температура' не менее 25 градусов. Во втором остальное
 lst = [{'номер': 1, 'облачность': 'ясно', 'температура': 26},
        {'номер': 2, 'облачность': 'облачно', 'температура': 18},
        ]

 lst1, lst2 = [], []
 for line in lst:
     match line:
         case {'облачность': 'ясно', 'температура': int(n)} if n >= 25:
             lst1.append(line)
         case _:
             lst2.append(line)
 print(lst1); print(lst2)
 # -> [{'номер': 1, 'облачность': 'ясно', 'температура': 26}]
 # -> [{'номер': 2, 'облачность': 'облачно', 'температура': 18}]


 # Тоже самое
 good, bad = [], []
 for el in lst:
     match el:
         case {'номер': num, 'облачность': cloudy as cl, 'температура': temp as t} if cl == 'ясно' and t >= 25:
             good.append(el)
         case _:
             bad.append(el)
 print(good, bad, sep='\n')
 # -> [{'номер': 1, 'облачность': 'ясно', 'температура': 26}]
 # -> [{'номер': 2, 'облачность': 'облачно', 'температура': 18}]
 -----------------------------------------------------------------------------------------------------------------------

 # Необходимо на основе него создать список lst со вложенными списками   Думаю вспомнишь что надо было сделать)
 tpl = (
     ['name - Побег из Шоушенка', 'year - 1994', 'genre - драма',
      'director - Фрэнк Дарабонт', 'rating - 9.1'],
     ['name: Властелин колец: Возв к', 'year: 2003', 'genre: фэнтези, прик, дра, бое',
      'director: Пит Дже', 'rating: 8.7'],
     {'name': 'Властелин колец: Две крепости', 'year': '2002', 'genre': 'фэнтези, приключения, драма, боевик',
      'director': 'Питер Джексон', 'rating': '8.6'},
     ('name: Иван Васильевич меняет профессию', 'year: 1973', 'genre: комедия, фант, прикл',
      'director: Леонид Гайдай', 'rating: 8.8'),
 )

 def sub_fun(m):
     if m[0] == '{':
         return '['
     if m[0] == '}':
         return ']'

 lst = []
 for i in tpl:
     match i:
         case tuple():
             pass
         case {'name': name, 'rating': rating, **kwargs} if len(kwargs) >= 2 and float(rating) > 8.6:
             lst.append(re.sub(r'[{}]|\'(?=:)|(?<=: )\'', sub_fun, str(i)))
         # case {'name': name, 'rating': rating, **kwargs} if len(kwargs) >= 2 and float(rating) > 8.6:
         #     lst.append([': '.join(j) for j in i.items()])
         case name1, _, _, _, rating1 if 'name' in name1 and 'rating' in rating1 and float(rating1.split()[-1]) > 8.6:
             lst.append([j.replace(' -', ':') for j in i])

 print(*lst, sep='\n')

 # ['name: Побег из Шоушенка', 'year: 1994', 'genre: драма', 'director: Фрэнк Дарабонт', 'rating: 9.1']
 # ['name: Властелин колец: Возв к', 'year: 2003', 'genre: фэнтези, прик, дра, бое', 'director: Пит Дже', 'rating: 8.7']
 -----------------------------------------------------------------------------------------------------------------------

 # возвращает первое уникальное число
 lst = [3, 2, 4, 6, 5, 4, 3, 2, 6, 8, 7, 5, 3]

 def func(a_list):                  def func(nums: list) -> int:
     for i in a_list:                   '''Принимает список и возвращает первое уникальное. Если такое отсутствует, то -1'''
         if a_list.count(i) == 1:       return next((i for i in nums if nums.count(i) == 1), -1)
             return i
     return -1

 print(func(lst))  # -> 8           print(func(lst))  # -> 8
 -----------------------------------------------------------------------------------------------------------------------

 # Запаковка/Распаковка Двапаковка  в список *
 lst = [1, 2, 3, *[4, 5, 6]]
 print(lst)                          # -> [1, 2, 3, 4, 5, 6]
 print(*lst)                         # -> 1 2 3 4 5 6

 *x, y, z = 1, 2, 3, 4, 5
 print(f'{x=}   {y=}   {z=}')        # -> x=[1, 2, 3]   y=4   z=5
 x, *y, z = 1, 2, 3, 4, 5
 print(f'{x=}   {y=}   {z=}')        # -> x=1   y=[2, 3, 4]   z=5
 x, y, *z = 1, 2, 3, 4, 5
 print(f'{x=}   {y=}   {z=}')        # -> x=1   y=2   z=[3, 4, 5]

 d = {1: 'one', 2: 'two'}
 print(*d.items())                   # -> (1, 'one') (2, 'two')


 # Распаковка Двапаковка ** Работает только Внутри словарей
 d = {1: 'one', 2: 'two'}
 print({**d})                         # -> {1: 'one', 2: 'two'}
 print({**d, 3: 'three', 4: 'four'})  # -> {1: 'one', 2: 'two', 3: 'three', 4: 'four'}


 # Хороший пример с игнорированием значений
 lst = [6, 3, 4, 7, 8, 4]

 _, *x, _, = lst
 print(x)  # -> [3, 4, 7, 8]
 -----------------------------------------------------------------------------------------------------------------------

 # Как можно использовать функции!!!
 a = 17

 lst = [bin, oct, hex]
 print(*[i(a) for i in lst])        # -> 0b10001 0o21 0x11
 # Моржик
 print(*[i(b := 17) for i in lst])  # -> 0b10001 0o21 0x11
 -----------------------------------------------------------------------------------------------------------------------

 # Как работает Моржик Посмотри :=

 # Без Моржика                                          # 1 раз обьявляем Моржика := и потом используем
 n = 10
 print(5 <= n < 10 or 101 < n < 201)  # -> # False      print(5 <= (n := 10) < 10 or 101 < n < 201)
 -----------------------------------------------------------------------------------------------------------------------

 # Моржика в условии нельзя
 print((n := 10)+10 if n % 2 == 0 else n-10)  # -> NameError: name 'n' is not defined
 print(n+10 if (n := 10) % 2 == 0 else n-10)  # -> 20
 -----------------------------------------------------------------------------------------------------------------------
 # Шифр Цезаря     # Шифер Цезаря

 s = "zzzbbb"
 shift = 1
 res = ''

 # Вариант 1
 for el in s:
     res+=chr((((ord(el)-97)+shift) % 26) + 97)
 print(res)                                                                                                 # -> aaaccc

 # Вариант 2
 print(*[chr((ord(c)-ord('a')+n)%26+ord('a')) for s,n in [["zzzbbb", 1]] for c in s], sep='')               # -> aaaccc

 # Вариант 3
 s, shift = "zzzbbb", 1 % 26                                                                                # -> aaaccc
 print(''.join([chr(((ord(char) - ord('a') + shift) % 26) + ord('a')) if char.islower() else char for char in s]))


 # Напишите программу-дешифратор шифра цезаря меняем +shift на -shift

 for el in s:
     res+=chr((((ord(el)-97)-shift) % 26) + 97)
 print(res)                                                                                                 # -> yyyaaa

 -----------------------------------------------------------------------------------------------------------------------

 # наибольшее количество подряд идущих одинаковых символов. Если таких несколько – выведите последнюю.
 from itertools import groupby

 s = "aaabbccccaaaab"
 print(*max(((k, len(list(g))) for k, g in groupby(s[::-1])), key=lambda x: x[1]), sep='=')  # -> a=4
 -----------------------------------------------------------------------------------------------------------------------

 # А вот метод format содержит в себе одно важное преимущество.
 # Дело в том, что в модульных проектах не всегда бывает так, что переменная находится в том же окружении, что и строка-шаблон.

 # у нас нет переменной name
 s = f"Моё имя - {name}"          # -> NameError: name 'name' is not defined

 # у нас нет переменной name
 s = "Моё имя - {name}"
 print(s.format(name='Антон'))    # -> Моё имя - Антон   ошибки уже не будет



 #  Можно использовать * и **    в format()
 a_dict = {'A': '1', 'B': '2'}
 a_list = ['C', 2, 'D']

 print('Coordinates: {A} , {B} '.format(**a_dict))       # ->   Coordinates: 1 , 2
 print('Coordinates: {1} , {2} , {0} '.format(*a_list))  # ->   Coordinates: 2 , D , C
 -----------------------------------------------------------------------------------------------------------------------

 # все нули в нем оказались в конце массива, сохранив при этом порядок чисел.
 lst = [10, 0, 3, 0, 4, 0, 0, 5, 6, 7, 8]

 print(sorted(lst, key=lambda x: x == 0))  # -> [10, 3, 4, 5, 6, 7, 8, 0, 0, 0, 0]
 -----------------------------------------------------------------------------------------------------------------------

 # Реализуйте кучу с максимумом в вершине для этого списка.   maxheap   Добавляем к числам минус -
 # Обрати внимание на match case и второй for

 numbers = [1, 5, 2, 6, 3, 7, 4, 8]
 numbers = [-i for i in numbers]
 heapq.heapify(numbers)

 numbers2 = ['insert 20', 'pop', 'insert 0', 'pop', 'insert 4', 'pop', 'end']

 for i in numbers2:
 # for i in iter(input, 'end'):                         # пока не будет слово end
     match i.split():
         case "insert", n:                              # тут интересно
             heapq.heappush(numbers, -int(n))
         case "pop",:
             print(-heapq.heappop(numbers), end=' ')  # -> 20 8 7


 # Тоже самое но с _heapify_max      но каждый раз нужно делать  heapq._heapify_max(numbers)
 numbers = [1, 5, 2, 6, 3, 7, 4, 8]
 heapq._heapify_max(numbers)

 numbers2 = ['insert 20', 'pop', 'insert 0', 'pop', 'insert 4', 'pop', 'end']

 for i in numbers2:
 # for i in iter(input, 'end'):
     match i.split():
         case "insert", n:
             heapq.heappush(numbers, int(n))
             heapq._heapify_max(numbers)
         case "pop",:
             print(heapq._heappop_max(numbers), end=' ')  # -> 20 8 7
 -----------------------------------------------------------------------------------------------------------------------

 # Посчитайте количество високосных годов между ними включительно.

 from calendar import leapdays, isleap

 year1, year2 = int('2020'), int('2028')

 print(len([i for i in range(year1, year2+1) if isleap(i)]))                             # -> 3
 print(leapdays(year1, year2+1))                                                         # -> 3
 print(len([i for i in range(year1, year2 + 1) if __import__('calendar').isleap(i)]))    # -> 3
 -----------------------------------------------------------------------------------------------------------------------

 # Определите количество дней между двумя годами.
 a, b = 2020, 2024

 year1 = datetime.date(a, 1, 1)
 year2 = datetime.date(b, 1, 1)

 print(*re.findall(r'\d+(?= )', str(year2 - year1)))  # -> 1461
 print(abs(year2 - year1).days)                       # -> 1461
 -----------------------------------------------------------------------------------------------------------------------

 # Вывести на экран произведение цифр.
 a = 1984
 from functools import reduce

 lst = [int(i) for i in str(a)]
 print(reduce(lambda x, y: x * y, lst))  # -> 288

 # Классное решение через eval()
 print('*'.join(str(a)))           # -> 1*9*8*4
 print(eval('*'.join(str(a))))     # -> 288


 # Другой Пример
 # Можно через math.prod()
 a = [1, 2, 3, 4]
 print(__import__('math').prod(a))         # -> 24

 # Если пустой, то возвращает 1
 print(__import__('math').prod([]))        # -> 1
 print(reduce(lambda x, y: x * y, [], 1))  # -> 1
 -----------------------------------------------------------------------------------------------------------------------

 # Общее количество секунд перевести в   часы, минуты и секунды
 a = 129700

 import time
 res = time.gmtime(a)
 print(time.strftime("%H:%M:%S", res))         # -> 12:01:40         # f-строки  не работают с time.struct_time

 from datetime import timedelta
 print(str(timedelta(seconds=a)).split()[-1])  # -> 12:01:40
 print(timedelta(seconds=a))                   # -> 1 day, 12:01:40
 -----------------------------------------------------------------------------------------------------------------------

 # Определить, содержится ли в этом числе хотя бы одна цифра 1
 a = 256

 print('Да' if '1' in str(a) else 'Нет')                      # -> Нет
 print(('Нет', 'Да')[str(a).count('1') >= 1])                 # -> Нет

 # Классные решения Пойми почему!
 print(('Нет', 'Да')['1' in str(a)])                          # -> Нет
 print(("Нет", "Да")[any(digit == '1' for digit in str(a))])  # -> Нет
 -----------------------------------------------------------------------------------------------------------------------

 # s = 'aaaabbсaa' преобразуется в 'a4b2с1a2'  Считаем символы которые идут подряд
 a = 'aaaabbcaa'

 # Придумал сам)
 print(re.sub(r'(\w)\1+|\w', lambda x: f'{x[0][0]}{len(x[0])}', a))  # -> a4b2c1a2

 # Первый способ с groupby
 from itertools import groupby

 for k, g in groupby(a):
     print(k, len(list(g)), sep='', end='')  # -> a4b2c1a2


 # Второй способ руками
 a = 'aaaabbcaa'
 genome = a+' '
 s = 0
 n=genome[0]
 for i in genome:
     if n!=i:
         print(n + str(s), end = '')         # -> a4b2c1a2
         s=0
         n=i
     s+=1


 # Тоже руками
 s='aaaabbcaa'
 last_word=s[0]
 last_count=1
 res=''

 for el in s[1:]:
     if el==last_word:
         last_count+=1
     else:
         res+=f'{last_word}{last_count}'
         last_count=1
         last_word=el

 res+=f'{last_word}{last_count}'
 print(res)                                 # -> a4b2c1a2
 -----------------------------------------------------------------------------------------------------------------------

 # Определить, сколько раз в этом списке два одинаковых элемента стоят рядом.
 lst = [1, 2, 2, 3, 4, 4, 5, 6, 6, 6, 7]
 print(sum(lst[i] == lst[i - 1] for i in range(1, len(lst))))  # -> 4

 # Тоже самое
 c=0
 for i in range(len(lst)-1):
     if lst[i]==lst[i+1]:
         c+=1
 print(c)                                                      # -> 4
 -----------------------------------------------------------------------------------------------------------------------

 # Найти все слова длиной не менее 5 символов и содержащие не менее 2 гласных
 s = 'The candle light will burn the whole night'.split()

 for i in s:
     x = sum([1 for l in i if l in 'aeiouy'])
     if len(i) >= 5 and x >= 2:
         print(i, end=' ')                              # ->  candle whole

 # Тоже самое
 for i in s.split():
    if len(i) > 4 and sum(w.lower() in 'aeiouy' for w in i) > 1:
        print(i)                                        # ->  candle whole

 -----------------------------------------------------------------------------------------------------------------------
 Валидация пароля  длина пароля не менее 8 символов   1 строчная, 1  прописная буква и хотя бы 1 цифра

 s = 'hGjk67_sdfkl56'
 print('-+'[bool(re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d_]{8,}$', s))])    # -> +


 # Тоже самое
 answer = '-'

 if bool(re.match('^[a-zA-Z0-9_]{8,}$', s)):
     a = bool(re.search('[a-z]', s))
     b = bool(re.search('[A-Z]', s))
     c = bool(re.search('[0-9]', s))
     answer = ('-+')[a * b * c]

 print(answer)                                                                          # -> +
 -----------------------------------------------------------------------------------------------------------------------

 # Определить количество пар соседних чисел, сумма которых кратна 5.
 c, lst = 0, [1, 7, 3, 2, 6, 8, 12]

 # Вариант 1
 from itertools import pairwise
 print(list(pairwise(lst)))                                      # -> [(1, 7), (7, 3), (3, 2), (2, 6), (6, 8), (8, 12)]

 for i in list(pairwise(lst)):
     if sum(i) % 5 == 0:
         c += 1
 print(c)                                                        # -> 3


 # Вариант 2
 print([(x, y) for x, y in zip(lst, lst[1:])])                   # -> [(1, 7), (7, 3), (3, 2), (2, 6), (6, 8), (8, 12)]
 print(sum(not (x + y) % 5 for x, y in zip(lst, lst[1:])))       # -> 3
 print(sum(not (a + b) % 5 for a, b in zip(lst[:-1], lst[1:])))  # -> 3


 # Вариант 3
 c=0
 for i in range(len(lst)-1):
     if (lst[i]+lst[i+1]) % 5==0:
         c+=1
 print(c)                                                        # -> 3
 -----------------------------------------------------------------------------------------------------------------------

 # Вывести задом-наперёд все слова, состоящие менее, чем из 6 букв, и не содержащие подряд идущих букв o или O.
 s = 'Temperature hehe rising too man'

 res = [i[::-1] for i in s.split() if len(i) < 6 and 'oo' not in i.lower()]
 print(*res)  # -> eheh nam
 -----------------------------------------------------------------------------------------------------------------------

 Разница между if  vs  elif   Важно!!!!                 <-----                               <-----

 # Программа должна определить, какой тип треугольника образуется по длинам введенных сторон:
 # Равнобедренный (два равных)  Равносторонний (все стороны равны) Разносторонний (все стороны разные).
 # Блок elif это тот же if, но только следующая проверка.   elif - Это можно перевести как "иначе если"

 a = 5
 b = 5
 c = 5

 # Без elif    2 Вывода              # С   elif  1 Вывод

 if a == b == c:                     if a == b == c:
     print("Равносторонний")             print("Равносторонний")
 if a == b or b == c or a == c:      elif a == b or b == c or a == c:
     print("Равнобедренный")             print("Равнобедренный")
 else:                               else:
     print("Разносторонний")             print("Разносторонний")

 # -> Равносторонний                 # -> Равносторонний                       # <-----
 # -> Равнобедренный                                                           # <-----


 # Тоже самое
 s = '5 5 5'
 print(['Равносторонний', 'Равнобедренный', 'Разносторонний'][len(set(s.split()))-1])  # -> Равносторонний
 -----------------------------------------------------------------------------------------------------------------------

 Используйте следующие правила:

 если каждое из трех измерений менее или равно 15 сантиметрам, то выведите на экран "Коробка №1";
 если хотя бы одно из измерений больше 2 метров, то выводите "Упаковка для лыж";
 если хотя бы одно из измерений больше 15 сантиметров, но менее 50 сантиметров, то выводите "Коробка №2";
 во всех остальных случаях выводите "Коробка №3".

 a = 15     # a = int(input())
 b = 55     # b = int(input())
 c = 15     # c = int(input())

 def is_valid(*args):
     if all(i <= 15 for i in args):
         return "Коробка №1"
     elif any(i > 200 for i in args):
         return "Упаковка для лыж"
     elif any(15 < i < 50 for i in args):
         return "Коробка №2"
     return "Коробка №3"

 print(is_valid(a, b, c))  # -> Коробка №3
 -----------------------------------------------------------------------------------------------------------------------

 # match case и Моржик и несколько переменных сразу
 a, b = 7, 4

 match (a:= 7), (b:= 4):
     case 7, 4:
         print(6)    # -> 6
     case 10, 5:
         print(10)
     case 6, 3:
         print(4)
 -----------------------------------------------------------------------------------------------------------------------

 # Использование __import__   Найти цифры длиной 5 символов
 s = '752f78'

 print(bool(__import__('re').search(r'\d{5}', s)))  # -> False

 -----------------------------------------------------------------------------------------------------------------------

 # Дано число секунд. Вычислите сколько это часов, минут и секунд.

 # Первый вариант НЕ лучший!
 import time
 t = time.gmtime(4000)
 h, m, s = time.strftime("%H:%M:%S", t).split(':')
 print(f'{int(h)} часов {m} минут {s} секунд')                  # -> 1 часов 06 минут 40 секунд


 # Второй вариант Лучший!!!
 from datetime import timedelta, datetime
 dt = datetime(year=1, month=1, day=1, minute=0, second=0)  # Создали дату
 print(dt)                 # -> 0001-01-01 00:00:00

 delta = timedelta(seconds=4000)  # Создали делту
 print(delta)              # -> 1:06:40

 # Можно даже Много плюсов использовать ошибки не будет + == +++++++ == + +             <-----            <-----
 print((dt ++++ delta).strftime('%H часов %M минут %S секунд'))  # -> 01 часов 06 минут 40 секунд

 # Или еще лучше через ф-строку
 print(f"{(dt + +++ delta):%H часов %M минут %S секунд}")        # -> 01 часов 06 минут 40 секунд

 -----------------------------------------------------------------------------------------------------------------------

 Как написать if else if else в тернарном операторе     И ПОСМОТРИ ВТОРОЙ ВАРИАНТ!                        <-----

 # Даны два числа определить какое из них больше.

 # Первый варинт
 a, b = [int(i) for i in '5 6'.split()]
 print('Первое больше' if a > b else 'Второе больше' if b > a else 'Равны')  # -> Второе больше

 # Второй варинт                                                             # -> Второе больше          <-----
 (lambda a, b: print(('Равны', 'Первое больше', 'Второе больше')[(a > b) - (b > a)]))(*map(int, '5 6'.split()))
 -----------------------------------------------------------------------------------------------------------------------

 # выигрыш=3/проигрыш=0/ничья=1 если другое ничего ''
 a = 3

 print('выигрыш' if a == 3 else 'проигрыш' if a == 0 else 'ничья' if a == 1 else '')   # -> выигрыш
 print({3: 'выигрыш', 1: 'ничья', 0: 'проигрыш'}.get(a, ''))                           # -> выигрыш
 -----------------------------------------------------------------------------------------------------------------------

 # Выведите на экран в одну строку числа от 5 до -5 включительно.
 [print(i, end=' ') for i in range(-5, 5+1)[::-1]]   # -> 5 4 3 2 1 0 -1 -2 -3 -4 -5
 print()
 [print(i, end=' ') for i in range(5, -6, -1)]       # -> 5 4 3 2 1 0 -1 -2 -3 -4 -5
 -----------------------------------------------------------------------------------------------------------------------

 # находит сумму и количество чисел, кратных 17 или выводит NO    Посмотри как можно в кортеже указывать  NO

 res = [int(i) for i in iter(input, '0') if int(i) % 17 == 0]
 print(*[sum(res), len(res)] if res else ('NO', ))

 # ИЛИ ТАК
 data = [*filter(lambda x: not x % 17, map(int, iter(input, '0')))]
 print(*(sum(data), len(data)) if data else ('NO', ))
 -----------------------------------------------------------------------------------------------------------------------

 # Распаковка сразу нескольких iterable *
 s = '-5 5 1 3 8 -1'
 res = [int(i) for i in s.split()]
 print(*[i for i in res if i > 0], *[i for i in res if i < 0])        # -> 5 1 3 8 -5 -1
 print(*filter(lambda x: x > 0, res), *filter(lambda x: x < 0, res))  # -> 5 1 3 8 -5 -1

 # Умный вариант
 print(*sorted(map(int, s.split()), key=lambda x: x <= 0))            # -> 5 1 3 8 -5 -1
 -----------------------------------------------------------------------------------------------------------------------

 # Упорядочите элементы по возрастанию их модуля (абсолютного значения).
 res = ['-5', '10', '-1', '2', '6', '4', '-9', '8', '40', '-15']

 print(sorted([int(i) for i in res], key=abs))               # -> [-1, 2, 4, -5, 6, 8, -9, 10, -15, 40]
 print(sorted([i for i in res], key=lambda x: abs(int(x))))  # -> ['-1', '2', '4', '-5', '6', '8', '-9', '10', '-15', '40']
 -----------------------------------------------------------------------------------------------------------------------

 # Упорядочить слова по убыванию их длин. Можно через добавление - сортировать
 res = 'слон бродит по джунглям'.split()

 print(*sorted(res, key=lambda x: -len(x)))  # -> джунглям бродит слон по
 print(*sorted(res, key=len, reverse=True))  # -> джунглям бродит слон по
 -----------------------------------------------------------------------------------------------------------------------

 # Поиск трех последовательных элементов, сумма которых максимальна, Вывести только первую   Как можно сделать 3 группы!
 res = [40, 500, 6, 8, 6, 7, 5, 56, 45]

 res = [i for i in zip(res, res[1:], res[2:])]
 print(res)               # ->[(40, 500, 6), (500, 6, 8), (6, 8, 6), (8, 6, 7), (6, 7, 5), (7, 5, 56), (5, 56, 45)]
 a_max = 0
 for i in res:
     if sum(i) > a_max:
         a_max = sum(i)

 for i in res:
     if sum(i) == a_max:
         print(*i)                          # -> 40 500 6
         break



 # Очень крутое решение!!!  Тоже самое

 from collections import deque

 res = [40, 500, 6, 8, 6, 7, 5, 56, 45]

 q, res2 = deque('', 3), (0,)
 for n in res:
     q.append(n)
     res2 = max(res2, tuple(q), key=sum)
 print(*res2)                               # -> 40 500 6
 -----------------------------------------------------------------------------------------------------------------------

 # Минимальное значение среди трёхзначных элементов массива, делящихся на 7.  В min/max можно задавать default!!!
 res = [40, 500, 6, 8, 6, 7, 5, 56, 45]

 res = [int(i) for i in res]
 res = [i for i in res if len(str(i)) == 3 and i % 7 == 0]

 print(min(res))                           # -> ValueError: min() arg is an empty sequence
 print(min(res) if res else 'Не найдено')  # -> Не найдено
 print(min(res, default='Не найдено'))     # -> Не найдено

 # Тоже самое
 print(min(filter(lambda x: (not int(x) % 7) and len(x.strip()) == 3, res), key=int, default='Не найдено'))  # -> Не найдено
 -----------------------------------------------------------------------------------------------------------------------

 # Определите максимальную длину цепочки вида ABCABCABC    фрагмент цепочки может быть неполным
 n = 'CCCCABCABCABCACCCC'

 # Асимптотика - поведение функции при стремлении аргумента к бесконечности
 # Асимптотический анализ — метод описания предельного поведения функций.

 print(max((len(s) for s in re.findall(r"A(?:BCA)*(?:BC?)?", n)), default=0))  # -> 10

 # Хз почему не проходил все тесты
 res = re.search(r'(ABC)+(AB?)*', n).group()
 print(len(res))                                                               # -> 10
 -----------------------------------------------------------------------------------------------------------------------

 # Количество 7-буквенные коды перестановкой букв слова КОННЕКТ. При этом нельзя ставить рядом две гласные.
 from itertools import permutations

 s = map(lambda x: ''.join(x), set(permutations('КОННЕКТ')))
 print(len([x for x in s if 'ОЕ' not in x and 'ЕО' not in x]))                                           # -> 900

 # Тоже самое
 res = sum(not any(x in ''.join(perm) for x in ("ОЕ", "ЕО")) for perm in set(permutations("КОННЕКТ")))
 print(res)                                                                                              # -> 900

 # Тоже самое
 print(sum(not ('ОЕ' in w or 'ЕО' in w) for w in {''.join(p) for p in permutations('КОННЕКТ')}))         # -> 900
 -----------------------------------------------------------------------------------------------------------------------

 # Количество 4-буквенные слова, в которых есть только буквы A, B, C, D, X, причём буква X появляется ровно 1 раз.
 import itertools                                         from itertools import product

 a = 0                                                    cnt = 0
 for word in itertools.product('ABCDX', repeat = 4):      for text in product('abcdx', repeat=4):
     t = word[0] + word[1] + word[2] + word[3]                if text.count('x') == 1:
     if t.count('X') == 1:                                        cnt += 1
         a += 1

 print(a)  # -> 256                                       print(cnt)  # -> 256

 # Тоже самое
 print(sum(1 for t in product('ABCDX', repeat=4) if t.count('X') == 1))  # -> 256
 print(sum(i.count('X') == 1 for i in product('ABCDX', repeat=4)))       # -> 256
 -----------------------------------------------------------------------------------------------------------------------

 # Все 5-буквенные слова, составленные из букв К, О, Р    Запишите слово, которое стоит под номером 237.
 from itertools import product

 for index, text in enumerate(product('КОР', repeat=5), start=1):
     if index == 237:
         print(''.join(text))  # -> РРРКР
         break

 # Тоже самое
 for i, el in enumerate(sorted(set(permutations('КОР' * 5, 5))), 1):
     if i == 237:
         print(''.join(el))    # -> РРРКР
         break
 -----------------------------------------------------------------------------------------------------------------------

 # Все четырёхбуквенные слова, составленные из букв А, Л, Г, О, Р, И, Т, М  Под каким номером начинается с букв ИГ?
 # Алгоритм нужна запускать по набору слов "АГИЛМОРТ", а не "АЛГОРИТМ".  - алфавитный порядок

 from itertools import product
 import re

 for index, text in enumerate(product('АГИЛМОРТ', repeat=4), start=1):
     if re.match(r'ИГ', ''.join(text)):
         print(index, ''.join(text))  # -> 1089 ИГАА
         break
 -----------------------------------------------------------------------------------------------------------------------

 # Классный пример
 a, b = 10, 15                      a, b = 10, 15
 print(-min(-a, -b))  # -> 15       print(-max(-a, -b))  # -> 10
 print(min(-a, -b))   # -> -15      print(max(-a, -b))   # -> -10
 print(min(a, b))     # -> 10       print(max(a, b))     # -> 15
 -----------------------------------------------------------------------------------------------------------------------

 # Интересные примеры с range()
 for i in range(0):
     print("Не забудь написать здесь что-нибудь")  # Ничего Не выведет Без Ошибки

 for i in range(-1):
    print("Не забудь написать здесь что-нибудь")   # Ничего Не выведет Без Ошибки

 for i in range(0, 5, 0):
     print(i, end=" ")     # -> ValueError: range() arg 3 must not be zero

 for i in range(0, 5, 15):
     print(i, end=" ")     # -> 0

 a, b, c = 1, 7, 2
 print(range(a, b, c))   # -> range(1, 7, 2)
 print(*range(a, b, c))  # -> 1 3 5

 -----------------------------------------------------------------------------------------------------------------------

 # Интересные примеры с break/continue

 # то есть, когда i будет 4, она подпадает под это условие, и выполнится continue
 for i in range(10):
    if i % 2 == 0:
        continue
    if i == 4:
        break
    print(i, end=" ")  # -> 1 3 5 7 9


 # else Отработал потому что цикл завершился в Штатном режиме
 for i in range(10):
     if i == 5:
         continue
     print(i, end="")
 else:
     print(5)   # -> 0123467895
 -----------------------------------------------------------------------------------------------------------------------

 # Вывести последний символ
 s = "Hello world"

 print(s[-1])                               # -> d
 print(s[slice(None, None, -1)][slice(1)])  # -> d
 print(s[~0])                               # -> d

 # ~0 == -1
 print(~0)                                  # -> -1
 print(~1)                                  # -> -2


 # Интересные примеры slice
 # Без первых двух и последних двух символов.
 s = "1234567890"

 print(f"{s[slice(2, -2, None)]}")  # -> 345678
 print(s[2:-2])                     # -> 345678
 -----------------------------------------------------------------------------------------------------------------------

 # Пример islower()/isupper()

 # Цифры всегда lower? нет, только если в строке есть хотя бы один символ в нижнем регистре
 print('1234'.islower())                           # -> False
 print('hello 1234'.islower())                     # -> True
 print('_hello'.islower())                         # -> True
 print("my password is \"miku1234\"".islower())    # -> True

 # Тоже самое для isupper()
 print('1234'.isupper())                           # -> False
 print('HELLO 1234'.isupper())                     # -> True
 print('_HELLO'.isupper())                         # -> True
 print("MY PASSWORD IS \"MIKU1234\"".isupper())    # -> True
 -----------------------------------------------------------------------------------------------------------------------

 # Что выводит m и вообще что такое m  Используем  m[0] или m.group(0) или m.group()

 def sub_fun(m):                def sub_fun(m):                      def sub_fun(m):
     print(m)                       print(m)                             print(m)
     if m[0] == 'Ё':                if m.group(0) == 'Ё':                if m.group() == 'Ё':
         return 'Е'                     return 'Е'                           return 'Е'
     if m[0] == 'ё':                if m.group(0) == 'ё':                if m.group() == 'ё':
         return 'е'                     return 'е'                           return 'е'

 # -> <re.Match object; span=(1, 2), match='ё'>
 # -> <re.Match object; span=(9, 10), match='Ё'>
 # -> <re.Match object; span=(16, 17), match='ё'>

 # match case  Bывод что такое m[0]   m.group()
 def sub_fun(m):
     print(f"{m},       ---{m[0]=}   ---  {m.group()=}")
     match m[0]:
         case 'ё':
             return 'е'
         case _:
             return 'Е'

 # -> <re.Match object; span=(1, 2), match='ё'>,       ---m[0]='ё'   ---  m.group()='ё'
 # -> <re.Match object; span=(9, 10), match='Ё'>,       ---m[0]='Ё'   ---  m.group()='Ё'
 # -> <re.Match object; span=(16, 17), match='ё'>,       ---m[0]='ё'   ---  m.group()='ё'


 # Ё нужно заменить Е   ё нужно заменить е
 s = "Чёрный, жЁлтый, ёжик"

 print(__import__('re').sub(r'ё|Ё', sub_fun, s))   # -> Черный, жЕлтый, ежик
 print(__import__('re').sub(r'[ёЁ]', sub_fun, s))  # -> Черный, жЕлтый, ежик
 -----------------------------------------------------------------------------------------------------------------------

 # Если вы хотите добавить строку к списку, можете использовать метод append() или оператор +=.
 lst = ['hello']
 lst += 'world'
 print(lst)                 # -> ['hello', 'w', 'o', 'r', 'l', 'd']

 lst = ['hello'] + 'world'  # -> TypeError: can only concatenate list (not "str") to list
 -----------------------------------------------------------------------------------------------------------------------

 # Преобразует список в одномерный.
 # То есть, за основу берётся пустой список, куда мы "прибавляем" прочие списки из многомерности)

 nested_list = [[1, 2], [3, 4], [5, 6]]
 flattened_list = sum(nested_list, [])
 print(flattened_list)                   # -> [1, 2, 3, 4, 5, 6]

 # Пример с start
 print(sum([1, 2, 3, 4], start=-10))  # -> 0
 -----------------------------------------------------------------------------------------------------------------------

 # Пример split()
 s = "---"
 print(s.split("-"))  # -> ['', '', '', '']
 -----------------------------------------------------------------------------------------------------------------------

 # Для map  list внутри genexp можно НЕ писать тоже будет работать
 s = '1 2 3 4 5 6 7 8 39'
 print([i for i in map(int, s.split()) if i % 2 == 0])           # -> [2, 4, 6, 8]   # map(int, s.split())
 print([i for i in list(map(int, s.split())) if i % 2 == 0])     # -> [2, 4, 6, 8]   # list(map(int, s.split()))

 # Тоже самое
 print(list(filter(lambda x: not x % 2, map(int, s.split()))))           # -> [2, 4, 6, 8]
 print(list(filter(lambda x: not x % 2, [int(i) for i in s.split()])))   # -> [2, 4, 6, 8]

 # Тоже самое без map
 print([i for i in [int(i) for i in s.split()] if i % 2 == 0])           # -> [2, 4, 6, 8]



 # class map(object):   возвращает итератор map object

 # Интересный пример с map                                                                      <-----      <-----
 # Работает как обычный итератор
 a = [-1, 2, -3]
 result = map(abs, a)
 print(result)        # -> <map object at 0x00000228C5CFE230>
 print(next(result))  # -> 1
 print(next(result))  # -> 2
 print(next(result))  # -> 3
 print(next(result))  # -> StopIteration


 # Можно обходить итератор map object сразу в цикле for
 a = [-1, 2, -3, 4, -5]
 for value in map(abs, a):
     print(value, end=' ')  # -> 1 2 3 4 5

 # Для повторного итерирования нужно будет создавать новый итератор при помощи map.
 a = [-1, 2, -3, 4, -5]
 iterator = map(abs, a)
 print(max(iterator))  # -> 5
 print(max(iterator))  # -> ValueError: max() arg is an empty sequence


 # Использование функций
 str_nums = ['-1', '4232', '-33', '312', '12']
 nums = list(map(int, str_nums))
 print(nums)                            # -> [-1, 4232, -33, 312, 12]

 a = ['hello', 'hi', 'good morning']
 b = list(map(len, a))
 print(b)                               # -> [5, 2, 12]

 # В качестве функции в map можно передавать не только встроенные и пользовательские функции, но и методы объектов.
 a = ['hello', 'hi', 'good morning']
 b = list(map(str.upper, a))
 print(b)                               # -> ['HELLO', 'HI', 'GOOD MORNING']


 list_strings = ['hello', 'hi']
 b = list(map(list, list_strings))
 print(b)                               # -> [['h', 'e', 'l', 'l', 'o'], ['h', 'i']]

 words = list(map(sorted, b))
 print(words)                           # -> [['e', 'h', 'l', 'l', 'o'], ['h', 'i']]


 # Всё тоже самое можно делать без map при помощи Генераторов

 list_strings = ['hello', 'hi', 'good morning']
 print(list(map(lambda x: x[::-1], list_strings)))  # -> ['olleh', 'ih', 'gninrom doog']
 print([i[::-1] for i in list_strings])             # -> ['olleh', 'ih', 'gninrom doog']

 # Главное примечание про map и filter и zip
 map представляет собой класс   class map(object):  тоже классы      class filter(object):      class zip(object):

 # Может принимать несколько последовательностей
 # class map(object)
 #    map(func, *iterables) --> map object

 nums1 = [1, 2, 3]
 nums2 = [4, 5, 6]
 nums3 = [7, 8, 9]

 result = map(lambda x, y, z: x + y + z, nums1, nums2, nums3)
 print(list(result))  # -> [12, 15, 18]


 # Что увидим на экране после запуска следующего кода?
 nums1 = [10, 20, 30, 40]
 nums2 = [20, 30, 40, 50]

 result = map(lambda x, y, w=0: x - y - w, nums2, nums1)
 print(sum(result))                                          # -> 40


 # Пример class filter(object):  является функцией/классом высшего порядка,   возвращает итератор filter object

 # Результат получается идентичным. Но filter Возвращает итератор а в нем физически не хранятся все элементы.
 def is_two_digit(x: int) -> bool:
     return x > 9 and x < 100

 numbers = [14, 0, 5, -79, 645, 7952, 18, 0, -192, 471]
 num_filters = list(filter(is_two_digit, numbers)) # фильтруем через filter
 print(num_filters)                  # -> [14, 18]

 # фильтруем через генератор списка
 num_list_comp = [n for n in numbers if is_two_digit(n)]
 print(num_list_comp)                # -> [14, 18]

 # Легкие пример filter
 nums = [1, 2, 3, 4, 5]
 for n in filter(lambda x: x > 2, nums):
     print(n, end=' ')

 # -> 3 4 5



 # Пример class zip(object):   возвращает итератор zip object

 # Посмотри все примеры!!!
 words = ['approach', 'monstrous', 'mobile']
 numbers = [100, 200, 300]
 s = 'AB'

 result_zip = zip(words, numbers, s)
 print(list(result_zip))                 # -> [('approach', 100, 'A'), ('monstrous', 200, 'B')]

 # Нужно создать новый итератор
 print(list(zip(*result_zip)))           # -> []

 # Создаем новый итератор потому что он закончился
 result_zip = zip(words, numbers, s)
 print(list(zip(*result_zip)))           # -> [('approach', 'monstrous'), (100, 200), ('A', 'B')]

 # Интересный вариант Распаковка
 result_zip = zip(words, numbers, s)
 col1, col2, col3 = zip(*result_zip)

 print(col1)  # -> ('approach', 'monstrous')
 print(col2)  # -> (100, 200)
 print(col3)  # -> ('A', 'B')


 # Все возвращают итератор
 print(zip([1, 2], [2, 3]))                # -> <zip object at 0x000002EEF0F0A700>
 print(map(str, [1, 2]))                   # -> <map object at 0x000002EEF26BE200>
 print(filter(lambda x: x > 2, [1, 2]))    # -> <filter object at 0x000002EEF26BE200>
 -----------------------------------------------------------------------------------------------------------------------

 # Циклическая ссылка  Рекурсия
 l = [1, 2, 3]
 l.append(l)
 print(l)    # -> [1, 2, 3, [...]]

 # Обьяснение
 Этот код создает список l с элементами 1, 2 и 3, а затем добавляет сам список l в конец этого списка.
 Это приводит к циклической ссылке внутри списка l.

 Когда вы выводите список l с помощью print(l), Python пытается представить этот список, и он обнаруживает
 циклическую ссылку. Результатом будет [1, 2, 3, [...]], где ... указывает на циклическую ссылку на сам список.

 Когда вы видите ... в выводе, это означает, что есть циклическая ссылка, и Python избегает бесконечной рекурсии
 при попытке представить всю структуру. Вместо этого он показывает ... для указания на циклическую ссылку.


 # Поскольку между пробелами нет других символов, результат split(' ') будет список
 print(len((' ' * 10).split(' ')))  # -> 11
 print(len((' ' * 10).split()))     # -> 0

 print((' ' * 10).split(' '))       # -> ['', '', '', '', '', '', '', '', '', '', '']
 print((' ' * 10).split())          # -> []
 -----------------------------------------------------------------------------------------------------------------------

 # Реализуйте программу, которая будет вычислять количество различных объектов в списке.    Очень круто!!!
 objects = [1, 2, 1, 5, True, False, True, 'false', [], [1,2], [1,2]]

 print(len(set(map(id, objects))))         # -> 9
 print(len(set(id(i) for i in objects)))   # -> 9

 # Так не работает!
 print(len(set(objects)))                  # -> TypeError: unhashable type: 'list'


 # Тоже самое

 n = len(objects)
 ans = n
 for i in range(n):
     for j in range(i):
         if id(objects[i]) == id(objects[j]):
             ans -= 1
             break

 print(ans)                                 # -> 9
 -----------------------------------------------------------------------------------------------------------------------

 # Приоритет с более высокой точностью (float).
 print(5 + 2.0)  # -> 7.0
 print(5 - 2.0)  # -> 3.0
 print(5 / 2)    # -> 2.5

 # Интересные примеры
 print(int(-2.8))         # -> -2
 print(int(4.9))          # -> 4
 print(round(-2.375, 2))  # -> -2.38
 -----------------------------------------------------------------------------------------------------------------------

 # Напечатайте индекс наименьшего числа в списке.
 lst = [5, 8, 3, 2, 7, 4, 9]

 print(abs(lst.index(min(lst))))                        # -> 3
 print((arr := [5, 8, 3, 2, 7, 4, 9]).index(min(arr)))  # -> 3  # Морж классный  <-----
 print(min(range(len(lst)), key=lst.__getitem__))       # -> 3
 -----------------------------------------------------------------------------------------------------------------------

 # Найти индекс последнего вхождения этого числа в список   ИЩЕМ ЧИСЛО 5
 lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5]
 res = []
 for i, v in enumerate(lst):
     if v == 5:
         res.append([i, v])

 print(res[-1][0] if res else 'Числа нет!')                                                # -> 9


 # Тоже самое
 a, b = ''.join('1 2 3 4 5 6 7 8 9 5'.split()), '5'
 c = a.rfind(b)
 print(c if c >= 0 else "Числа нет!")                                                      # -> 9


 # Тоже самое
 a, b = ''.join('1 2 3 4 5 6 7 8 9 5'.split()), '5'
 print(["Числа нет!", a.rfind(b)][b in a])                                                 # -> 9


 # Тоже самое  Через словарь
 lst = '1 2 3 4 5 6 7 8 9 5'
 print({value: index for index, value in enumerate(lst.split())}.get('5', "Числа нет!"))   # -> 9


 # Тоже самое
 l, n = '1 2 3 4 5 6 7 8 9 5'.split(), '5'
 l.reverse()
 try:
     print(len(l) - l.index(n) - 1)                                                        # -> 9
 except:
     print('Числа нет!')


 # Тоже самое
 data, num = [*map(int, '1 2 3 4 5 6 7 8 9 5'.split())], 5
 idx = len(data)
 while (idx := idx - 1) >= 0:
     if num == data[idx]:
         print(idx)
         break
 else:
     print('Числа нет!')                                                                    # -> 9
 -----------------------------------------------------------------------------------------------------------------------

 # Заменить запятые на Одну запятую
 s = '1, 2, , , , 3, 4, 5'

 print(__import__('re').sub(r'(, )+', ', ', s))          # -> 1, 2, 3, 4, 5
 print(*__import__('re').findall(r'\w+', s), sep=', ')   # -> 1, 2, 3, 4, 5
 -----------------------------------------------------------------------------------------------------------------------

 # Убрать лишние пробелы
 s = 'Алгоритмы     это основа    программирования'
 
 print(*s.split())               # -> Алгоритмы это основа программирования
 print(' '.join(s.split()))      # -> Алгоритмы это основа программирования
 print(re.sub(r'\s+', r' ', s))  # -> Алгоритмы это основа программирования
 -----------------------------------------------------------------------------------------------------------------------

 # Наибольший общий делитель двух чисел  math.gcd
 print(__import__('math').gcd(30, 18))   # -> 6
 -----------------------------------------------------------------------------------------------------------------------

 # Выведите True, если последовательность возрастающая и False, если нет.

 lst = [-6, -3, 1, 4, 6, 10]
 for i, j in zip(lst, lst[1:]):
     if i > j:
         print(False)
         break
 else:
     print(True)                                                                                 # -> True

 # Тоже самое
 print(lst == sorted(lst) and len(lst) == len(set(lst)))                                         # -> True
 print((lst:='-6 -3 1 4 6 10'.split()) == sorted(lst, key=int) and len(lst) == len(set(lst)))    # -> True
 print((lambda *arr: all(a < b for a, b in zip(arr, arr[1:])))(lst))                             # -> True
 -----------------------------------------------------------------------------------------------------------------------

 # Обновить словарь
 students = {"Alice": {"English": 85}, "Bob": {"English": 92}}
 additional_scores = {"Alice": {"History": 87, "Geography": 76}, "Bob": {"History": 91,    "Geography": 83}}
 # print(eagles | beavers)

 # Создать новый словарь
 a_dict = {}
 for k, v in zip(additional_scores.items(), students.items()):
     # a_dict[k[0]] = v[1] | k[1]
     a_dict[k[0]] = {**v[1], **k[1]}
 print(a_dict)
 # {'Alice': {'English': 85, 'History': 87, 'Geography': 76}, 'Bob': {'English': 92, 'History': 91, 'Geography': 83}}

 # Обновить текущий
 for k, v in students.items():
     v.update(additional_scores[k])
 print(students)
 # {'Alice': {'English': 85, 'History': 87, 'Geography': 76}, 'Bob': {'English': 92, 'History': 91, 'Geography': 83}}

 # Обновить текущий
 students['Alice'].update(additional_scores['Alice'])
 students["Bob"].update(additional_scores["Bob"])
 print(students)
 # {'Alice': {'English': 85, 'History': 87, 'Geography': 76}, 'Bob': {'English': 92, 'History': 91, 'Geography': 83}}
 -----------------------------------------------------------------------------------------------------------------------

 #  Определите, какое слово в тексте встречается чаще всего и напечатайте, сколько раз оно встретилось в тексте.
 s = 'The cat sat on the mat'.lower().split()

 # Простой вариант
 print(s.count(max(s, key=lambda x: s.count(x))))                                    # -> 2

 # Варинт Counter
 from collections import Counter
 print(max(Counter(s).values()))                                                     # -> 2

 # Варинт Counter и регулярка
 import re
 from collections import Counter

 s = 'The cat sat on the mat'
 print(Counter(re.findall('\w+', s.lower())).most_common(1)[0][1])                   # -> 2
 print(Counter(re.findall('\w+', s.lower())).most_common(1))                         # -> [('the', 2)]

 # Интерсный вариант
 from collections import Counter
 from string import punctuation
 import re

 print(max(Counter(re.sub(fr'[{punctuation}]', '', s).lower().split()).values()))    # -> 2
 -----------------------------------------------------------------------------------------------------------------------

 # Пример с Без распаковки *  Общие элементы есть
 s = set('John, Mary, David, Alice, Charlie'.split(', '))
 s1 = set('Mary, Kate, Peter, Emily, Frank'.split(', '))
 res = s & s1

 print(', '.join(sorted(res)) if res else 'Общих друзей нет!', sep=', ')  # -> Mary


 # Пример с распаковкой *  Общих элементов нет
 s = set('John, David, Alice, Charlie'.split(', '))
 s1 = 'Kate, Peter, Emily, Frank'.split(', ')
 res = s.intersection(s1)

 # При использование * в print Распаковка для всего Посмотри пример
 print(*sorted(res)if res else ['Общих друзей нет!'], sep=', ')  # -> Общих друзей нет!
 print(*sorted(res)if res else 'Общих друзей нет!', sep=', ')    # -> О, б, щ, и, х,  , д, р, у, з, е, й,  , н, е, т, !
 -----------------------------------------------------------------------------------------------------------------------

 # Найти пересечение
 lst = [{'Salad', 'Fries', 'Pizza'}, {'Steak', 'Salad', 'Pizza'}, {'Salad', 'Pizza', 'Fries'}]

 res = set.intersection(*lst)
 print(*sorted(res) if res else ["Общих вкусов нет!"], sep=', ')  # -> Pizza, Salad
 -----------------------------------------------------------------------------------------------------------------------

 # Проверьте, что все значения этого словаря являются непустыми строками.
 profile = {'name': 'John', 'age': '30', 'occupation': '', 'location': 'London'}
 print(all(profile.values()))  # -> False

 profile = {'name': 'Alice ', 'occupation': 'programmer'}
 print(all(profile.values()))  # -> True
 -----------------------------------------------------------------------------------------------------------------------

 # Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор).
 s = '123123 is good too'

 print(re.search(r"\b(\w+)\1\b", s).group())            # -> 123123
 print(__import__('re').search(r'(\b\w+)\1\b', s)[0])   # -> 123123

 s = 'aaa'
 print(re.search(r"\b(\w+)\1\b", s))                    # -> None
 print(__import__('re').search(r'(\b\w+)\1\b', s))      # -> None
 -----------------------------------------------------------------------------------------------------------------------

 # Нельзя пользоваться встроенными сортировками в Python
 lst = [19, 4, 5, 17, 1]

 def quick_sort(lst):
     no_sorted = sorted
     return no_sorted(lst)

 print(quick_sort(lst))  # -> [1, 4, 5, 17, 19]
 -----------------------------------------------------------------------------------------------------------------------

 # Часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ... (число повторяется столько раз, чему равно)
 # Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4.

 from itertools import chain
 number = 7

 res = list(chain.from_iterable([[i]*i for i in range(1, number+1)]))
 print(*res[:number])                                                  # -> 1 2 2 3 3 3 4


 # Тоже самое
 from itertools import islice, count
 print(*islice((n for n in count() for _ in range(1, n+1)), number))   # -> 1 2 2 3 3 3 4
 -----------------------------------------------------------------------------------------------------------------------

 # Выведите его дробную часть.
 a = 17.9

 print(a - int(a))  # -> 0.8999999999999986
 print(a % 1)       # -> 0.8999999999999986
 -----------------------------------------------------------------------------------------------------------------------

 # Дано 10 целых чисел. Вычислите их сумму.     Вывод сразу всех чисел из Консоли
 print(sum(map(int, __import__('sys').stdin)))
 print(sum(map(int, open(0))))
 print(sum(int(input()) for _ in range(10)))
 print(sum(map(int, __import__('sys').stdin.readlines())))
 -----------------------------------------------------------------------------------------------------------------------

 # Если бы мы вводили такие цифры подряд:
 # 5
 # 0
 # 700
 # 0
 # 200
 # 2

 #  Вывод был бы таким:
 res = [i for i in __import__('sys').stdin]
 print(res)                                  # -> ['5\n', '0\n', '700\n', '0\n', '200\n', '2']
 -----------------------------------------------------------------------------------------------------------------------

 # Задача «Максимальное число идущих подряд равных элементов»
 lst = [1, 7, 7, 9, 1]                        # Или пока не введут 0            # Или пока не введут 0
                                                                                max_n, count = 1, 1
 count, max_count = 1, 1                      prev = rep = mc = c = 0           prev_num = int(input())
 for i in range(1, len(lst)):                 while (e := int(input())):        while (num := int(input())) != 0:
     if lst[i] == lst[i - 1]:                     if e == prev:                     if num == prev_num:
         count += 1                                   c += 1                            count += 1
         if max_count < count:                    else:                                 max_n = max(max_n, count)
             max_count = count                        mc = max(c, mc)               else:
     else:                                            prev, c = e, 1                    count = 1
         count = 1                            print(max(c, mc))                     prev_num = num
 print(max_count)  # -> 2                                                       print(max_n)

 -----------------------------------------------------------------------------------------------------------------------

 # Задача «Стандартное отклонение»
 lst = [1, 7, 9]

 from statistics import stdev
 print(stdev(lst, sum(lst) / len(lst)))  # -> 4.163331998932265
 -----------------------------------------------------------------------------------------------------------------------

 # Удалите из этой строки первое и последнее вхождение буквы h,а также все символы, находящиеся между ними.
 s = 'In the hole in the ground there lived a hobbit'

 print(__import__('re').sub(r'h.*h', '', s))  # -> In tobbit
 -----------------------------------------------------------------------------------------------------------------------

 # Дана строка. Замените в этой строке все появления буквы h на букву H, кроме первого и последнего вхождения.
 s = 'In the hole in the ground there lived a hobbit'

 n = s.count("h")
 s1 = s.replace("h", "H", n-1)

 print(s1.replace("H", "h", 1))  # -> In the Hole in tHe ground tHere lived a hobbit
 -----------------------------------------------------------------------------------------------------------------------

 # Задача «Пингвины»

 # Первый вариант                           # Второй вариант                            # Мой вариант
 n = 3                                      n = 3                                       n = 3
 penguin = ['''   _~_                       '''\                                        a = r'   _~_    '
   (o o)                                       _~_                                      b = r'  (o o)   '
  /  V  \\                                    (o o)                                     c = r' /  V  \  '
 /(  _  )\\                                  /  V  \                                    d = r'/(  _  )\ '
   ^^ ^^   '''.split("\n")]                 /(  _  )\\                                  e = r'  ^^ ^^   '
                                              ^^ ^^  '''                                res = [a, b, c, d, e]
 penguins = zip(*penguin * n)                                                           [print(i*n) for i in res]
 print("\n".join(map("".join, penguins)))   n = int(input())
                                            for row in __doc__.split('\n'):
   _~_       _~_       _~_                      print(' '.join([row] * n), end=' \n')
  (o o)     (o o)     (o o)
 /  V  \   /  V  \   /  V  \
/(  _  )\ /(  _  )\ /(  _  )\
  ^^ ^^     ^^ ^^     ^^ ^^
 -----------------------------------------------------------------------------------------------------------------------

 # Задача «Больше предыдущего»  Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.
 res = [1, 5, 2, 4, 3]

 print(*[res[i] for i in range(1, len(res)) if res[i] > res[i-1]])  # -> 5 4
 -----------------------------------------------------------------------------------------------------------------------

 # Задача «Больше своих соседей»
 res = [1, 2, 3, 4, 5]

 print(sum(res[i - 1] < res[i] > res[i + 1] for i in range(1, len(res) - 1)))   # -> 0
 -----------------------------------------------------------------------------------------------------------------------

 # Простое число — это число, которое делится только на 1 и на себя.
 # Проверка числа на простоту в Python

 # SymPy — это библиотека Python для выполнения символьных вычислений. Это система компьютерной алгебры
 import sympy

 print(sympy.isprime(5))  # -> True
 print(sympy.isprime(4))  # -> False


 # Найдите все простые числа в диапазоне от 2 до n включительно.
 n = 6

 print(*[i for i in range(2, n + 1) if __import__('sympy').isprime(i)])  # -> 2 3 5
 -----------------------------------------------------------------------------------------------------------------------

 # В нижний регистр первый символ, а все остальные — в верхний регистр.
 s = 'Hello World'

 print(*[f"{i[0].lower()}{i[1:].upper()}" for i in s.split()])  # -> hELLO wORLD
 print(s.title().swapcase())                                    # -> hELLO wORLD
 -----------------------------------------------------------------------------------------------------------------------

 # Проверка число на ПРОСТОЕ 2 Способа

 # Тоже самое  Первый способ
 def check_prime(number):
     sqrt = math.sqrt(number)
     for i in range(2, int(sqrt)+1):
         if (number / i).is_integer():
             return False
     return True

 print(f'check_prime(10_000_000) = {check_prime(10_000_000)}')  # - > check_prime(10_000_000) = False
 print(f'check_prime(10_000_019) = {check_prime(10_000_019)}')  # - > check_prime(10_000_019) = True


 # Тоже самое  Второй способ

 from sympy import isprime

 print(f'isprime(10_000_000) = {isprime(10_000_000)}')          # - > isprime(10_000_000) = False
 print(f'isprime(10_000_019) = {isprime(10_000_019)}')          # - > isprime(10_000_019) = True
 -----------------------------------------------------------------------------------------------------------------------

 # Интересный Пример
 print(f"Python {3 + .2}")  # -> Python 3.2
 -----------------------------------------------------------------------------------------------------------------------

 # Интересный Пример
 x1 = {"jack": 30, "john": 35}
 x2 = {"jack": 355, "john": 35}

 print(x1 > x2)  # -> TypeError: '>' not supported between instances of 'dict' and 'dict'
 -----------------------------------------------------------------------------------------------------------------------

 # ВАЖНО !!! eval vs ast.literal_eval()                                             <-----                  <-----

 # Функции eval() и ast.literal_eval() интерпретируют строки как код Python.
 # ast.literal_eval() - обрабатывает только строки, представляющие литералы, более безопасный в применении.
 # eval()             - функция способна выполнить любые команды. Более Производительный

 import ast
 s = '[4, 2, 5, 9, 1]'

 print(ast.literal_eval(s))           # -> [4, 2, 5, 9, 1]  # Создание безопасного аналога eval()
 print(eval(s))                       # -> [4, 2, 5, 9, 1]  # eval() Более Производительный

 print(ast.literal_eval('{"a":10}'))  # -> {'a': 10}  # Из строки сделали словарь
 print(eval('{"a":10}'))              # -> {'a': 10}  # Из строки сделали словарь


 # Наглядный пример                                                                 <-----                  <-----
 s = "deque([1, 2, 3])"

 print(eval(s))              # -> deque([1, 2, 3])
 print(ast.literal_eval(s))  # -> ValueError: malformed node or string on line 1: <ast.Call object at 0x00000252CC0DA6E0>

 -----------------------------------------------------------------------------------------------------------------------

 # Как обрезать вручную
 s = '1234567'
 i = 0
 while i < len(s):
     print(s[i:i + 3])
     i = i + 3

 # 123
 # 456
 # 7
 -----------------------------------------------------------------------------------------------------------------------

 # Roman number to decimal  # В римской системе счисления   print(__import__('roman').fromRoman('MCMLXXXIV')) # -> 1984
 import roman
 res = roman.fromRoman("MCMLXXXIV")
 res1 = roman.fromRoman("IX")

 print(res)   # -> 1984
 print(res1)  # -> 9
 -----------------------------------------------------------------------------------------------------------------------
 # Наоборот сделать                                         print(__import__('roman').toRoman(1984))     # -> MCMLXXXIV

 import roman
 res = roman.toRoman(1984)
 res1 = roman.toRoman(9)

 print(res)   # -> MCMLXXXIV
 print(res1)  # -> IX
 -----------------------------------------------------------------------------------------------------------------------

 # Интересные примеры  exec   eval    Разница между   exec  vs   eval                    <-----               <-----

 exec("print(f'{a+b}')", globals(), {'a': 8, 'b': 11})  # -> 19

 exec('''print(f'10*2')''')  # -> 10*2
 eval('''print(f'10*2')''')  # -> 10*2

 exec("print(a)", globals(), {'a': 42})  # -> 42
 eval("print(a)", globals(), {'a': 42})  # -> 42

 exec(f"print([i for i in range(3) if i > 0])")  # -> [0, 1, 2]
 eval(f"print([i for i in range(3) if i > 0])")  # -> [0, 1, 2]

 a = exec(f"print(eval('+'.join('111')))")  # -> 3
 print(a)  # -> None


 a = 5
 # Возвращает Результат
 print(eval('37 + a'))  # -> 42
 # Возвращает None
 print(exec('37 + a'))  # -> None


 # exec Может создать переменную
 print(exec('a = 47'))  # -> 47
 # eval НЕ Может создать переменную
 print(eval('a = 47'))  # -> SyntaxError: invalid syntax


 # Выполняет блок кода exec()      # Ошибка eval()
 program = '''                     program = '''
 for i in range(2):                for i in range(2):
     print("Python, sep=' '")          print("Python, sep=' '")
 '''                               '''

 exec(program)                     eval(program)  # -> SyntaxError: invalid syntax

 # Python, sep=' '
 # Python, sep=' '

 Функция eval() делает то же самое для одного выражения и возвращает значение выражения:
 a = 2
 print(eval('42 * a'))  # -> 84


 # eval vs exec

 exec('print(5)')            # -> 5
 exec('print(5)\nprint(6)')
 # -> 5
 # -> 6
 exec('if True: print(6)')   # -> 6
 exec('5')                   # -> Ничего не возвращает


 # eval vs exec

 x = eval('5')
 print(x)                    # -> 5
 x = eval('%d + 6' % x)
 print(x)                    # -> 11
 x = eval('abs(%d)' % -100)
 print(x)                    # -> 100


 # eval() НЕ Будет работать!
 x = eval('x = 5')          # INVALID; assignment is not an expression.
 x = eval('if 1: x = 4')    # INVALID; if is a statement, not an expression.

 # exec() Будет работать!
 exec('x = 5')
 print(x)                 # -> 5
 x = exec('if 1: x = 4')
 print(x)                 # -> None
 -----------------------------------------------------------------------------------------------------------------------

 # Число  удваивается
 print([10 * 2**i for i in range(12)])  # -> [10, 20, 40, 80, 160, 320, 640, 1280, 2560, 5120, 10240, 20480]
 print([10 << i for i in range(12)])    # -> [10, 20, 40, 80, 160, 320, 640, 1280, 2560, 5120, 10240, 20480]
 -----------------------------------------------------------------------------------------------------------------------

 # Обновить словарь  Через defaultdict
 from collections import defaultdict

 a_dict = defaultdict(dict)

 res = ['Ivanov paper 10', 'Petrov pens 5', 'Ivanov marker 3', 'Ivanov paper 7', 'Petrov envelope 20', 'Ivanov envelope 5']

 for i in res:
     a, b, c = i.split()
     a_dict[a].setdefault(b, 0)
     a_dict[a][b] += int(c)

 print(a_dict)
 # defaultdict(<class 'dict'>, {'Ivanov': {'paper': 17, 'marker': 3, 'envelope': 5}, 'Petrov': {'pens': 5, 'envelope': 20}})


 # Через обычный словарь
 res = ['Ivanov paper 10', 'Petrov pens 5', 'Ivanov marker 3', 'Ivanov paper 7', 'Petrov envelope 20', 'Ivanov envelope 5']

 a_dict = {}
 for line in res:
     a, b, c = line.strip().split(' ')
     a_dict.setdefault(a, {}).setdefault(b, 0)
     a_dict[a][b] += int(c)

 print(a_dict)  # -> {'Ivanov': {'paper': 17, 'marker': 3, 'envelope': 5}, 'Petrov': {'pens': 5, 'envelope': 20}}
 -----------------------------------------------------------------------------------------------------------------------

 # Напишите код, который использует метод .get() вместо операторов if/else
 books = {"Life of Pi": "Adventure Fiction", "Good Omens": "Comedy"}
 s = 'Good Omens'

 print(books.get(s, 'Книга не найдена'))                       # -> Comedy
 print(books[s] if s in books.keys() else 'Книга не найдена')  # -> Comedy

 books = {"Life of Pi": "Adventure Fiction"}
 print(books.get(s, 'Книга не найдена'))                       # -> Книга не найдена
 print(books[s] if s in books.keys() else 'Книга не найдена')  # -> Книга не найдена
 -----------------------------------------------------------------------------------------------------------------------

 # Получить значение через get()/if-else                Важно Посмотри вариант с -1
 contacts = {"David": ["123-321-88", "david@test.com"]}

 s = 'David'
 print(contacts.get(s)[1] if s in contacts.keys() else 'Не найден')  # -> david@test.com
 print(contacts.get(s, ['Не найден'])[-1])                           # -> david@test.com    # Интересный Вариант

 s = 'Ivan'
 print(contacts.get(s)[1] if s in contacts.keys() else 'Не найден')  # -> Не найден
 print(contacts.get(s, ['Не найден'])[-1])                           # -> Не найден         # Интересный Вариант
 -----------------------------------------------------------------------------------------------------------------------

 # Какого цвета клетка?
 d = {'a': '2468', 'b': '1357', 'c': '2468', 'd': '1357', 'e': '2468', 'f': '1357', 'g': '2468', 'h': '1357'}
 a, b = 'b2'
 print('Белая' if b in d.get(a) else 'Чёрная')                     # -> Чёрная

 # Тоже самое
 a = 'b2'
 print('Чёрная' if (ord(a[0]) - int(a[1])) % 2 == 0 else 'Белая')  # -> Чёрная
 -----------------------------------------------------------------------------------------------------------------------

 # Сначало пользователь вводит число, а потом процент, который нужно от него посчитать.
 #  Как можно Сразу Вызывать lambda с аргументами                <-----                              <-----
 a, b = 128, 42
 print((lambda x, y: x / 100 * y)(a, b))  # -> 53.76
 print((lambda x, y: (x*y) / 100)(a, b))  # -> 53.76

 # Или посчитать % от числа
 print(f"{a / b:.2%}")                    # -> 304.76%
 -----------------------------------------------------------------------------------------------------------------------

 # lambda выводит минимальное число

 print((lambda *args: min(*args))([8, 13, 4, 42, 120, 7]))  # -> 4
 -----------------------------------------------------------------------------------------------------------------------

 # Нужно, чтобы номера телефонов, которые начинаются с "00", заменялись на "+"
 s = '0014860098'

 print(s.replace('00', '+', 1) if s.startswith('00') else s)     # -> +14860098
 print(__import__('re').sub(r'^00', sub_fun, s))                 # -> +14860098
 -----------------------------------------------------------------------------------------------------------------------

 # модуль предлагает универсальный парсер строк даты/времени   <----     <----     <----   Крутой модуль dateutil
 from dateutil import parser

 # Поменять местами или заменить Текст на число
 s = '7/26/2019'
 res = parser.parse(s, dayfirst=True)
 print(f"{res.day}/{res.month}/{res.year}")  # -> 26/7/2019

 s = 'January 1, 2021'
 res = parser.parse(s, dayfirst=True)
 print(f"{res.day}/{res.month}/{res.year}")  # -> 1/1/2021
 -----------------------------------------------------------------------------------------------------------------------

 # Аналог chunked из more_itertools Но строку не разбивает

 # Первый Вариант
 chunker = lambda data, chunk: (data[x:x + chunk] for x in range(0, len(data), chunk))

 # Второй Вариант
 def chunker(sequence, size):
     for i in range(0, len(sequence), size):
         yield sequence[i:i + size]

 print(list(chunker([1, 2, 3, 4, 5], 2)))  # -> [[1, 2], [3, 4], [5]]
 print(list(chunker(['abcde'], 2)))        # -> [['abcde']]
 -----------------------------------------------------------------------------------------------------------------------

 # от 6 до 11 включительно, программа выводит сообщение "Доброе утро!"
 # от 12 до 17 включительно, программа выводит сообщение "Добрый день!"
 # от 18 до 23 включительно, программа выводит сообщение "Добрый вечер!"
 # от 0 до 5 включительно, программа выводит сообщение "Доброй ночи!"

 print(["Доброй ночи!", "Доброе утро!", "Добрый день!", "Добрый вечер!"][int(input())//6])
 -----------------------------------------------------------------------------------------------------------------------

 # Требуется вывести одно число - количество различных типов данных в строке.
 a = '1, 2.5, "hello", [1, 2, 3], "world", 5'

 # Моё решение
 res = [type(i) for i in re.findall(r'(\[.*])|(\(.*\))', a)]
 res1 = re.sub(r'(\[.*])|(\(.*\))', '', a)
 res2 = [type(eval(i)) for i in res1.split(', ') if i]+res
 print(len(set(res2)))   # -> 4


 # Лучше варианты
 a = '1, 2.5, "hello", [1, 2, 3], "world", 5'

 # Посмотри что будет в eval()
 print(eval(a))  # -> (1, 2.5, 'hello', [1, 2, 3], 'world', 5)


 # Хороший вариант
 try:
     s = set(map(type, eval(a)))
     print(len(s))
 except:
     print(1)
 # -> 4

 # В качестве безопасной альтернативы для eval можно использовать ast.literal_eval:

 # from ast import literal_eval as eval
 # однако, literal_eval парсить только очень ограниченное подмножество элементов языка Python.

 print(len(set(map(type, eval(a.join('[]'))))))  # -> 4

 # Простой вариант
 a = eval('1, 2.5, "hello", [1, 2, 3], "world", 5')
 print(len(set(type(i) for i in a)) if type(a) == tuple else 1)  # -> 4
 print(len({type(i) for i in a}) if type(a) == tuple else 1)     # -> 4
 -----------------------------------------------------------------------------------------------------------------------

 # Дублирование фрагмента
 # Дана строка, в которой буква h встречается как минимум два раза. Повторите последовательность символов,
 # заключенную между первым и последнием появлением буквы h два раза, сами буквы h повторять не надо.

 s ='qwertyhasdfghzxcvb'.lower()
 res = s[:s.rfind('h')]+s[s.find('h')+1:]
 print(s[:s.rfind('h')]+s[s.find('h')+1:])  # -> qwertyhasdfgasdfghzxcvb

 assert res == 'qwertyhasdfgasdfghzxcvb'
 -----------------------------------------------------------------------------------------------------------------------

 # Суммирует все кубические значения от 1 до n (включительно) и возвращает эту сумму.

 # Можно перед range НЕ ставить list               # Тоже самое
 def sum_cubes(n):                                 def sum_cubes(n):
     return sum(map(lambda x: x**3, range(n+1)))       return sum(i**3 for i in range(n+1))

 print(sum_cubes(10), 3025)  # -> 3025 3025


 # Интересный вариант!!!
 def sum_cubes(n):
     res = iter(list(range(n+1)))
     return sum([next(res)**3 for _ in range(n+1)])

 print(sum_cubes(10), 3025)  # -> 3025 3025
 -----------------------------------------------------------------------------------------------------------------------

 # "Even" для четных чисел или "Odd" для нечетных чисел.
 # Функция также должна возвращать "Even" или "Odd" при доступе к значению по целочисленному индексу.

 # Тоже самое                                        # Тоже самое
 class EvenOrOdd:                                    class EvenOrOdd:
     def __call__(self, num):                            def __call__(self, number):
         return "Even" if num % 2 == 0 else "Odd"            return ['Even', 'Odd'][number % 2]

     def __getitem__(self, num):                         def __getitem__(self, number):
         return self(num)                                    return self.__call__(number)

 even_or_odd = EvenOrOdd()

 print(even_or_odd(10))  # -> Even
 print(even_or_odd(9))   # -> Odd

 # Можно вызывать через []
 print(even_or_odd[10])  # -> Even
 print(even_or_odd[9])   # -> Odd

 # Тоже самое
 class Obj:
     __call__ = __getitem__ = lambda self, n: "Even" if not n % 2 else "Odd"

 even_or_odd = Obj()

 # Тоже самое
 even_or_odd = type('', (), {'__call__': (f:=lambda _, n: 'EOvdedn'[n%2::2]), '__getitem__': f})()
 -----------------------------------------------------------------------------------------------------------------------

 # Найти индекс в списке две заглавные буквы О, с как минимум одним тире между ними!

 find_glasses = lambda x: next(i for i, v in enumerate(x) if re.search(r'O-+O', v))

 print(find_glasses(["O-O"]), 0)           # -> 0 0
 print(find_glasses(['o-o', "O---O"]), 1)  # -> 1 1
 -----------------------------------------------------------------------------------------------------------------------

 # JavaScript предоставляет встроенный метод parseInt. Его можно использовать следующим образом:
 # parseInt("10")              возвращается 10
 # parseInt("10 apples") также возвращается 10

 # Мы хотели бы, чтобы он возвращался "NaN"(в виде строки) во втором случае, поскольку входная строка не является допустимым числом.

 def my_parse_int(strn):
     return int(s.group()) if (s:=re.fullmatch(r'\s*\d+\s*', strn)) else 'NaN'

 print(my_parse_int("1"), 1)              # -> 1 1
 print(my_parse_int("  1 "), 1)           # -> 1 1
 print(my_parse_int("08"), 8)             # -> 8 8
 print(my_parse_int("5 friends"), "NaN")  # -> NaN NaN
 print(my_parse_int("16.5"), "NaN")       # -> NaN NaN


 # Тоже самое
 my_parse_int = lambda s: int(s) if s.strip().isdigit() else "NaN"


 # Хитрый вариант
 def my_parse_int(s):
     try:
         return int(s)
     except ValueError:
         return 'NaN'

 -----------------------------------------------------------------------------------------------------------------------

 # Реализуйте функцию createTemplate, которая принимает строку с тегами, упакованными {{brackets}} в качестве входных
 # данных, и возвращает замыкание, которое может заполнять строку данными (плоский объект, где ключами являются имена тегов).

 # Пример что должно быть на выходе:

 # template = create_template("{{name}} likes {{animalType}}")
 # template(name="John", animalType="dogs")  # ->  John likes dogs

 # Первый вариант
 from jinja2 import Template

 def create_template(template):
     return lambda **vals: Template(template).render(vals)


 # Второй вариант
 def create_template(template):
     return lambda **kwargs: re.sub(r'{{(.*?)}}', lambda m: kwargs.get(m.group(1), ''), template)


 # Третий вариант
 def create_template(template):
    def closure(**kwargs):
        return re.sub(r"{{(\w+)}}", lambda x: kwargs.get(x.group(1)) ,template)

    return closure


 template = create_template("{{firstName}} {{lastName}} likes {{interests}}")
 print(template(firstName="John", lastName="Smith", interests="sport"), "John Smith likes sport")
 print(template(firstName="Albert", lastName="Einstein", occuptation="physicist"), "Albert Einstein likes ")
 -----------------------------------------------------------------------------------------------------------------------

 Валидация пароля  длина пароля От 8 до 20 символов  1 заглавная, 1 строчная, 1 цифра, специальные символы из!@#$%^&*?

 # Первый вариант
 def check_password(s):
     if re.search('^(?=.*?[a-z])(?=.*?[A-Z])(?=.*?\d)(?=.*?[!@#$%^&*?])[a-zA-Z\d!@#$%^&*?]{8,20}$', s):
         return 'valid'
     else:
         return 'not valid'


 # Второй вариант
 PATTERN = re.compile(
 '^'                   # begin string
 '(?=.*?[A-Z])'        # at least one uppercase letter
 '(?=.*?[a-z])'        # at least one lowercase letter
 '(?=.*?\d)'           # at least one digit
 '(?=.*?[!@#$%^&*?])'  # at least one special character
 '[A-Za-z\d!@#$%^&*?]' # only the given characters
 '{8,20}'              # between 8 and 20 characters long
 '$'                   # end string
 )

 def check_password(s):
     return "valid" if PATTERN.match(s) else "not valid"

 print(check_password("P1@p"), "not valid")  # -> not valid not valid
 print(check_password("P1@pP1@p"), "valid")  # -> valid valid
 -----------------------------------------------------------------------------------------------------------------------

 # Ваша задача — удалить все последовательные дубликаты
 def remove_consecutive_duplicates(s):
     res = []
     for i in s.split():
         if i not in res:
             res.append(i)
         if i != res[-1]:
             res.append(i)
     return ' '.join(res)


 # Тоже самое
 from itertools import groupby

 def remove_consecutive_duplicates(s):
     return ' '.join(k for k,_ in groupby(s.split()))

 # Тоже самое
 def remove_consecutive_duplicates(s):
     return re.sub(r'\b(\w+)(?:\s\1)+\b', r'\1', s)


 print(remove_consecutive_duplicates('alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'))
 # alpha beta gamma delta alpha beta gamma delta

 print(remove_consecutive_duplicates('1 2 2 2 2 3 3 3 3 3 3 3 3 3'))  # -> 1 2 3
 -----------------------------------------------------------------------------------------------------------------------

 # Создайте регулярное выражение, которое соответствует строке со строчными символами в алфавитном порядке,
 # включая любое количество пробелов. Между группами одинаковых букв НЕ может быть пробелов. Начальные и конечные пробелы
 # также разрешены. Должна соответствовать пустая строка.

 REGEX = r'^ *a* *b* *c* *d* *e* *f* *g* *h* *i* *j* *k* *l* *m* *n* *o* *p* *q* *r* *s* *t* *u* *v* *w* *x* *y* *z* *\Z'
 REGEX = fr"\A *{'* *'.join('abcdefghijklmnopqrstuvwxyz')}* *\Z"
 -----------------------------------------------------------------------------------------------------------------------

 # Вам будет дан массив строк. Слова в массиве должны сцепляться вместе, где одна или несколько букв в конце одного слова
 # будут иметь те же буквы (в том же порядке), что и следующее слово в массиве.

 # Моё решение
 import re
 from itertools import pairwise

 def word_mesh(words):
     res = []
     for i in pairwise(words):
         for j in range(len(i[0])):
             if re.match(rf'{i[0][j:]}', i[1]):
                 res.append(i[0][j:])
                 break
     return ''.join(res) if len(res)+1 == len(words) else "failed to mesh"


 # Тоже самое
 def word_mesh(arr):
     common = re.findall(r'(.+) (?=\1)',' '.join(arr))
     return ''.join(common) if len(common) + 1 == len(arr) else 'failed to mesh'

 print(word_mesh(["beacon", "condominium", "umbilical", "california"]), "conumcal")               # -> conumcal conumcal
 print(word_mesh(["allow", "lowering", "ringmaster", "terror"]), "lowringter")                    # -> lowringter lowringter
 print(word_mesh(['muchbetter', 'terriblestorm', 'stormwarning', 'greatlymissed']), 'terstormg')  # -> terstormg terstormg
 -----------------------------------------------------------------------------------------------------------------------

 # Верните общий балл в виде целого числа.
 def eval_parentheses(s):
     return eval(s.replace(')(', ')+(').replace('()', '1').replace('(', '2*('))


 # Тоже самое
 from re import compile

 REGEX = compile(r"\(\)|[\(\)]").finditer

 def eval_parentheses(s):
     level = result = 0
     for x in REGEX(s):
         match x.group(0):
             case "(": level += 1
             case ")": level -= 1
             case _:  result += 1 << level
     return result

 print(eval_parentheses("()"), 1)         # -> 1 1
 print(eval_parentheses("(())"), 2)       # -> 2 2
 print(eval_parentheses("()()"), 2)       # -> 2 2
 print(eval_parentheses("((())())"), 6)   # -> 6 6
 print(eval_parentheses("(()(()))"), 6)   # -> 6 6
 print(eval_parentheses("()(())"), 3)     # -> 3 3
 print(eval_parentheses("()((()))"), 5)   # -> 5 5
 -----------------------------------------------------------------------------------------------------------------------

 # Если строка может рассматриваться как повторение более простого/короткого подшаблона или нет.

 def has_subpattern(strng):
     return bool(re.fullmatch(r'(.+)\1+', strng))                     <-----        \1+

 print(has_subpattern("a"), False)          # -> False False
 print(has_subpattern("aaaa"), True)        # -> True True
 print(has_subpattern("abcd"), False)       # -> False False
 print(has_subpattern("abababab"), True)    # -> True True
 print(has_subpattern("ababababa"), False)  # -> False False
 -----------------------------------------------------------------------------------------------------------------------

 # Есть два кортежа, получить третий как объединение уникальных элементов первых двух кортежей, НЕ встречающихся
 # одновременно в обоих кортежах  >>> (1, 2, 3, 4, 5)

 a = (1, 2, 3)
 b = (3, 4, 5)

 print(tuple({*a, *b}))         # ->  (1, 2, 3, 4, 5)
 print(tuple(set(a) + set(b)))  # ->  TypeError: unsupported operand type(s) for +: 'set' and 'set'
 print(set(tuple(a + b)))       # ->  {1, 2, 3, 4, 5}
 print((a + b).unique())        # ->  AttributeError: 'tuple' object has no attribute 'unique'
 -----------------------------------------------------------------------------------------------------------------------

 # Какие обозначения не стоит использовать при именовании с точки зрения рекомендаций PEP 8?

 [X] 1. l
 [X] 2. O
 [ ] 3. i
 [X] 4. L
 [ ] 5. a
 [X] 6. I
 [ ] 7. bad_name

 # Обьяснение
 1. `l` (маленькая буква "l") - может быть спутана с цифрой "1".
 2. `O` (большая буква "O")   - может быть спутана с цифрой "0".
 3. `I` (большая буква "I")   - может быть спутана с цифрой "1".
 4. `L` (большая буква "L")   - может быть спутана с цифрой "1".
 -----------------------------------------------------------------------------------------------------------------------

 # По рекомендации PEP 8 каким должен быть единичный отступ?

 4 пробела
 -----------------------------------------------------------------------------------------------------------------------

 # Для чего используется пустой слайс [:] списка?

 # Для получения всех элементов коллекции
 print([1, 2, 3][:])  # -> [1, 2, 3]
 # Для кортежа тоже самое
 print((1, 2, 3)[:])  # -> (1, 2, 3)
 -----------------------------------------------------------------------------------------------------------------------

 # Отметьте верные способы создать список (list) с элементами [1, 2, 3, 4]

 print([i + 1 for i in range(4)])       # ->  [1, 2, 3, 4]
 print([i for i in range(4)],)          # ->  [0, 1, 2, 3]
 print([i for i in range(5)][1:])       # ->  [1, 2, 3, 4]
 print(list(i + 1 for i in range(4)))   # ->  [1, 2, 3, 4]
 -----------------------------------------------------------------------------------------------------------------------

 Необходимо обменять значение двух переменных, не применяя других переменных. Отметьте верный способ.

 a = 1
 b = 'q'

 print(swap(a, b))  # -> NameError: name 'swap' is not defined
 print(a.swap(b))   # -> AttributeError: 'int' object has no attribute 'swap'
 {a, b} = {b, a}    # -> SyntaxError: cannot assign to set display here. Maybe you meant '==' instead of '='?

 a, b = b, a
 print(a, b)  # -> q 1
 -----------------------------------------------------------------------------------------------------------------------

 # Необходимо обменять значение двух переменных, не применяя других переменных. Отметьте верный способ.
 # >>> {'John': 1, 'Peter': 2}

 a = ('John', 'Peter')
 b = (1, 2)

 print({key: value for key, value in zip(a, b)})  # -> {'John': 1, 'Peter': 2}
 print({key: value for key, value in (a, b)})     # -> {'John': 'Peter', 1: 2}
 print(dict(keys=a, values=b))                    # -> {'keys': ('John', 'Peter'), 'values': (1, 2)}
 print({key: b[i] for i, key in enumerate(a)})    # -> {'John': 1, 'Peter': 2}

 print(dict(zip(a, b)))                           # -> {'John': 1, 'Peter': 2}
 -----------------------------------------------------------------------------------------------------------------------

 # Интересный пример
 a = [[]] * 3
 a[1].append(1)
 print(a)        # -> [[1], [1], [1]]
 -----------------------------------------------------------------------------------------------------------------------

 Важно !!! \1+
 # Если в строке встречаются дубликаты более двух буквенных символов, возвращать строку со всеми лишними символами в скобках.


 # Первый Вариант
 def string_parse(s):
     if isinstance(s, str):
         return re.sub(r"(.)\1(\1+)", r"\1\1[\2]", s)
     return "Please enter a valid string"

 print(string_parse("aaaabbcdefffffffg"), "aa[aa]bbcdeff[fffff]g")  # -> aa[aa]bbcdeff[fffff]g aa[aa]bbcdeff[fffff]g

 assert string_parse("aaaabbcdefffffffg") == "aa[aa]bbcdeff[fffff]g"


 # Второй Вариант
 def string_parse(string):
     return re.sub(r'(.)\1(\1+)', r'\1\1[\2]', string) if isinstance(string, str) else 'Please enter a valid string'



 # Моё решение!!!   Важно (\w)\1+
 def string_parse(strng):
     c = strng
     if type(strng) != str:
         return "Please enter a valid string"
     if not strng:
         return strng
     res = []
     while strng:
         if res_2 := re.match(r'(\w)\1+', strng):               #  (\w)\1+   <-----   <-----
             res.append(res_2.group())
             strng = strng.replace(res_2.group(), '', 1)
             continue
         if res_3 := re.match(r'\w', strng):
             res.append(res_3.group())
             strng = strng.replace(res_3.group(), '', 1)
     res_res = ''.join([f'{i[:2]}[{i[2:]}]' if len(i) > 2 else i for i in res])
     return c if all([len(i) <= 2 for i in res]) else res_res
 -----------------------------------------------------------------------------------------------------------------------

 # is_audio , соответствует 1 или + заглавным/строчным буквам (возможны комбинации), с расширением .mp3, .flac, .alac или .aac.
 # is_image , соответствует 1 или + заглавным/строчным буквам (возможны комбинации), с расширением .jpg, .jpeg, .png, .bmp или .gif.

 # Первый вариант
 def is_audio(filename):
     name, ext = filename.split('.')
     return name.isalpha() and ext in {'mp3', 'flac', 'alac', 'aac'}

 def is_image(filename):
     name, ext = filename.split('.')
     return name.isalpha() and ext in {'jpg', 'jpeg', 'png', 'bmp', 'gif'}


 # Второй вариант
 def is_audio(file_name):
     return bool(re.match(r'^[A-Za-z]+\.(mp3|flac|alac|aac)$', file_name))

 def is_image(file_name):
     return bool(re.search(r'^[A-Za-z]+\.(jpg|jpeg|png|bmp|gif)$', file_name))


 print(is_audio("Nothing Else Matters.mp3"), False)    # -> False False
 print(is_audio("NothingElseMatters.mp3"), True)       # -> True True
 -----------------------------------------------------------------------------------------------------------------------

 # Если с первой строчки написать/ Вначале файла/модуля

 '''Hello World!'''
 print(__doc__)  # -> Hello World!
 -----------------------------------------------------------------------------------------------------------------------

 # Команда замена print()   __import__('sys').stdout.write('Принимает на вход строку')
 # ЧТОБЫ БЫЛ КАК print   ДОБАВЛЯЕМ В КОНЦЕ \n

 # Будет работать быстрее чем print        у print - БУДУТ ДОПОЛНИТЕЛЬНЫЕ РАСХОДЫ    <-----      <-----    <-----
 # Разница в производительности может быть НЕЗНАЧИТЕЛЬНОЙ в большинстве случаев      <-----      <-----    <-----

 # Просто записывает строку в стандартный вывод без дополнительных обработок.
 __import__('sys').stdout.write(f'{[1, 2, 3]}\n')       # -> [1, 2, 3]

 # Выполняет больше операций, чем просто вывод текста. Обрабатывает аргументы и может принимать дополнительные параметры
 print([1, 2, 3])                                       # -> [1, 2, 3]


 # Интересный пример!   два варианта выведут одно и тоже                            <-----            <-----

 __import__('sys').stdout.write('Hello World!')  # -> 'Hello World!'                <-----            <-----
 print('Hello World!')                           # -> 'Hello World!'

 # Можно с ф-строкой использовать
 world = 'World'
 __import__('sys').stdout.write(f'Hello {world}!')  # -> 'Hello World!'

 # Принимает только строку иначе ОШИБКА!
 __import__('sys').stdout.write(str([1, 2, 3]))  # -> [1, 2, 3]
 __import__('sys').stdout.write([1, 2, 3])  # -> TypeError: write() argument must be str, not list

  # ЧТОБЫ БЫЛ КАК print   ДОБАВЛЯЕМ В КОНЦЕ \n                                      <-----            <-----
 __import__('sys').stdout.write(str([1, 2, 3]) + '\n')  # -> [1, 2, 3]
 __import__('sys').stdout.write(f'{[1, 2, 3]}\n')       # -> [1, 2, 3]
 -----------------------------------------------------------------------------------------------------------------------

 # Изменится ли значение a?
 a = 10
 B = [a for a in range(20, 30)]
 print(a)  # -> 10
 -----------------------------------------------------------------------------------------------------------------------

 # Возвращает сумму элементов переданного списка.  Учитывать нужно и отрицательные числа

 def sum_eval(value: int) -> int:
     return eval('+'.join(re.sub(r'[^-\d+]', '', str(value))))

 print(sum_eval([1, 2, 3]))  # -> 6
 -----------------------------------------------------------------------------------------------------------------------

 # Создать полную копию встроенного объекта range. Он может быть вызван от одного, двух или трех аргументов.
 # P.S. И да, функцией range пользоваться нельзя, можете конечно попробовать, но у вас ничего не получится

 def my_range_gen(*args):
     try:
         return vars(__builtins__)['range'](*args)
     except:
         return iter('')

 for i in my_range_gen(5):
     print(i, end=' ')     # -> 0 1 2 3 4
 -----------------------------------------------------------------------------------------------------------------------

 Интересные Возможности!!!

 # Можно использовать все строенные функции
 print(vars(__builtins__)['max'](1, 2))                   # -> 2
 print(vars(__builtins__)['min'](['a', 'ab'], key=len))   # -> a
 print(vars(__builtins__)['sum']([1, 2]))                 # -> 3

 # Можно использовать все строенные функции через точку .
 print(__builtins__.min(1, 2))                            # -> 1
 print(__builtins__.max(['a', 'ab'], key=len))            # -> ab
 print(__builtins__.sorted([1, 2, 1]))                    # -> [1, 1, 2]

 # Посмотреть все возможные атрибуты
 print(__builtins__.globals())   # -> {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__':...
 print(__builtins__.locals())    # -> {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__':...
 print(__builtins__.vars())      # -> {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__':...
 -----------------------------------------------------------------------------------------------------------------------

 # Напишите функцию, которая будет брать ключ X и помещать его в середину Y, повторяя N раз.
 # Внутри f-строки можно использовать {} Внимательно посмотри пример
 def middle_me(N, X, Y):
     if N % 2 == 0:
         return f'{Y}{X:{Y}^{N}}'
     return X

 print(middle_me(18, 'z', '#'), '#########z#########')  # ->  #########z######### #########z#########
 print(middle_me(19, 'z', '#'), 'z')                    # ->  z z
 -----------------------------------------------------------------------------------------------------------------------

 # Remove Duplicates from Sorted Array/Удалить дубликаты из отсортированного массива    Можно просто использовать [:]

 # Мой Вариант
 def removeDuplicates(nums: List[int]) -> int:
     while len(nums) != len(set(nums)):
         for i in nums:
             if nums.count(i) > 1:
                 nums.remove(i)
     return len(nums)

 nums = [0,0,1,1,1,2,2,3,3,4]

 print(removeDuplicates(nums))  # 5
 print(nums)                    # [0, 1, 2, 3, 4]


 # Хороший варинт    Можно просто использовать [:]
 def removeDuplicates(nums: list[int]) -> int:
     nums[:] = sorted(set(nums))
     return len(nums)

 nums = [0,0,1,1,1,2,2,3,3,4]

 print(removeDuplicates(nums))  # [0, 1, 2, 3, 4]
 print(nums)                    # [0, 1, 2, 3, 4]
 -----------------------------------------------------------------------------------------------------------------------

 # Проверить совпадают типы или нет.
 def type_validation(variable, _type):
     return type(variable).__name__ == _type

 print(type_validation(42, "int"), True)     # -> True True
 print(type_validation("42", "int"), False)  # -> False False


 def type_validation(variable, _type):
     return _type in str(type(variable))

 print(type_validation(42, "int"), True)     # -> True True
 print(type_validation("42", "int"), False)  # -> False False
 -----------------------------------------------------------------------------------------------------------------------

 # Интересный момент

 print(type(42).__name__)  # -> int
 print(type(42))           # -> <class 'int'>
 -----------------------------------------------------------------------------------------------------------------------

 # Простая функция Фибоначчи с assert внутри   Лучше использовать functools lru_cache  Но с большим число НЕ будет Работать

 cache = {}

 def fib1(n):
     assert n >= 0
     if n not in cache:
         cache[n] = n if n <= 1 else fib1(n - 1) + fib1(n - 2)
     return cache[n]

 print(fib1(8))   # -> 21
 print(fib1(-1))  # -> AssertionError
 -----------------------------------------------------------------------------------------------------------------------

 # Вернуть элемент, следующий сразу за указанным элементом.
 def next_item(xs, item):
     xs = iter(xs)
     try:
         for i in xs:
             if i == item:
                 return next(xs)
     except:
         pass

 print(next_item([1, 2, 3, 4, 5, 6, 7, 8], 5), 6)  # -> 6 6
 print(next_item(['a', 'b', 'c'], 'd'), None)      # -> None None
 print(next_item(['a', 'b', 'c'], 'c'), None)      # -> None None
 print(next_item('testing', 't'), 'e')             # -> e e
 print(next_item(iter(range(1, 30000)), 12), 13)   # -> 13 13
 -----------------------------------------------------------------------------------------------------------------------

 # Логический оператор «исключающее или» (xor)    Разные варианты ответа
 def xor(a, b):
     return a != b

 def xor(a, b):
     return a ^ b

 def xor(a,b):
     return a is not b

 from operator import xor


 print(xor(False, False), False, "False xor False == False")
 print(xor(True, False), True, "True xor False == True")
 print(xor(False, True), True, "False xor True == True")
 print(xor(True, True), False, "True xor True == False")
 -----------------------------------------------------------------------------------------------------------------------

 # Отформатируйте любое предоставленное целое число в строку, расставив «,» (запятые) в нужных местах.    f'{100:,}'
 # Пример 100000 == '100,000'   5678545 == '5,678,545'   -420902 == '-420,902'
 # print(f'{1000000:,}')  # -> 1,000,000

 def number_format(n):
     return f'{n:,}'

 print(number_format(100000), "100,000")      # -> 100,000 100,000
 print(number_format(5678545), "5,678,545")   # -> 5,678,545 5,678,545
 print(number_format(-420902), "-420,902")    # -> -420,902 -420,902
 print(number_format(-3), "-3")               # -> -3 -3
 print(number_format(-1003), "-1,003")        # -> -1,003 -1,003
 -----------------------------------------------------------------------------------------------------------------------

 # Разделить по Нулям(0) и получить сумму   Merge Nodes in Between Zeros

 def mergeNodes(head):
     res = re.sub(r'[,\s\]\[]', '', str(head))
     return [eval('+'.join(i)) for i in re.split(r'0', res) if i]

 # Тоже самое но с map
 def mergeNodes(head):
     res = ''.join([*map(str, head)]).split('0')
     return [sum(map(int, ' '.join(i).split())) for i in res if i]

 head = [0,3,1,0,4,5,2,0]
 print(mergeNodes(head))  # -> [4, 11]
 head = [0,1,0,3,0,2,2,0]
 print(mergeNodes(head))  # -> [1, 3, 4]
 -----------------------------------------------------------------------------------------------------------------------

 # Проверяет, находятся ли гласные (a, e, i, o, u) и согласные в чередующемся порядке.
 def is_alt(s):
     return re.search(r'[aeiou]{2}|[^aeiou]{2}', s)

 print(is_alt("amazon"), True)   # -> None True
 print(is_alt("apple"), False)   # -> <re.Match object; span=(1, 3), match='pp'> False
 print(is_alt("banana"), True)   # -> None True
 print(is_alt("orange"), False)  # -> <re.Match object; span=(3, 5), match='ng'> False
 -----------------------------------------------------------------------------------------------------------------------

 # reversed/__reversed__() НЕ Работает с generator/iterator  (Любой итератор)

 print(*reversed([1 for _ in '123']))          # -> 1 1 1
 print([1 for _ in '123'].__reversed__())      # -> <list_reverseiterator object at 0x000001DB708FFA30>
 print(*reversed((1 for _ in '123')))          # -> TypeError: 'generator' object is not reversible
 print(*reversed(iter([1 for _ in '123'])))    # -> TypeError: 'list_iterator' object is not reversible
 -----------------------------------------------------------------------------------------------------------------------

 # Перевернуть генератор/итератор   reversed(list)

 # Через list
 my_list = [1, 2, 3, 4, 5]
 my_generator = (x**2 for x in my_list)

 for item in reversed(list(my_generator)):
     print(item, end=' ')  # -> 25 16 9 4 1


 # Тоже самое только через tuple
 my_list = [1, 2, 3, 4, 5]
 my_generator = (x**2 for x in my_list)

 for item in reversed(tuple(my_generator)):
     print(item, end=' ')  # -> 25 16 9 4 1


 # Что будет на выходе ПОСМОТРИ
 my_list = [1, 2, 3, 4, 5]
 my_generator = (x**2 for x in my_list)

 print(reversed(list(my_generator)))  # -> <list_reverseiterator object at 0x000001C4286F3A00>
 print(my_generator)                  # -> <generator object <genexpr> at 0x000001CA17B23850>
 print(list(my_generator))            # -> []
 -----------------------------------------------------------------------------------------------------------------------

 # Напишите программу, которая будет читать ТРИ любых ЧИСЛА в столбце, а затем эти же ТРИ ЧИСЛА выводить на экран
 # в том же порядке В ОДНУ СТРОКУ БЕЗ ПРОБЕЛОВ.

 a = '5'
 b = '6'
 c = '7'

 res = [a, b, c]


 print('{}{}{}'.format(*map(int, res)))  # -> 567
 print('{}{}{}'.format(*res))            # -> 567
 print('{}{}{}'.format(a, b, c))         # -> 567

 # Или сразу считываем ввод
 print(print('{}{}{}'.format(*map(int, open(0)))))
 print(*map(int, open(0)), sep='')
 print(*(input() for _ in 'eee'), sep='')
 [print(input(), end='') for _ in '___']
 -----------------------------------------------------------------------------------------------------------------------

 # format Не работает с ф-строкой  SyntaxError: f-string: empty expression not allowed

 a = 'Hello'
 b = 'World'
 c = 78

 print("{} набрал {} баллов на экзамене по {}!".format(a, c, b))   # -> Hello набрал 78 баллов на экзамене по World!
 print(f"{} набрал {} баллов на экзамене по {}!".format(a, c, b))  # -> SyntaxError: f-string: empty expression not allowed
 -----------------------------------------------------------------------------------------------------------------------

 # Можно использовать f-string в format в арументах

 print('{} {}'.format(f'Имя: {input()},', f'Возраст: {input()}'))
 -----------------------------------------------------------------------------------------------------------------------

 # Интересные примеры с import operator vs lambda

 import operator

 print(operator.itemgetter(1,3,5)('ABCDEFG'))      # -> ('B', 'D', 'F')
 print((lambda x: (x[1], x[3], x[5]))('ABCDEFG'))  # -> ('B', 'D', 'F')


 class MyObj:
     def __init__(self, arg):
         self.arg = arg
         self.name = 'name'

 m = MyObj('arg')
 print(operator.attrgetter('arg')(m))              # -> arg
 print(operator.attrgetter('name')(m))             # -> name
 print((lambda x: x.arg)(m))                       # -> arg

 print(operator.attrgetter('name', 'arg')(m))      # -> ('name', 'arg')
 print((lambda x: (x.arg, x.name))(m))             # -> ('arg', 'name')
 -----------------------------------------------------------------------------------------------------------------------

 # Как вывести в print Несколько распаковок  Оборачиваем выражение в ()  В Выражении два оператора * или ** Нельзя

 Python нельзя использовать два оператора распаковки `*` одновременно в одном выражении, особенно в контексте
 `if ... else`. Чтобы обойти это ограничение и распечатать содержимое списков, можно использовать один оператор *


 # Пример с *
 res = [1, 2, 7]
 res_2 = [4, 4, 5]

 print(*(res if sum(res) < sum(res_2) else res_2))  # -> 1 2 7
 print(*[res if sum(res) < sum(res_2) else res_2])  # -> [1, 2, 7]

 # Так можно!!
 print(*res, *res_2)                                # -> 1 2 7 4 4 5

 # Совмещение двух операторов `*` в `print()` напрямую НЕ поддерживается из-за синтаксических ограничений языка.
print(*res if sum(res) < sum(res_2) else *res_2)   # -> SyntaxError: invalid syntax


 # Пример с **
 dict1 = {'x': 1}
 dict2 = {'y': 2}

 # Это вызовет SyntaxError
 print(**dict1, **dict2)    # -> TypeError: 'x' is an invalid keyword argument for print()

 # Оборачиваем и будет работать!!!
 print({**dict1, **dict2})  # -> {'x': 1, 'y': 2}
 -----------------------------------------------------------------------------------------------------------------------

 # Напишите программу, которая получает два числа в качестве аргументов (значение двух катетов) и выводит в терминал
 # длину гипотенузы. Напомню, что сумма квадратов катета равна квадрату гипотенузы.

 # Очень интересно что   0.5 ==  .5    ТОЧКА ЧИСЛО тоже самое что и НОЛЬ ТОЧКА ЧИСЛО     <-----
 a, b = 3, 4
 print(sum([a ** 2, b ** 2]) ** .5)
 print(sum([a ** 2, b ** 2]) ** 0.5)
 -----------------------------------------------------------------------------------------------------------------------

 # Интересный пример    Можно опускать   до и после   точки .
 num1 = 40.000
 num2 = 40.0
 num3 = 40.
 num4 = 0.5
 num5 = .5

 print(num1)  # -> 40.0
 print(num2)  # -> 40.0
 print(num3)  # -> 40.0
 print(num4)  # -> 0.5
 print(num5)  # -> 0.5
 -----------------------------------------------------------------------------------------------------------------------

 # Напишите программу, которая выводит все пары соседних элементов списка чисел

 from itertools import pairwise

 numbers = [3, 7, 12, 5, 9]

 for i, j in pairwise(numbers):
     print(f'{i} и {j}', end=' ')                     # -> 3 и 7 7 и 12 12 и 5 5 и 9

 for i, _ in enumerate(numbers[:-1]):                                                     # <----- Интересный вариант
     print(numbers[i], "и", numbers[i + 1], end=' ')  # -> 3 и 7 7 и 12 12 и 5 5 и 9

 for i in range(len(numbers)-1):
     print(f'{numbers[i]} и {numbers[i+1]}', end=' ')  # -> 3 и 7 7 и 12 12 и 5 5 и 9
 -----------------------------------------------------------------------------------------------------------------------

 # Найдите ключ, соответствующий максимальному значению. Выведите этот ключ

 d = {"a": 10, "b": 20, "c": 15}

 print(max(d, key=d.get))  # -> b
 -----------------------------------------------------------------------------------------------------------------------

 # Словарь Содержащий только те пары ключ-значение, которые присутствуют в обоих словарях с одинаковыми значениями.

 d1 = {"a": 1, "b": 2, "c": 3}
 d2 = {"a": 1, "b": 4, "c": 3}

 print({i[0]: i[1] for i, j in zip(d1.items(), d2.items()) if i[1] == j[1]})  # -> {'a': 1, 'c': 3}
 print({k: v for k, v in d1.items() if (k, v) in d2.items()})                 # -> {'a': 1, 'c': 3}
 -----------------------------------------------------------------------------------------------------------------------

 # Напишите программу, которая распакует координаты для каждой точки и выведет их на экран.
 points = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

 for point in points:                    for i in points:
     x, y, z = point                         print('x: {}, y: {}, z: {}'.format(*i))
     print(f"x: {x}, y: {y}, z: {z}")

 # x: 1, y: 2, z: 3                      # x: 1, y: 2, z: 3
 # x: 4, y: 5, z: 6                      # x: 4, y: 5, z: 6
 # x: 7, y: 8, z: 9                      # x: 7, y: 8, z: 9
 -----------------------------------------------------------------------------------------------------------------------

 # Нужно оборачивать в кортеж в лямбде
 min_max = lambda lst: (min(lst), max(lst))
 print(min_max([1, -4, 23, 5, 33, 16]))      # -> (-4, 33)

 min_max = lambda lst: min(lst), max(lst)    # NameError: name 'lst' is not defined. Did you mean: 'List'?
 print(min_max([1, -4, 23, 5, 33, 16]))
 -----------------------------------------------------------------------------------------------------------------------

 # Интересный момент   Можно НЕ передавать аргументы при вызове функции
 def ff(*args, **kwargs):          def ff(*args, **kwargs):       def ff(*args, **kwargs):      def ff(*args, **kwargs
     return args, kwargs               pass                           return args                   return kwargs

 print(ff())  # -> ((), {})        print(ff())   # -> None        print(ff())  # -> ()          print(ff())  # -> {}
 -----------------------------------------------------------------------------------------------------------------------

 # Может определить Атрибут позже       # Если атрибут НЕ Установил Ошибка
 class Student:                         class Student:
     age = 10
     def show(self):                        def show(self):
         print(self.name, self.age)             print(self.name, self.age)

 student = Student()
 student.name = 'Jessa'                 student = Student()
 student.age = 14                       student.name = 'Jessa'
 student.show()    # -> Jessa 14        student.show()    # -> AttributeError: 'Student' object has no attribute 'age'
 -----------------------------------------------------------------------------------------------------------------------

 # Напишите функцию apply_multiple(funcs, value), которая принимает список функций funcs и значение value.
 Функция должна последовательно применять все функции из списка к значению и вернуть результат.

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
 -----------------------------------------------------------------------------------------------------------------------

 # Скобки помогают возводить в степень отрицательные числа.
 a = (-5)**2
 b = -5**2
 print(a)     # -> -25
 print(b)     # -> 25

 print((-5))  # -> -5
 -----------------------------------------------------------------------------------------------------------------------

 # Можно конкатенировать РАЗНЫЕ ИТЕРИРУЕМЫЕ объекты   # Тоже самое через extend

 a = [1]                                              a = [1]
 print(id(a))  # -> 2734326301824 # Одинаковые id     print(id(a))  # -> 2734326301824 # Одинаковые id
 a += (2, 3)                                          a.extend((2, 3))
 a += '45'                                            a.extend('45')
 a += {6, 7}                                          a.extend({6, 7})
 a += {'8': 1, 9: 0}                                  a.extend({'8': 1, 9: 0})
 print(id(a))  # -> 2734326301824 # Одинаковые id     print(id(a))  # -> 2734326301824 # Одинаковые id
 print(a)  # -> [1, 2, 3, '4', '5', 6, 7, '8', 9]     print(a)  # -> [1, 2, 3, '4', '5', 6, 7, '8', 9]
 -----------------------------------------------------------------------------------------------------------------------

 Дан массив чисел. Преобразовать исходный массив, вычитая максимальное значение массива из элементов массива,
 идущих после минимального.

 arr = [*map(int, '12 -30 23 43 1 -3 18 -25 44 31 -28 54 4 14 6 -40 12 -10 -23 21'.split())]

 min_arr = min(arr)
 max_arr = max(arr)
 min_index = arr.index(min_arr)

 for i in range(min_index + True, len(arr)):
     arr[i] -= max_arr

 print(' '.join(map(str, arr)))  # -> 12 -30 23 43 1 -3 18 -25 44 31 -28 54 4 14 6 -40 -42 -64 -77 -33
 -----------------------------------------------------------------------------------------------------------------------

 # Можно использовать цифры в reverse    ИНТЕРПРЕТИРУЮТСЯ как True и False   НО ЛУЧШЕ ИСПОЛЬЗУЕМ True или False
 lst = [1, 2, 3, 4, 5, 2]
 print(sorted(lst, reverse=True))   # -> [5, 4, 3, 2, 2, 1]
 print(sorted(lst, reverse=1))      # -> [5, 4, 3, 2, 2, 1]
 print(sorted(lst, reverse=11111))  # -> [5, 4, 3, 2, 2, 1]

 print(sorted(lst, reverse=False))  # -> [1, 2, 2, 3, 4, 5]
 print(sorted(lst, reverse=0))      # -> [1, 2, 2, 3, 4, 5]
 print(sorted(lst, reverse=00000))  # -> [1, 2, 2, 3, 4, 5]
 -----------------------------------------------------------------------------------------------------------------------

 # Очень инетересный пример LISTCOMPS/GENEXP Можно ставить ДВА УСЛОВИЯ ВНУТРИ!!!   ВНАЧАЛЕ и в КОНЦЕ
 print([i if i > 2 else 100 for i in [1, 2, 3]])           # -> [100, 100, 3]
 print([i if i > 2 else 100 for i in [1, 2, 3] if i > 1])  # -> [100, 3]
 print([i if i > 2 else 100 for i in [1, 2, 3] if i < 2])  # -> [100]
 print([i if i > 2 else 100 for i in [1, 2, 3] if i > 2])  # -> [3]
 print((i if i > 2 else 100 for i in [1, 2, 3] if i < 2))  # -> <generator object <genexpr> at 0x00000176AEF68D40>]
 -----------------------------------------------------------------------------------------------------------------------

 # Интересный момент  Без запятой внутри они склеиваются
 a = 'Hello'    'Hello'
 print(a)  # -> HelloHello
 -----------------------------------------------------------------------------------------------------------------------

 # format_map  и vars               vars - Работают с Эк
 s = '{name} has {n} messages'
 class Info:
     def __init__(self, name, n):
         self.name = name
         self.n = n

 a = Info('Guido', 37)
 print(s.format_map(vars(a)))         # -> Guido has 37 messages
 print(s.format(name='Guido', n=37))  # -> Guido has 37 messages
 print(s.format(name='Guido'))        # -> KeyError: 'n'
 -----------------------------------------------------------------------------------------------------------------------

 # textwrap   - для переформатирования выводимого текста

 import textwrap
 s = 'Look into my eyes, look into my eyes, the eyes, the eyes'
 print(textwrap.fill(s, 20))

 # Вывод
 '''Look into my eyes,
 look into my eyes,
 the eyes, the eyes'''
 -----------------------------------------------------------------------------------------------------------------------

 # БАЙТОВАЯ строка и ОБЫЧНАЯ строка
 s = 'Hello World'
 print(s[0])                     # -> H

 s_bytes = b'Hello World'
 print(s_bytes[0])               # -> 72

 # Декоде
 print(s_bytes.decode('ascii'))  # -> Hello World
 print(s_bytes)                  # -> b'Hello World'
 -----------------------------------------------------------------------------------------------------------------------

 # Порядок от старшего к младшего и наоборот
 x = 0x01020304

 print(x.to_bytes(4, 'big'))     # -> b'\x01\x02\x03\x04'
 print(x.to_bytes(4, 'little'))  # -> b'\x04\x03\x02\x01'
 -----------------------------------------------------------------------------------------------------------------------

 # Интересные примеры  inf   nan
 a = float('inf')
 print(a)            # -> inf
 print(a+45)         # -> inf
 print(a*10)         # -> inf
 print(10/a)         # -> 0.0
 print(a/a)          # -> nan

 b = float('-inf')
 print(a+b)          # -> nan

 c = float('nan')
 d = float('nan')
 print(c+23)         # -> nan
 print(c/2)          # -> nan
 print(c*2)          # -> nan
 print(__import__('math').sqrt(c))  # -> nan
 print(c == d)       # -> False
 print(c is d)       # -> False
 -----------------------------------------------------------------------------------------------------------------------

 # Интересный модуль dateutil
 from dateutil.relativedelta import relativedelta

 a = datetime(2012, 9, 23)

 # ТАК НЕ РАБОТАЕТ
 # a + timedelta(months=1)  # -> TypeError: 'months' is an invalid keyword argument for __new__()

 print(a+relativedelta(months=+1))          # -> 2012-10-23 00:00:00
 print(a+relativedelta(months=+4))          # -> 2013-01-23 00:00:00

 b = datetime(2012, 12, 21)
 d = b - a
 print(d)                                   # -> 89 days, 0:00:00
 d = relativedelta(b, a)

 print(d.months)                            # -> 2
 print(relativedelta(months=+2, days=+28))  # -> relativedelta(months=+2, days=+28)
 -----------------------------------------------------------------------------------------------------------------------

 # Функция strptime  Работает МЕДЛЕННО потому что написана на ЧИСЛОМ Python
 # Можно использовать  pandas, dateutil  или написать самописные функции

 from datetime import datetime, timedelta
 text = '2012-09-20'
 y = datetime.strptime(text, '%Y-%m-%d')
 z = datetime.now()
 diff = z - y
 print(diff)                                      # -> 4454 days, 14:06:11.801976
 print(timedelta(3, 77824, 177393))               # -> 3 days, 21:37:04.177393
 print(datetime(2012, 9, 23, 21, 37, 4, 177393))  # -> 2012-09-23 21:37:04.177393
 nice_z = datetime.strftime(z, '%A %B %d, %Y')
 print(nice_z)                                    # -> Saturday November 30, 2024



 # Если вы уверены что даты представлены в формате 'YYYY-MM-DD'  можно использовать такую функции  Работает в 7 раз БЫСТРЕЕ
 # ДЛЯ БОЛЬШИХ ОБЪЕМОВ ДАННЫХ БУДЕТ РАБОТАТЬ БЫСТРЕЕ

 from datetime import datetime
 def parse_ymd(s):
     year_s, mon_s, day_s = s.split('-')
     return datetime(int(year_s), int(mon_s), int(day_s))

 print(parse_ymd(text))  # -> 2012-09-20 00:00:00
 -----------------------------------------------------------------------------------------------------------------------

 # Распаковка из функции     # Функция также возвращает кортеж и выходит обычная распаковка
 def myfun():
     return 1, 2, 3

 a, b, c = myfun()
 print(a, b, c)  # -> 1 2 3

 x = myfun()
 print(x)       # -> (1, 2, 3)

 # Тоже самое
 a = (1, 2)             # Со скобками
 print(a)  # -> (1, 2)
 b = 1, 2               # Без скобок
 print(b)  # -> (1, 2)
 -----------------------------------------------------------------------------------------------------------------------

 # x - в lambda-выражении, является СВОБОДНАЯ ПЕРЕМЕННАЯ которая связывается во время выполнения, а НЕ вовремя определения

 x = 10
 a = lambda y: x + y
 x = 20
 b = lambda y: x + y
 print(a(10))  # -> 30
 print(b(10))  # -> 30

 x = 15
 print(a(10))  # -> 25
 print(b(10))  # -> 25

 # Чтобы lambda ЗАХВАТИЛА ЗНАЧЕНИЕ  нужно использовать значение по-умолчанию      x=x
 x = 100
 a = lambda y, x=x: x + y
 x = 200
 b = lambda y, x=x: x + y

 print(a(10))  # -> 110
 print(b(10))  # -> 210
 -----------------------------------------------------------------------------------------------------------------------

 # Хороший пример  ЗАХВАТИТЬ ПЕРЕМЕННУЮ

 funcs = [lambda x: x+n for n in range(5)]
 for f in funcs:
     print(f(0), end=' ')  # -> 4 4 4 4 4

 print()

 funcs = [lambda x, n=n: x+n for n in range(5)]
 for f in funcs:
     print(f(0), end=' ')  # -> 0 1 2 3 4
 -----------------------------------------------------------------------------------------------------------------------

 # ВЕРСИЯ с Замыканием Работает БЫСТРЕЕ  на 8% БЫСТРЕЕ . Выигрыш возникает за счет прямого доступа к переменным Эк.
 # Замыкание быстрее, потому что не используют дополнительную переменную self.    <----
 import sys

 class ClosureInstance:
     def __init__(self, locals=None):
         if locals is None:
             locals = sys._getframe(1).f_locals

         self.__dict__.update((key, value) for key, value in locals.items() if callable(value))

     def __len__(self):
         return self.__dict__['__len__']()


 def Stack():
     items = []
     def push(item):
         items.append(item)

     def pop():
         return items.pop()

     def __len__():
         return len(items)

     return ClosureInstance()

 s = Stack()
 s.push(10)
 s.push(20)
 s.push('Hello')
 print(len(s))   # -> 3
 print(s.pop())  # -> Hello
 print(s.pop())  # -> 20
 print(s.pop())  # -> 10



 class Stack2():
     def __init__(self):
         self.items = []


     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def __len__(self):
         return len(self.items)


 s = Stack()
 print('Stack ', timeit.timeit('s.push(1);s.pop()', 'from __main__ import s'))  # -> Stack  0.5749851999571547

 s = Stack2()
 print('Stack2', timeit.timeit('s.push(1);s.pop()', 'from __main__ import s'))  # -> Stack2 0.5046093000564724
 -----------------------------------------------------------------------------------------------------------------------

 # Пример использования Расширение свойства в подклассе
 class Person:
     def __init__(self, name):
         self.name = name

     @property
     def name(self):
         return self._name

     @name.setter
     def name(self, value):
         if not isinstance(value, str):
             raise TypeError("Expected a string")
         self._name = value

     @name.deleter
     def name(self):
         raise AttributeError("Can't delete attribute")


 # Чтобы расширить только один из методов свойства, используйте такой код:
 class SubPerson(Person):                       class SubPerson(Person):
     @Person.name.getter      # РАБОТАЕТ            @property                   # НЕ РАБОТАЕТ     <-----    <-----
                                                    # @Person.getter            # Попробуй такой вариант с ним ошибка
     def name(self):                                def name(self):
         print('Getting name')                          print('Getting name')
         return super().name                            return super().name

     @Person.name.setter                                                                          <-----    <-----
     def name(self, value):
         print('Setting name to', value)
         super(SubPerson, SubPerson).name.__set__(self, value)


 s = SubPerson("Guido")
 s.name              # -> Setting name to Guido
 s.name = 'Larry'    # -> Setting name to Guido

 s.name = 42
 # -> Setting name to 42
 # -> TypeError: Expected a string
 -----------------------------------------------------------------------------------------------------------------------

 # Сигнатура вызываемого объекта  inspect.signature
 from inspect import signature

 def spam(x, y, z=42):
     pass

 sig = signature(spam)
 print(sig)             # -> (x, y, z=42)
 print(sig.parameters)  # -> OrderedDict([('x', <Parameter "x">), ('y', <Parameter "y">), ('z', <Parameter "z=42">)])
 print(sig.parameters['z'].name)     # -> z
 print(sig.parameters['z'].default)  # -> 42
 print(sig.parameters['z'].kind)     # -> POSITIONAL_OR_KEYWORD
 -----------------------------------------------------------------------------------------------------------------------

 # Декораторы  КЛАССА И ЭК
 from functools import wraps

 class A:
     def decorator(self, func):
         @wraps(func)
         def wrapper(*args, **kwargs):
             print('Decorator 1')
             return func(*args, **kwargs)
         return wrapper

     @classmethod
     def decorator2(cls, func):
         @wraps(func)
         def wrapper(*args, **kwargs):
             print('Decorator 2')
             return func(*args, **kwargs)
         return wrapper

 a = A()

 @a.decorator   # Применения из ЭК                                      <-----     <-----
 def spam():
     pass

 @A.decorator2  # Применения из Класса                                  <-----     <-----
 def grok():
     pass
 -----------------------------------------------------------------------------------------------------------------------

 # Чтобы определить декоратор как ЭК  - нужно чтобы в нем были методы  __call__()  и  __get__()
 import types
 from functools import wraps

 class Profiled:

     def __init__(self, func):
         wraps(func)(self)
         self.ncalls = 0

     def __call__(self, *args, **kwargs):
         self.ncalls += 1
         return self.__wrapped__(*args, **kwargs)

     def __get__(self, instance, owner):
         if instance is None:
             return self
         else:
             return types.MethodType(self, instance)

 @Profiled
 def add(x, y):
     return x + y

 class Spam:
     @Profiled
     def bar(self, x):
         print(self, x)

 print(add(2, 3))    # -> 5
 print(add(4, 5))    # -> 9
 print(add.ncalls)   # -> 2

 s = Spam()
 s.bar(1)            # -> <__main__.Spam object at 0x000001AD739E5890> 1
 s.bar(2)            # -> <__main__.Spam object at 0x000001AD739E5890> 2
 -----------------------------------------------------------------------------------------------------------------------

 # РАБОТА СБОРЩИКА МУСОРА И СЛАБЫХ ССЫЛОК
 class Data:
     def __del__(self):
         print('Data.__del__')


 class Node:
     def __init__(self):
         self.data = Data()
         self.parent = None
         self.children = []


     # НИКОГДА ТАК НЕ ДЕЛАЙТЕ
     # ПОКАЗАНО ТОЛЬКО ДЛЯ ДЕМОНСТРАЦИИ ПАТОЛОГИЧЕСКОГО ПОВЕДЕНИЯ
     def __del__(self):
         del self.data
         del self.parent
         del self.children

     def add_child(self, child):
         self.children.append(child)
         child.parent = self


 # В ЭТОМ СЛУЧАЕ СТУРУКТУРА ДАННЫХ НИКОГДА НЕ БУДЕТ УДАЛЕНА СБОРЩИКОМ МУСОРА
 a = Node()
 a.add_child(Node())
 # Data.__del__
 # Data.__del__
 del a            # Нет сообщения (не собрано)
 import gc
 gc.collect()     # Нет сообщения (не собрано)


 # БУДЕТ УДАЛЕНА СБОРЩИКОМ МУСОРА   Слабые ссылки решают проблему ссылочных циклов   <-----
 import weakref
 a = Node()      # -> Data.__del__
 a_ref = weakref.ref(a)
 print(a_ref)    # -> <weakref at 0x0000029705565490; to 'Node' at 0x000002977FACEAD0>
 print(a_ref())  # -> <__main__.Node object at 0x000001AD3FA8EB10>
 del a
 Data.__del__
 print(a_ref())  # -> None
 -----------------------------------------------------------------------------------------------------------------------

 # Интересный пример
 x = 3
 [print(*[x] * 4, end=' \n') for _ in range(2)]

 # 3 3 3 3
 # 3 3 3 3
 -----------------------------------------------------------------------------------------------------------------------

 # Интересный пример.   Интересно еще вывод сдвигает если вставлять его в комменты
 for k in range(3):
     print(*[k * i for i in range(5)], sep='\t', end='\t\n')

 #  0	0	0	0	0
 #  0	1	2	3	4
 #  0	2	4	6	8
 -----------------------------------------------------------------------------------------------------------------------

 # Выведите в строке числа по убыванию от a до b с интервалом 5.

 a, b = 20, 0
 res = [i for i in range(a-1, b-1, -5)]
 print(*res)  # -> 19 14 9 4
 -----------------------------------------------------------------------------------------------------------------------

 # abs() возвращает положительное значение для целых и вещественных чисел, а для комплексных чисел — их модуль

 print(abs(-3.14))   # -> 3.14
 print(abs(-5))      # -> 5
 print(abs(3 - 4j))  # -> 5.0   # Вывод: 5.0 (модуль комплексного числа)
 -----------------------------------------------------------------------------------------------------------------------

 # Lambda function in list comprehensions  Лямбда+ф-строка в Listcomps:
 f = lambda x: x*x
 [f(x) for x in range(5)]                # -> [0, 1, 4, 9, 16]
 [f"{f(x)}" for x in range(5)]           # -> ['0', '1', '4', '9', '16']  ПРИМЕР с   f-string

 [(lambda x: x**2)(i) for i in range(5)] # -> [0, 1, 4, 9, 16]
 [i**2 for i in range(5)]                # -> [0, 1, 4, 9, 16]
 -----------------------------------------------------------------------------------------------------------------------

 # ОЧЕНЬ ИНТЕРЕСНЫЙ ПРИМЕР ПОДУМАЙ ПОЧЕМУ!!!       <-----      <-----
 sets = {0, 1, 2, 3}
 sets.add((frozenset(('a', 'b'))))
 print(sets)  # -> {0, 1, 2, 3, frozenset({'a', 'b'})}
 sets.remove({'a', 'b'})  # <-----   Можно удалить множество set из set
 print(sets)  # -> {0, 1, 2, 3}

 # ОТВЕТ ПОЧЕМУ В ФИГУРНЫХ   это его стандартное строковое представление (repr).
 print(frozenset(('a', 'b')))  # -> frozenset({'b', 'a'})
 print(frozenset(['a', 'b']))  # -> frozenset({'b', 'a'})
 print(set(('a', 'b')))        # -> {'a', 'b'}
 print(set(['a', 'b']))        # -> {'a', 'b'}

 # Независимо от того, передан кортеж, список или множество, repr(frozenset(...)) всегда возвращает строку в формате
 # frozenset({...}). Это сделано для единообразия и удобства отладки.
 -----------------------------------------------------------------------------------------------------------------------

 # .keys() и .items() объекта  dict()  Удивительно похожи на frozenset()
 # .keys() и items() -  Поддерживают наиболее полезные операторы и методы класса frozenset()   <-----
 d1 = dict(a=1, b=2, c=3, d=4)
 d2 = dict(b=20, d=40, e=50)

 # Легко получить пересекающиеся ключи
 print(d1.keys() & d2.keys())     # ->  {'d', 'b'}

 print(d1.keys() - d2.keys())     # ->  {'a', 'c'}
 print(d1.keys() | d2.keys())     # ->  {'c', 'e', 'd', 'a', 'b'}

 print(d1.items() & d2.items())   # ->  set()
 print(d1.items() - d2.items())   # ->  {('b', 2), ('d', 4), ('a', 1), ('c', 3)}
 print(d1.items() | d2.items())   # ->  {('b', 2), ('b', 20), ('a', 1), ('e', 50), ('c', 3), ('d', 40), ('d', 4)}
 -----------------------------------------------------------------------------------------------------------------------

 # Нечистый lstrip   lst[:]  return НЕ НУЖЕН при изменении списка                                             <-----

 # Напишите функцию lstrip, которая принимает список lst и значение value. Функция lstrip должна удалить из начала списка
 # lst все упоминания значения value, остальные элементы должны остаться без изменения, даже те, которые равны значению
 # value, но не находятся в начале списка.

 # Изначальный список lst должен измениться после вызова lstrip. Сама lstrip ничего не возвращает

 def lstrip(lst, value):
     # lst[::]  Тоже самое будет
     lst[:] =  [*__import__('itertools').dropwhile(lambda x: x.__eq__(value), lst)]

 data = [0, 0, 1, 0, 2, 3]
 print(data)                  # -> [0, 0, 1, 0, 2, 3]
 print(lstrip(data, 0)) # -> None
 print(data)                  # -> [1, 0, 2, 3]
 -----------------------------------------------------------------------------------------------------------------------

 # Вводится строка с нечётным количеством символов, нужно вывести символ посередине.
 import numpy as np
 res = python!
 print(res[int(np.median(list(range(len(res)))))])  # -> h
 print(np.median(res))                              # -> Ошибка!!  Работает только с числами!

 # Простой вариант!
 print(res[len(res) // 2])                          # -> h
 -----------------------------------------------------------------------------------------------------------------------

 # Доп. решение sympy fibonacci
 from sympy import fibonacci
 print(fibonacci(50))                       # -> 12586269025

 print(__import__('sympy').fibonacci(50))   # -> 12586269025
 -----------------------------------------------------------------------------------------------------------------------

 # Интересный факториал из разных модулей

 print((lambda x: __import__('sympy').factorial(x))(6))  # -> 720
 print((lambda x: __import__('math').factorial(x))(6))   # -> 720
 -----------------------------------------------------------------------------------------------------------------------

 # Разные варианты рекурсивной функции  Сумма списка
 res = [2, 3, 8, 11, 4, 6]

 # Обычная рекурсивная функция
 def recursive_sum(lst):
     if len(lst) == 1:
         return lst[0]
     else:
         return lst[0] + recursive_sum(lst[1:])

 print(recursive_sum(res))  # -> 34


 # Рекурсивная лямбда функция Обычная
 rec = (lambda f: lambda lst: lst[0] if len(lst) == 1 else lst[0] + f(f)(lst[1:]))(
     lambda f: lambda lst: lst[0] if len(lst) == 1 else lst[0] + f(f)(lst[1:])
 )

 print(rec(res))            # -> 34


 # Рекурсивная лямбда функция через redude
 from functools import reduce
 recursive_sum = lambda lst: reduce(lambda x, y: x + y, lst)

 print(recursive_sum(res))  # -> 34
 -----------------------------------------------------------------------------------------------------------------------

 # Выберите в каких случаях результат будет FALSE    # Выберите в каких случаях результат будет TRUE
 print(False and True)   # False                     print(False or True)    # True
 print(not False)        # True                      print(True or True)     # True
 print(False and False)  # False                     print(True and True)    # True
 print(False or False)   # False                     print(True or False)    # True
 print(False or True)    # True                      print(not True)         # False
 print(not True)         # False
 -----------------------------------------------------------------------------------------------------------------------

 # Вывести слово кит. Обратный цикл

 s = 'информатика'
 print(s[-2:-5:-1])  # -> кит
 print(s[-2:-5])     # -> ничего не выведет
 -----------------------------------------------------------------------------------------------------------------------

 # Интересно про метод  str.count        В Python метод count считает количество НЕПЕРЕСЕКАЮЩИХСЯ подстрок в строке.

 # В начале, В конце, между символами  - считается пустой строкой
 print('Hello World'.count(''))  # -> 12
 print('Hello'.count(''))        # -> 6
 -----------------------------------------------------------------------------------------------------------------------

 # Создание кортежа (Добавляем запятую)

 res = [1, 2, 3],
 print(res)  # -> ([1, 2, 3],)
 -----------------------------------------------------------------------------------------------------------------------

 # Интересный пример разные выводы из-за запятой      #  Интересное задание. Почему такой вывод?    <-----   <-----

 # ПЕРВЫЙ случай
 res = [1, 2, 7, 8, 9],                                              # Тут из-за запятой   res = ([1, 2, 7, 8, 9],)
 print([res[i]-res[i+1] for i in range(len(res)-1)])  # -> []

 # ВТОРОЙ случай
 res = [1, 2, 7, 8, 9]
 print([res[i]-res[i+1] for i in range(len(res)-1)])  # -> [-1, -5, -1, -1]


 # В ПЕРВОМ случае res - кортеж с одним элементом, а именно списком: ([1, 2, 7, 8, 9],). Когда вы обращаетесь к res[i],
 # вы получаете сам список, а не его элементы. Поэтому res[i+1] выходит за пределы, и результат пустой.

 # Во ВТОРОМ случае res — это просто список [1, 2, 7, 8, 9], и вы правильно обращаетесь к его элементам,
 # что дает ожидаемые разности.
 -----------------------------------------------------------------------------------------------------------------------

 # Хитрое создание кортежа  без ()           # Тоже самое создание кортежа с ()
 my_tuple = 12,3                             my_tuple = (12,3)
 my_tuple_2 = 12, 3, 4, 5, 1                 my_tuple_2 = (12, 3, 4, 5, 1)
 print(my_tuple)     # -> (12, 3)            print(my_tuple)     # -> (12, 3)
 print(my_tuple_2)   # -> (12, 3, 4, 5, 1)   print(my_tuple_2)   # -> (12, 3, 4, 5, 1)
 -----------------------------------------------------------------------------------------------------------------------

 # // ВСЕГДА округляет в меньшую сторону     # Тоже самое
 print((2+1)//2)  # -> 1                     print((2+1).__floordiv__(2))  # -> 1
 print((3+2)//2)  # -> 2                     print((3+2).__floordiv__(2))  # -> 2
 print((5+4)//2)  # -> 4                     print((5+4).__floordiv__(2))  # -> 4
 -----------------------------------------------------------------------------------------------------------------------

 # Интересный пример с рекурсией
 def countdown(i):
     print(i, end=' ')
     if i <= 1:
         return
     else:
         countdown(i-1)

 countdown(3)  # -> 3 2 1
 -----------------------------------------------------------------------------------------------------------------------

 # Можно добавлять также элементы как и в list

 from collections import deque

 a_deque = deque([1, 2])
 print(type(a_deque))  # -> <class 'collections.deque'>
 a_deque += [3, 4]
 a_deque.extend([5, 6])
 print(a_deque)        # -> deque([1, 2, 3, 4, 5, 6])
 -----------------------------------------------------------------------------------------------------------------------

 # Результат будет ОДИНАКОВЫЙ!

 a, b = 1, 2

 # Более длинная запись (стандартная конструкция)          # Условное выражение (conditional expression)
 if a > b:                                                 maxval = a if a > b else b
     maxval = a
 else:
     maxval = b

 print(maxval)  # -> 2                                     print(maxval)  # -> 2
 -----------------------------------------------------------------------------------------------------------------------

 # Интересный пример Особенной с format
 x = '37'

 print('The value of x is ' + str(x))   # -> The value of x is 37
 print('The value of x is ' + repr(x))  # -> The value of x is '37'

 x = 37
 # Сколько будет пробелов
 print('The value of x is ' + format(x, '4d'))       # ->  The value of x is   37
 print('The value of x is ' + format(x, '11d'))      # ->  The value of x is          37
 print('The value of x is ' + format(str(a), '4d'))  # -> ValueError: Unknown format code 'd' for object of type 'str'
 -----------------------------------------------------------------------------------------------------------------------

 # Несколько примеров range
 a = range(5)        # a = 0, 1, 2, 3, 4
 b = range(1, 8)     # b = 1, 2, 3, 4, 5, 6, 7
 c = range(0, 14, 3) # c = 0, 3, 6, 9, 12
 d = range(8, 1, -1) # d = 8, 7, 6, 5, 4, 3, 2
 -----------------------------------------------------------------------------------------------------------------------

 # Идентификатор, возвращаемый id(), не всегда является адресом в памяти, хотя в большинстве случаев это так.  <------
 class Stack:
     def __repr__(self):
         return f'<__main__.{type(self).__name__} object at 0x00000{id(self):x}>'  # x - hex представление

 # Будет совпадать по значению идентификатора, но в разных форматах (строка и шестнадцатеричное представление).  <-----
 print(Stack())          # -> <__main__.Stack object at 0x00000203f182fad0>
 print(hex(id(Stack()))) # ->                                0x203f182fad0

 class Stack: pass
 print(Stack())          # -> <__main__.Stack object at 0x00000203F182FAD0>
 -----------------------------------------------------------------------------------------------------------------------

 # Только одна переменная с префиксом *.  Несколько переменных с префиксом *                 <-----        <-----

 # При распаковке одного итерируемого объекта может использоваться только одна переменная с префиксом *.   <-----
 # Однако при распаковке различных итерируемых объектов можно использовать оператор распаковки * для каждого из них.
 items = [1, 2, 3, 4, 5]
 a, b, *extra = items     # a = 1, b = 2, extra = [3,4,5]
 *extra, a, b             # extra = [1,2,3], a = 4, b = 5
 a, *extra, b             # a = 1, extra = [2,3,4], b = 5


 # Но при распаковке более сложных структур данных, в которых задействованы разные итерируемые объекты,
 # можно использовать несколько переменных с префиксом *.                                                  <-----
 # Очень хороший пример!!!                                                     <-----        <-----        <-----

 items = [1, 2, 3]
 a = [10, *items, 11]     # a = [10, 1, 2, 3, 11]      (список)
 b = (*items, 10, *items) # b = (1, 2, 3, 10, 1, 2, 3) (кортеж)
 c = {10, 11, *items}     # c = {1, 2, 3, 10, 11}      (множество)
 -----------------------------------------------------------------------------------------------------------------------

 # Так тоже можно использовать slice  0 или None

 firstfive = slice(None, 5)                 firstfive = slice(0, 5)
 s = 'hello world'                          s = 'hello world'
 print(s[firstfive]) # Выводит 'hello'      print(s[firstfive]) # Выводит 'hello
 -----------------------------------------------------------------------------------------------------------------------

 # Здесь значения ключей представляют кортеж             # Тоже самое
 d = { }                                                 d = { }
 d[1,2,3] = "foo"                                        d[(1,2,3)] = "foo"
 d[1,0,3] = "bar"                                        d[(1,0,3)] = "bar"
 print(d)  # -> {(1, 2, 3): 'foo', (1, 0, 3): 'bar'}     print(d)  # -> {(1, 2, 3): 'foo', (1, 0, 3): 'bar'}
 -----------------------------------------------------------------------------------------------------------------------

 # Предотвращения двойного вычисления   <-----    <-----    <-----

 # ДВОЙНОЕ ВЫЧИСЛЕНИЕ
 def toint(x):
     try:
         return int(x)
     except ValueError:
         return None
 values = [ '1', '2', '-4', 'n/a', '-3', '5' ]
 data1 = [ toint(x) for x in values ]
 print(data1)  # -> [1, 2, -4, None, -3, 5]

 data2 = [ toint(x) for x in values if toint(x) is not None ]
 print(data2)  # -> [1, 2, -4, -3, 5]


 # Для предотвращения ДВОЙНОГО ВЫЧИСЛЕНИЯ toint(x) в последнем примереиспользуйте оператор :=
 data3 = [ v for x in values if (v:=toint(x)) is not None ]                                   <-----    <-----    <-----
 print(data3)  # -> [1, 2, -4, -3, 5]

 data4 = [ v for x in values if (v:=toint(x)) is not None and v >= 0 ]
 print(data4)  # -> [1, 2, 5]
 -----------------------------------------------------------------------------------------------------------------------

 # Интересные пример с распаковкой * и =

 s = [ (1, 2), (3, 4, 5), (6, 7, 8, 9) ]
 for x, y, *extra in s:
     print(f'{x=} {y=} {extra=}')

 # x=1 y=2 extra=[]
 # x=3 y=4 extra=[5]
 # x=6 y=7 extra=[8, 9]
 -----------------------------------------------------------------------------------------------------------------------

 # raise Exception([value])

 # Выдает исключение (несколько аргументов)
 raise RuntimeError(1, 2, 3, 'Unrecoverable Error')  # -> RuntimeError: (1, 2, 3, 'Unrecoverable Error')
 raise RuntimeError('Unrecoverable Error')           # -> RuntimeError: Unrecoverable Error
 -----------------------------------------------------------------------------------------------------------------------

 # Интересный пример

 line = 'ACME,100,490.10'
 column_types = [str, int, float]
 parts = line.split(',')
 row = [ty(val) for ty, val in zip(column_types, parts)]
 print(row)  # -> ['ACME', 100, 490.1]
 -----------------------------------------------------------------------------------------------------------------------

 # Показывает, что целые числа ничего не знают о числах с плавающей точкой.                             <-----
 a = 42  # int
 b = 3.7 # float
 print(a.__add__(b))   # -> NotImplemented

 # При этом числа с плавающей точкой знают о целых числах.                                              <-----
 print(b.__add__(a))   # -> 45.7
 print(b.__radd__(a))  # -> 45.7
 -----------------------------------------------------------------------------------------------------------------------

 # Сталкиваясь с выражением (например, x + y), интерпретатор вызывает комбинацию методов x.__add__(y) или y.__radd__(x)
 # для выполнения операции. Сначала он пытается применять x.__add__(y) во всех случаях, кроме ОСОБОГО,
 # когда y оказывается подтипом x, — тогда сначала выполняется y.__radd__(x).

 # Особый случай
 class Base:
     def __add__(self, other):
         return "Base __add__"

 class Derived(Base):
     def __radd__(self, other):
         return "Derived __radd__"

 x = Base()
 y = Derived()

 print(x + y)  # Вывод: "Base __add__"
 print(y + x)  # Вывод: "Derived __radd__"


 # В этом примере, когда мы складываем x (объект класса Base) и y (объект класса Derived), вызывается метод __add__
 # класса Base, так как x является объектом этого класса. Однако, когда мы складываем y и x, вызывается метод
 # __radd__ класса Derived, потому что y является подтипом Base, и Python сначала пытается вызвать y.__radd__(x).
 -----------------------------------------------------------------------------------------------------------------------

 # Кроме случаев, где b — подтип a. В этом конкретном случае выполняется b.__gt__(a).
 class Base:
     def __lt__(self, other):
         return "Base __lt__"

 class Derived(Base):
     def __gt__(self, other):
         return "Derived __gt__"

 a = Base()
 b = Derived()

 print(a < b)  # Вывод: "Base __lt__"
 print(b < a)  # Вывод: "Derived __gt__"

 # Упорядочение определяется операторами отношений (<, >, <= и >=) с использованием таких методов, как __lt__() и __gt__().
 # Как и в случае с другими математическими операторами, в правилах вычисления есть нюансы. Чтобы вычислить a < b,
 # интерпретатор сначала пытается выполнить a.__lt__(b) — кроме
 # случаев, где b — подтип a. В этом конкретном случае выполняется b.__gt__(a).    <-----
 -----------------------------------------------------------------------------------------------------------------------

 # Команда for x in s в Python фактически выполняется с использованием итератора.
 # Цикл for в Python действительно использует итераторы для перебора элементов

 # Этот код эквивалентен следующему  ->    # Тоже самое
 _iter = [1, 2, 3].__iter__()              for x in [1, 2, 3]:
 while True:                                   print(x, end=' ')
     try:
         x = _iter.__next__()
         print(x, end=' ')
     except StopIteration:
         break
 -----------------------------------------------------------------------------------------------------------------------

 # Изменение элементов на месте   # Изменить items      # Изменение элементов с помощью среза   # Изменить items
 def square(items):                                     def square(items):
     for i, x in enumerate(items):                          items[:] = [x * x for x in items] # Изменить items на месте
         items[i] = x * x # Изменить items на месте

 a = [1, 2, 3, 4, 5]                                    a = [1, 2, 3, 4, 5]
 square(a)                                              square(a)
 print(a)  # -> [1, 4, 9, 16, 25]                       print(a)  # -> [1, 2, 3, 4, 5]


 # НЕ Изменить items  Создание нового списка
 def square(items):
     items = [x * x for x in items]
     return items

 a = [1, 2, 3, 4, 5]
 square(a)
 print(a)  # -> [1, 2, 3, 4, 5]
 -----------------------------------------------------------------------------------------------------------------------

 # Разница в выводе связана с тем, как Python обрабатывает замыкания и ссылается на переменные в области видимости.

 # Пример 1

 # переменная name ссылается на одну и ту же область видимости, и в момент вызова функции она уже равна последнему
 # элементу списка — 'Margaret'.
 def make_greetings(names):
     funcs = []
     for name in names:
         funcs.append(lambda: print('Hello', name))
     return funcs

 a, b, c = make_greetings(['Guido', 'Ada', 'Margaret'])
 a() # -> Выводит 'Hello Margaret'
 b() # -> Выводит 'Hello Margaret'
 c() # -> Выводит 'Hello Margaret'


 # Пример 2

 # Подсвечиваем name но работает
 # при помощи name=name происходит создание нового значения для каждой лямбда-функции, что позволяет каждой функции
 # "запомнить" свое значение name на момент создания              # Тоже самое что и ПРИМЕР 2
 def make_greetings(names):                                       def make_greetings(names):
     funcs = []                                                       funcs = []
     for name in names:                                               for name in names:
         funcs.append(lambda name=name: print('Hello', name))             def greeting(name=name):
     return funcs                                                             print('Hello', name)
                                                                          funcs.append(greeting)
                                                                      return funcs
 a, b, c = make_greetings(['Guido', 'Ada', 'Margaret'])           a, b, c = make_greetings(['Guido', 'Ada', 'Margaret'])
 a() # -> Выводит 'Hello Guido'                                   a() # -> Выводит 'Hello Guido'
 b() # -> Выводит 'Hello Ada'                                     b() # -> Выводит 'Hello Ada'
 c() # -> Выводит 'Hello Margaret'                                c() # -> Выводит 'Hello Margaret'
 -----------------------------------------------------------------------------------------------------------------------

 # Использование partial
 from functools import partial

 def func(a, b, c, d):
     print(a, b, c, d)
 f = partial(func, 1, 2)         # Зафиксировать a=1, b=2
 f(3, 4)   # func(1, 2, 3, 4)
 f(10, 20) # func(1, 2, 10, 20)

 g = partial(func, 1, 2, d=4)    # Зафиксировать a=1, b=2, d=4
 g(3)      # func(1, 2, 3, 4)
 g(10)     # func(1, 2, 10, 4)
 -----------------------------------------------------------------------------------------------------------------------

 # Интересный пример с partial
 from functools import partial

 def func(x, y):
     print(x + y)

 a = 2
 b = 3
 f = lambda: func(a, b)
 g = partial(func, a, b)
 a = 10
 b = 20
 f() # Использует текущие значения a, b  вывод ->  30

 g() # Использует текущие значения a, b  вывод ->  5
 -----------------------------------------------------------------------------------------------------------------------

 # Каррированная версия интересная

 # Функция с тремя аргументами
 def f(x, y, z):
     return x + y + z

 # Каррированная версия
 def fc(x):
     return lambda y: (lambda z: x + y + z)

 # Пример использования
 a = f(2, 3, 4)   # Функция с тремя аргументами
 b = fc(2)(3)(4)  # Каррированная версия

 print(a)  # -> 9
 print(b)  # -> 9
 -----------------------------------------------------------------------------------------------------------------------

 # При возобновлении выполнение продолжается с команды, следующей за yield.        <-----    <-----

 def simple_generator():
     print("Начало генератора")
     yield 1
     print("Продолжение генератора")
     yield 2
     print("Конец генератора")

 gen = simple_generator()

 # Запускаем генератор
 print(next(gen))  # Вывод: "Начало генератора", затем 1
 print(next(gen))  # Вывод: "Продолжение генератора", затем 2
 -----------------------------------------------------------------------------------------------------------------------

 # ОПАСНОСТЬ НАСЛЕДОВАНИЯ ОТ ВСТРОЕННЫХ ТИПОВ
 # Проблема в том, что встроенные типы Python не реализуются как нормальные классы Python — они написаны на C.  <-----
 # Обычно субклассирования встроенных типов лучше избегать.                                                     <-----

 # принудительно использовать ключи в верхнем регистре, можно переопределить метод __setitem__() так:
 class udict(dict):
     def __setitem__(self, key, value):
         super().__setitem__(key.upper(), value)

 # И на первый взгляд такое решение работает
 u = udict()
 u['name'] = 'Guido'
 u['number'] = 37
 print(u)  # -> {'NAME': 'Guido', 'NUMBER': 37}


 # И теперь начинает казаться, что он вообще НЕ работает
 # Проблема в том, что встроенные типы Python не реализуются как нормальные классы Python — они написаны на C.  <-----
 u = udict(name='Guido', number=37)
 print(u)  # -> {'name': 'Guido', 'number': 37}

 u.update(color='blue')
 print(u)  # -> {'name': 'Guido', 'number': 37, 'color': 'blue'}



 # В модуле collections есть специальные классы UserDict, UserList и UserString.
 # Они могут использоваться для создания БЕЗОПАСНЫХ субклассов dict, list и str.

 from collections import UserDict
 class udict(UserDict):
     def __setitem__(self, key, value):
         super().__setitem__(key.upper(), value)

 # Всё работает как надо!!!
 u = udict()
 u['name'] = 'Guido'
 u['number'] = 37
 print(u)  # -> {'NAME': 'Guido', 'NUMBER': 37}

 u = udict(name='Guido', number=37)
 print(u)  # -> {'NAME': 'Guido', 'NUMBER': 37}

 u.update(color='blue')
 print(u)  # -> {'NAME': 'Guido', 'NUMBER': 37, 'COLOR': 'blue'}
 -----------------------------------------------------------------------------------------------------------------------

 # Учтите: преобразование имен не выполняется в таких функциях, как
 # getattr(), hasattr(), setattr() или delattr(), где имя атрибута задается
 # в виде строки. В таких функциях для обращения к атрибуту придется использовать преобразованное имя вида '_Класс__имя'.

 class MyClass:
     def __init__(self):
         self.__private_attr = "Я приватный атрибут"

     def get_private_attr(self):
         return self.__private_attr

 obj = MyClass()

 # Попытка доступа к приватному атрибуту напрямую вызовет ошибку
 # print(obj.__private_attr)  # AttributeError

 # Правильный способ доступа через метод
 print(obj.get_private_attr())  # Вывод: Я приватный атрибут

 # Использование getattr для доступа к приватному атрибуту
 print(getattr(obj, '_MyClass__private_attr'))  # Вывод: Я приватный атрибут
 -----------------------------------------------------------------------------------------------------------------------

 # ДИСПЕТЧЕРИЗАЦИЯ ВЫЗОВОВ В ЗАВИСИМОСТИ ОТ ТИПА


 # Такие большие блоки if-elif-else неэлегантны и ненадежны       # Элегантное решение с использованием словаря

 class Duck:                                                      class Duck:
     pass                                                             pass

 class Trombonist:                                                class Trombonist:
     pass                                                             pass

 class Cyclist:                                                   class Cyclist:
     pass                                                             pass

 def handle_duck(obj):                                            def handle_duck(obj):
     print("Handling a duck.")                                        print("Handling a duck.")

 def handle_trombonist(obj):                                      def handle_trombonist(obj):
     print("Handling a trombonist.")                                  print("Handling a trombonist.")

 def handle_cyclist(obj):                                         def handle_cyclist(obj):
     print("Handling a cyclist.")                                     print("Handling a cyclist.")

 def process(obj):                                                # Словарь диспетчеризации
     if isinstance(obj, Duck):                                    handlers = {
         handle_duck(obj)                                             Duck: handle_duck,
     elif isinstance(obj, Trombonist):                                Trombonist: handle_trombonist,
         handle_trombonist(obj)                                       Cyclist: handle_cyclist,
     elif isinstance(obj, Cyclist):                               }
         handle_cyclist(obj)
     else:                                                        def dispatch(obj):
         raise RuntimeError('Unknown object')                         func = handlers.get(type(obj))
                                                                      if func:
                                                                          return func(obj)
                                                                      else:
                                                                          raise RuntimeError(f'No handler for {obj}')

 # Пример вызова                                                  # Пример вызова
 process(Duck())        # Handling a duck.                        dispatch(Duck())        # Handling a duck.
 process(Trombonist())  # Handling a trombonist.                  dispatch(Trombonist())  # Handling a trombonist.
 process(Cyclist())     # Handling a cyclist.                     dispatch(Cyclist())     # Handling a cyclist.


 # Поддержка наследования                                  # Реализация через класс с использованием getattr
                                                           # реализует паттерн "Посетитель" (Visitor)

 def handle_duck(obj):                                     class Duck:
     print("Handling a duck.")                                 pass

 def handle_trombonist(obj):                               class Trombonist:
     print("Handling a trombonist.")                           pass

 def handle_cyclist(obj):                                  class Cyclist:
     print("Handling a cyclist.")                              pass

 class Animal:                                             class Dispatcher:
     pass                                                      def handle(self, obj):
                                                                   for ty in type(obj).__mro__:
 class Duck(Animal):                                                   meth = getattr(self, f'handle_{ty.__name__}', None)
     pass                                                              if meth:
                                                                           return meth(obj)
 class Trombonist(Animal):                                         raise RuntimeError(f'No handler for {obj}')
     pass
                                                               def handle_Duck(self, obj):
 class Cyclist(Animal):                                            print("Handling a duck.")
     pass
                                                               def handle_Trombonist(self, obj):
 handlers = {                                                      print("Handling a trombonist.")
     Duck: handle_duck,
     Trombonist: handle_trombonist,                            def handle_Cyclist(self, obj):
     Cyclist: handle_cyclist,                                      print("Handling a cyclist.")
 }

 def dispatch(obj):
     for ty in type(obj).__mro__:
         func = handlers.get(ty)
         if func:
             return func(obj)
     raise RuntimeError(f'No handler for {obj}')
                                                           # Создание экземпляра диспетчера
 # Пример вызова                                           dispatcher = Dispatcher()
 dispatch(Duck())        # Handling a duck.                dispatcher.handle(Duck())        # Handling a duck.
 dispatch(Trombonist())  # Handling a trombonist.          dispatcher.handle(Trombonist())  # Handling a trombonist.
 dispatch(Cyclist())     # Handling a cyclist.             dispatcher.handle(Cyclist())     # Handling a cyclist.
 -----------------------------------------------------------------------------------------------------------------------

 # Пример класса, автоматически создающего __repr__() по сигнатуре __init__()

 import inspect
 class Base:
     @classmethod
     def __init_subclass__(cls):
         # Создать метод __repr__
         args = list(inspect.signature(cls).parameters)
         argvals = ', '.join('{self.%s!r}' % arg for arg in args)
         code = 'def __repr__(self):\n'
         code += f' return f"{cls.__name__}({argvals})"\n'
         locs = { }
         exec(code, locs)
         cls.__repr__ = locs['__repr__']

 # Наследование от Base                         # Без наследования
 class Point(Base):                             class Point:
     def __init__(self, x, y):                      def __init__(self, x, y):
         self.x = x                                     self.x = x
         self.y = y                                     self.y = y

 # Пример использования                         # Пример использования
 p = Point(1, 2)                                p = Point(1, 2)
 print(p)  # -> Point(1, 2)                     print(p)  # -> <__main__.Point object at 0x000002BBE23EBF20>
 -----------------------------------------------------------------------------------------------------------------------

 # ДИНАМИЧЕСКОЕ СОЗДАНИЕ КЛАССА

 # Класс может быть создан и без команды class. Для этого используется конструкция types.new_class()

 import types

 def init(self, owner, balance):
     self.owner = owner
     self.balance = balance

 def deposit(self, amount):
     self.balance += amount

 def withdraw(self, amount):
     self.balance -= amount

 methods = {'__init__': init, 'deposit': deposit, 'withdraw': withdraw}
 Account = types.new_class('Account', (), exec_body=lambda ns: ns.update(methods))

 # Создание экземпляра класса
 a = Account('Guido', 1000.0)
 a.deposit(50)
 a.withdraw(25)

 print(a.balance)  # Выводит: 1025.0
 -----------------------------------------------------------------------------------------------------------------------

 # При определении нового класса командой class происходит ряд событий.
 # Следующий код показывает выполняемые низкоуровневые операции

 # Шаг 1: Создание пространства имен класса
 namespace = type.__prepare__('Account', ())

 # Шаг 2: Выполнение тела класса
 exec('''
 def __init__(self, owner, balance):
     self.owner = owner
     self.balance = balance
 def deposit(self, amount):
     self.balance += amount
 def withdraw(self, amount):
     self.balance -= amount
 ''', globals(), namespace)

 # Шаг 3: Создание итогового объекта класса
 Account = type('Account', (), namespace)

 p = Account(10, 100)
 print(p.balance)  # -> 100
 print(p.owner)    # -> 10
 -----------------------------------------------------------------------------------------------------------------------

 # Определение литерала bytes (обратите внимание на префикс b)
 a = b'hello'
 print(a)    # -> b'hello'
 # Обращение к значениям байтов
 print(a[0]) # -> выводит 104


 # Создание bytes по списку целых чисел
 b = bytes([0x68, 0x65, 0x6c, 0x6c, 0x6f])

 for x in b: # Выводит 104 101 108 108 111
     print(x, end=' ')


 # Создание и заполнение bytearray по частям
 c = bytearray()
 c.extend(b'world') # c = bytearray(b'world')
 c.append(0x21)     # c = bytearray(b'world!')
 print(c)           # -> 104 101 108 108 111 bytearray(b'world!')
 -----------------------------------------------------------------------------------------------------------------------

 # Создание файла логов

 # Поддерживаются пять уровней журнального вывода, упорядоченных по критичности.

 import logging
 log = logging.getLogger(__name__)
 # Функция, использующая logging
 def func(args):
     log.debug("A debugging message")
     log.info("An informational message")
     log.warning("A warning message")
     log.error("An error message")
     log.critical("A critical message")
 # Конфигурация вывода в журнал (выполняется один раз при запуске)
 if __name__ == '__main__':
     logging.basicConfig(
     level=logging.WARNING,
     filename="output.log"
 )
 -----------------------------------------------------------------------------------------------------------------------

 x = ([], )

 # Не атомарная операция
 x[0] += [1]  # -> TypeError: 'tuple' object does not support item assignment

 # Если обернуть в try результат будет такой!
 print(x)  # -> ([1],)
 -----------------------------------------------------------------------------------------------------------------------

 # Складывает ДВЕ последовательности!
 from operator import concat

 print(concat([1], [2]))  # -> [1, 2]
 print(concat(1, 2))      # -> TypeError: 'int' object can't be concatenated
 -----------------------------------------------------------------------------------------------------------------------

 # Библиотека statistics в Python предоставляет функции для выполнения различных статистических операций,
   таких как вычисление среднего, медианы, моды и стандартного отклонения.

 from statistics import mean, fmean

 res = [1, 2, 3]
 print(mean(map(float,res)))  # -> 2.0
 print(fmean(res))            # -> 2.0
 -----------------------------------------------------------------------------------------------------------------------

 # Проверяет, являются ли все числа больше 10.
 res = '15 20 25'

 print(all(map(int(10).__lt__, map(int, res.split()))))   # -> True                 # Интересные варинты!!!   <-----
 print(list(map(int(10).__lt__, map(int, res.split()))))  # -> [True, True, True]   # Интересные варинты!!!   <-----

 print(all(map(lambda z: int(z) > 10, res.split())))      # -> True

 # Тоже самое но уже без split и проверка __gt__
 res = [15, 20, 25]
 print(list(map(int(10).__gt__, res)))                    # -> [False, False, False]
 print([int(10).__gt__(i) for i in res])                  # -> [False, False, False]



 # То же самое, но уже без split
 res = [15, 20, 25]
 print(list(map(lambda x: x > 10, res)))                  # -> [True, True, True]
 print([i > 10 for i in res])                             # -> [True, True, True]
 -----------------------------------------------------------------------------------------------------------------------

 # IEEE — числа с плавающей точкой в Python используют стандарт IEEE 754, который определяет, как такие числа представляются в памяти.
 print(float.__getformat__('double'))  # -> IEEE, little-endian                  <-----                      <-----
 -----------------------------------------------------------------------------------------------------------------------

 #  Монада — это способ структурировать вычисления, чтобы сделать код более предсказуемым и удобным для работы.
 #  В Python монады не являются встроенной концепцией, но их можно реализовать с помощью классов и методов.

 # Монада
 class Maybe:
     def __init__(self, value):
         self.value = value

     def bind(self, func):
         if self.value is None:   # Если значение отсутствует
             return self
         return func(self.value)  # Применяем функцию к значению

 # Пример использования
 result = Maybe(10).bind(lambda x: Maybe(x + 5)).bind(lambda x: Maybe(x * 2))
 print(result.value)  # 30

 -----------------------------------------------------------------------------------------------------------------------

 def func():
     globals().update({'aaaaaaaaaa': 1})  # Добавляем переменную в глобальную область видимости
     print(aaaaaaaaaa)  # Работает  хотя подсвечиваем красным переменную

 func()  # -> 1
 -----------------------------------------------------------------------------------------------------------------------

 # Выражения через and быстрее  (потому что будет меньше байт-кода)  Разница в скорости минимальна
 # Тоже самое
 print(1 == 1.0 == True)          # -> True
 print(1 == 1.0 and 1.0 == True)  # -> True

 # Тоже самое
 print(5 > 4 > 3)                 # -> True
 print(5 > 4 and 4 > 3)           # -> True
 -----------------------------------------------------------------------------------------------------------------------

 # Почему вывод 4 если байтов 3?

 print(bytearray().__alloc__())         # -> 0
 # __alloc__() показывает выделенную память, а НЕ фактическое количество байтов в данных. Это связано с внутренней оптимизацией.
 print(bytearray(b'123').__alloc__())   # -> 4
 -----------------------------------------------------------------------------------------------------------------------

 # выводит её первую и последнюю букву.
 (s := 'Python') and print(s[0], s[-1])  # -> P n
 -----------------------------------------------------------------------------------------------------------------------

 # Изменение tuple через ctypes   # Прямое манипулирование памятью в Python # tuple хранит элементы в виде массива указателей
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

 # Вычисляем размер данных, которые нужно скопировать
 size = ctypes.sizeof(ctypes.c_void_p) * len(tup1)  # Размер одного элемента кортежа (указателя) * количество элементов

 # Изменяем длину кортежа tup1
 length_offset = ctypes.sizeof(ctypes.c_size_t) + ctypes.sizeof(ctypes.c_void_p)
 ctypes.cast(id(tup1) + length_offset, ctypes.POINTER(ctypes.c_ssize_t))[0] = len(tup2)

 # Копируем данные из tup2 в tup1
 ctypes.memmove(id(tup1) + offset, id(tup2) + offset, ctypes.sizeof(ctypes.c_void_p) * len(tup2))

 # Печатаем измененные значения
 print("After modification:")
 print(f"tup1: {tup1}, id: {id(tup1)}")  # -> tup1: (11, 111, 1111, 11111), id: 2723780112000
 print(f"tup2: {tup2}, id: {id(tup2)}")  # -> tup2: (11, 111, 1111, 11111), id: 2723780473536
 -----------------------------------------------------------------------------------------------------------------------

 # Изменение frozenset через ctypes   # Прямое манипулирование памятью в Python  # frozenset использует хэш-таблицу.

 import ctypes

 # Создаем два frozenset
 fs1 = frozenset([1, 2, 3])
 fs2 = frozenset([4, 5, 6, 7, 8])

 # Печатаем значения и id
 print("Before modification:")
 print(f"fs1: {fs1}, id: {id(fs1)}")  # -> fs1: frozenset({1, 2, 3}),       id: 2747102248544
 print(f"fs2: {fs2}, id: {id(fs2)}")  # -> fs2: frozenset({4, 5, 6, 7, 8}), id: 2747103297600

 # Вычисляем смещение до данных frozenset
 offset = (
         ctypes.sizeof(ctypes.c_size_t)  # Размер счетчика ссылок
         + ctypes.sizeof(ctypes.c_void_p)  # Размер указателя на тип объекта
         + ctypes.sizeof(ctypes.c_void_p)  # Размер указателя на длину frozenset
 )

 # Изменяем длину frozenset fs1
 length_offset = ctypes.sizeof(ctypes.c_size_t) + ctypes.sizeof(ctypes.c_void_p)
 ctypes.cast(id(fs1) + length_offset, ctypes.POINTER(ctypes.c_ssize_t))[0] = len(fs2)

 # Копируем данные из fs2 в fs1
 ctypes.memmove(id(fs1) + offset, id(fs2) + offset, ctypes.sizeof(ctypes.c_void_p) * len(fs2))

 # Печатаем измененные значения
 print("After modification:")
 print(f"fs1: {fs1}, id: {id(fs1)}")  # -> fs1: frozenset({4, 5, 6, 7, 8}), id: 2747102248544
 print(f"fs2: {fs2}, id: {id(fs2)}")  # -> fs2: frozenset({4, 5, 6, 7, 8}), id: 2747103297600
 -----------------------------------------------------------------------------------------------------------------------

 # Изменение str через ctypes

 import ctypes

 # Создаем строки   # Если str2 = "wwwwwwwwww"  то будет  str1 = "wwwww"   # Если  str2 = "world12345"    str1 = "world"
 str1 = "hello"
 str2 = "world"     # Если заменить на такую строку    str2 = "worldworld"   то str1 будет равно    str1 = "world"


 print("Before modification:")
 print(f"str1: {str1}, id: {id(str1)}")  # -> str1: hello, id: 3030659487312
 print(f"str2: {str2}, id: {id(str2)}")  # -> str2: world, id: 3030659487504

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

 # Изменяем str1 на "wello"                                              #   wello   <-----
 ctypes.memmove(id(str1) + offset, id(str2) + offset, size)

 print("After modification:")
 print(f"str1: {str1}, id: {id(str1)}")  # -> str1: wello, id: 3030659487312
 print(f"str2: {str2}, id: {id(str2)}")  # -> str2: world, id: 3030659487504
 -----------------------------------------------------------------------------------------------------------------------

 # Изменение указателя через ctypes
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
 -----------------------------------------------------------------------------------------------------------------------

 # В Python значение -1 зарезервировано для внутренних механизмов
 # Если hash -1 Значит что-то не так

 print(hash(-2))  # -> -2
 print(hash(-3))  # -> -3
 print(hash(-1))  # -> -2  (специальный случай)
 print(hash(0))   # -> 0
 -----------------------------------------------------------------------------------------------------------------------

 #  Удаляет указанные символы с начала и конца строки
 s = "ritritAlgorithmtirtir"
 print(s.strip("tir"))  # -> Algorithm

 s = "ritritAlgorithmtirtir"
 print(s.strip("irt"))  # -> Algorithm
 -----------------------------------------------------------------------------------------------------------------------

 # Вставить число n в начало и в конец каждого подсписка
 values = [
     [1, 2, 3],
     [4, 5],
     [6, 7, 8, 9]
 ]
 n = 0

 print([[n] + i + [n] for i in values])  # -> [[0, 1, 2, 3, 0], [0, 4, 5, 0], [0, 6, 7, 8, 9, 0]]
 -----------------------------------------------------------------------------------------------------------------------

 # Как можно использовать в for скобки ()   <-----          <-----
 players = [("Alice", 10), ("Bob", 15), ("Charlie", 20), ("Dave", 25)]


 for (i, ii), (j, jj) in itertools.pairwise(players):     # Тут посмотри как можно использовать скобки  ()  <-----
     print(i, ii, j, jj)

 # Alice 10 Bob 15
 # Bob 15 Charlie 20
 # Charlie 20 Dave 25
 -----------------------------------------------------------------------------------------------------------------------

 # Определение самого «дорогого» слова
 alphabet = {
     'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6,
     'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
     'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17,
     'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22,
     'w': 23, 'x': 24, 'y': 25, 'z': 26
 }

 res = 'abc bca cab'.split()

 print(max(enumerate(res), key=lambda x: (sum(map(alphabet.get, x[1])), x[0]))[1])  # -> cab
 print(max(res[::-1], key=lambda word: sum(map(alphabet.get, word))))               # -> cab
 -----------------------------------------------------------------------------------------------------------------------

 # Если оно больше 10, нужно вывести "Big". Если оно меньше 10, вывести "Small". Если равно 10, вывести "Equal".

 print(('Small', 'Big', 'Equal')[((n:=11) >= 10) + (n == 10)])  # -> Big            # <----  Важно индекс
 print(('Small', 'Big', 'Equal')[((n:=10) >= 10) + (n == 10)])  # -> Equal          # <----  Важно индекс
 print(('Small', 'Big', 'Equal')[((n:=9) >= 10) + (n == 10)])   # -> Small          # <----  Важно индекс
 -----------------------------------------------------------------------------------------------------------------------

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
 -----------------------------------------------------------------------------------------------------------------------

 Сколько в одном Гигабайте Байт?
 print(1024*1024*1024)  # -> 1073741824
 print(2**30)           # -> 1073741824
 -----------------------------------------------------------------------------------------------------------------------

 # Создает вложенные кортежи
 b = (42, 3.14), (2.718, 2.618),  # Интерпретатор Python игнорирует запятые в конце.   <-----
 print(b)  # -> ((42, 3.14), (2.718, 2.618))
 -----------------------------------------------------------------------------------------------------------------------

 # метод popleft() - это более с коростная версияр pор(0) в обычном списке. В остальном эти реализации действительно очень похожи.
 from collections import deque

 # Обычный список
 my_list = [1, 2, 3, 4]
 first_element = my_list.pop(0)      # Удаляет первый элемент, но медленно для больших списков
 print("List after pop(0):", my_list)       # -> [2, 3, 4]

 # Дек (двусторонняя очередь)
 my_deque = deque([1, 2, 3, 4])
 first_element = my_deque.popleft()  # Удаляет первый элемент очень быстро
 print("Deque after popleft():", my_deque)  # -> deque([2, 3, 4])
 -----------------------------------------------------------------------------------------------------------------------

 # Задача  палиндромом без создания дополнительных строк и с временной сложностью O(n) и пространственной сложностью O(1)
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
 print(is_palindrome("A man, a plan, a canal: Panama")) # True
 print(is_palindrome("race a car"))                     # False
 print(is_palindrome("No 'x' in Nixon"))                # True
 print(is_palindrome("Was it a car or a cat I saw?"))   # True
 print(is_palindrome("!@#$%^&*()"))                     # True, так как пустая строка между символами и игнорируемые символы
 print(is_palindrome("12321"))                          # True
 print(is_palindrome("123456"))                         # False
 -----------------------------------------------------------------------------------------------------------------------

 # Ошибки НЕ будет если бежать по пустому [], {}, (), ''

 for i in []:                         # for i in '':
     print(i) # Ничего не выводит     #     print(i) # Ничего не выводит
 -----------------------------------------------------------------------------------------------------------------------

 # Синтаксис позволяет без отступа писать  #  Потому что там вызов функции
 print([i.split()for i in 'abc'])  # -> [['a'], ['b'], ['c']]  # Тут без отступа
 print([i.split() for i in 'abc']) # -> [['a'], ['b'], ['c']]
 -----------------------------------------------------------------------------------------------------------------------

 # Поиск самой длинной подстроки без повторяющихся символов

 # Лучший - Вариант, обеспечивает оптимальную производительность O(n) и обрабатывает каждый символ ровно один раз.
 # Оптимизированный метод скользящего окна с хэш-мап для больших строк    (O(n))    O(min(m, n)) по памяти

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

 print(lengthOfLongestSubstring("bbbbb"))     # -> 1
 print(lengthOfLongestSubstring("abcabcbb"))  # -> 3
 print(lengthOfLongestSubstring("abcb"))      # -> 3
 print(lengthOfLongestSubstring("pwwkew"))    # -> 3
 print(lengthOfLongestSubstring("ckilbkd"))   # -> 5
 print(lengthOfLongestSubstring("dvdf"))      # -> 3
 -----------------------------------------------------------------------------------------------------------------------

 # Нахождение самой длинной палиндромной подстроки


 # Алгоритм Манакера (O(n) времени и O(n) памяти)  макс. производительность! самый быстрый известный алгоритм

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
 -----------------------------------------------------------------------------------------------------------------------

 # Даны строка-шаблон pattern и строка s. Нужно определить, соответствует ли строка s шаблону pattern.    Word Pattern

 # Время: O(n), где n — длина pattern (один проход по всем символам и словам).
 # Память: O(n), так как храним словари для всех уникальных символов и слов.
 def wordPattern(pattern: str, s: str) -> bool:
     words = s.split()  # Разбиваем строку на слова

     # Если длины не совпадают, соответствия быть не может
     if len(pattern) != len(words):
         return False

     # Создаём два словаря для двустороннего соответствия
     char_to_word = {}  # ключ: символ, значение: слово
     word_to_char = {}  # ключ: слово, значение: символ

     for char, word in zip(pattern, words):
         # Проверяем, что символ соответствует слову
         if char in char_to_word:
             if char_to_word[char] != word:
                 return False
         else:
             char_to_word[char] = word

         # Проверяем, что слово соответствует символу
         if word in word_to_char:
             if word_to_char[word] != char:
                 return False
         else:
             word_to_char[word] = char

     return True


 print(wordPattern("abba", "dog cat cat dog")) # -> True
 print(wordPattern("aaaa", "dog cat cat dog")) # -> False
 -----------------------------------------------------------------------------------------------------------------------

 # Даны две строки s и t. Нужно определить, являются ли они изоморфными.   Тоже самое     leetcode   Word Pattern

 def isIsomorphic(s: str, t: str) -> bool:
     if len(s) != len(t):
         return False

     s_to_t = {}  # Словарь для соответствия s → t
     t_to_s = {}  # Словарь для соответствия t → s

     for char_s, char_t in zip(s, t):
         # Проверяем соответствие s → t
         if char_s in s_to_t:
             if s_to_t[char_s] != char_t:
                 return False
         else:
             s_to_t[char_s] = char_t

         # Проверяем соответствие t → s
         if char_t in t_to_s:
             if t_to_s[char_t] != char_s:
                 return False
         else:
             t_to_s[char_t] = char_s

     return True


 print(isIsomorphic("egg", "add")) # -> True
 print(isIsomorphic("foo", "bar")) # -> False
 -----------------------------------------------------------------------------------------------------------------------

 # МОЖНО ПЕРЕДЕЛАТЬ В СТАНДАРТНЫЕ СТРУКТУРЫ ДАННЫХ PYTHON!  collections
 from collections import deque, Counter

 a_deque = deque([1, 2, 3])
 print(a_deque)         # -> deque([1, 2, 3])
 print(list(a_deque))   # -> [1, 2, 3]

 b_counter = Counter([1, 2, 3])
 print(b_counter)         # -> Counter({1: 1, 2: 1, 3: 1})
 print(dict(b_counter))   # -> {1: 1, 2: 1, 3: 1}
 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


 -----------------------------------------------------------------------------------------------------------------------


  --- Функциональное программирование на Python ---

 def repeat_phrase_n_times(phrase, n) -> str:
     print(f"{phrase}\n"*n)                       # Можно \n перенос так использовать

 repeat_phrase_n_times('Белье надевают под одежду', 2)
 # -> Белье надевают под одежду
 # -> Белье надевают под одежду

 -----------------------------------------------------------------------------------------------------------------------

 # Проверка на ВИСОКОСНОСТЬ

 # Разные варианты
 from calendar import isleap         def is_leap(year):
 def is_leap(year):                     return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
     return isleap(year)

 print(is_leap(1900))  # -> False

 # Или lambda
 is_leap = lambda x: __import__('calendar').isleap(x)


 # Список ВИСОКОСНЫХ лет
 get_leap_years = lambda x, y: [i for i in range(x, y) if __import__('calendar').isleap(i)]

 print(get_leap_years(2000, 2018))  # -> [2000, 2004, 2008, 2012, 2016]


 -----------------------------------------------------------------------------------------------------------------------

 from functools import reduce
 import operator

 # принимает список чисел и находит их произведение и start - начальное значение произведения
 def my_product(lst, start=1):                 def my_product(nums: list[int], start: int = 1) -> int:
     return reduce(operator.mul, lst, start)      return __import__('functools').reduce(lambda x, y: x * y, nums, start)

 print(my_product([1, 2, 3]))      # -> 6
 print(my_product([1, 2, 3], 10))  # -> 60


 -----------------------------------------------------------------------------------------------------------------------

 # Если include_quantities = True, вы вывeсти {количество}x{имя_товара}   иначе выводите только имя.
 shopping_list = {'Bread': 13, 'Potato': 5}

 Только регуляркой!!!
 # Вариант с  match case                                    # Вариант с  if
 def sub_fun(m):                                            def sub_fun(m):
     match m[0]:                                                if m[0] in ["'", '[', ']', ' ', '"']:
         case x if x in ["'", '[', ']', ' ', '"']:                  return ''
             return ''                                          if m[0] == ':':
         case ':':                                                  return 'x'
             return 'x'                                         if m[0] == ',':
         case ',':                                                  return '\n'
             return '\n'

 def show_list(include_quantities=True):
     shop = re.findall(r'(?i)\'\w+\': \d+', str(shopping_list))
     shop_sub = re.sub(r'[\'\]\[ :,"]', sub_fun, str(shop))
     if include_quantities:
         print(re.sub(r'(\w+)(x)(\d+)', r'\3\2\1', shop_sub))
     else:
         print(re.sub(r'[\dx]', r'', shop_sub))


 # А вот решения без регулярки!!!
 def show_list(include_quantities=True):           def show_list(include_quantities: bool =True) -> None:
    for key, value in shopping_list.items():           for i, quantity in shopping_list.items():
        if include_quantities:                             print(f'{quantity}x' * int(include_quantities) + i)
            print(f"{value}x{key}")
        else:
            print(f"{key}")

 show_list(include_quantities=False)
 # -> Bread
 # -> Potato
 show_list()
 # -> 13xBread
 # -> 5xPotato


 -----------------------------------------------------------------------------------------------------------------------

 # Что увидим на экране после выполнения следующего кода?

 def do_it_something(lst):
     lst[0] = "Гавайская"
     lst[1] = "пицца"
     return lst

 values = ['Ребрышки', 'гриль', 'это', 'очень', 'вкусно']
 new_values = do_it_something(values)

 print(values)      # -> ['Гавайская', 'пицца', 'это', 'очень', 'вкусно']
 print(new_values)  # -> ['Гавайская', 'пицца', 'это', 'очень', 'вкусно']


 -----------------------------------------------------------------------------------------------------------------------

 # Простая функция но как написать с lambda?            # А ВОТ ТАК!
 def truncate_sentences(a, *args):                      truncate_sentences = lambda a, *x: [print(i[:a]) for i in x]
     for i in args:
         print(i[:a], end='  ')    # -> ABC  DEF  GHI
 truncate_sentences(3, "ABC","DEF","GHI")


 -----------------------------------------------------------------------------------------------------------------------

 # Обменный пункт.  делим одно на другое и умножаем на количество
 # у тебя есть 100 долларов, тебе нужно поменять эту сумму на евро Сколько ты получишь евро если курс 0.861775 за 1 дол
 exchange_rates = {
     "USD": 1.0,
     "EUR": 0.861775,
 }
 def convert(value, value_2, n):
     return round((exchange_rates[value_2]/exchange_rates[value]) * n, 2)

 currency = convert("USD", "EUR", 100)
 print(currency)  # -> 86.18

 convert = lambda c1, c2, n: round(float.__truediv__(*map(exchange_rates.get, (c2, c1))) * n, 2)
 currency = convert("EUR", "USD", 100)
 print(currency)  # -> 116.04


 -----------------------------------------------------------------------------------------------------------------------

 --- sys.stdin,  open(0) ---

 0 - это дискриптора стандартного потока ввода, соответственно open(0) открывает поток ввода. Более универсальный
 надежный подход к считыванию всех данных одной строкой - через модуль sys
 -- Другими словами, с помощью функции open мы считываем все данные и потом работаем с ними (построчно). --

 Поток ввода (sys.stdin) — это специальный объект в программе, куда попадает весь текст, который ввёл пользователь.
 Потоком его называют потому, что данные хранятся в нем до тех пор, пока программа их не прочитала.

 Поток ввода (sys.stdin) — является итератором, который невозможно перезапустить. Как и любой итератор,
 он может двигаться только вперёд. Как только данные прочитаны, они удаляются из потока ввода безвозвратно.

 # Примеры Посмотри как написан код и else:    <-----


 import re                                     import re, sys

 for i, line in enumerate(open(0), 1):         for i, line in enumerate(sys.stdin, 1):
     if res := re.search(r'[Кк]од', line):         if s := re.search('[Кк]од', line):
         print(i, res.start())                         print(i, s.start())
         break                                         break
 else:                                         else:
     print('код не найден')                        print('код не найден')

 # Тоже самое но установили сколько будет введего строк

 lst = ['Как мне такое? Не знаю', 'Paypal это круто', 'Код запуска: ИлонМаксим2007', 'A']   # Пример что было введено

                                                # Варинт с использованием lst и ответ в конце
 import re                                      import re

 for i in range(4):                             for i, v in enumerate(lst):
     s = input()                                    result = re.search("[кК]од", v)
     result = re.search("[кК]од", s)                if result:
     if result:                                         print(i + 1, result.span()[0])
         print(i + 1, result.span()[0])                 break
         break
 else:                                          else:
     print('код не найден')                         print('код не найден')
                                                # -> 3 0

 sys.stdin вроде в Пичарме не получится использовать, т.к. он не умеет прерывать поток ввода.   <-----

 Обычно я просто копирую в отдельную переменную то, что необходимо и потом с этим работаю (каким угодно способом),
 либо копирую ввод в файл и работаю с файлом через менеджер контекста, в принципе, одно и тоже получается.   <-----
 -----------------------------------------------------------------------------------------------------------------------


 --- Comprehensions: list, dict, set ---
 Работают быстрее цикла for или    цикпа while!                                                 <-----

 Существует 4 генератора (не функций):
 1. list comprehension   - генератор списков   [выражение for переменная in последовательность if условие]          []
 2. set comprehension    - генератор множеств  {выражение for переменная in последовательность if условие}          {}
 3. dict comprehension   - генератор словарей  {ключ: значение for ключ, значение in последовательность if условие} {k:v}
 4. generator expression - выражение-генератор (выражение for переменная in последовательность if условие)          ()

 -- List Comprehensions         Listcomps --

 # Сравнение с обычным for

 # Квадраты чисел ** 2                                        # list comp   Работает быстрее                 <-----
 squares = []                                                 squares = [i**2 for i in range(10)]
 for i in range(10):
     squares.append(i**2)
 print(squares)  # -> [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]    print(squares)  # -> [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

 # Тоже сомое но с lambda
 squares = list(map(lambda x: x**2, range(10)))
 print(squares)  # -> [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

 # Внутри может быть любой iterable
 print([i*5 for i in 'hello'])     # -> ['hhhhh', 'eeeee', 'lllll', 'lllll', 'ooooo']
 print([ord(i) for i in 'hello'])  # -> [104, 101, 108, 108, 111]

 # 10 случайных чисел
 import random
 print([random.randrange(1, 10) for i in range(10)])  # -> [6, 3, 8, 2, 9, 4, 8, 5, 5, 7]
 print([random.randint(1, 10) for i in range(10)])    # -> [7, 3, 3, 5, 7, 3, 7, 10, 3, 1]

 -----------------------------------------------------------------------------------------------------------------------

 Условие внутри:

 a_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]   # list(range(10)) Тоже самое
 # Числа больше 5
 print([i for i in range(10) if i > 5])                         # -> [6, 7, 8, 9]
 # Числа больше 5  не 6, 9
 print([i for i in range(10) if i > 5 and i != 6 and i != 9])   # -> [7, 8]

 # Объединяет элементы двух списков, если они не равны
 combs = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
 print(lst)  # -> [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

 # Тоже самое но с циклом for
 combs = []
 for x in [1,2,3]:
     for y in [3,1,4]:
         if x != y:
             combs.append((x, y))
 print(lst)  # -> [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]


 # if else  Прописывается вначале!!                                                                             <-----
 print([i if i > 7 else 'A' for i in range(10)])  # -> ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 8, 9]
 # Условия работают как в тернарном операторе
 value = 123
 print('even' if value % 2 == 0 else 'odd')                  # -> odd
 print(['even' if i % 2 == 0 else 'odd' for i in range(3)])  # -> ['even', 'odd', 'even']

 -----------------------------------------------------------------------------------------------------------------------

 vec = [-4, -2, 0, 2, 4]

 # Умножить каждый элемент на 2
 print([x * 2 for x in vec])   # -> [-8, -4, 0, 4, 8]
 # Применить функцию к каждому элементу
 print([abs(x) for x in vec])  # -> [4, 2, 0, 2, 4]

 freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
 # Применить метод к каждому элементу
 print([weapon.strip() for weapon in freshfruit])  # -> ['banana', 'loganberry', 'passion fruit']

 # Создать список из двух кортежей типа (число, квадрат)
 print([(x, x**2) for x in range(6)])  # -> [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

 # Похожий пример
 print([(i, j) for i in 'ab' for j in [1, 2]])  # -> [('a', 1), ('a', 2), ('b', 1), ('b', 2)]

 # Понимания списков могут содержать сложные выражения и вложенные функции:
 print([str(round(i*0.344, i)) for i in range(1, 6)])  # ->['0.3', '0.69', '1.032', '1.376', '1.72']

 -----------------------------------------------------------------------------------------------------------------------

 -- Nested List Comprehensions     Понимание вложенных списков --

 matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
 ]
 # Сравни их
 print([i for row in matrix for i in row])     # -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
 print([[i for i in row] for row in matrix])   # -> [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
 -----------------------------------------------------------------------------------------------------------------------

 matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
 ]

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

 -----------------------------------------------------------------------------------------------------------------------
 Примеры интересные!

 # Обход Списка кортежей
 a = [
     ("Sidorov", 1995),
     ("Lukov", 2002),
     ]

 print([i for i in a])                       # -> [('Sidorov', 1995), ('Lukov', 2002)]
 print([i[0] for i in a])                    # -> ['Sidorov', 'Lukov']
 print([i[0] for i in a if i[1] > 1995])     # -> ['Lukov']
 print([i[0][2] for i in a if i[1] > 1995])  # -> ['k']

 # Обход Словаря
 a = {
     'Sidor': {'age': 1995, 'hob': 'soc', 'car': 'BMW'},
     'Lukov': {'age': 2002, 'hob': 'bas', 'car': 'Opel'},
 }
 print([i for i in a])     # -> ['Sidor', 'Lukov']  # Ключи Словаря
 print([a[i] for i in a])  # -> [{'age': 1995, 'hob': 'soc', 'car': 'BMW'}, {'age': 2002, 'hob': 'bas', 'car': 'Opel'}]
 print([a[i]['car'] for i in a])                             # -> ['BMW', 'Opel']     # Определенный ключ
 print([a[i]['hob'] for i in a])                             # -> ['soc', 'bas']      # Определенный ключ
 print([a[i]['car'] for i in a if a[i]['age'] > 1995])       # -> ['Opel']            # Определенный ключ по условию
 print([(i, a[i]['car']) for i in a])                        # -> [('Sidor', 'BMW'), ('Lukov', 'Opel')] #  Все
 print([(i, a[i]['car']) for i in a if a[i]['age'] > 1995])  # -> [('Lukov', 'Opel')] # Ключ значение в кортеже Условие

 -----------------------------------------------------------------------------------------------------------------------


 -- Set Comprehensions         Set comps --

 squares = {i ** 2 for i in range(10)}
 cubes = {i ** 3 for i in range(10, 21)}
 chars = {c for c in 'abcdefg'}
 print(squares)  # -> {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}
 print(cubes)    # -> {1728, 4096, 8000, 1000, 5832, 6859, 3375, 4913, 1331, 2197, 2744}
 print(chars)    # -> {'d', 'e', 'a', 'g', 'c', 'f', 'b'}

 Сравнение с циклом for

 d = [1, 2, 3, '1', '2', -4, 3, 5]       d = [1, 2, 3, '1', '2', -4, 3, 5]

 # Цикл for                              # set comp   Работает быстрее                                  <-----
 set_d = set()                           a_set = {int(i) for i in d}
 for i in d:
     set_d.add(int(i))
 print(set_d)  # -> {1, 2, 3, 5, -4}     print(a_set)  # -> {1, 2, 3, 5, -4}

 -----------------------------------------------------------------------------------------------------------------------


 -- Dict Comprehensions         Dict comps --

 Сравнение с циклом for

 # Цикл for                                        # dict comp   Работает быстрее                       <-----
 squares = {}                                      squares = {i: i**2 for i in range(5) if i % 2 == 0}
 for i in range(5):
     if i % 2 == 0:
         squares[i] = i**2
 print(squares)  # -> {0: 0, 2: 4, 4: 16}         print(squares)  # -> {0: 0, 2: 4, 4: 16}

 # Генераторы вложенных словарей
 squares = {i: {j: j**2 for j in range(i + 1)} for i in range(3)}
 print(squares)  # -> {0: {0: 0}, 1: {0: 0, 1: 1}, 2: {0: 0, 1: 1, 2: 4}}
 -----------------------------------------------------------------------------------------------------------------------

 Примеры интересные!

 Пример 1
 a = {word:len(word) for word in ['hi', 'hello', 'www']}
 print(a)  # -> {'hi': 2, 'hello': 5, 'www': 3}

 Пример 2
 data = {
     'A_a': '2',
     'b_b': '1',
 }
 new_data = {key.title(): int(value) for key, value in data.items()}
 print(new_data)  # -> {'A_A': 2, 'B_B': 1}

 Пример 3
 from pprint import pprint
 users = [
     [0, 'Bob', 'password'],
     [1, 'code', 'python'],
     [51, 'qwerty', '1234']
 ]
 new_users = {user[0]: user for user in users}
 pprint(new_users)
 print('*'*15)
 pprint(new_users[1])
 pprint(new_users[51])

 # Красивый Вывод pprint
 # {0: [0, 'Bob', 'password'],
 #  1: [1, 'code', 'python'],
 #  51: [51, 'qwerty', '1234']}
 # ***************
 # [1, 'code', 'python']
 # [51, 'qwerty', '1234']

 -----------------------------------------------------------------------------------------------------------------------


 -- Generator expressions         Gen exp --
 Чистый Итератор

 a_gen = (i for i in range(2))
 print(a_gen)             # -> <generator object <genexpr> at 0x0000022CF49B9A40>
 print(next(a_gen))       # -> 0
 print(a_gen.__next__())  # -> 2
 print(a_gen.__next__())  # -> StopIteration

 # Получили ссылку на генератор
 a_gen = [(i for i in range(10))]
 print(a_gen)     # -> [<generator object <genexpr> at 0x00000241E6CF9A40>]
 print(a_gen[0])  # -> <generator object <genexpr> at 0x0000027C7C1E9A40>

 # Интересныe примеры
 a = [1, 2, 3]
 # print(next(a))     # -> TypeError: 'list' object is not an iterator

 d = iter(a)
 print(next(d))       # ->  1
 print(next(d))       # ->  2
 print(d.__next__())  # ->  3
 print(d.__next__())  # ->  StopIteration

 # Одноразовый
 a_gen = (i for i in range(5))
 print(list(a_gen))  # -> [0, 1, 2, 3, 4]
 print(list(a_gen))  # -> []

 -----------------------------------------------------------------------------------------------------------------------

 --- lambda ---

 # Вторичный критерий сортировки указываем в кортеже
 people = [{"name": "B", "country": "AA", "age": 50}, {"name": "A", "country": "AA", "age": 50}]
 sorted(people, key=lambda x: x['age'])
 sorted(people, key=lambda x: (x['age'], x['name']))  # Вторичный критерий сортировки указываем в кортеже     <-----

 # Или просто пишем x без ничего
 people = ["CA", "BA", "DA", "AA", "FD"]
 sorted(people, key=lambda x: (len(x), x))  # ['AA', 'BA', 'CA', 'DA', 'FD']
 sorted(people, key=len)                    # ['CA', 'BA', 'DA', 'AA', 'FD']

 Сортировать одновременно и по значениям, и по ключам, а не сначала по-одному, потом по-другому. Унарный минус <-----
 # Унарный минус работает только с числами!!!  Минус  -   Работает как  reverse=True  Но к элементу            <-----
 a = [('ФФФ', 5), ('Укк', 4), ('Бил', 4)]
 print(sorted(a))                               # -> [('Бил', 4), ('Укк', 4), ('ФФФ', 5)]
 print(sorted(a, key=lambda x: (-x[1], x[0])))  # -> [('ФФФ', 5), ('Бил', 4), ('Укк', 4)]   <----- Унарный минус - Числа



 ---  В отличие от обычной функции, лямбда-функция — это одно выражение. ---

 # НЕЛЬЗЯ использовать  return и pass
 Bad = lambda x: pass       # -> SyntaxError: invalid syntax
 Bad = lambda x: return x   # -> SyntaxError: invalid syntax

 # НЕЛЬЗЯ реализовать аналоги функций, содержащих ЦИКЛЫ.  while/for

 # Условия if else через Тернарный оператор   get_sign = lambda x: 'positive' if x>0 else 'negative or 0'

 # МОЖНО использовать анонимную функцию без параметров
 h = lambda: 'hello'
 print(h())

 # Тоже самое              # Тоже самое
 def surprise():           surprise = lambda: print('surprise')
     print('surprise')     print(surprise())
     return None


 # Хорошее решение                                                                                  <-----       <-----
 # хозяйке на заметку - str.startswith и str.endswith вполне умеют принимать кортежи и проверять каждую букву отдельно
 check_word = lambda x: x.upper().startswith(('Q', 'R')) and x.upper().endswith(tuple('AEIUO'))
 print(check_word.__name__)  # -> <lambda>
 print(check_word('radio'))  # -> True

 check_word = lambda x: x[0].upper() in 'QR' and x[-1].upper() in 'AEIUO'
 print(check_word.__name__)  # -> <lambda>
 print(check_word('radio'))  # -> True

 # Тоже самое
 check_word = lambda x: bool(__import__('re').match(r'(?i)[QR].*[AEIUO]$', x))


 # Интересные решения Тоже самое
 sale_lambda = lambda x: x * 0.9 if x > 50 else x
 sale_lambda = lambda x: (x, x * 0.9)[x > 50]
 print(sale_lambda.__name__)  # -> <lambda>
 print(sale_lambda(50.0))     # -> 50.0


 # Среднее арифметическое. Avg
 average = lambda *args: sum(args) / len(args)
 print(average.__name__)  # -> <lambda>
 print(average(4, 5, 6))  # -> 5.0


 -----------------------------------------------------------------------------------------------------------------------

 --- Вложенные функции ---
 Внутренняя функция (Inner function), также известная как вложенная (nested function), — это функция,
 которая определена внутри другой функций.

 # Увеличивает значение на 1
 def wrap_increment(value):
     def _inc(value):
         return value + 1
     return _inc(value)

 print(wrap_increment(41))  # -> 42


 # Интересный
 def get_extensions(file_list):
     _get_extension = lambda x: x.split(".")[-1] if "." in x else  ""
     return [_get_extension(i) for i in file_list]

 print(get_extensions(["foo.txt", "bar.mp4", "python3"]))  # -> ['txt', 'mp4', '']

 # Тоже самое
 def get_extensions(file_list: list[str]) -> list[str]:
     def _get_extension(filename: str) -> str:
         return ('', filename[filename.rfind('.') + 1:])['.' in filename]
     return [_get_extension(filename) for filename in file_list]

 print(get_extensions(["foo.txt", "bar.mp4", "python3"]))  # -> ['txt', 'mp4', '']

  # Тоже самое
 from pathlib import Path

 def get_extensions(file_list):
     def _get_ext(f_name):
         return Path(f_name).suffix.lstrip('.')
     return [*map(_get_ext, file_list)]

 print(get_extensions(["foo.txt", "bar.mp4", "python3"]))  # -> ['txt', 'mp4', '']



 # Внимательно посмотри как работают
 # double, увеличивающая число в два раза   is_odd, проверяющая на нечетность
 def double_odd_numbers(numbers):
     def double(num):
         return num * 2

     def is_odd(num):
         if num % 2:
             return num
     return [double(num) for num in numbers if is_odd(num)]

 print(double_odd_numbers([1, 2, 3, 4, 5]))  # -> [2, 6, 10]

 # Тоже самое!
 def double_odd_numbers(numbers):
     double = lambda x: x * 2
     is_odd = lambda x: x % 2 != 0
     return [double(num) for num in numbers if is_odd(num)]

 # Тоже самое!                                                                                      <-----       <-----
 def double_odd_numbers(numbers, double=lambda x: x * 2, is_odd=lambda x: x % 2):
     return [double(num) for num in numbers if is_odd(num)]


 -----------------------------------------------------------------------------------------------------------------------

 --- Функция высшего порядка (аббревиатура ФВП) ---

 # Функция-применитель  Посмотри ВСЕ Варианты
 def apply(func, lst):
     return [func(i) for i in lst]

 def square(num):
     return num ** 2

 print(apply(square, [5, 7, 0, 3]))  # -> [25, 49, 0, 9]


 # Тоже самое
 def apply(func, x): return list(map(func, x))

 # Тоже самое
 apply = lambda *args: [*map(*args)]


 # Применить каждую функцию к Каждому значению
 def compute(funcs, *args):
     return [func(arg) for func in funcs for arg in args]

 def square(num):
     return num ** 2

 def inc(num):
     return num + 1

 print(compute([square, inc], 10))  # -> [100, 11]

 # Тоже самое
 compute = lambda f, *args: [el(j) for el in f for j in args]


 # Применить каждую функцию к Одному значению   # Очень хороший пример Разбери как работает
 def compute(funcs, *args):
     res = []
     for arg in args:
         for func in funcs:
             arg = func(arg)
         res.append(arg)
     return res

 def square(num):
     return num ** 2

 def inc(num):
     return num + 1

 print(compute([square, inc], 10))  # -> [101]


 # Интересно как работает Тоже самое ----->                 Тоже самое  Разбери попробуй!
 def filter_collection(f, lst):                             def filter_collection(f, seq):
    match lst:                                                  data = filter(f, seq)
        case str():                                             if isinstance(seq, str):
            return ''.join([i for i in lst if f(i)])                return ''.join(data)
        case list():                                            return type(seq)(data)
            return [i for i in lst if f(i)]
        case _:
             return tuple([i for i in lst if f(i)])

 print(filter_collection(lambda x: x not in 'aeiou', 'I never heard those lyrics before'))  # -> I nvr hrd ths lyrcs bfr


 -----------------------------------------------------------------------------------------------------------------------

 --- Замыкания (Closure) ---

 # Замыкание для умножения Посмотри  как можно вызывать Замыкание в print
 def multiply(a):
     def inner(x):
         return a*x
     return inner

 print(multiply(4)(3))    # -> 12
 print(multiply(400)(5))  # -> 2000

 f_2 = multiply(4)
 print(f_2(3))            # -> 12
 f_3 = multiply(400)
 print(f_3(5))            # -> 2000


 # Присвоение значений Нужно использовать nonlocal Иначе будет ошибка
 # UnboundLocalError: cannot access local variable 'total' where it is not associated with a value
 def create_accumulator():
     total = 0
     def inner(n):
         nonlocal total
         total += n
         return total
     return inner

 summator_1 = create_accumulator()
 print(summator_1(5))  # -> 5

 summator_2 = create_accumulator()
 print(summator_2(3))  # -> 3


 # функцию-замыкание count_calls, которая подсчитывает сколько раз она была вызвана.
 # Особенность этого замыкания заключается в том, что количество вызовов должно хранится в атрибуте total_calls.

 def count_calls():
     def inner():
         inner.total_calls += 1
     inner.total_calls = 0
     return inner

 counter = count_calls()
 counter()
 counter()
 print(counter.total_calls)  # -> 2
 counter()
 print(counter.total_calls)  # -> 3



 # Только функцию-замыкание count_calls, которая подсчитывает сколько раз она была вызвана.
 def count_calls():
     count = 0
     def inner():
         nonlocal count
         count += 1
         return count
     return inner

 counter = count_calls()

 print(counter())  # -> 1
 print(counter())  # -> 2
 -----------------------------------------------------------------------------------------------------------------------

 --- Декораторы ---   return None - Закрывает декоратор

 # return None    # Закрывает декоратор    Посмотри внамательно пример особенно как можно использовать ;
 def validate_all_args_str(func):
     def wrapper(*args, **kwargs):
         if all(type(el) == str for el in args): return func(*args, **kwargs)
         else: print('Все аргументы должны быть строками'); return None         # Закрывает декоратор
     return wrapper

 @validate_all_args_str
 def concatenate(**kwargs):
     result = ""
     for arg in kwargs.values():
         result += str(arg)
     return result
 print(concatenate(a="Я", b="Выучу", c="Этот", d="Питон", e="!"))  # -> ЯВыучуЭтотПитон!


 # В dict comprehension прописывать условие k: v Посмотри
 def uppercase_elements(func):
     def wrapper(*args, **kwargs):
         res = func(*args, **kwargs)
         if isinstance(res, list):
             return [i.upper() if isinstance(i, str) else i for i in res]
         return {k.upper() if isinstance(k, str) else k: v for k, v in res.items()}   # Тут условие
     return wrapper

 @uppercase_elements
 def my_func(**kwargs):
     return {1: 'one', 2: 'store', 'three': 3, 'four': 4} | kwargs

 print(my_func(**{'Five': 5, 'sIx': 6}))  # -> {1: 'one', 2: 'store', 'THREE': 3, 'FOUR': 4, 'FIVE': 5, 'SIX': 6}



 # Классные решения!!!
 # Фильтрация аргументов  Ваша задача создать два декоратора

 from functools import wraps
 from typing import Collection

 def filter_even(func):
     @wraps(func)
     def inner(*args, **kwargs):
         check = lambda x: (isinstance(x, Collection) and not len(x) % 2) or (isinstance(x, int) and not x % 2)
         return func(*filter(check, args), **kwargs)

     return inner


 def delete_short(func):
     @wraps(func)
     def inner(*args, **kwargs):
         return func(*args, **{k: kwargs[k] for k in filter(lambda x: len(x) > 4, kwargs)})

     return inner


 @filter_even
 @delete_short
 def concatenate(*args, **kwargs):
     result = ""
     for arg in args + tuple(kwargs.values()):
         result += str(arg)
     return result

 print(concatenate("Я", "хочу", "Выучить", "Питон", a="За", qwerty=10, c="Месяцев"))  # -> хочу10


 # Тоже самое
 def filter_even(func):
     def wrapper(*args, **kwargs):
         return func(*[el for el in args if el == False or
                       (isinstance(el, (str, list, tuple, dict)) and len(el) % 2 == 0) or
                       (isinstance(el, int) and int(el) % 2 == 0)], **kwargs)
     return wrapper

 def delete_short(func):
     def wrapper(*args, **kwargs):
         return func(*args, **{k:v for k, v in kwargs.items() if len(str(k)) > 4})
     return wrapper

 @filter_even
 def concatenate(*args):
     result = ""
     for arg in args:
         result += arg
     return result

 print(concatenate("Ну", "Когда", "Уже", "Я", "Выучу", "Питон?"))  # -> НуПитон?


 # проверяет количество переданных аргументов. 
 from functools import update_wrapper

 class check_count_args:
     def __init__(self, func):
         update_wrapper(self, func)
         self.func = func

     def __call__(self, *args, **kwargs):
         match sum(map(len, (args, kwargs))):
             case 1 | 0:
                 return print('Not enough arguments')
             case 2:
                 return self.func(*args, **kwargs)
             case _:
                 return print('Too many arguments')


 -----------------------------------------------------------------------------------------------------------------------

 --- Декораторы с параметрами ---

 # Умножает результат декорированной функции на N
 from functools import wraps

 def multiply_result_by(N):
     def my_decor(func):
         @wraps(func)
         def inner(*args, **kwargs):
             return func(*args, **kwargs) * N

         return inner
     return my_decor

 @multiply_result_by(2)
 def my_function(x, y):
     return x + y

 print(my_function(5, 6))  # -> 22


 # Декоратор monkey_patching - 2
 from functools import wraps

 def monkey_patching(arg='Monkey', kwarg='patching'):
     def my_decor(func):
         @wraps(func)
         def inner(*args, **kwargs):
             return func(*[arg for _ in args], **{k:kwarg for k, v in kwargs.items()})

         return inner
     return my_decor

 @monkey_patching(arg='Super')
 def print_args_kwargs(*args, **kwargs):
     for i, value in enumerate(args):
         print(i, value, end='   ')
     for k, v in sorted(kwargs.items()):
         print(f'{k} = {v}', end='   ')

 print_args_kwargs(1, 2, b=300, w=40)  # -> 0 Super   1 Super   b = patching   w = patching


 # Пробрасывает Аргументы декоратора дополнительно к аргументам которые передаются при вызове оригинальной функции
 from functools import wraps
                                                        # Тоже самое
 def pass_arguments(*args, **kwargs):                   def pass_arguments(*args_ext, **kwargs_ext):
     arg = args                                             def wrapper(func):
     kwarg = kwargs                                             @wraps(func)
     def my_decor(func):                                        def inner(*args, **kwargs):
         @wraps(func)                                               return func(*args + args_ext, **kwargs | kwargs_ext)
         def inner(*args, **kwargs):                            return inner
             return func(*args, *arg, **kwargs, **kwarg)    return wrapper

         return inner
     return my_decor

 @pass_arguments(s='Когда', w='-', r='нибудь!')
 def concatenate(**kwargs):
     result = ""
     for arg in kwargs.values():
         result += str(arg)
     return result

 print(concatenate(a="Я", b="Выучу", c="Этот", d="Питон", e="!"))  # -> ЯВыучуЭтотПитон!Когда-нибудь!


 # Разбери как работает!!!
 from functools import wraps

 def compose(*funcs):
     def wrapper(func):
         @wraps(func)
         def inner(*args, **kwargs):
             res = func(*args, **kwargs)
             for f in funcs:
                 res = f(res)
             return res
         return inner
     return wrapper

 def double_it(a):
     return a * 2

 def increment(a):
     return a + 1

 @compose(double_it, increment)
 def get_sum(*args):
     return sum(args)

 print(get_sum(5))          # -> 11
 print(get_sum(20, 10))     # -> 61
 print(get_sum(5, 15, 25))  # -> 91

 -----------------------------------------------------------------------------------------------------------------------

  --- iterator ---

 Как в python реализован цикл for

 # Тоже самое                   # Тоже самое
 s = 'Python'                   s = 'Python'

 it = iter(s)                   for letter in s:
 while True:                        print(letter)
     try:
         print(next(it))
     except StopIteration:
         del it
         break


 # Занимаемая память

 from sys import getsizeof

 numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
 iterator = iter(numbers)
 print(getsizeof(numbers), getsizeof(iterator))           # -> 136 48

 # Чем больше список, тем будет заметнее разница
 too_much_numbers = list(range(1000000))
 iterator = iter(numbers)
 print(getsizeof(too_much_numbers), getsizeof(iterator))  # -> 8000056 48



 -----------------------------------------------------------------------------------------------------------------------
 --- all zip ---

 # Сравнение внутри создадим пары
 lst = [7, 6, 5, 4, 3, 2, 1]
 print(list(zip(lst, lst[1:])))   # -> [(7, 6), (6, 5), (5, 4), (4, 3), (3, 2), (2, 1)]
 print(all([a > b for a, b in zip(lst, lst[1::])]))  # -> True  # Сравнение!  Тоже самое
 print(all(map(lambda x, y: x > y, lst, lst[1:])))   # -> True  # Сравнение!  Тоже самое

 # Создадим словарь
 a_str = 'abc'
 a_list = [1, 2, 3]
 print(dict(zip(a_list, a_str)))  # -> {'a': 1, 'b': 2, 'c': 3}   # Создали словарь   dict(zip(a_list, a_str))

 # Как Зипануть     Легко но всё же
 def read_csv():
     with open('data.csv', encoding='utf-8') as file:
         data = file.readline().replace('\n', '').split(',')
         lst = [i.replace('\n', '').split(',') for i in file.readlines()]
         lst_1 = [dict(zip(data, i)) for i in lst]                              <-----
         return lst_1

 # Тоже самое
 def read_csv():
     with open('data.csv') as file:
         keys = file.readline().strip().split(',')
         return [dict(zip(keys, line.strip().split(','))) for line in file]     <-----

 -----------------------------------------------------------------------------------------------------------------------

 --- with ---

 # Был долгий тупняк!!!                                                                             <-----
 with open('data.txt', encoding='utf-8') as file, open('forbidden_words.txt') as file_2:
     text, lst = file.read(), file_2.read().split()
     for i in lst:
         text = re.sub(i, '*' *len(i), text, flags=re.IGNORECASE)     # Тупняк был тут!   <-----
     print(text)


 # В print Можно использовать параметр file=   Запись в файл
 # Классный параметр  file=                                                                         <-----       <-----
 with open('output1.txt', 'w', encoding='utf-8') as file, open('logfile1.txt', encoding='utf-8') as file_2:
     for i in file_2.read().split('\n'):
         c, a, b = i.split(', ')
         d = datetime.datetime.strptime(b, "%H:%M") - datetime.datetime.strptime(a, "%H:%M")
         if d.seconds >= 3600:
             print(c, file=file)  #  file - Выбор куда записывать                                   <-----       <-----



 # Файл считывается 1 раз                                 # Файл считывается 1 раз
 with open('file.txt', encoding='utf-8') as file:         with open('file.txt', encoding='utf-8') as file:
     data = file.read()                                       # data = file.read()                     # Закоментили
     lst = [i.split() for i in file]                          lst = [i.split() for i in file]
     print(f'{len(lst)} lines')  # -> 0 lines                 print(f'{len(lst)} lines')  # -> 12 lines
     print(len(data))            # -> 1340                    # print(len(data))     # -> 0            # Закоментили

 # Записываем из одного файла в другой с помощью словаря
 d = {'а': 'a', 'к': 'k', 'х': 'h', 'б': 'b'}
 with open('file_1.txt', encoding='utf-8') as file, open('file_2.txt', 'w+') as file_2:
     for i in file.read():
         if i in d:
             print(d[i], file=file_2, end='')                # Выбор куда запись Параметр  file=
         else:
             print(i, file=file_2, end='')                   # Выбор куда запись Параметр  file=

 -----------------------------------------------------------------------------------------------------------------------

 --- json ---

 # Классное решение  Внутри цикла переменные посмотри как делать

 first = ''
 last = ''
 max_total = 0

 with open('manager_sales.json') as file:
     data = json.load(file)
     for element in data:
         name = element['manager']['first_name']
         lastname = element['manager']['last_name']
         total = 0                                    # Обнуляется каждый раз считаем заново
         for car in element['cars']:
             total += car['price']
         if total > max_total:
             max_total = total
             max_name = name
             max_lastname = lastname
         print(first, last, max_total)

 # Создал словарь всех
 import json

 with open('manager_sales.json') as file:
     data = json.load(file)
     a = {}
     for i in data:
         totals = 0
         for j in i['cars']:
             totals += j['price']
             if totals > 0:
                 a[f"{i['manager']['first_name']} {i['manager']['last_name']}"] = totals
     print(*sorted(a.items(), key=lambda x: x[1], reverse=True)[0])

 # Тоже самое с match case
 with open('manager_sales.json') as file:
     data = json.load(file)
     a = {}
     for i in data:
         totals = 0
         for j in i['cars']:
             totals += j['price']
             match totals:                                                                       # match case <-----
                 case totals if totals > 0:
                     a[f"{i['manager']['first_name']} {i['manager']['last_name']}"] = totals
     print(*sorted(a.items(), key=lambda x: x[1], reverse=True)[0])

 -----------------------------------------------------------------------------------------------------------------------

 # Похожий пример
 import json

 with open('group_people.json') as file:
     data = json.load(file)
     maximum = 0
     max_group = None
     for group in data:
         id_group = group['id_group']
         count = 0
         for person in group['people']:
             if person['gender'] == 'Female' and person['year'] > 1977:
                 count += 1
         if count > maximum:
             maximum = count
             max_group = id_group
     print(max_group, maximum)

 # Создал словарь всех
 with open('group_people.json') as file:
     data = json.load(file)
     a = {}
     for i in data:
         count = 0
         for j in i['people']:
             if j['gender'] == 'Female' and j['year'] > 1977:
                 count += 1
                 a[i['id_group']] = count
     print(*sorted(a.items(), key=lambda x: x[1], reverse=True)[0])

 # Тоже самое match case

 with open('group_people.json') as file:
     data = json.load(file)
     a = {}
     for i in data:
         count = 0
         for j in i['people']:
             match j:                                                                             # match case <-----
                 case {'gender': male, 'year': year} if year > 1977 and male == 'Female':
                     count += 1
                     a[i['id_group']] = count
     print(*sorted(a.items(), key=lambda x: x[1], reverse=True)[0])
 -----------------------------------------------------------------------------------------------------------------------

 Открыть сразу 2 и более файлов в одном with

 import json

 with open('Alphabet.json') as file, open('Abracadabra__1_.txt') as file_2:
     file = json.load(file)
     file_2 = file_2.read()
     a_str = ''
     for i in file_2:
         if i in file:
             a_str += file[i]
         else:
             a_str += i
     print(a_str.strip())

 # Тоже самое с match case

 with open('Alphabet.json.json') as file_json, open('Abracadabra__1_.txt.txt') as file_text:
     data_json = json.load(file_json)
     data_text = file_text.read()
     a_str = ''
     for i in data_text:
         match i:                                                                                 # match case <-----
             case i if i in data_json:
                 a_str += data_json[i]
             case _:
                 a_str += i
 print(a_str.strip())

 -----------------------------------------------------------------------------------------------------------------------
 # Открытие файлов разные способы!
 Через запятую ,
 with open('first_file.json') as file_1, open('second_file.txt') as file_2:                               <-----
    ...

 Вариант 2!
 with open(''first_file.txt', 'r') as file_1:
    ...
    with open('second_file.txt', 'r') as file_2:
        ...

 Можно отдельными блоками!
 with open(''first_file.txt', 'r') as file_1:
    ...
 with open('second_file.txt', 'r') as file_2:
    ...

 -----------------------------------------------------------------------------------------------------------------------

 --- Разные Подсчеты Руками ---

 # Метод Подсчета Руками
 a = [2, 1, 2, 3, 2, 1, 2, 3, 3, 2, 0, 3, 5, 3, 2]
 count = [0]*6

 for i in a:
     count[i] += 1
 print(count)                                   # -> [1, 2, 6, 5, 0, 1]

 for i in range(6):
     if count[i] > 0:
         print((str(i)+' ') *count[i], end='')  # -> 0 1 1 2 2 2 2 2 2 3 3 3 3 3 5

 -----------------------------------------------------------------------------------------------------------------------

 # Подсчет букв классно можно расчитать диапазон букв

 s = 'abcdefghigklmnopqrstuvwxyzsdhasd ASDKASD asdasd 543 *(^!*&@#'

 letters = [0] * 26

 for i in s.lower():
     if i >= 'a' and i <= 'z':             # -> Сделали Диапазон
         number = ord(i) - 97
         letters[number] += 1
         print(f"{i}: {number} ", end='')  # -> a: 0 b: 1 c: 2 d: 3 e: 4 f: 5 g: 6 h: 7 i: 8 g: 6 k: 10.......
 print('--'*50)
 for i in range(26):
     if letters[i] > 0:
         print(chr(i+97)*letters[i], end='')  # -> aaaaaabcdddddddefgghhikklmnopqrssssssstuvwxyz
 -----------------------------------------------------------------------------------------------------------------------


 --- Вложенные циклы ---

 # Разбор как работает

 Для Одного Внешнего цикла будет выполнятся 5 раз внутренний
                                                              # Выводим i                   # Выводим j
 for i in range(3):            #  1 Раз Внешний цикл          for i in range(3):            for i in range(3):
    for j in range(5):         #  5 Раз Внутренний                for j in range(5):            for j in range(5):
        print('*', end='')                                            print(i, end='')              print(j, end='')
    print()                    # Перенос строки                   print()                       print()

 # *****                                                      # 00000                       # 01234
 # *****                                                      # 11111                       # 01234
 # *****                                                      # 22222                       # 01234
 -----------------------------------------------------------------------------------------------------------------------

 Еще пример Работы Вложенного цикла

 for i in range(1, 3):            for i in 'ab':
     for j in range(10, 12):          for j in 'cd':
         print(i, j)                      print(i, j)

 # 1 10                           # a c
 # 1 11                           # a d
 # 2 10                           # b c
 # 2 11                           # b d

 -----------------------------------------------------------------------------------------------------------------------
 a = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
 b = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]]
 c = []

 # Складываем a+b списки
 for i, v in enumerate(a):
     for j, k in enumerate(v):
         c.append(k + b[i][j])

 print(c)  # -> [2, 3, 4, 5, 4, 5, 6, 7, 6, 7, 8, 9]
 -----------------------------------------------------------------------------------------------------------------------
 M, N = 2, 3
 zeros = []

 for i in range(M):
     zeros.append([0]* N)

 # Создали список списков из 0
 print(zeros)  # -> [[0, 0], [0, 0], [0, 0]]

 for i in range(M):
     for j in range(N):
         zeros[i][j] = 1
 # Все 0 заменили на 1
 print(zeros)  # -> [[1, 1], [1, 1], [1, 1]]
 -----------------------------------------------------------------------------------------------------------------------
 Строки заменить на столбцы - Транспонированная матрица

 A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

 for i in range(len(A)):
     for j in range(i+1, len(A)):
         A[i][j], A[j][i] = A[j][i], A[i][j]

 for r in A:                        #  1    5    9     13
     for x in r:                    #  2    6    10    14
         print(x, end='\t')         #  3    7    11    15
     print()                        #  4    8    12    16

 -----------------------------------------------------------------------------------------------------------------------
 Важно посмотри!!!

 n = 4

 # Если создавать список так:
 lst = [[1] * n] * n
 # То просто копируется ссылка на один и тот же список.
 print(lst)  # -> [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
 lst[0][n-1] = 5
 print(lst)  # -> [[1, 1, 1, 5], [1, 1, 1, 5], [1, 1, 1, 5], [1, 1, 1, 5]]  # Заменили ВСЕ последние элементы на 5

 # Если так:
 lst2 = [[1] * n for _ in range(n)]
 # То создаются отдельные списки
 print(lst2)  # -> [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
 lst2[0][n-1] = 5
 print(lst2)  # -> [[1, 1, 1, 5], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]  # Заменили Только 1 последний элемент на 5

 # Или делаем руками
 n = 4

 lst = [[1]*n]*n
 print(lst)  # -> [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
 for i, v in enumerate(lst):
     for j, k in enumerate(v):
         lst[i][-1] = 5

 print(lst)  # -> [[1, 1, 1, 5], [1, 1, 1, 5], [1, 1, 1, 5], [1, 1, 1, 5]]


 Копируется ссылка на один и тот же список.              <-----

 # Хороший пример
                    A = [[1]*N]*N              A[0][N-1] = 5         for i in range(4):
 N = 4              Был такой                  Сделали таким             for j in range(3):      Тоже самое
 A = [[1]*N]*N      #  1 1 1 1                 #  1 1 1 5                    print(1, end=' ')   # 1 1 1 5
 A[0][N-1] = 5      #  1 1 1 1                 #  1 1 1 5                print(5)                # 1 1 1 5
 for i in A:        #  1 1 1 1                 #  1 1 1 5                                        # 1 1 1 5
     print(*i)      #  1 1 1 1                 #  1 1 1 5                                        # 1 1 1 5

 -----------------------------------------------------------------------------------------------------------------------
 n = 4                                                     [print(*[i]*n) for i in range(n)]   # Хитрый вывод
 lst = [[i]*n for i in range(n)]     #  0 0 0 0            #  0 0 0 0
                                     #  1 1 1 1            #  1 1 1 1
 for i in lst:                       #  2 2 2 2            #  2 2 2 2
     print(*i)                       #  3 3 3 3            #  3 3 3 3


 -----------------------------------------------------------------------------------------------------------------------


 --- Вложенные Списки  Nested lists ---

 Элементы матрицы мы можем обходит в любом порядке

 # Обращение по индексам во вложенных списках Nested lists                # Матрица или Таблица  Добавил переносы в a_list
 a_list = [[0, 2, 4, 6], [1, 5, 9, 13], [3, 10, [4, 5, 7, 11], 17, 19]]
                                                                          a_list = [
 print(len(a_list))       # -> 3    # Длина всего списка                      [0, 2, 4, 6],
 print(a_list[2][3])      # -> 17                                             [1, 5, 9, 13],
 print(a_list[0][3])      # -> 6                                              [3, 10, 17, 19]
 print(a_list[0][1])      # -> 2                                          ]
 print(a_list[2][2][1])   # -> 5
 -----------------------------------------------------------------------------------------------------------------------

 # Строка(str) внутри Списка(list) считается вложенным элементом
 b = ['hello', 'hi', 'world']

 print(b[2])      # -> world
 print(b[2][4])   # -> d
 print(b[2][-1])  # -> d

 -----------------------------------------------------------------------------------------------------------------------

 -- Как Работают переменные внутри цилка! Посмотри обязательно!                    <-----   <-----

 1 Вариант обхода Просмотри в Дебаге!

 a_list = [[0, 2, 4, 6], [1, 5, 9, 13], [3, 10, 17, 19]]
 for i in a_list:                                                   # Вывод Внутри
     for j in i:                                                    # 10 12 14 16
         j += 10            # Не изменяет a_list                    # 11 15 19 23
         print(j, end=' ')  # Но выводит Измененный результат       # 13 20 27 29
         b_list = j+10      # Но мы можем создать Переменную
     print()
 print(a_list)  # -> [[0, 2, 4, 6], [1, 5, 9, 13], [3, 10, 17, 19]]      #  a_list Такой же как и был
 print(b_list)  # -> 39                                                  #  Создали перменную b_list
 -----------------------------------------------------------------------------------------------------------------------

 2 Вариант обхода!  Обход по индексам  Изменяет Исходник

 a_list = [[0, 2, 4, 6], [1, 5, 9, 13], [3, 10, 17, 19]]

 for i in range(3):                                                 # Вывод Внутри  Такой же
     for j in range(4):                                             # 10 12 14 16
         a_list[i][j] += 10            # ИЗМЕНЯЕТ a_list            # 11 15 19 23
         print(a_list[i][j], end=' ')                               # 13 20 27 29
     print()
 print(a_list) # -> [[10, 12, 14, 16], [11, 15, 19, 23], [13, 20, 27, 29]]  #  a_list Изменился

 # Если нужен другой  вывод меняем местами Циклы:  j i
 a_list = [[0, 2, 4, 6], [1, 5, 9, 13], [3, 10, 17, 19]]
                                                                    # Вывод Внутри
 for j in range(4):                                                 # 0 1 3
     for i in range(3):                                             # 2 5 10
         print(a_list[i][j], end=' ')                               # 4 9 17
     print()                                                        # 6 13 19

 # Обход в Обратном порядке
 for i in range(2, -1, -1):                                         # 19 17 10 3
     for j in range(3, -1, -1):                                     # 13 9 5 1
         print(a_list[i][j], end=' ')                               # 6 4 2 0
     print()

 # Сумма строк                                                                      Посмотри где переменная   <-----
 a_list = [[0, 2, 4, 6], [1, 5, 9, 13], [3, 10, 17, 19]]
 for i in range(3):                                                 # 12
     s = 0               # Каждый раз сумма обнуляется!!!           # 28
     for j in range(4):                                             # 49
         s += a_list[i][j]
     print(s)

 # Сумма Столбцов                                                                                             <-----
 for j in range(4):                                                 # 4
     s = 0               # Каждый раз сумма обнуляется!!!           # 17
     for i in range(3):                                             # 30
         s += a_list[i][j]                                          # 38
     print(s)

 -----------------------------------------------------------------------------------------------------------------------
 Как устроены матрицы!                                                                                        <-----

 # i < j    # Выше главной диагонали                                                                    <-----
 # i == j   # Главная диагональ                                                                         <-----
 # i > j    # Ниже главной диагонали                                                                    <-----

 a = []
 for i in range(3):
     a.append([0]*3)        #    Создаем Список(list)
 print(a)                   # -> [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

 for i in range(3):
     for j in range(3):
         if i == j:         # i == j   # Главная диагональ
             a[i][j] = 10
         elif i > j:        # i > j    # Ниже главной диагонали
             a[i][j] = 3
         elif i < j:        # i < j    # Выше главной диагонали
             a[i][j] = 5

 print(a)                   # -> [[10, 5, 5], [3, 10, 5], [3, 3, 10]]

 for i in a:
     print(i)

 # [10, 5, 5]
 # [3, 10, 5]
 # [3, 3, 10]
 -----------------------------------------------------------------------------------------------------------------------

 # Матрицы как смотреть вверх, вправо, вниз, влево                                                          <-----
 DIRS = [(-1,0),(0,1),(1,0),(0,-1)] # up right down left

 -----------------------------------------------------------------------------------------------------------------------

 # Несколько примеров для закрепления!

 # Создание и вывод матрицы                n = 2                                   n = 2
 n = 2                                     a = []                                  a = []
 a = []
 for i in range(n):                        for i in range(n):                      for i in range(n):
     a.append([5, 2, 1])                       a.append([5, 2, 1])                     a.append([5, 2, 1])

 print(a)  # -> [[5, 2, 1], [5, 2, 1]]     print(a)  # -> [[5, 2, 1], [5, 2, 1]]   print(a)  # -> [[5, 2, 1], [5, 2, 1]]

                                           # Поменяли местами i j                  # i j  Отрицательные индексы!
 for i in range(n):                        for j in range(n+1):                    for j in range(n, -1, -1):
     for j in range(n+1):                      for i in range(n):                      for i in range(n-1, -1, -1):
         print(a[i][j], end=' ')                   print(a[i][j], end=' ')                 print(a[i][j], end=' ')
     print()                                   print()                                 print()

 # 5 2 1                                   # 5 5                                   # 1 1
 # 5 2 1                                   # 2 2                                   # 2 2
                                           # 1 1                                   # 5 5
 -----------------------------------------------------------------------------------------------------------------------

 Работа Матриц/Матрицы/матриц/матрицы/МАТРИЦ/МАТРИЦЫ/!!! Посмотри интересно                <-----              <-----


 m = [['a', 'a', 'b', 'b'], ['a', 'a', 'b', 'b'], ['c', 'c', 'd', 'd'], ['c', 'c', 'd', 'd']]

 Вот матрица m:
 a a b b
 a a b b
 c c d d
 c c d d

 # m[i][j] распечатает матрицу как она есть:    # m[j][i] отразит матрицу по главной диагонали:

 for i in range(4):                             for i in range(4):
     for j in range(4):                             for j in range(4):
         print(m[i][j], end=' ')                        print(m[j][i], end=' ')
     print()                                        print()

 # a a b b                                      # a a c c
 # a a b b                                      # a a c c
 # c c d d                                      # b b d d
 # c c d d                                      # b b d d


 Вот матрица m:
 a a b b
 a a b b
 c c d d
 c c d d

 # m[~i][j] отразит верх и низ:   # m[i][~j] отразит лево и право:   # m[~j][~i] отразит относительно побочной диагонали:

 for i in range(4):               for i in range(4):                 for i in range(4):
     for j in range(4):               for j in range(4):                 for j in range(4):
         print(m[~i][j], end=' ')         print(m[i][~j], end=' ')           print(m[~j][~i], end=' ')
     print()                          print()                            print()

 # c c d d                        # b b a a                          # d d b b
 # c c d d                        # b b a a                          # d d b b
 # a a b b                        # d d c c                          # c c a a
 # a a b b                        # d d c c                          # c c a a


 Вот матрица m:
 a a b b
 a a b b
 c c d d
 c c d d

 # Тоже самое с enumerate()  Лучше использовать enumerate()

 # m[~j][i] - поворот вправо на 90°     # m[j][~i] - поворот на 90° влево

 for i, v in enumerate(m):              for i, v in enumerate(m):
     for j, k in enumerate(m):              for j, k in enumerate(m):
         print(m[~j][i], end=' ')               print(m[j][~i], end=' ')
     print()                                print()

 # c c a a                              # b b d d
 # c c a a                              # b b d d
 # d d b b                              # a a c c
 # d d b b                              # a a c c

 -----------------------------------------------------------------------------------------------------------------------
 Как работает интересно!
 n = 2
 a_str = 'a b c d e f'

 def chunked(a_str, n):
     a_str = a_str.split()
     a = []
     while len(a_str) != 0:
         c = a_str[:n]
         a.append(c)
         a_str = a_str[n:]
     return a
 print(chunked(a_str, n))  # -> [['a', 'b'], ['c', 'd'], ['e', 'f']]

 -----------------------------------------------------------------------------------------------------------------------

 --- Словарь(dict) ---
 # классный пример   Cоздать словарь из iterable     используем - dict.update()

 persons= [
     ('All H.', 3, 'M', '1'),
     ('Meg M.', 1, 'F', '2'),
 ]
 a_dict = {}
 for i in persons:
     a_dict.update({i[0]: {'salary': i[1], 'gender': i[2], 'passport': i[3]}})

 [a_dict.update({i[0]: {'salary': i[1], 'gender': i[2], 'passport': i[3]}}) for i in persons]  # Тоже работает
 print(a_dict)
 # -> {'All H.': {'salary': 3, 'gender': 'M', 'passport': '1'}, 'Meg M.': {'salary': 1, 'gender': 'F', 'passport': '2'}}

 -----------------------------------------------------------------------------------------------------------------------

 Побитовые операторы: Тильда ~
 # Тильда побитовый оператор ~  Инверсия - противоположное состояние
 a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
 print([[~i for i in i] for i in a])  # -> [[-2, -3, -4], [-5, -6, -7], [-8, -9, -10]]

 print(max((input().split()[~i] for i in range(int(input()))), key=int)) # Интересное решение с вводом матриц
 -----------------------------------------------------------------------------------------------------------------------


 --- match case  Тоже самое что  if...elif...else  но более гибкий ---                 <-----     <-----


 СРАЗУ НЮАНСЫ match case!

 # Нельзя использовать Глобальные переменные
 CMD_3 = 3
 CMD_5 = 5

 cmd = 5
 match cmd:
     case CMD_3:
         print('3')
     case CMD_5:
         print('5')

 # -> SyntaxError: name capture 'CMD_3' makes remaining patterns unreachable
 -----------------------------------------------------------------------------------------------------------------------
 Хитрости чтобы Работало!!!                                                  <-----            <-----
                                      через . переменные из другого модуля         class Consts:    # Можно через Класс
 CMD_3 = 3                                                                             CMD_3 = 3
 CMD_5 = 5                            import my_module                                 CMD_5 = 5

 cmd = 5                              cmd = 5                                      cmd = 5
 match cmd:                           match cmd:                                   match cmd:
     case int() as x if x == CMD_3:       case my_module.CMD_3:  #  через точку .      case Consts.CMD_3:    # точка .
         print('3')                           print('3')                                   print('3')
     case int() as x if x == CMD_5:       case my_module.CMD_5:  #  через точку .      case Consts.CMD_5:    # точка .
         print('5')                           print('5')                                   print('5')

 # -> 5                               # -> 5                                       # -> 5

 -----------------------------------------------------------------------------------------------------------------------

 В блоке case должен быть хоть 1 оператор:

 def connect_db(connect: dict) -> str:
     match connect:
         case {'server': host, 'login': login, 'password': psw, 'port': port}:
             pass
         case {'server': host, 'login': login, 'password': psw}:
             port = 22
         case _:  # wildcard
             return 'error connection'
     return f'connection: {host}@{login}.{psw}:{port}'

 request = {'server': '127.0.0.1', 'login': 'root', 'password': '1234'}

 result = connect_db(request)
 print(result)  # -> connection: 127.0.0.1@root.1234:22

 -----------------------------------------------------------------------------------------------------------------------
 # case _  Тоже самое  else
 # Пример простой    _ wildcard - отрабатывает всегда:

 cmd = 'bottom'                           cmd = 'top'                             cmd = 'MATCH CASE'

 match cmd:                               match cmd:                              match cmd:
     case 'bottom':                           case 'bottom':                          case 'bottom':
         print(f'Команда bottom')                 print(f'Команда bottom')                print(f'Команда bottom')
     case 'top':                              case 'top':                             case 'top':
         print(f'Команда top')                    print(f'Команда top')                   print(f'Команда top')
     case _:                                  case _:                                 case _:
         print('Неверная команда')                print('Неверная команда')               print('Неверная команда')

 # -> Команда bottom                      # -> Команда top                        # -> Неверная команда
 -----------------------------------------------------------------------------------------------------------------------

 # Пример '|' ИЛИ:

 cmd = 'top'                              cmd = 'MATCH CASE'

 match cmd:                               match cmd:
     case 'bottom' | 'top':                   case 'bottom' | 'top':
         print(f'Команда {cmd}')                  print(f'Команда {cmd}')
     case _:                                  case _:
         print('Неверная команда')                print('Неверная команда')

 # -> Команда top                         # -> Неверная команда
 -----------------------------------------------------------------------------------------------------------------------

 # Пример if...else и создание переменной:

 cmd = 'right'                                                  cmd = 'COOL'

 # Тоже самое что и if else Нельзя менять местами if else       # Создает перменную
 match cmd:                                                     match cmd:
     case 'bottom' | 'top':               # if                      case command:
         print(f'Команда {cmd}')                                        print(f'Команда {command}')
     case command:                        # else
         print(f'Команда {command}')

 # -> Команда right                                             # -> Команда COOL
 -----------------------------------------------------------------------------------------------------------------------

 # Пример Проверки типа и создание переменной:
                                                                  # Создание перменной          # Или через 'as'
 cmd = 10000                    cmd = 'STRING'                    cmd = 'NEW VARIABLE'          cmd = 'NEW VARIABLE'

 match cmd:                     match cmd:                        match cmd:                    match cmd:
     case str(cmd):                 case str(cmd):                    case str(new):                case str() as new:
         print(f'{cmd} Строка')         print(f'{cmd} Строка')            print(f'{new}')               print(f'{new}')
     case int(cmd):                 case int(cmd):                    case int(new):                case int() as new:
         print(f'{cmd} Число')          print(f'{cmd} Число')             print(f'{new}')               print(f'{new}')
     case _:                        case _:                           case _:                       case _:
         print('Другое')                print('Другое')                   print('Другое')               print('Другое')

 # ->  10000 Число              # -> STRING Строка                # ->  NEW VARIABLE            # ->  NEW VARIABLE


 # Тоже самое но с isinstance    if...elif...else

 cmd = 10000                    cmd = 'STRING'                    cmd = 'NEW VARIABLE'        cmd = 'NEW VARIABLE'

 if isinstance(cmd, str):       if isinstance(cmd, str):          if isinstance(cmd, str):    if isinstance(cmd, str):
     print(f'{cmd} Строка')         print(f'{cmd} Строка')            print(f'{cmd}')             print(f'{cmd}')
 elif isinstance(cmd, int):     elif isinstance(cmd, int):        elif isinstance(cmd, int):  elif isinstance(cmd, int):
     print(f'{cmd} Число')          print(f'{cmd} Число')             print(f'{cmd}')             print(f'{cmd}')
 else:                          else:                             else:                       else:
     print('Другое')                print('Другое')                   print('Другое')             print('Другое')

 # ->  10000 Число              # -> STRING Строка                # -> NEW VARIABLE           # -> NEW VARIABLE


 -----------------------------------------------------------------------------------------------------------------------

 # Дополнильные проверки if - guard(защитник)           # Не Прошло Проверку
 cmd = 1                                                cmd = 100000

 match cmd:                                             match cmd:
     case int() as new if 0 <= new <= 1000:                 case int() as new if 0 <= new <= 1000:    # guard(защитник)
         print(f'Число Прошло проверку {new}')                  print(f'Число Прошло проверку {new}')
     case _:                                                case _:
         print(f'Число НЕ Прошло проверку {cmd}')               print(f'Число НЕ Прошло проверку {cmd}')

 # ->  Число Прошло проверку 1                          # ->  Число НЕ Прошло проверку 100000
 -----------------------------------------------------------------------------------------------------------------------

 # Несколько проверок сразу
                                                      # Создание перменной  variables
 cmd = 1                                              cmd = 1
 match cmd:                                           match cmd:
     case int() | float() | list():                       case int() | float() | list() as variables:
         print(f'Число Прошло проверку {cmd}')                print(f'Число Прошло проверку {variables} {cmd}')
     case _:                                              case _:
         print(f'Число НЕ Прошло проверку {cmd}')             print(f'Число НЕ Прошло проверку {cmd}')

 # ->  Число Прошло проверку 1                        # ->  Число Прошло проверку 1 1

 -----------------------------------------------------------------------------------------------------------------------
 # Пример с Функцией

 def get_data(value):                                     def get_data(value):
     match value:                                             match value:
         case int(value) if value > 0:                            case int() | float() | str() as v_1:
             return value                                             return v_1
         case float(value) if -100 <= value <= 100:               case list() | tuple() as v_2:
             return value                                             return v_2
         case str(value):                                         case dict() | set() as v_3:
             return f'{value}'                                        return v_3
         case _:                                                  case _:
             return f"Другой Вариант"                                 return 'ВВедите другое'

 print(get_data(10))               # -> 10                print(get_data('hello'))          # ->  hello
 print(get_data('Hello'))          # -> Hello             print(get_data([10, 20]))         # ->  [10, 20]
 print(get_data(10.000))           # -> 10.0              print(get_data({'A': [30, 40]}))  # ->  {'A': [30, 40]}
 print(get_data([1000, 'Hello']))  # -> Другой Вариант    print(get_data(b'Hello'))         # ->  ВВедите другое

 -----------------------------------------------------------------------------------------------------------------------

 -- Работа с Списками(list) и Кортежами(tuple)                                                        <-----    <-----
 Sequence Types в match case - list, tuple, range

 cmd = ("Learning", "Python", 2000.78)  # 3 Элемента         cmd = ("Learning", "Python", 2000.78, 5, 3)  # 5 Элементов
 author, title, price = cmd   # Распаковка аналогичная ниже  author, title, price = cmd  # ValueError: too many values..
 print(author, title, price)  # -> Learning Python 2000.78   author, title, price
                                                             # ValueError: too many values to unpack (expected 3)
 # Будет работать если Кортеж содержить ровно 3 элемента!    # Кортеж содержить 5 Элементов!
 match cmd:                                                  match cmd:
     case author, title, price:               # Распаковка       case author, title, price:
         print(f'Кортеж: {author} {title} {price}')                  print(f'Кортеж: {author} {title} {price}')
     case _:  # wildcard                                         case _:  # wildcard
         print(f'Непонятный формат данных')                          print(f'Непонятный формат данных')

 # -> Кортеж: Learning Python 2000.78                        # -> Непонятный формат данных
 -----------------------------------------------------------------------------------------------------------------------

 -- Всё Работает так же как и при обычной распаковке '*'

 cmd = ["Learning", "Python", 2000.78, 5, 3, 5, 10]  # 7 Элементов Список
 author, title, price, *_ = cmd   # Так будет работать используем *    *_
 author, title, price = cmd       # -> ValueError: too many values to unpack (expected 3)
 print(author, title, price)      # -> Learning Python 2000.78

 # Список содержить 7 элементов и всё Работает!   *_    # Ограничить Размер Кортежа/Списка используем guard if
 match cmd:                                             match cmd:
     case author, title, price, *_:  #  *_                  case author, title, price, *_ if len(cmd) < 7:   # guard
         print(f'Список: {author} {title} {price}')             print(f'Список: {author} {title} {price}')
     case _:  # wildcard                                    case _:  # wildcard
         print(f'Непонятный формат данных')                     print(f'Непонятный формат данных')

 # -> Список: Learning Python 2000.78                   # -> Непонятный формат данных
 -----------------------------------------------------------------------------------------------------------------------

 -- Можно использовать группирующие скобки () или []  НЕ Создают Список ИЛИ Кортеж  Нет разница с () [] или без   <-----
 Говорит Python что будет Последовательность(Sequence) из определенного количества элементов
 Sequence Types в match case - list, tuple, range

 cmd = ("Learning", "Python", 2000.78, 5, 3, 5, 10)  # 7 Элементов Список

 # () - Просто группирующие скобки                           # [] - Просто группирующие скобки
 match cmd:                                                  match cmd:
     case (author, title, price, *_) if len(cmd) < 8: # ()       case [author, title, price, *_] if len(cmd) < 8:
         print(f'Кортеж: {author} {title} {price}')                  print(f'Кортеж: {author} {title} {price}')
     case _:  # wildcard                                         case _:  # wildcard
         print(f'Непонятный формат данных')                          print(f'Непонятный формат данных')

 # -> Кортеж: Learning Python 2000.78                        # -> Кортеж: Learning Python 2000.78
 -----------------------------------------------------------------------------------------------------------------------

 Строка(str) - Не относиться к Последовательностям/Sequences

 cmd = "Hello World"                                  cmd = ["Learning", "Python", 2000.78, 5, 3, 5, 10]  # 7 Элементов

 match cmd:                                           match cmd:
     case (author, title, price, *_):                     case (author, title, price, *_):
         print(f'Кортеж: {author} {title} {price}')           print(f'Список: {author} {title} {price}')
     case _:  # wildcard                                  case _:  # wildcard
         print(f'Непонятный формат данных')                   print(f'Непонятный формат данных')
 # -> Непонятный формат данных                        # -> Список: Learning Python 2000.78

 -----------------------------------------------------------------------------------------------------------------------

 Проверка типов данных внутри переменной и распаковка
 cmd = ("Learning", "Python", 2000.78, 5, 3, 5, 10)  # 7 Элементов Кортеж

 # Проверка прошла!                                                 # Проверка НЕ прошла 3 элемент не list!
 match cmd:                                                         match cmd:
     case [str() as author, str() as title, float() as price, *_]:      case [str(author), str(title), list(price), *_]:
         print(f'Кортеж: {author} {title} {price}')                         print(f'Кортеж: {author} {title} {price}')
     case _:  # wildcard                                                case _:  # wildcard
         print(f'Непонятный формат данных')                                 print(f'Непонятный формат данных')

 # -> Кортеж: Learning Python 2000.78                               # -> Непонятный формат данных

 # Можно Кмобинировать:  case [str() | int() as author, str() | list() as title, float() | dict() as price, *_]:
 -----------------------------------------------------------------------------------------------------------------------

 guard if Проверка типов данных внутри переменной и распаковка

 cmd = ("Learning", "Python", 2000.78, 5, 3, 5, 10)  # 7 Элементов Кортеж
 # Проверка прошла!
 match cmd:
     case [str() as author, str() as title, float() as price, *_] if len(cmd) < 8 and len(author) < 50 and len(title) < 10:
         print(f'Кортеж: {author} {title} {price}')
     case _:  # wildcard
         print(f'Непонятный формат данных')
 # -> Кортеж: Learning Python 2000.78

 -----------------------------------------------------------------------------------------------------------------------

 Несколько форматов
 cmd = ("Learning", "Python", 2000.78)                           # 3 Элемента
 cmd = [1, 10, "Learning", "Python", 2000.78, 5, 3, 5, 10, 'a']  # 10 Элементов

 # Два варианты но во втором убрали дублирование кода:   case [author, title, price] | (_, _, author, title, price, *_)
 # Имена перменных и их количество должны совпадать!!
 match cmd:                                          match cmd:
     case [author, title, price]:                        case (author, title, price) | (_, _, author, title, price, *_):
         print(f'Кортеж 1: {author} {title} {price}')        print(f'Кортеж 1: {author} {title} {price}')
     case [_, _, author, title, price, *_]:              case _:  # wildcard
         print(f'Кортеж 2: {author} {title} {price}')        print(f'Непонятный формат данных')
     case _:  # wildcard
         print(f'Непонятный формат данных')

 # -> Кортеж 2: Learning Python 2000.78              # -> Кортеж 1: Learning Python 2000.78
 -----------------------------------------------------------------------------------------------------------------------
 cmd = (1, 10, "Learning", "Python", 2000.78, 5, 3, 5, 10, 'a')  # 10 Элементов

 # Если Нужно добавить еще элемент
 match cmd:
     case [author, title, price]:
         print(f'Кортеж 1: {author} {title} {price}')
     case [_, _, author, title, price, number, *_]:
         print(f'Кортеж 2: {author} {title} {price}, {number}')  # number
     case _:  # wildcard
         print(f'Непонятный формат данных')
 # -> Кортеж 2: Learning Python 2000.78, 5      # Дополнительно вывели еще 5    <-----
 -----------------------------------------------------------------------------------------------------------------------
 Валидация последовательности в начале

 cmd = [1, 10, "Learning", "Python", 2000.78, 5, 3, 5, 10, 'a']  # 10 Элементов

 # Если Не хотим Список или Кортеж
 match cmd:
     case list() | tuple() as no_valid:  # <-----
         print(f'Список или Кортеж нельзя: {no_valid}')
     case [author, title, price]:
         print(f'Кортеж 1: {author} {title} {price}')
     case [_, _, author, title, price, number, *_]:
         print(f'Кортеж 2: {author} {title} {price}, {number}')
     case _:  # wildcard
         print(f'Непонятный формат данных')

 # -> Список или Кортеж нельзя: [1, 10, 'Learning', 'Python', 2000.78, 5, 3, 5, 10, 'a']

 -----------------------------------------------------------------------------------------------------------------------
 # Решение посмотри:

 book = [1, 'Балакирев С.М.', 'Python', 2100.0, 2023]                                           # YES
 book = [2, 'Зингаро. Д', 'Python без проблем', 1000.0, 2019]                                   # NO
 book = [1, 'Балакирев С.М.', 'Python', 0]                                                      # NO
 book = [4]                                                                                     # NO
 book = [5, 'Яв', 'Python. Лучшие практики и инструменты', 1500.1, 2021]                        # YES
 book = [5, 'Яв', 'Python. Лучшие практики и инструменты']                                      # NO
 book = [5, 'Яворски Михаил', 'Python. Лучшие практики и инструменты']                          # YES

 match book:
     case [_, str(f1), str(f2)] if len(f1) >= 6 and len(f2) >= 10:             # использую  str(f1)
         print('Yes')
     case (_, str(f1), str(f2), float(f3)) if len(f1) >= 6 and f3 > 0:         # использую  str(f1), float(f3)
         print('Yes')
     case (_, str() as f1, str() as f2, int() as f3) if f3 > 2020:             # использую  str() as f1,  int() as f3
         print('Yes')
     case _, str() as f1, str() as f2, float() as f3, int() as f4 if f3 > 0 and f4 > 2020:
         print('Yes')
     case _:
         print('No')

 # Создает переменные можно посмотреть их и использовать  Только которые прошли проверки
 print(f2)  # -> Python. Лучшие практики и инструменты


 # Придумал вместе с регулярками  Тоже самое что и выше!!!                        <-----               <-----

 match book:
     case int(_), str() as author, str() as title if re.search(r'\w{6,}', author) and re.search(r'\w{10,}', title):
         print('Yes')
     case int(_), str(author), str(title), float(price) if re.search(r'\w{6,}', author) and re.match(r'[1-9]', str(price)):
         print('Yes')
     case int(_), str() as author, str() as title, int() as year if re.match(r'202[0-9]+', str(year)):
         print('Yes')
     case int(_), str(author), str(title), float(price), int(year) if re.match(r'[1-9]', str(price)) and re.match(r'202[0-9]+', str(year)):
         print('Yes')
     case _:
         print('No')
 -----------------------------------------------------------------------------------------------------------------------

 -- Работа с Словарями(dict) и Множествами(set)                                                       <-----    <-----
 Sequence Types в match case - list, tuple, range


 -- Словарь(dict)     если прописываем в match case {} - значит мы работает со словарем(dict)
 -----------------------------------------------------------------------------------------------------------------------

 request = {'url': 'https://www.python.org/', 'method': 'GET', 'timeout': 1000}

 # Отрабатывает если на вход поступает словарь
 match request:
     case {'url': str() as url, 'method': str(method)}:  # url если записываем переменную, то значение может быть любое
         print(f'Запрос: url: {url}, method: {method}')
     case _:  # wildcard
         print('Неверный запрос')

 # -> Запрос: url: https://www.python.org/, method: GET
 -----------------------------------------------------------------------------------------------------------------------

 request = {'url': 'https://www.python.org/', 'method': 'GET', 'timeout': 100}

 # Если значение НЕ переменная, то отработает только если указали ТОЧНОЕ ЗНАЧЕНИЕ
 match request:
     case {'url': str() as url, 'method': str(method), 'timeout': 1000}:   # 'timeout' должен быть 100 как и в request
         print(f'Запрос: url: {url}, method: {method}')
     case _:  # wildcard
         print('Неверный запрос')

 # -> Неверный запрос

 Можно использовать ИЛИ  |
 case {'url': str() as url, 'method': str(method), 'timeout': 1000 | 2000 | 3000 | 40}:                         <-----
 Шаблоны можно записывать тоже через ИЛИ  |   Но только с ОДИНАКОВЫМИ  ПЕРЕМЕННЫМИ остальное может быть любое
 case {'url': str() as url, 'method': str(method), 'timeout': 1000} | {'NO': float() as url, 'GOOD': method}:   <-----
 Так же работает    guard(защитник)    Можно использовать все конструкции которые учили ранее
 case {'url': str() as url, 'method': str(method), 'timeout': 1000} if len(request) <= 3:                       <-----
 -----------------------------------------------------------------------------------------------------------------------

 Распакова в словаре **

 request = {'url': 'https://www.python.org/', 'method': 'GET', 'timeout': 1000, 'a': 10, 'b': 20}

 # Можем посмотреть другие ключи: значения   **kwards
 match request:
     case {'url': str() as url, 'method': str(method), **kwards}:
         print(f'Запрос: url: {url}, method: {method}, {kwards}')
     case _:  # wildcard
         print('Неверный запрос')

 # -> Запрос: url: https://www.python.org/, method: GET, {'timeout': 1000, 'a': 10, 'b': 20}

 -----------------------------------------------------------------------------------------------------------------------

 # Дополнительно может быть не более 2-х ключей  используем оператор упаковки **
 match request:
     # case {'url': str() as url, 'method': str(method), **kwards} if len(kwards) <= 2:  # Можно делать разные проверки
     case {'url': str() as url, 'method': str(method), **kwards} if not kwards:      # Можно делать разные проверки
         print(f'Запрос: url: {url}, method: {method}, {kwards}')
     case _:  # wildcard
         print('Неверный запрос')

 # -> Неверный запрос

 -----------------------------------------------------------------------------------------------------------------------
 Валидация данных!

 json_data = {'id': 2, 'type': 'list', 'data': [1, 2, 3], 'access': True, 'date': '14.06.2024'}

 # Проверяет конкретное значение и выводит данные
 match json_data:
     case {'type': 'list', 'data': list() as lst, **kwards}:      # Сработает если 'type'=='list' и 'data'==list
         print(f'JSON-данные: type-list: {lst}')
     case _:  # wildcard
         print('Неверный запрос')

 # -> JSON-данные: type-list: [1, 2, 3]

 -----------------------------------------------------------------------------------------------------------------------
 Более сложная Валидация данных!
 json_data = {'id': 2, 'access': True, 'info': ['14.06.2024', {'login': '123', 'email': 'email@m.ru'}, True, 1000]}

 # Найти в других коллекциях нужные данные
 match json_data:                                                   # Отработает если Список будет содержать 4 элемента
     case {'access': access, 'info': [_, {'email': email}, _, _]}:  # При распаковке нужно указывать все перменные _, _,
         print(f'JSON: access: {access}, email: {email}')           # или используем *_    <-----    <-----
     case _:  # wildcard
         print('Неверный запрос')

 # -> JSON: access: True, email: email@m.ru

 -----------------------------------------------------------------------------------------------------------------------
 # Решение посмотри:
 def parse_json(data):
     match data:
         case {'access': bool() as access, 'data': list([date, *_])}:
             return access, date
     return None

 json_data = {'id': 2, 'access': False, 'data': ['26.05.2023', {'login': '1234', 'email': 'xxx@mail.com'}, 2000, 56.4]}
 print(parse_json(json_data))  # -> (False, '26.05.2023')
 -----------------------------------------------------------------------------------------------------------------------

 # Другое Решение посмотри:
 def parse_json(data):
     match data:
         case {'access': access, 'data': [_, {'login': login, 'email': email}, *_]} if access:
             return login, email

 json_data = {'id': 2, 'access': True, 'data': ['26.05.2023', {'login': '1234', 'email': 'xxx@mail.com'}, 2000, 56.4]}

 print(parse_json(json_data))  # -> ('1234', 'xxx@mail.com')
 -----------------------------------------------------------------------------------------------------------------------


 -- Множество(set)

 primary_keys = {1, 2, 3}

 # Для работы с Множеством(set)  делаем проверку на set и дальше работаем
 match primary_keys:
     case set() as keys if len(keys) == 3:  # Проверили на множество(set) и длина множество(set) == 3
         print(f'Primary Keys: {keys}')
     case _:  # wildcard
         print('Неверный запрос')

 # -> Primary Keys: {1, 2, 3}

 -----------------------------------------------------------------------------------------------------------------------
 Общий пример работы!

 # Шаблоны обрабатывают словари иначе чем кортежи и списки
 def book1_to_tuple(data: dict | tuple | list, min_year=1800, max_year=3000) -> tuple | None:
     price = None
     match data:
         case [book, title, int() as year] if min_year < year < max_year:
             pass
         case (book, title, int() as year, price, *_) if min_year < year < max_year:
             pass
         case {'book': book, 'title': title, 'year': year, 'price': price}:  # Сначала больше проверок в dict (Частный)
             pass
         case {'book': book, 'title': title, 'year': year}:                  # Общий шаблон Должен идти после Частного
             pass
         case _:  # wildcard
             return None
     if not (min_year < year < max_year):
         return None
     return book, title, year, price


 book_1 = ('BOOK', 'Python', 2024)
 book_2 = ['BOOK', 'Python OOP', 3024, 3000]
 book_3 = {'book': 'Pyton', 'title': 'Нейросети', 'year': 2024}
 book_4 = {'book': 'Pyton', 'title': 'Keras + Tensorflow', 'price': 5430, 'year': 2024}

 print(book1_to_tuple(book_1))  # -> ('BOOK', 'Python', 2024, None)
 print(book1_to_tuple(book_2))  # -> None
 print(book1_to_tuple(book_3))  # -> ('Pyton', 'Нейросети', 2024, None)
 print(book1_to_tuple(book_4))  # -> ('Pyton', 'Keras + Tensorflow', 2024, 5430)

 -----------------------------------------------------------------------------------------------------------------------

 --- Битовые операции ---

 Проверка на включенность (1): if flags & mask == mask: # Бит включен (1)
 Выключение бита:              flags & ~mask
 Включение бита:               flags | mask
 Переключение бита:            flags ^ mask
 Инверсия бит:                 ~number == -number - 1
 Смещение бит вправо:          number >> 1 == number // (2 ** 1)
 Смещение бит влево:           number << 1 == number * (2 ** 1)


 Приоритеты             Полная форма   Краткая форма
 1) ИЛИ                  a = a | b     a |= b
 1) ИЛИ(XOR)             a = a & b     a &= b
 2) И                    a = a ^ b     a ^= b
 3) НЕ                   ~a

 >> Смещение бит вправо  a = a >> b    a >>= b  Делит    / Исходное число на выбранное
 << Смещение бит влево   a = a << b    a <<= b  Умножает * Исходное число на выбранное
 >>  <<  Работают быстрее чем обычные операторы / *

 # Битовая операция НЕ ~    1 операнд     ~ Тильда инверсия бит
 a = 121
 print(bin(a))  # -> 0b1111001  Старший Бит Это первый 0   Если он равен 0 число Положительное  -1 число Отрицательное
 print(~a)      # -> -122
 d = 0
 print(~d)      # -> -1
 d = -10
 print(~d)      # -> 9


 # Битовая операция И &     2 операнда    & Амперсанд
 flags = 5                                  flags = 1
 mask = 4                                   mask = 4
 res = flags & mask                         res = flags & mask
 print(res)     # -> 4                      print(res)     # -> 4
 if flags & mask == mask:                   if flags & mask == mask:
     print('Включен 2-й бит числа')             print('Включен 2-й бит числа')
 else:                                      else:
     print('2-й бит Выключен')                  print('2-й бит Выключен')
 # -> Включен 2-й бит числа                 # -> 2-й бит Выключен

 flags = 13
 mask = 5
 flags = flags & ~mask  # Выключение определенных Битов
 print(flags)  # -> 8

 # Битовая операция ИЛИ |     2 операнда    | Вертикальная черта
 flags = 8
 mask = 5
 flags = flags | mask  # Включение отдельных Битов переменной
 flags |= mask         # Тоже самое
 print(flags)  # -> 13

 # Битовая операция XOR Исключающее ИЛИ |     2 операнда    | Вертикальная черта
 # Шифрование так работает в Zip  Пароль mask
 flags = 9
 mask = 1
 flags = flags ^ mask
 print(flags)  # -> 8
 flags ^= mask         # Тоже самое
 print(flags)  # -> 9  # Работает без потерь возвращает Изначальное значение flags

 # Работают быстрее чем обычные операторы / *
 # >> Смещение бит вправо
 # << Смещение бит влево

 # Делит    / Исходное число на выбранное
 # Умножает * Исходное число на выбранное
 x = 160
 print(bin(x))  # -> 0b10100000
 x = x >> 1     # -> Делит / на 2   2*2
 print(x)       # -> 80
 print(bin(x))  # -> 0b1010000  # На 0 меньше
 x = x >> 2     # -> Делит / на 4
 print(x)       # -> 20

 x = 160
 x = x << 2     # -> Умножает * 4
 print(x)       # -> 640

 # Задачи
 a = 100
 print(a | (1 << 3))  # -> 108   Включить третий бит

 -----------------------------------------------------------------------------------------------------------------------



 --- OOP ---

 -----------------------------------------------------------------------------------------------------------------------

 -- Атрибуты класса --

 class Person:
     name = 'Ivan'
     age = 30

 print(Person.__dict__)                #  Словарь всех атрибутов класса
 print(getattr(Person, 'x', 100))      # -> 100    Получить атрибут без ошибки
 print(getattr(Person, 'Ivan', 200))   # -> 200    Получить атрибут без ошибки
 print(Person.name)                    # -> Ivan   Через . точку обращение

 print(hasattr(Person, 'name'))        # -> True   Проверка атрибута

 Person.name = 'Misha'                 #           Присвоение атрибута
 Person.x = 10                         #           Создание атрибута которого не было через точку .
 print(setattr(Person, 'x', 1000))     #           Присвоение атрибута
 print(setattr(Person, 'y', 50))       #           Создание атрибута которого не было

 del Person.x                          #           Удаление атрибута через точку .
 # del Person.x    # AttributeError:.. #           Нельзя Удалить атрибут которого нет
 print(delattr(Person, 'y'))           #           Удаление атрибута

 -----------------------------------------------------------------------------------------------------------------------
 # Создание атрибутов на основе Списка кортежей
 class Empty:
     pass

 my_list = [
     ('apple', 23),
     ('banana', 80),
 ]
                                                                    # Альтернатива
 for i in my_list:                                                  for attr, val in my_list:
     # setattr(Empty, i[0], i[1])                                       setattr(Empty, attr, val)
     setattr(Empty, *i)              # Можно и так распаковать

 # [setattr(Empty, *i) for i in my_list]  # Тоже работает

 # В классе появились атрибуты
 print([i for i in Empty.__dict__.items() if not i[0].endswith('__')])  # -> [('apple', 23), ('banana', 80)]

 -----------------------------------------------------------------------------------------------------------------------


 -- Атрибуты Экземпляра класса  --

 # Работает как поиск LEGB пространство имен

 class Person:
     name = 'Ivan'
     age = 30

 man = Person()                #              # Создаём ЭК и связываем его с переменной man
 print(man.age)                # ->  30       # Получаем текущее значение атрибута age в ЭК man
 man.money = 100               #              # Создаём в ЭК атрибут money со значением 100
 print(man.money)              # ->  100      # Получаем текущее значение атрибута money в ЭК man
 man.money = 250               #              # Изменяем текущее значение атрибута money в ЭК man на 250
 print(man.money)              # ->  250      # Получаем текущее значение атрибута money в ЭК man
 delattr(man, 'money')         #              # Удаляем атрибут money из ЭК
 print(hasattr(man, 'money'))  # ->  False    # Проверяем наличие атрибута money в ЭК man: False

 # атрибуты не создаются в самом ЭК, а получают ссылку на атрибут класса.
 print(man.__dict__)           # -> {}
 print(Person.__dict__)        # -> {'__module__': '__main__', 'name': 'Ivan', 'age': 30, '__dict__': <attribute....

 # Но в случае изменения атрибута из-под ЭК, данный атрибут со своим значением отразится в словаре атрибутов
 print(man.__dict__)           # -> {}
 man.name = 'Alex'
 print(man.__dict__)           # {'name': 'Alex'}

 # Изменения не затронут сам класс, так как изменение значения проводилось из-под ЭК
 print('Атрибуты класса:', Person.__dict__)   # -> Атрибуты класса: {'__module__': '__main__', 'name': 'Ivan',...
 print('Атрибуты ЭК man:', man.__dict__)      # -> Атрибуты ЭК man: {'name': 'Alex'}

 # Атрибуты двух ЭК независимы друг от друга
 dude = Person()
 print('Атрибуты ЭК dude:', dude.__dict__)    # -> Атрибуты ЭК dude: {}
 dude.name = 'Sergey'
 print('Атрибуты ЭК dude:', dude.__dict__)    # -> Атрибуты ЭК dude: {'name': 'Sergey'}
 print('Атрибуты ЭК man:', man.__dict__)      # -> Атрибуты ЭК man: {'name': 'Alex'}

 # При удалении атрибута с одинаковыми именами и разными значениями. ЭК будет выводиться аргумент из самого класса:
 print(Person.name, man.name)                 # -> Ivan Alex
 del man.name
 print(Person.name, man.name)                 # -> Ivan Ivan
 -----------------------------------------------------------------------------------------------------------------------

 # Пример создания атрибутов из функции:
 def _clear() -> None: ...
 def _clear() -> None: pass

 # pass - это просто заглушка
 # ...  - это просто Другая заглушка  ... - объект Ellipsis


 class Config: ...

 def create_instance(n: int) -> Config:
     obj = Config()
     obj.__dict__ = {f'attribute{i}': f'value{i}' for i in range(1, n + 1)}
     return obj

 # Тоже самое
 class Config:
    pass

 def create_instance(num):
     obj = Config()
     for i in range(1,num+1):
         obj.__dict__[f'attribute{str(i)}'] = f'value{str(i)}'
     return obj

 # Ниже расположены проверки для функции create_instance

 config_2 = create_instance(2)
 assert isinstance(config_2, Config)
 assert config_2.__dict__ == {'attribute1': 'value1', 'attribute2': 'value2'}

 -----------------------------------------------------------------------------------------------------------------------

 -- Методы экземпляра. Аргумент self --

 Метод — функция, которая определена внутри класса
 1) Метод связан с ЭК и вызывается от него.
 2) При вызове метода первым параметром будет передан тот ЭК, от которого метод был вызван.  self


  --- Compare with Clipboard   PyCharm  Как сравнить текст или файл ---
 Ctrl + C или Ctrl + Х   и выделяем другой текст  и нажимаем ЛКМ и выбираем Compare with Clipboard
 Можно сравнивать и файлы.  Текст должен быть в тройных кавычках


 # Примеры

 # Установка атрибута экземпляра


# Явное лучше НЕявного
class Robot:                                              class Robot:
    name = None

    def set_name(self, name):                                 def set_name(self, name):
        self.name = name                                          setattr(self, 'name', name)

    def say_hello(self):                                      def say_hello(self):
        if self.name:                                             if hasattr(self, 'name'):
            print(f'Hello, human! My name is {self.name}')            print(f'Hello, human! My name is {self.name}')
        else:                                                     else:
            print('У робота нет имени')                               print(f'У робота нет имени')

 class Robot:
     def set_name(self, name):
         self.name = name

     def say_hello(self):
         try:
             if self.name:
                 print(f'Hello, human! My name is {self.name}')
         except:
             print(f'У робота нет имени')

 c3po = Robot()
 c3po.say_hello()
 c3po.set_name('R2D2')
 c3po.say_hello()

 # Еще один пример Установки значений

 class Constructor:                          class Constructor:
     def add_atribute(self, name, value):        def add_atribute(self, name, value):
         self.__dict__[name] = value                 setattr(self, name, value)

     def display(self):                          def display(self):
         print(self.__dict__)                        print(self.__dict__)

 # Проверка на экземпляр класса
 class Point:                           class Point:                            class Point:

     def set_coordinates(self, x, y):       def set_coordinates(self, x, y):        def set_coordinates(self, x, y):
         self.x = x                             self.x = x                              self.x = x
         self.y = y                             self.y = y                              self.y = y

     def get_distance(self, obj):           def get_distance(self, obj):            def get_distance(self, obj):
         if isinstance(obj, Point):             if hasattr(obj, 'x' and 'y'):           try:
             return self.x, self.y                  return self.x, self.y                   return self.x, self.y
         else:                                  else:                                   except:
             print("Неверно")                       print("Неверно")                        print("Неверно")

 # match case
    def get_distance(self, obj):             def get_distance(self, obj):
        match obj:                               match obj:
            case Point():                            case Point() as my_obj:
                return self.x, self.y                    return self.x, self.y
            case _:                                  case _:
                print("Неверно")                         print("Неверно")

 -----------------------------------------------------------------------------------------------------------------------


 # Примеры  __init__


 class Person:                      class Person:
     def __init__(self, name, age):     def __init__(self, name, age):
         self.name = name                   self.name = name
         self.age = age                     self.age = age
                                            self.greet = lambda: f'Hi, my name is {self.name},I am {self.age} years old'
     def greet(self):
         return f"Hello, my name is {self.name}, and I am {self.age} years old"

 -----------------------------------------------------------------------------------------------------------------------

 # Примеры **kwargs  в __init__   Результат одинаковый   Посмотри третий пример **kwargs и kwargs без **      <-----

class CustomLabel:                       class CustomLabel:                         class CustomLabel:

    def __init__(self, text, **kwargs):      def __init__(self, text:str, **kwargs):    def __init__(self, text, **kwargs):
        self.text = text                         self.text = text                           self.text = text
        for key, value in kwargs.items():        self.config(**kwargs)                      self.__dict__.update(kwargs)
            self.__dict__[key] = value                                                      self.__dict__.update(**kwargs)

    def config(self, **kwargs):             def config(self, **kwargs):                 def config(self, **kwargs):
        for key, value in kwargs.items():       for key, value in kwargs.items():           self.__dict__.update(kwargs)
            self.__dict__[key] = value              setattr(self, key, value)               self.__dict__.update(**kwargs)


 # Присмотрись к решению      Последний класс посмотри     class Employee       <-----             <-----
 class Person:

     def __init__(self, name, age):
         self.name = name
         self.age = age

     def display_person_info(self):
         print(f"Person: {self.name}, {self.age}")

 class Company:

     def __init__(self, company_name, location):
         self.company_name = company_name
         self.location = location

     def display_company_info(self):
         print(f"Company: {self.company_name}, {self.location}")

 class Employee:
     def __init__(self, name, age, company_name, location):
         self.personal_data = Person(name, age)
         self.work = Company(company_name, location)

 emp = Employee('Jessica', 28, 'Google', 'Atlanta')
 print(emp.personal_data.name)                       # -> Jessica
 print(emp.personal_data.age)                        # -> 28
 emp.personal_data.display_person_info()             # -> Person: Jessica, 28
 print(emp.work.company_name)                        # -> Google
 print(emp.work.location)                            # -> Atlanta
 emp.work.display_company_info()                     # -> Company: Google, Atlanta

 -----------------------------------------------------------------------------------------------------------------------




 -----------------------------------------------------------------------------------------------------------------------




 -----------------------------------------------------------------------------------------------------------------------





 -----------------------------------------------------------------------------------------------------------------------

________________________________________________________________________________________________________________________















"""