import random

print("""Высчитывание списков. Задайте длину списка, в него будут добавлены случайные целые числа от 1 до 10000
Список будет показан, также будет высчитано среднее арифметическое и сумма списка
Для суммирования при помощи while введите W
Для суммирования при помощи for введите F""")

list = []
index = 0
sum = 0
sum_average = 0

while True:
    n = input("Введите нужную длину списка: ")

    if n == "":
        print("Введите число!")

    elif int(n) > 0:
        break

    elif int(n) <= 0:
        print("Введите число больше нуля!")

while True:
    choiсe = input("Введите способ суммирования: ")

    if choiсe.lower() == "w":

        method = "цикл while"
        while index != int(n):
            list_number = random.randint(1, 10000)
            index = index + 1
            list.append(list_number)
            sum = sum + list_number
        break

    elif choiсe.lower() == "f":

        method = "цикл for"
        while index != int(n):
            list_number = random.randint(1, 10000)
            index = index + 1
            list.append(list_number)
        for i in list:
            sum = sum + i
        break

    else:
        print("Введите правильную комманду!")

for i in list:
    sum_average = sum / int(n)

print("Список: " + str(list) + """
Метод: """ + method + """
Сумма всех чисел списка: """ + str(sum) + """
Среднее арифметическое всех чисел списка: """ + str(sum_average))


