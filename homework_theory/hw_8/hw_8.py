# class Profile:
#
#     BANK = 'StarBank'
#
#     def __init__(self, first_name, last_name, balance):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.balance = balance
#
#
# mike = Profile('Mike', 'McDonnell', 100)
# jack = Profile('Jack', 'Johnson', 100)
#
# print(mike.BANK)
# print(jack.BANK)


# class Numbers:
#     PI = 3.14
#     E = 2.71828
#
# print(Numbers.PI)
# print(Numbers.E)

# class Profile:
#
#     BANK = 'StarBank'
#     _counter = 0
#
#     def __init__(self, first_name, last_name, balance):
#         self.first_name = first_name
#         self.last_name = last_name
#         self._balance = balance
#
#         Profile._counter += 1
#
#         self._id = Profile._counter
#
#     def get_balance(self):
#         return self._balance
#
#     def add_money(self, amount):
#         if type(amount) == int:
#             self._balance += amount
#         else:
#             print(f'{amount} is not a number')
#
#
# mike = Profile('Mike', 'McDonnell', 100)
# jack = Profile('Jack', 'Johnson', 453)
#
# print(mike._id)
# print(jack._id)


# class Profile:
#
#     BANK = 'StarBank'
#     _counter = 0
#
#     def __init__(self, first_name, last_name, balance):
#         self.first_name = first_name
#         self.last_name = last_name
#         self._balance = balance
#
#         Profile._counter += 1
#
#         self._id = Profile._counter
#
#     def __str__(self):
#         return f'Profile: {self.first_name} {self.last_name} {self._balance}'
#
#     def get_balance(self):
#         return self._balance
#
#     def add_money(self, amount):
#         if type(amount) == int:
#             self._balance += amount
#         else:
#             print(f'{amount} is not a number')
#
#
# mike = Profile('Mike', 'McDonnell', 100)
# jack = Profile('Jack', 'Johnson', 453)
#
# print(1) # __str__
# print([1, 2, 3]) # __str__
#
# print(mike) # __str__
# print(jack) # __str__
#
# len() # __len__

# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def eat(self):
#         print(f'{self.name} ест.')
#
#     def sleep(self):
#         print(f'{self.name} спит.')
#
#     def greet(self):
#         print(f'Привет, {self.name}')
#
# class Dog(Animal):
#     def bark(self):
#         print('Гаф!')
#
# class Cat(Animal):
#     def meow(self):
#         print('Мяу!')
#
#     def eat(self):
#         print(f'Моя кошка: {self.name} ест.')
#
#
# dog = Dog('Шарик')
# cat = Cat('Чиппи')
#
# dog.eat()
# dog.sleep()
# dog.bark()
#
# cat.eat()
# cat.sleep()
# cat.meow()



# class Profile:
#
#     BANK = 'StarBank'
#
#     def __init__(self, first_name, last_name, balance):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.balance = balance
#
#     def greet(self):
#         print(f"Hello {self.first_name} {self.last_name}!")
#
#
# class PremiumProfile(Profile):
#     def __init__(self, first_name, last_name, balance, description):
#         super().__init__(first_name, last_name, balance)
#         self.description = description


# profile = Profile('Jack', 'Smith', 120000)
# profile.greet()
#
# premium_profile = PremiumProfile('Oksana', 'Smith', 100, 'Всем привет!')
# premium_profile.greet()

# Домашнее задание (Занятие 8)

# 1 Интернет-банк

# - Создайте класс BankAccount, который принимает имя владельца (name) в
# виде строки и текущее состояние счета (balance) в виде целого числа. Оба
# этих атрибута должны быть _защищенными
# - Создайте метод deposit(), который принимает 1 аргумент (если не считать
# self, конечно) amount (целое число). Метод должен увеличить текущий
# баланс аккаунта на amount.
# - Создайте метод withdraw(), который принимает 1 аргумент amount (целое
# число). Метод должен уменьшить текущий баланс аккаунта на amount. Если
# денег на счету недостаточно, то метод выводит на экран “Недостаточно
# средств!”.
# - Создайте метод get_balance(), который возвращает текущее значение
# баланса аккаунта.
# Пример:
# account = BankAccount("Maria", 1000)
# account.deposit(700)
# account.withdraw(200)
# print(account.get_balance()) # 1500

# class BankAccount:
#     def __init__(self, name, balance):
#         self._name = name
#         self._balance = balance
#
#     def deposit(self, amount):
#         self._balance += amount
#         print(f"Было + поступило: {self._balance}")
#
#     def withdraw(self, amount):
#         if amount > self._balance:
#             return('Недостаточно средств!')
#         else:
#             self._balance -= amount
#             print(f"Было + поступило - убыло: {self._balance}")
#
#     def get_balance(self):
#         return self._balance
#
#     def get_name(self):
#         return self._name

# account = BankAccount("Maria", 1000)

# print(f"У {account.get_name()} на счету:")
# account.deposit(700)         # вызываем, не печатаем return, т.к. метод сам печатает
# account.withdraw(200)        # вызываем, не печатаем return, т.к. метод сам печатает
# print(f"Текущий баланс: {account.get_balance()}") # выведет итоговый баланс


# 2 Овердрафт

# Создайте класс OverdraftAccount, унаследованный от вашего класса
# BankAccount из предыдущей задачи.
# Переопределите существующий метод withdraw(), но теперь, если баланс
# аккаунта меньше или равен 0, то это не выводит на экран сообщение
# “Недостаточно средств!”, а уменьшает баланс в минус.
# Пример:
# jack_account = OverdraftAccount("Jack", 0)
# jack_account.withdraw(100)
# jack_account.withdraw(100)
# jack_account.withdraw(100)
# print(jack_account.get_balance()) # -300

# class BankAccount:
#     def __init__(self, name, balance):
#         self._name = name
#         self._balance = balance
#
#     def deposit(self, amount):
#         self._balance += amount
#         print(f"Было + поступило: {self._balance}")
#
#     def withdraw(self, amount):
#         if amount > self._balance:
#             return('Недостаточно средств!')
#         else:
#             self._balance -= amount
#             print(f"Было + поступило - убыло: {self._balance}")
#
#     def get_balance(self):
#         return self._balance
#
#     def get_name(self):
#         return self._name
#
#
# class OverdraftAccount(BankAccount):
#     def __init__(self, name, balance):
#         super().__init__(name, balance)
#
#     def withdraw(self, amount):
#         self._balance -= amount
#         print(f"Было + поступило - убыло: {self._balance}")
#
#
# jack_account = OverdraftAccount("Jack", 0)
#
# print(f"У {jack_account.get_name()} на счету:")
# jack_account.withdraw(100)
# jack_account.withdraw(100)
# jack_account.withdraw(100)  # вызываем, не печатаем return, т.к. метод сам печатает
# print(f"Текущий баланс: {jack_account.get_balance()}") # выведет итоговый баланс

#  №3
# Есть список пользователей users, где каждый пользователь представлен словарем с ключами id, name, и age.
# Некоторые пользователи могут иметь некорректное значение для ключа name.
# Под некорректным значением понимается любой тип, который не является строкой.
# Создайте список ids, в который будут включены идентификаторы (id) тех пользователей, у которых значение по ключу name некорректно.
# Выведите список на экран.

# users = [
# {'id': 345324, 'name': 'Alice', 'age': 25},
# {'id': 1232, 'name': 123, 'age': 30},
# {'id': 7854, 'name': 'Bob', 'age': 22},
# {'id': 33412, 'name': None, 'age': 35},
# {'id': 78845, 'name': 'Charlie', 'age': 28},
# {'id': 45325, 'name': 'Eve', 'age': 40},
# {'id': 745633, 'name': True, 'age': 19},
# {'id': 64364, 'name': 'Frank', 'age': 33}
# ]

# Ответ должен быть: [1232, 33412, 745633]
#
# class User:
#     def __init__(self, user_id, name, age):
#         self.id = user_id
#         self.name = name
#         self.age = age
#
#
# class UserCollection:
#     def __init__(self, users):
#         # Принимаем список словарей и создаём список объектов User
#         self.users = [User(u['id'], u['name'], u['age']) for u in users]
#
#     def get_invalid_name_ids(self):
#         # Возвращаем список id пользователей, у которых name не является строкой
#         return [user.id for user in self.users if not isinstance(user.name, str)]
#
# users_data = [
#     {'id': 345324, 'name': 'Alice', 'age': 25},
#     {'id': 1232, 'name': 123, 'age': 30},
#     {'id': 7854, 'name': 'Bob', 'age': 22},
#     {'id': 33412, 'name': None, 'age': 35},
#     {'id': 78845, 'name': 'Charlie', 'age': 28},
#     {'id': 45325, 'name': 'Eve', 'age': 40},
#     {'id': 745633, 'name': True, 'age': 19},
#     {'id': 64364, 'name': 'Frank', 'age': 33}
# ]
#
# collection = UserCollection(users_data)
# invalid_ids = collection.get_invalid_name_ids()
# print(invalid_ids)  # [1232, 33412, 745633]

#
# users = [
#     {'id': 345324, 'name': 'Alice', 'age': 25},
#     {'id': 1232, 'name': 123, 'age': 30},
#     {'id': 7854, 'name': 'Bob', 'age': 22},
#     {'id': 33412, 'name': None, 'age': 35},
#     {'id': 78845, 'name': 'Charlie', 'age': 28},
#     {'id': 45325, 'name': 'Eve', 'age': 40},
#     {'id': 745633, 'name': True, 'age': 19},
#     {'id': 64364, 'name': 'Frank', 'age': 33}
# ]
#
# ids = [user['id'] for user in users if not isinstance(user['name'], str)]
#
# print(ids)  # Выведет: [1232, 33412, 745633]

