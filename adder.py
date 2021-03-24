print("Сумматор. Начальное число = 0. Для окончания нажмите Y")

a = 0
a = input("Введите число: ")
print(a)
while True:
    sum = input("Введите число: ")
    if sum.lower() == "y":
       break
    a = float(a) + float(sum)
    print("Результат суммирования: " + str(a))

print("Работа завершена. Ваш результат: " + str(a))