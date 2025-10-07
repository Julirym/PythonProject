# №1
# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#
#     def info(self):
#         print(f"Книга: {self.title}, Автор: {self.author}, Страниц: {self.pages}")
#
# # Создаем экземпляр класса Book
# book = Book("Book", "Kook", 20)
#
# # Выводим информацию о книге
# book.info()

# №2
# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
#
#     def deposit(self, amount):
#         self.balance += amount  # обновляем баланс
#         print(f"Пополнено: {amount}")
#
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount  # обновляем баланс
#             print(f"Снято: {amount}")
#         else:
#             print("Недостаточно средств для снятия")
#
#     def get_balance(self):
#         return self.balance
#
# # Создаем экземпляр
# bank = BankAccount("Lola", 200)
#
# # Вызываем методы у экземпляра
# bank.deposit(10)
# bank.withdraw(20)
#
# # Проверяем баланс
# print(f"Баланс: {bank.get_balance()}")

# №3
#
# class Student:
#     def __init__(self, name, grades):
#         self.name = name
#         self.grades = grades
#
#     def add_grade(self, grade):
#             self.grades.append(grade)
#
#     def average(self):
#             return sum(self.grades) / len(self.grades)
#
# #Создаем экземпляр
# score = Student("Lola", [0, 2, 10, 8, 3])
#
# #Вызываем методы у экземпляра
# score.add_grade(1)
# score.average()
#
# print(f"Средний бал: {score.average()}")

# №4
# class Calculator:
#     def __init__(self):
#         self.value = 0
#
#     def add(self, x):
#         self.value += x
#         print(self.value)
#
#     def sub(self, x):
#         self.value -= x
#         print(self.value)
#
#     def mul(self, x):
#         self.value *= x
#         print(self.value)
#
#     def div(self, x):
#         if x == 0:
#             print('No zero')
#         else:
#             self.value /= x
#             print(self.value)
#
#     def show(self):
#         print(self.value)
#
# #Создаем экземпляр
# integ = Calculator()
#
# #Вызываем методы у экземпляра
# integ.add(50)
# integ.sub(25)
# integ.mul(3)
# integ.div(0)
# integ.show()

# №5
# class Glosery:
#     def __init__(self, items):
#         self.items = items
#
#     def add_item(self, item):
#         self.items.append(item)
#
#     def remove_item(self, item):
#         self.items.remove(item)
#
#     def show_items(self):
#         print(self.items)
#
# books = Glosery(["Пила", "Лейка", "Цветы", "Куртка", "Сок", "Зубы"])
# books.add_item("Шарф")
# books.remove_item("Зубы")
# books.show_items()

# class TrafficLight:
#     def __init__(self):
#         self.color = "red"
#
#     def switch(self):
#         if self.color == 'red':
#             self.color = 'yellow'
#         elif self.color == 'yellow':
#             self.color = 'green'
#         else:
#             self.color = 'red'
#
#     def show(self):
#         print(self.color)
#
# traffic_light = TrafficLight()
#
# traffic_light.switch()
# print(traffic_light.color)  # yellow
#
# traffic_light.switch()
# print(traffic_light.color)  # green
#
# traffic_light.switch()
# print(traffic_light.color)  # red
#
# traffic_light.switch()
# print(traffic_light.color)  # yellow
#
# traffic_light.switch()
# print(traffic_light.color)  # green
#
# traffic_light.switch()
# print(traffic_light.color)  # red

class Lamp:
    def __init__(self, is_on):
        self.is_on = is_on

    def turn_on(self):
        if self.is_on:


    def turn_off(self):

    def toggle(self):

    def status(self):
        print()


