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

        go_to_completening_question_keyboard(update, context, command[1])
    elif command[0] == 'go_to_set_object':
        gen_set_obj_keyboard(update, context, command[1])

    elif command[0] == "go_to_completening_question":
        go_to_completening_question_keyboard(update, context, command[1])

        query.edit_message_text(text=msg, reply_markup=reply_markup)


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