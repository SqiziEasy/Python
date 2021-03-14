import random

print("Игра Камень, Ножницы, Бумага! Ваш противник - компьютер. Для окончания нажмите Y.")

player_win = 0
comp_win = 0
draw = 0

list = ["камень", "ножницы", "бумага"]

while True:
    comp_choice = random.choice(list)
    choice = input("Выберите знак: ")
    if choice.lower() == comp_choice:
        draw = draw + 1
        print("Ничья! Побед: " + str(player_win) + ", Ничьих: " + str(draw) + ", Поражений: " + str(comp_win))

    elif choice.lower() == "камень" and comp_choice == "бумага":
        comp_win = comp_win + 1
        print("Вы проиграли! Побед: " + str(player_win) + ", Ничьих: " + str(draw) + ", Поражений: " + str(comp_win))

    elif choice.lower() == "камень" and comp_choice == "ножницы":
        player_win = player_win + 1
        print("Вы победили! Побед: " + str(player_win) + ", Ничьих: " + str(draw) + ", Поражений: " + str(comp_win))

    elif choice.lower() == "ножницы" and comp_choice == "бумага":
        player_win = player_win + 1
        print("Вы победили! Побед: " + str(player_win) + ", Ничьих: " + str(draw) + ", Поражений: " + str(comp_win))

    elif choice.lower() == "ножницы" and comp_choice == "камень":
        comp_win = comp_win + 1
        print("Вы проиграли! Побед: " + str(player_win) + ", Ничьих: " + str(draw) + ", Поражений: " + str(comp_win))

    elif choice.lower() == "бумага" and comp_choice == "камень":
        player_win = player_win + 1
        print("Вы победили! Побед: " + str(player_win) + ", Ничьих: " + str(draw) + ", Поражений: " + str(comp_win))

    elif choice.lower() == "бумага" and comp_choice == "ножницы":
        comp_win = comp_win + 1
        print("Вы проиграли! Побед: " + str(player_win) + ", Ничьих: " + str(draw) + ", Поражений: " + str(comp_win))

    elif choice.lower() == "y":
        break

    else: 
        print("Введите правильный знак!")

print("Работа завершена. Побед: " + str(player_win) + ", Ничьих: " + str(draw) + ", Поражений: " + str(comp_win))