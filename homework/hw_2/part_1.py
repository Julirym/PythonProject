# n = int(input("Число: "))
#
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")
#
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")


day = str(input("Сегодня день: "))
title_day = day.title()
if title_day == "Суббота" or title_day == "Воскресенье":
    print("Сегодня выходной!")
elif title_day == "Среда":
    print("Мне сегодня к стоматологу в 15:30")
elif (
    title_day == "Понедельник"
    or title_day == "Вторник"
    or title_day == "Четверг"
    or title_day == "Пятница"
):
    print("Сегодня обычный день")
else:
    print("Это не день недели!")
