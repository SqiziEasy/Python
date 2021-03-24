name = input("Введите ваше имя: ")
print("Привет, " + str(name) + "!")

a = input("Нужно что-нибудь сложить. Введите первое число: ")
b = input("Теперь введите второе число для сложения: ")
rezult1 = (float(a) + float(b))
print(sum_result)

a = input("Очень хочется произвести вычитание. Введите первое число: ")
b = input("А теперь вычитаемое: ")
rezult2 = (float(a) - float(b))
print(substraction_result)

a = input("Что-ж, теперь умножение. Введите первое число: ")
b = input("А теперь второе: ")
rezult3 = (float(a) * float(b))
print(multiplication_result)

a = input("Пришло время для деления! Введите первое число: ")
b = input("Наконец, второе: ")
rezult4 = (float(a) / float(b))
print(division_result)

a = input("Теперь целочисленное деление. Введите первое число: ")
b = input("Теперь второе число для целочисленного деления: ")
rezult5 = (float(a) // float(b))
print(int_division_result)

a = input("Попробуем делить, но с остатком от деления. Введите первое число: ")
b = input("И снова второе число: ")
rezult6 = (float(a) % float(b))
print(modulo_result)

a = input("Наконец-то последняя операция - возведение в степень! Введите первое число: ")
b = input("И второе: ")
rezult7 = (float(a) ** float(b))
print(exponention_result)

print("Ну что, " + name + ", вот твои результаты: " + "Сложение: " + str(sum_result) + ", Вычитание: " + str(substraction_result) + ", Умножение: " + str(multiplication_result) + ", Деление: " + str(division_result) + ", Целочисленное деление: " + str(int_division_result) + ", Остаток от деления: " + str(modulo_result) + ", Возведение в степень: " + str(exponention_result)) 