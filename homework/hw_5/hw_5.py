# def greet(name):
#     print("*****")
#     print(f"Hello! {name}!")
#     print("*****")
#
#
# greet("Оксана")
# greet("Леша")
# greet("Леша")
# greet("Саша")
# greet(123)
from homework.hw_4.hw_4 import total


# def greet(name="Гость"):
#     print("*****")
#     print(f"Hello! {name}!")
#     print("*****")
#
#
# greet()
# greet("Oksana")
#
# def greet(name, surname):
#     print("*****")
#     print(f"Hello! {name} {surname}!")
#     print("*****")
#
#
# greet(surname="Smith", name="Oksana")
# greet("Oksana", "Smith")

# def greet(surname, name="231"):
#     print("*****")
#     print(f"Hello! {name} {surname}!")
#     print("*****")
#
#
# greet("Oksana")

# def my_function(a, b, *args):
#     print(args)
#
#
# my_function(1, 2, 3, 4, 5, 6)
#
#
# def my_function(**kwargs):
#     print(kwargs)
#
#
# my_function(a=10, b=20)

# def sub(a, b):
#     result = a - b
# return result
#
# a = sub(3, 4) # None
#
# print(a + 3)
#
#
# def add(a, b):
#     result = a + b
#
#     return result
#
# b = add(2, 2) # 4
#
# print(b + 3) # 7
#
#
#
# def my_function(a):
#     if a % 2 == 0:
#         return a * 2
#     else:
#         return a * 3
#
# print(my_function(1))

# b = 2
#
# def add(a):
#     b = 10
#
#     result = a + b
#
#     return result
#
#
# print(add(1))

# message = "Глобальная"
#
# def function():
#     message = "Локальная"
#
#     print(message)
#
# function()
# print(message)

# a = 1
#
# def function():
#     global a
#     a += 1
#
#     print(a)
#
# function()
# print(a)


# def add(a: int, b: int) -> int:
#     """
#     Суммирует 2 числа.
#
#     :param a: Первое число (int)
#     :param b: Второе число (int)
#     :return: Сумма этих двух чисел (int)
#     """
#
#     return a + b
#
# print(add(1,2))


# Продвинутый sum.
# Встроенная функция sum() в python вызывает ошибку, если один из элементов последовательности не является числом, например sum([1, 2, ‘A’]).
# Напишите функцию sum_ignore_non_numbers(), которая имеет один параметр items (список или кортеж).
# Функция должна вернуть сумму всех чисел (int, float) в переданной последовательности. При этом все нечисловые значения должны игнорироваться.
# Если чисел нет, то функция должна вернуть 0.
# Если вызвать функцию со списком [1, 2, 'Hey', None, 4.3], то она должна вернуть 7.3


# def sum_ignore_non_numbers(items):
#     total = 0
#     for i in items:
#         if isinstance (i, (int, float)):
#             total += i
#     return total
#
# items = [1, 2, 'Hey', None, 4.3]
#
# print(sum_ignore_non_numbers(items))

# Треугольник.
# Треугольник возможен, если сумма любых двух его сторон больше длины третьей стороны.
# Напишите функцию is_triangle(), которая имеет 3 параметра - длины сторон треугольника.
# Функция должна возвращать True, если треугольник с переданными сторонами может существовать, и False в противном случае.
# Для is_triangle(2, 4, 9) правильный ответ - False, для is_triangle(3, 4, 5) - True.

# №1
# def is_triangle(a, b, c):
#     if a + b > c and a + c > b and b + c > a:
#         return True
#     else:
#         return False

# is_triangle(2, 4, 9)

# print(is_triangle(2, 4, 9))

# №2
# def is_triangle(a, b, c):
#     if a + b > c and a + c > b and b + c > a:
#         return True
#     else:
#         return False

# is_triangle(3, 4, 5)

# print(is_triangle(3, 4, 5))

# Среднее значение.
# Напишите функцию average(), которая принимает произвольное количество позиционных аргументов. (Можно передать любое число аргументов).
# Функция должна посчитать среднее арифметическое всех переданных чисел. (Представим, что в функцию передаются только числа).
# Если не передать ни одного аргумента, то функция должна вернуть 0.
#
# Такой вызова функции average(1, 2, 3, 4, 5, 6, 7, 8) должен вернуть 4.5

# def average(*args):
#     if not args:
#         return 0
#     return sum((args)) / len((args))
#
# result = average(1, 2, 3, 4, 5, 6, 7, 8)
#
# print(result)

# Общие строки.
# Напишите функцию common_strings(), которая имеет 3 параметра: list1, list2 и ingore_case=True (значение по умолчанию).
# Функция должна вернуть новый список из тех значений, которые встречаются в обоих списках.
# При этом, если ignore_case равен True, функция должна игнорировать регистр и считать строки “string” и “STRING” одинаковыми.
# В противном случае функция должна учитывать регистр символов и считать такие строки разными.
# Все строки в результирующем списке должны быть в нижнем регистре.
# Например, существуют 2 списка:
# fruits_1 = [‘banana’, ‘APPLE’, ‘watermelon’, ‘cherry’]
# fruits_2 = [‘Mango’, ‘apple’, ‘orange’, ‘cherry’]
# То вызов функции common_strings(fruits_1, fruits_2) должен вернуть [‘apple’, ‘cherry’].

list = []
def common_strings(fruits_1, fruits_2, ingore_case=True):
    for i in range(len(fruits_1),len(fruits_2)):
    if ingore_case == True:
        fruits_1 = fruits_1.lower()
        fruits_2 = fruits_2.lower()
    else:
        fruits_1 = fruits_1.lower()


fruits_1 = ['banana', 'APPLE', 'watermelon', 'cherry']
fruits_2 = ['Mango', 'apple', 'orange', 'cherry']

print(common_strings(fruits_1, fruits_2))

# keys = ['name', 'age', 'city', 'occupation', 'email', 'phone', 'hobby', 'education', 'company', 'salary']
# values = ['Alice', 30, 'New York', 'Engineer', 'alice@example.com', '+1234567890', 'Reading', 'Masters in Computer Science', 'TechCorp', 90000]

# info = {}

# for i in range(len(keys)):
#     info[keys[i]] = values[i]

# print(info)

# def sum_ignore_non_numbers(items):
#     total = 0
#     for i in items:
#         if isinstance (i, (int, float)):
#             total += i
#     return total

# items = [1, 2, 'Hey', None, 4.3]

# print(sum_ignore_non_numbers(items))