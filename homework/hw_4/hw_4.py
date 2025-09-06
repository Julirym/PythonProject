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

