#4)Напишите программу, которая в последовательности натуральных чисел определяет максимальное число, кратное 5.
# Программа получает на вход количество чисел в последовательности, а затем сами числа.
# В последовательности всегда имеется число, кратное 5.
# Программа должна вывести одно число - максимальное число, кратное 5.

#HW:
#Codewars:
#Is the string uppercase?
#Reversed Words
#simple calculator

#Задание со *. Напишите калькулятор, который будет принимать 2 числа (не обязательно от 0 до 9) и знак.
# После чего программа должна произвести нужную математическую операцию и вывести результат.
#Пример:
#21/3
#Ответ:7

                                              #УРОК 4

# numbers = []
# print(numbers)

# numbers = [6, 4, 3, 1]
# a = numbers[2]
# b = numbers[0]
#
# del numbers[2]
#
# print(numbers)
# print(a)
# print(b)

# numbers = [6, 4, 3, 1, 5, 4, 3, 3, 2, 1]
#
# a = numbers[25]
# print(a)

# numbers = [1, 4, 5]
#
# numbers.append(15)
# numbers.append('Привет')
#
# print(numbers)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# a = numbers.pop(3)
#
# print(numbers)
# print(a)

# numbers = [5, 12, 1, 5, 3, 2, 'hello', 123]
# print(len(numbers))
# print(sorted(numbers))
# print(sum(numbers))
# print(min(numbers))
# print(max(numbers))

# '123', range(10), [1, 2, 3]

# 123 -> int
# 3.14 -> float
# 'hello' -> str
# True -> bool
# None -> NoneType
# [1, 2, 3] -> list

# numbers = [5, 12, '123', 1, 5, 3, 2, True]

# for i in numbers:
#     if type(i) == int:
#         print(i)
#
#
# for i in numbers:
#     if isinstance(i, int):
#         print(i)

# items = [1, '123', 34, True]
# numbers = []
#
# for item in items:
#     if type(item) == int:
#         numbers.append(item)
#
# print(numbers)

# numbers = []
#
# for i in range(10):
#     if i % 2 == 0:
#         numbers.append(i)
#
# print(numbers)
#
# numbers2 = [i for i in range(10) if i % 2 == 0]
#
# print(numbers2)

# 123, '123', True, None, ...
# [1, 2, 3], ...

# a = 5
# b = a # 5
#
# a += 1
#
# print(a)
# print(b)
#
# numbers = [1, 2, 3, 4, 5]
# numbers2 = numbers
#
# numbers.append(6)
#
# print(numbers)
# print(numbers2)

# numbers = (1, 2, 3, 4)
# numbers2 = (1, 2, 3, 4)
#
# num3 = numbers + numbers2
#
# print(num3)
#
#
# for i in numbers:
#     print(i)
#
# print(numbers)

# print(list('123123'))

# info = [25, 5442433, 'Оксана']
# info2 = [45, 512323, 'Сережа']

# data = {'name': 'Oksana', 'age': 25, 'id': 244354}
#
# info = {'name': 'Сережа', 'country': 'USA'}
# info['id'] = 324545
# info['name'] = 'Маша'
#
# print(info)

# data = {
#     'name': 'Oksana',
#     'age': 25,
#     'id': 244354,
#     'country': 'USA'
# }

# print(data.keys())
# print(data.values())
# print(data.items())

# for key in data.items():
#     print(key)

# for key in data:
#     data[key] = 123
#
# print(data)

# print(data.get('country', 'Страна не указана'))
# print('country' in data)

# items = [1, 2, 3, {'name': 'Oksana'}, ['a', 'b', 'c']]
# info = items[3] # {'name': 'Oksana'}
# letters = items[4] # ['a', 'b', 'c']
#
# print(letters[2])
# print(info)
# print(items)

# items = [1, 2, 3, {'name': 'Oksana'}, [[1, 2, 3], 'b', 'c']]
# print(items[3]['name'])
# print(items[4][0][1])

# data = {
#     'name': 'Oksana',
#     'data': {
#         'id': 2,
#         'country': 'China',
#     }
# }
#
# print(data['name'])
# print(data['data']['id'])

# numbers = [1, 2, 2, 2, 3, 5, 5, 6]
# result = []
#
# for i in numbers:
#     if i not in result:
#         result.append(i)
#
# print(result)

#Задача 1  - 4 урок
# Сгенерируйте список numbers, состоящий из чисел в диапазоне от 0 до 100 включительно, которые делятся без остатка как на 2, так и на 3.
# Выведите список numbers на экран.
#Ответ: [0, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96]
# Решите эту задачу в 2 способа - с помощью генератора списков и без него.

# number = [i for i in range(100) if i % 2 == 0 and i % 3 == 0]
# print(number)

# numbers = []
# for i in range(100):
#     if i % 2 == 0 and i % 3 == 0:
#         numbers.append(i)
#
# print(numbers)

#Задача 2 - 4 урок
# Имеется список items = [1.2, 3, None, 100, {'info': 'bla-bla'}, 44, 'Hi!', 99, 44.32, None]
# Составьте новый список numbers, который содержит только целые числа (int) и вещественные числа (float) из списка items.
# Выведите на экран сумму чисел в numbers.
# Ответ: 291.52

# items = [1.2, 3, None, 100, {'info': 'bla-bla'}, 44, 'Hi!', 99, 44.32, None]
# numbers = []
#
# for i in items:
#     if type(i) in (int, float):
#         numbers.append(i)
#
# #print(numbers)
# print(sum(numbers))

#Задача 3 - 4 урок
# Создать список messages, который будет хранить “сообщения”.
# Программа должна в бесконечном цикле запрашивать у пользователя ввести сообщение (строку) с клавиатуры и сохранять ее в список messages.
# Причем программа должна запоминать не более 5 последних сообщений.
# То есть, если длина списка messages превысила 5, то первое сообщение в нем должно быть удалено.
# Если пользователь ввел “Пока”, то программа должна вывести “Ну ладно, пока!” и список последних сообщения на экран.

# Пример: если пользователь вводил такие сообщения (без кавычек):
# “Привет!”, “Как твои дела?”, “Как твое настроение?”, “Бла-бла-бла”, “Что нового?”, “Сори я занят”, “Пока”
# То программа должна вывести:
# # Ну ладно, пока!
# ['Как твое настроение?', 'Бла-бла-бла', 'Что нового?', 'Сори я занят', 'Пока']

# messages = []
#
# while True:
#
#     a = input("Введите сообщение: ")
#     messages.append(a)
#
#     if len(messages) > 5:
#         messages.pop(0)  #удаляем первое сообщение, если их становится 6, потом цикл начинается заново
#
#     if a == 'Пока':
#         print('Ну ладно, пока!')
#         break
#
# print("Последние сообщения:", messages)

#Задача 4 - 4 урок
#Программиста попросили написать кусок кода, который проверяет, что пользователь совершеннолетний или он является администратором.
#Если одно из этих условий истинно, то ему предоставляют доступ, в противном случае доступ запрещен.
# Но что-то пошло не так и код работает совсем не так, что нужно исправить?

# age = 16
# admin = True
#
# if age >=18 or admin == True:
#     print("Доступ разрешен")
# else:
#     print("Доступ запрещен")

#Задача 5 - 4 урок.
# Есть словарь с товарами:
products = {
     "apple": {"quantity": 10, "price": 100},
    "banana": {"quantity": 20, "price": 50},
    "orange": {"quantity": 15, "price": 80},
    "grape": {"quantity": 8, "price": 120},
    "milk":{"quantity": 12, "price": 90},
     "bread": {"quantity": 30, "price": 40}
}

# Необходимо увеличить цену всех продуктов на 20 процентов.
# Удалить товар “milk”.
# Добавить товар “Salt” с количеством 7 и ценой 12.
# Вывести общую стоимость всех товаров в магазине. Ответ: 6516.0

# products = {
#     "apple": {"quantity": 10, "price": 100},
#     "banana": {"quantity": 20, "price": 50},
#     "orange": {"quantity": 15, "price": 80},
#     "grape": {"quantity": 8, "price": 120},
#     "milk":{"quantity": 12, "price": 90},
#     "bread": {"quantity": 30, "price": 40}
# }
#
# for c in products.values():
#     c["price"] *=1.2
# print(products)
#
# products["apple"]["price"] = products["apple"]["price"] * 1.2
# products["banana"]["price"] = products["banana"]["price"] * 1.2
# products["orange"]["price"] = products["orange"]["price"] * 1.2
# products["grape"]["price"] = products["grape"]["price"] * 1.2
# products["milk"]["price"] = products["milk"]["price"] * 1.2
# products["bread"]["price"] = products["bread"]["price"] * 1.2
# print(products)

# del products['milk']

# print(products)

# products["Salt"] = {"quantity": 7, "price": 12}  # добавляем новую пару ключ-значение
# print(products)

# total_cost = sum(products['quantity'] * products['price'] for products in products.values())
# print(total_cost)
total = 0
for i in products.values():
    total += i["quantity"] * i["price"]


#Задача 6 - 4 урок
# Есть два списка одинаковой длины:
# keys = ['name', 'age', 'city', 'occupation', 'email', 'phone', 'hobby', 'education', 'company', 'salary']
# values = ['Alice', 30, 'New York', 'Engineer', 'alice@example.com', '+1234567890', 'Reading', 'Masters in Computer Science', 'TechCorp', 90000]
#
# Создай словарь info из ключей keys и значений values. (Каждое значение занимает ту же позицию, что и ключ в другом списке)
# Выведи словарь info на экран
#
# keys = ['name', 'age', 'city', 'occupation', 'email', 'phone', 'hobby', 'education', 'company', 'salary']
# values = ['Alice', 30, 'New York', 'Engineer', 'alice@example.com', '+1234567890', 'Reading', 'Masters in Computer Science', 'TechCorp', 90000]
#
# info = {}
#
# for i in range(len(keys)):
#     info[keys[i]] = values[i]
#
# print(info)

# info = dict(zip(keys, values))
# print(info)  #Чтобы создать словарь из двух списков в Python,
# можно использовать функцию zip(),
# которая объединяет элементы двух списков попарно, и затем преобразовать результат в словарь с помощью dict().

#Задача 7 - 4 урок
# Шифр.
# Есть сообщение (строка):
# "2__234йшDGмёшSDFжкъrrrщзнSDF78юкйфуSDFшёью$#2Sшжйи3%узфsdf34нкфыvvя"
# И ключ к шифру, где каждую букву нужно заменить на ее значение в словаре:
# cipher = {
#     "а": "щ", "б": "д", "в": "ю", "г": "ф", "д": "з", "е": "м", "ё": "р",
#     "ж": "т", "з": "п", "и": "я", "й": "с", "к": "н", "л": "э", "м": "к",
#     "н": "л", "о": "ё", "п": "ж", "р": "ц", "с": "б", "т": "у", "у": "в",
#     "ф": "о", "х": "и", "ц": "х", "ч": "г", "ш": "е", "щ": "й", "ъ": "ы",
#     "ы": "ч", "ь": "ш", "э": "ъ", "ю": "а", "я": "ь"
# }
# Расшифруйте секретное сообщение с помощью ключа cipher, при этом мусорные значение (которых нет в словаре) должны быть пропущены и не добавлены в результат.
# Выведите результат на экран.
# Дополнительно: напишите программу, которая получает строку через ввод с клавиатуры и “отправляет” зашифрованный ответ агенту.

# secret_message = "2__234йшDGмёшSDFжкъrrrщзнSDF78юкйфуSDFшёью$#2Sшжйи3%узфsdf34нкфыvvя"
# cipher = {
#     "а": "щ", "б": "д", "в": "ю", "г": "ф", "д": "з", "е": "м", "ё": "р",
#     "ж": "т", "з": "п", "и": "я", "й": "с", "к": "н", "л": "э", "м": "к",
#     "н": "л", "о": "ё", "п": "ж", "р": "ц", "с": "б", "т": "у", "у": "в",
#     "ф": "о", "х": "и", "ц": "х", "ч": "г", "ш": "е", "щ": "й", "ъ": "ы",
#     "ы": "ч", "ь": "ш", "э": "ъ", "ю": "а", "я": "ь"
# }
# decrypted_message = ""
#
# for c in secret_message:
#     if c in cipher:
#         decrypted_message += cipher[c]
#
# print(decrypted_message)

# Самая популярная буква.
# Есть строка:
# dialog = """Doc: Запомни! Согласно моей теории, ты помешал знакомству своих родителей.
# Если они не встретятся, то не влюбятся, не поженятся, и у них не будет детей.
# Поэтому твой старший брат исчезает с фотографии. Затем очередь твоей сестры,
# и если ты все не исправишь, ты будешь следующим.
# Marty: Тяжелый случай.
# Doc: Вес тут совершенно ни при чем. """
# # Тройные кавычки позволяют удобно писать текст в несколько строк.
# С помощью словаря подсчитайте количество букв в строке dialog игнорируя регистр. Ключами в словаре должны быть буквы, а значения - количество вхождения буквы в текст. Например: {'т': 26, 'е': 32...}
# Вывести на экран букву, которая встречается максимальное количество раз.

# counter = {}
#
# for c in dialog:
#     if c.isalpha():
#         counter.setdefault(c.lower(), 0)
#         counter[c.lower()] += 1
#
# max_number = max(counter.values())
#
# for key in counter:
#     if max_number == counter[key]:
#         print(f"Самая частая буква: {key}")
#         break