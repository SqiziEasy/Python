name = input("Введите ваше имя: ")
print("Привет, " + str(name) + "!")

chislo1 = input("Нужно что-нибудь сложить. Введите первое число: ")
chislo2 = input("Теперь введите второе число для сложения: ")
rezult1 = (float(chislo1) + float(chislo2))
print(rezult1)

chislo3 = input("Очень хочется произвести вычитание. Введите первое число: ")
chislo4 = input("А теперь вычитаемое: ")
rezult2 = (float(chislo3) - float(chislo4))
print(rezult2)

chislo5 = input("Что-ж, теперь умножение. Введите первое число: ")
chislo6 = input("А теперь второе: ")
rezult3 = (float(chislo5) * float(chislo6))
print(rezult3)

chislo7 = input("Пришло время для деления! Введите первое число: ")
chislo8 = input("Наконец, второе: ")
rezult4 = (float(chislo7) / float(chislo8))
print(rezult4)

chislo9 = input("Теперь целочисленное деление. Введите первое число: ")
chislo10 = input("Теперь второе число для целочисленного деления: ")
rezult5 = (float(chislo9) // float(chislo10))
print(rezult5)

chislo11 = input("Попробуем делить, но с остатком от деления. Введите первое число: ")
chislo12 = input("И снова второе число: ")
rezult6 = (float(chislo11) % float(chislo12))
print(rezult6)

chislo13 = input("Наконец-то последняя операция - возведение в степень! Введите первое число: ")
chislo14 = input("И второе: ")
rezult7 = (float(chislo13) ** float(chislo14))
print(rezult7)

print("Ну что, " + name + ", вот твои результаты: " + "Сложение: " + str(rezult1) + ", Вычитание: " + str(rezult2) + ", Умножение: " + str(rezult3) + ", Деление: " + str(rezult4) + ", Целочисленное деление: " + str(rezult5) + ", Остаток от деления: " + str(rezult6) + ", Возведение в степень: " + str(rezult7)) 