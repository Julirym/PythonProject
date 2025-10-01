# class User:  #классы называются с большой буквы
#     pass     #не делай ничего

# user = User()
# user2 = User()
#
# user.name = 'Oksana'
# user.age = 30
#
# user2.name = 'Mike'
# user2.age = 25
#
#
# print(user.name, user.age)
# print(user2.name, user2.age)


# class User:
#     def __init__(self, name, age, country='USA'):
#         self.name = name
#         self.age = age
#         self.country = country
#
#
# user = User('Oksana', 24)
# user2 = User('Mike', 25)
# user3 = User('Jack', 40)
#
# print(user.name, user.age, user.country)
# print(user2.name, user2.age, user2.country)
# print(user3.name, user3.age, user3.country)

#
# class User:
#     def __init__(self, name, age, description=None):
#         self.name = name
#         self.age = age
#         self.description = description
#
#     def say_hello(self):
#         print(f"Hello, {self.name}!")
#
#     def get_info(self):
#         return f"User: {self.name} {self.age}"
#
#     def set_description(self, new_description):
#         self.description = new_description
#
#
# from tools import User
#
#
# user = User("Oksana", 24)
# user.get_info()


'''
Домашнее задание (Занятие 7)

1  Прямоугольник
Создайте класс Rectangle, который принимает ширину и высоту прямоугольника при создании и должен иметь соответствующие атрибуты width и height (целые числа).
Создайте метод area(), который возвращает площадь прямоугольника.
Создайте метод perimeter(), который возвращает периметр прямоугольника.
Пример:
rect = Rectangle(2, 4)
a = rect.area() # Вернул 8
p = rect.perimeter() # Вернул 12

2  Автомобиль
Создайте класс Car, который принимает марку автомобиля (make) в виде строки и максимально возможную скорость (max_speed) в виде целого числа при создании. Также при инициализации (в теле __init__) экземпляра Car должен быть автоматически создан атрибут speed, равный 0 (текущая скорость автомобиля).
Создайте метод display_speed(), который выводит в консоль текущую скорость автомобиля.
Создайте метод accelerate(), который увеличивает скорость автомобиля на 10, при этом скорость автомобиля не должна превышать max_speed, если вызывается accelerate() при максимальной скорости, то скорость не должна увеличиваться.
Создайте метод brake(), который уменьшает скорость автомобиля на 10, при этом скорость автомобиля не может быть меньше 0. Если вызывается метод brake() при скорости равной 0, то скорость не должна уменьшаться.

Пример:
my_toyota = Car("Toyota", 180)
my_toyota.accelerate()
my_toyota.accelerate()
my_toyota.accelerate()
my_toyota.display_speed() # вывел в консоль 3
'''

# 1  Прямоугольник
# Создайте класс Rectangle, который принимает ширину и высоту прямоугольника при создании и должен иметь соответствующие атрибуты width и height (целые числа).
# Создайте метод area(), который возвращает площадь прямоугольника.
# Создайте метод perimeter(), который возвращает периметр прямоугольника.
# Пример:
# rect = Rectangle(2, 4)
# a = rect.area() # Вернул 8
# p = rect.perimeter() # Вернул 12

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
# rect = Rectangle(2, 4)
#
# p = (rect.width + rect.height) *2
# a = rect.width * rect.height
#
# print(a)
# print(p)

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#
# rect = Rectangle(2, 4)
#
# print(rect.area())
# print(rect.perimeter())

'''
2  Автомобиль
Создайте класс Car, который принимает марку автомобиля (make) в виде строки и максимально возможную скорость (max_speed) в виде целого числа при создании. 
Также при инициализации (в теле __init__) экземпляра Car должен быть автоматически создан атрибут speed, равный 0 (текущая скорость автомобиля).
Создайте метод display_speed(), который выводит в консоль текущую скорость автомобиля.
Создайте метод accelerate(), который увеличивает скорость автомобиля на 10, при этом скорость автомобиля не должна превышать max_speed, если вызывается accelerate() при максимальной скорости, то скорость не должна увеличиваться.
Создайте метод brake(), который уменьшает скорость автомобиля на 10, при этом скорость автомобиля не может быть меньше 0. Если вызывается метод brake() при скорости равной 0, то скорость не должна уменьшаться.

Пример:
my_toyota = Car("Toyota", 180)
my_toyota.accelerate()
my_toyota.accelerate()
my_toyota.accelerate()
my_toyota.display_speed() # вывел в консоль 3
'''

class Car:
    def __init__(self, make, max_speed, speed = 0):
        self.make = make
        self.max_speed = max_speed
        self.speed = speed


    def display_speed():
        return

    def accelerate():

    def brake():

my_toyota = Car("Toyota", 180)
my_toyota.accelerate()