# a = True
# b = False
#
# # 4 + 5 -> 9
# # 4 < 5 -> True
#
# print(4 > 3)
# print(4 < 3)
# print(4 <= 3) # False
# print(4 >= 3)
# print(4 != 3) # True
# print(4 == 3) # False
#
# print('abc' == 'Abc') # False
# print('abc' != 'abcCD')
#
# result = len('abc') # 3
# print(result)
#
# print(len('abc') == len('ccc'))
#
# print('abc'.lower() == 'Abc'.lower())
#
# print('ab' in 'abc')

# age = 30
#
# if age >= 18:
#     print('Привет')
#     print('Доступ есть!')
#
#
# print('Продолжение')

# is_admin = False
# is_manager = False
# age = 15
#
# if is_admin == True:
#     print("admin")
# elif is_manager == True:
#     print("manager")
# elif age >= 18:
#     print("Взрослый")
# else:
#     print('Кто вы?')

# result = 5 > 3 and 2 > 1 # True - True
# result = 5 < 3 or 2 < 1 # False - False -> False
#
# print(result)

# age = 25
# is_citizen = True
#
# if age >= 18 and is_citizen == True:
#     print('Вы можете голосовать')
# else:
#     print('Вы не можете голосовать')
#
# is_student = False
# age = 25
#
# if is_student == True or age >= 65:
#     print('Вам положена скидка')
# else:
#     print('Скидки не будет :(')
#
# is_admin = False
#
# # not is_admin -> not False -> True
#
# if not is_admin:
#     print('Вы не админ')

# print((a and b) or is_admin)

# print((1 + 1) * (5 / (6 / 2)))

# not
# and
# or

# is_admin = True
#
# if is_admin:
#     print('Вы админ!')

# 1, 45, -2, "abc", True, 3.14, ...   -> True
# 0, None, False, "", ...

# a = False
#
# if a:
#     print("is true")

# count = 0
#
# if count:
#     print(f"У вас есть деньги! {count}")
# else:
#     print("У вас нет денег :(")

# age = 25
# is_ban = True
#
# if age >= 18 and not is_ban:
#     print('У вас есть доступ!')
# else:
#     print('Доступа нет!')

# print("hello world")
# print("hello world")
# print("hello world")
# print("hello world")
# print("hello world")
# print("hello world")
# print("hello world")
# print("hello world")
# print("hello world")
# print("hello world")

# range(), "abc"
# 1, True, None, ...

# for i in range(10): # 0, 1, 2, 3 ... 9
#     i = i + 1
#     print(i)

# count = 0
#
# for c in "Hello":
#     print(c)
#     if c == 'l':
#         print('Мы нашли l!')
#         count = count + 1
#     else:
#         print('Это не l!')
#
# print(count)

# for i in range(30):
#     if i == 14:
#         continue
#     print(i)

# password = "12324Hfnd"
# is_valid = True
#
# # "*" in "*()-+" -> False
#
# for c in password:
#     print(c)
#     if c in "*()-+": # True
#         is_valid = False
#         break
#
# if is_valid:
#     print("Password is valid")
# else:
#     print("Password is not valid")

# for i in range(10):
#     print(i)
#
# for c in "Hello":
#     print(c)
#
# for _ in range(25):
#     print("hey")

# n = 10
#
# while True:
#     print(n)
#     n = n - 1
#
#     if n == 5:
#         break

# while True:
#     message = input("Enter a message: ")
#
#     if message == "quit":
#         break
#
#     print(message)
#
# print("Thank you!")

# day = str(input("Сегодня день: "))
#
# if day == "Суббота" or day == "Воскресенье":
#     print("Сегодня выходной!")
# elif day == "Среда":
#     print("Мне сегодня к стоматологу в 15:30")
# else:
#     print("Сегодня обычный день")

# day = (input("Сегодня день: ")
# title_day = day.title()
# if title_day == "Суббота" or title_day == "Воскресенье":
#     print("Сегодня выходной!")
# elif title_day == "Среда":
#     print("Мне сегодня к стоматологу в 15:30")
# elif (
#     title_day == "Понедельник"
#     or title_day == "Вторник"
#     or title_day == "Четверг"
#     or title_day == "Пятница"
# ):
#     print("Сегодня обычный день")
# else:
#     print("Это не день недели!")

count = 0

while True:
    a = int(input("Введите целое число: "))
    if a < 0:
        break
    count = count + a  # count += a (тоже самое)

print("Сумма всех введенных чисел (без отрицательного):", count)
