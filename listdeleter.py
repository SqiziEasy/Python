import random

print("""Программа создаст два списка со случайными значениями, списки будут продемонстривованы.
При наличии совпадений, они будут удалены из первого списка.""")

first_list = []
second_list = []
n = 0

while n != 20:
    number_first = random.randint(0, 25)
    number_second = random.randint(0, 25)
    n = n + 1
    first_list.append(number_first)
    second_list.append(number_second)

print("Первый список: " + str(first_list) + """
Второй список: """ + str(second_list))

for coincidence in second_list:
    if coincidence in first_list:
        first_list.remove(coincidence)

print("Итоговый список: " + str(first_list))

