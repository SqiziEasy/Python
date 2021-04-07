from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, InlineQueryHandler, CallbackQueryHandler, CommandHandler, MessageHandler, Filters
import requests
import math
import random

count_btn_inline = 3

objects = {
    "math": {
        "name": "Математика",
        "questions": [
            [ #задание 11
                {
                    "difficult": "1",
                    "question": "Из пункта A в пункт B одновременно выехали два автомобиля. Первый проехал с постоянной скоростью весь путь. Второй проехал первую половину пути со скоростью, меньшей скорости первого на 13 км/ч, а вторую половину пути – со скоростью 78 км/ч, в результате чего прибыл в пункт В одновременно с первым автомобилем. Найдите скорость первого автомобиля, если известно, что она больше 48 км/ч. Ответ дайте в км/ч.",
                    "answer": "52"
                }, 
                {
                    "difficult": "2",
                    "question": "Первая труба пропускает на 1 литр воды в минуту меньше, чем вторая. Сколько литров воды в минуту пропускает вторая труба, если резервуар объемом 110 литров она заполняет на 1 минуту быстрее, чем первая труба?",
                    "answer": "11"
                },
                {
                    "difficult": "3",
                    "question": "Из одной точки круговой трассы, длина которой равна 10 км, одновременно в одном направлении стартовали два автомобиля. Скорость первого автомобиля равна 78 км/ч, и через 40 минут после старта он опережал второй автомобиль на один круг. Найдите скорость второго автомобиля. Ответ дайте в км/ч.",
                    "answer": "63"
                }
            ],
            [ #задание 4
                {
                    "difficult": "1",
                    "question": "Конкурс исполнителей проводится в 3 дня. Всего заявлено 55 выступлений — по одному от каждой страны. Исполнитель из России участвует в конкурсе. В первый день 33 выступления, остальные распределены поровну между оставшимися днями. Порядок выступлений определяется жеребьёвкой. Какова вероятность, что выступление представителя России состоится в третий день конкурса?",
                    "answer": "0,2"
                }, 
                {
                    "difficult": "2",
                    "question": "На экзамене по геометрии школьник отвечает на один вопрос из списка экзаменационных вопросов. Вероятность того, что это вопрос на тему «Тригонометрия», равна 0,25. Вероятность того, что это вопрос на тему «Внешние углы», равна 0,1. Вопросов, которые одновременно относятся к этим двум темам, нет. Найдите вероятность того, что на экзамене школьнику достанется вопрос по одной из этих двух тем.",
                    "answer": "0,35"
                },
                {
                    "difficult": "3",
                    "question": "В классе 16 учащихся, среди них два друга — Вадим и Сергей. Учащихся случайным образом разбивают на 4 равные группы. Найдите вероятность того, что Вадим и Сергей окажутся в одной группе.",
                    "answer": "0,2"
                }
            ],
            [ #задание 1
                {
                    "difficult": "1",
                    "question": "Одного рулона обоев хватает для оклейки полосы от пола до потолка шириной 1,6 м. Сколько рулонов обоев нужно купить для оклейки прямоугольной комнаты размерами 2,3 м на 4,2 м?",
                    "answer": "9"
                }, 
                {
                    "difficult": "2",
                    "question": "На бензоколонке один литр бензина стоит 35 руб. 60 коп. Водитель залил в бак 15 литров бензина и купил бутылку воды за 23 рубля. Сколько рублей сдачи он получит с 1000 рублей?",
                    "answer": "443"
                },
                {
                    "difficult": "3",
                    "question": "В школе 800 учеников, из них 30% — ученики начальной школы. Среди учеников средней и старшей школы 20% изучают немецкий язык. Сколько учеников в школе изучают немецкий язык, если в начальной школе немецкий язык не изучается?",
                    "answer": "112"
                }
            ]
        ]
    },
    "rus": {
        "name": "Русский язык",
        "questions": [
            [
                {
                    "difficult": "1",
                    "question": "текст задания",
                    "answer": "ответ"
                }, 
                {
                    "difficult": "2",
                    "question": "текст задания",
                    "answer": "ответ"
                },
                {
                    "difficult": "3",
                    "question": "текст задания",
                    "answer": "ответ"
                }
            ],
            [
                {
                    "difficult": "1",
                    "question": "текст задания",
                    "answer": "ответ"
                }, 
                {
                    "difficult": "2",
                    "question": "текст задания",
                    "answer": "ответ"
                },
                {
                    "difficult": "3",
                    "question": "текст задания",
                    "answer": "ответ"
                }
            ],
            [
                {
                    "difficult": "1",
                    "question": "текст задания",
                    "answer": "ответ"
                }, 
                {
                    "difficult": "2",
                    "question": "текст задания",
                    "answer": "ответ"
                },
                {
                    "difficult": "3",
                    "question": "текст задания",
                    "answer": "ответ"
                }
            ]
        ]
    },
}

users = {}

def gen_set_obj_keyboard(update, context, chat_id):
    keyboard = [[] for i in range(math.ceil(len(objects) / count_btn_inline))]

    for idx, key in enumerate(objects):
        keyboard[math.floor(idx / count_btn_inline)].append(InlineKeyboardButton(objects[key]['name'], callback_data=('set_obj ' + str(key) + ' ' + str(chat_id))))

    reply_markup = InlineKeyboardMarkup(keyboard)

    context.bot.send_message(chat_id=chat_id, text="Выберите предмет", reply_markup=reply_markup)

def start(update, context):
    chat_id = update.message.chat_id

    users[chat_id] = {
        "current_object": "",
        "current_task_number": "",
        "completed_question": []
    }

    gen_set_obj_keyboard(update, context, chat_id)

def go_to_completening_question_keyboard(update, context, chat_id):

    keyboard_cmplt = [[
        InlineKeyboardButton(" Перейти к решению номера", callback_data=("go_to_completening_question" + str(chat_id)))
    ]]

    reply_markup = InlineKeyboardMarkup(keyboard_cmplt)

    context.bot.send_message(chat_id=chat_id, text="Перейти к решению задания", reply_markup=reply_markup)

    #keyboard = [[] for i in range(count_btn_inline)]
    #keyboard[0].append(InlineKeyboardButton("Перейти к решению номера", callback_data=("go_to_completening_question"  + str(chat_id))))
    #reply_markup = InlineKeyboardMarkup(keyboard)
    #random.randint(0, objects[key]["questions"].len - 1)

def button(update, context):
    query = update.callback_query

    command = query.data.split()

    print(users)


    if command[0] == 'set_obj':
        print(int(command[2]))

        users[int(command[2])]["current_object"] = command[1]

        msg = "Вы выбрали " + objects[command[1]]["name"] + " в качестве предмета для подготовки."  

        keyboard = [[] for i in range(math.ceil(len(objects[command[1]]['questions']) / count_btn_inline))]

        for idx in range(len(objects[command[1]]['questions'])):
            keyboard[math.floor(idx / count_btn_inline)].append(InlineKeyboardButton(idx + 1, callback_data=('set_n_of_task ' + str(idx) + ' ' + command[2])))

        keyboard[math.floor(idx / count_btn_inline)].append(InlineKeyboardButton("Выбрать предмет", callback_data=('go_to_set_object ' + command[2])))

        reply_markup = InlineKeyboardMarkup(keyboard)
        
        query.edit_message_text(text=msg, reply_markup=reply_markup)
    elif command[0] == 'set_n_of_task':
        users[int(command[2])]["current_task_number"] = int(command[1])

        msg = "Вы выбрали " + str(users[int(command[2])]["current_task_number"] + 1) + " в качестве номера для подготовки."  

        query.edit_message_text(text=msg)

        go_to_completening_question_keyboard(update, context, command[2])

        current_user_object = users[int(command[2])]["current_object"]

        crnt_q = random.randint(0, len(objects[current_user_object]["questions"][int(users[int(command[2])]["current_task_number"])]) - 1)

        message = objects[current_user_object]["questions"][int(users[int(command[2])]["current_task_number"])][crnt_q]["question"]

        context.bot.send_message(chat_id=command[2], text=message)

    elif command[0] == 'go_to_set_object':
        gen_set_obj_keyboard(update, context, command[1])

    elif command[0] == "go_to_completening_question":
        go_to_completening_question_keyboard(update, context, command[2])

    query.answer()


def main():
    updater = Updater('1787533409:AAHes3McJcf49B5JnbMSIIgQXJxqy8aizkg', use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()