# ZeroDivisionError

# a = 1 / 0

# IndexError
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# print(numbers[10])

# raise ValueError("Возникла ошибка!")

# class FirstNameError(Exception):
#     pass
#
#
# def greet(name):
#     if not isinstance(name, str):
#         raise TypeError('name должен быть строкой!')
#
#     if not name.isalpha():
#         raise FirstNameError(f'{name} - плохое имя!')
#
#     print(f"Hello, {name}!")
#
#
# greet("Hello123")


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# print(numbers[100])

# try:
#     # 1 / 0 # ZeroDivisionError
#     numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
#     print(numbers[100])
# except IndexError:
#     print('Возникла ошибка!')
# except ZeroDivisionError:
#     print('На ноль делить нельзя!!')
#
#
# print('Что-то делаем дальше!')

# w, r, a, ...

# with open('my_text.txt', 'w', encoding='utf-8') as file:
#     file.write('Hello World')
#
# with open('my_text.txt', 'a', encoding='utf-8') as file:
#     file.write('Hello World\n')
#
# with open('my_text.txt', 'r', encoding='utf-8') as file:
#     print(file.read())
#
#
# print('Что-то делаем дальше!')

# with open('text.txt', 'a', encoding='utf-8') as file:
#     while True:
#         message = input('Enter a message: ')
#
#         if message == 'q':
#             break
#
#         file.write(f"{message}\n")

# import json
#
# data = {
#     'number': 100,
#     'objects': [123, True, '123']
# }
#
# with open('data.json', 'w', encoding='utf-8') as file:
#     json.dump(data, file, indent=4)
#
# with open('data.json', 'r', encoding='utf-8') as file:
#     file_data = json.load(file)
#
#     print(file_data)
