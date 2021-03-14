print("Сумматор. Начальное число = 0. Для окончания нажмите Y")

a = input("Введите число: ")
print(a)
while sum != "y":
    sum = input("Введите число: ")
    if sum.lower() == "y":
        break
    a = float(a) + float(sum)
    print("Результат суммирования: " + str(a))

print("Работа завершена. Ваш результат: " + str(a))