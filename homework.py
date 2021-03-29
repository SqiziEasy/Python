name = input("Введите ваше имя: ")
print("Привет, " + str(name) + "!")

a = input("Нужно что-нибудь сложить. Введите первое число: ")
b = input("Теперь введите второе число для сложения: ")
sum_result = (float(a) + float(b))
print(sum_result)

a = input("Очень хочется произвести вычитание. Введите первое число: ")
b = input("А теперь вычитаемое: ")
substraction_result = (float(a) - float(b))
print(substraction_result)

a = input("Что-ж, теперь умножение. Введите первое число: ")
b = input("А теперь второе: ")
multiplication_result = (float(a) * float(b))
print(multiplication_result)

a = input("Пришло время для деления! Введите первое число: ")
b = input("Наконец, второе: ")
division_result = (float(a) / float(b))
print(division_result)

a = input("Теперь целочисленное деление. Введите первое число: ")
b = input("Теперь второе число для целочисленного деления: ")
int_division_result = (float(a) // float(b))
print(int_division_result)

a = input("Попробуем делить, но с остатком от деления. Введите первое число: ")
b = input("И снова второе число: ")
modulo_result = (float(a) % float(b))
print(modulo_result)

a = input("Наконец-то последняя операция - возведение в степень! Введите первое число: ")
b = input("И второе: ")
exponention_result = (float(a) ** float(b))
print(exponention_result)

print("Ну что, " + name + ", вот твои результаты: " + "Сложение: " + str(sum_result) + ", Вычитание: " + str(substraction_result) + ", Умножение: " + str(multiplication_result) + ", Деление: " + str(division_result) + ", Целочисленное деление: " + str(int_division_result) + ", Остаток от деления: " + str(modulo_result) + ", Возведение в степень: " + str(exponention_result)) 