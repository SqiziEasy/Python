import random

print("Игра Камень, Ножницы, Бумага! Ваш противник - компьютер. Для окончания нажмите Y.")

player_win = 0
comp_win = 0
draw = 0

# 0 - камень
# 1 - ножницы
# 2 - бумага

while True:
    comp_choice = random.randint(0, 2)
    choice = input("Выберите знак: ")
    if choice.lower() == "камень" and comp_choice == 0:
        draw = draw + 1
        print("Ничья! Побед: " + str(player_win) + ", Ничьих: " + str(draw) + ", Поражений: " + str(comp_win))

    elif choice.lower() == "ножницы" and comp_choice == 1:
        draw = draw + 1
        print("Ничья! Побед: " + str(player_win) + ", Ничьих: " + str(draw) + ", Поражений: " + str(comp_win))

    elif choice.lower() == "бумага" and comp_choice == 2:
        draw = draw + 1
        print("Ничья! Побед: " + str(player_win) + ", Ничьих: " + str(draw) + ", Поражений: " + str(comp_win))

    elif choice.lower() == "камень" and comp_choice == 2:
        comp_win = comp_win + 1
        print("Вы проиграли! Побед: " + str(player_win) + ", Ничьих: " + str(draw) + ", Поражений: " + str(comp_win))

    elif choice.lower() == "камень" and comp_choice == 1:
        player_win = player_win + 1
        print("Вы победили! Побед: " + str(player_win) + ", Ничьих: " + str(draw) + ", Поражений: " + str(comp_win))

    elif choice.lower() == "ножницы" and comp_choice == 2:
        player_win = player_win + 1
        print("Вы победили! Побед: " + str(player_win) + ", Ничьих: " + str(draw) + ", Поражений: " + str(comp_win))

    elif choice.lower() == "ножницы" and comp_choice == 0:
        comp_win = comp_win + 1
        print("Вы проиграли! Побед: " + str(player_win) + ", Ничьих: " + str(draw) + ", Поражений: " + str(comp_win))

    elif choice.lower() == "бумага" and comp_choice == 0:
        player_win = player_win + 1
        print("Вы победили! Побед: " + str(player_win) + ", Ничьих: " + str(draw) + ", Поражений: " + str(comp_win))

    elif choice.lower() == "бумага" and comp_choice == 1:
        comp_win = comp_win + 1
        print("Вы проиграли! Побед: " + str(player_win) + ", Ничьих: " + str(draw) + ", Поражений: " + str(comp_win))

    elif choice.lower() == "y":
        break

    else: 
        print("Введите правильный знак!")

print("Работа завершена. Побед: " + str(player_win) + ", Ничьих: " + str(draw) + ", Поражений: " + str(comp_win))