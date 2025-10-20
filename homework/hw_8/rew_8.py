# Создай класс Person с атрибутами name и age и методом introduce(), который выводит: Привет, меня зовут <name>, мне <age> лет.
# Создай класс-наследник Student, который добавляет атрибут school и переопределяет метод introduce(), чтобы добавить информацию о школе.
# Пример: Привет, меня зовут Аня, мне 15 лет, я учусь в школе №123

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def introduce(self):
#         print(f"Меня зовут {self.name}, мне {self.age} лет")
# class Student(Person):
#     def __init__(self, name, age, school):
#         self.school = school
#         self.name = name
#         self.age = age
#     def introduce(self):
#         print(f"Меня зовут {self.name}, мне {self.age} лет, я учусь в школе {self.school}")
#
# student_account = Student("Аня", 15, "№123")
# student_account.introduce()  # вызываем, не печатаем return, т.к. метод сам печатает

Создайте класс Person с приватным атрибутом _age.
Сделайте геттер и сеттер для age: если в age присваивают число < 0, автоматически ставьте 0; если > 120, автоматически поставьте 120.

