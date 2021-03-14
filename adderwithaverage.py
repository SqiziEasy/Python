print("Сумматор. Начальное число = 0. Для окончания нажмите Y. После окончания работы произойдет вывод среднефого арифметического всех сумм.")

a = 0
n = 0
num_average = 0

while sum != "y":
    sum = input("Введите число: ")
    if sum.lower() == "y":
        break
    a = float(a) + float(sum)
    n = float(n) + 1
    num_average = float(num_average) + float(sum)
    print("Результат суммирования: " + str(a))

sum_average = float(num_average) / float(n)

print("Работа завершена. Ваш результат: " + str(a) + " Среднее арифметическое сумм: " + str(sum_average))