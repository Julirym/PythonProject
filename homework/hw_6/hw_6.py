# from my_functions import add, sub
#
# print(add(1, 2))
# print(sub(3, 2))
#
# import my_functions
#
# print(my_functions.add(1, 2))
# print(my_functions.sub(5, 4))

# import my_functions as func
#
# print(func.add(1, 2))
# print(func.sub(5, 4))


# from my_functions import *
#
# print(add(1, 2))
# print(sub(5, 4))


# import math
# from collections import Counter
# import operator
#
#
# counter = Counter("dfkgfdjgn3243")


# print(counter.most_common(2))

# from functions.functions1 import add
#
# print(add(1, 2))


# items = [1, 2, 3, '123', print]
# print(items)
#
# a = sorted
# print(a)
#
# b = print
#
# b(1, 2, 3)

# def function(a):
#     return a
#
#
# result = function(print)
# print(result)
#
# def add_one(x):
#     return x + 1
#
#
# numbers = [1, 2, 3, 4, 5]
#
# # map(add_one, numbers)
#
# result = list(map(add_one, numbers))
#
# print(result)


# def function(n):
#     return n % 2 == 1
#
#
# numbers = [1, 2, 3, 4, 5]
#
# result = filter(function, numbers)
# list_result = list(result)
#
# print(list_result)


# def my_filter(func, items):
#     result = []
#
#     for item in items:
#         if func(item):
#             result.append(item)
#
#     return result


# numbers = [1, 2, 3]
#
# result = list(map(lambda x: x ** 2, numbers))
#
# print(result)
#
#
# numbers = [1, 2, 3, 4, 5]
#
# result = filter(lambda x: x > 3, numbers)
# list_result = list(result)
#
# print(list_result)


# from tools import function_logs, add_smile
#
# @add_smile
# def mul(a, b):
#     return a * b
#
# result = mul(2, 3)
# print(result)
#
# def div(a, b):
#     return a / b


# Домашнее задание (занятие 6)

# 1
# Модуль.
# Перенесите ваши функции из прошлого домашнего задания в отдельный
# файл и импортируйте их в основной (исполняемый) файл.
# Запустите каждую вашу функцию по 1 или более раз в исполняемом файле.

# 2
# Анонимная функция
# Создайте анонимную функцию pow, которая принимает 2 аргумента x и y.
# Функция должна возвращать x, возведенное в степень y.

# 3
# Змея
# Создайте функцию snake_talk, которая принимает 1 аргумент text (строка).
# Функция должна создать новую строку, где все гласные буквы aeiouyAEIOUY в строке text дублируются.
# Например, такой вызовы функции snake_talk(“Harry”) должен вернуть строку “Haaryy”