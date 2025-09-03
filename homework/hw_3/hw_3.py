count = 0

while True:
    a = int(input("Введите целое число: "))
    if a < 0:
        break
    count = count + a  # count += a (тоже самое)

print("Сумма всех введенных чисел (без отрицательного):", count)
