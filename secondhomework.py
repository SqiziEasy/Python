print ("""Калькулятор. Инструкция по использованию:
1. Написать первое число
2. Написать второе число
3. Выбрать нужную математическую операцию

Математические операции:
+ - сложение
- - вычитание
* - умножение
/ - деление
// - целочисленное деление
% - остаток от деления
** - возведение в степень
 """)

a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
mathop = input("Введите математическую операцию: ")

if mathop == "+":
    print(float(a) + float(b))
elif mathop == "-":
    print(float(a) - float(b))
elif mathop == "*":
    print(float(a) * float(b))
elif mathop == "/":
    print(float(a) / float(b))
elif mathop == "//":
    print(float(a) // float(b))
elif mathop == "%":
    print(float(a) % float(b))
elif mathop == "**":
    print(float(a) ** float(b))
else:
    print("Введите правильную математическую операцию")    



