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
math_op = input("Введите математическую операцию: ")

if math_op == "+":
    print(float(a) + float(b))

elif math_op == "-":
    print(float(a) - float(b))

elif math_op == "*":
    print(float(a) * float(b))

elif math_op == "/":

    if a or b == 0:
        print("На ноль делить нельзя!")
    else:
        print(float(a) / float(b))

elif math_op == "//":

    if a or b == 0:
        print("На ноль делить нельзя!")
    else:
        print(float(a) // float(b))

elif math_op == "%":

    if a or b == 0:
        print("На ноль делить нельзя!")
    else:
        print(float(a) % float(b))

elif math_op == "**":
    print(float(a) ** float(b))

else:
    print("Введите правильную математическую операцию")    



