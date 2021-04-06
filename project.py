from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, InlineQueryHandler, CallbackQueryHandler, CommandHandler, MessageHandler, Filters
import requests
import math

count_btn_inline = 3

objects = [{
    "math": [
    {  
        "1": [
        {
            "variants_of_task": [
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
            }]
        }]
    },
    {
        "2": [
        {
            "variants_of_task": [
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
            }]
        }]
    },
    {
       "3": [
        {
            "variants_of_task": [
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
            }]
        }] 
    }]
},
{
    "rus": [
    {  
        "1": [
        {
            "variants_of_task": [
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
            }]
        }]
    },
    {
        "2": [
        {
            "variants_of_task": [
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
            }]
        }]
    },
    {
       "3": [
        {
            "variants_of_task": [
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
            }]
        }] 
    }]
}]

users = []

def start(update, context):
    chat_id = update.message.chat_id

    users.append({
        str(chat_id): {
        "current_object": "",
        "current_task_number": "",
        "current_variant_of_task": "",
        "completed_question": []
        }
    })

    keyboard = [[] for i in range(math.ceil(len(objects) / count_btn_inline))]

    for idx, key in enumerate(objects):
        keyboard[math.floor(idx / count_btn_inline)].append(InlineKeyboardButton(users[0][str(chat_id)]["current_object"], callback_data=('set_obj ' + str(key))))

    reply_markup = InlineKeyboardMarkup(keyboard)

    context.bot.send_message(chat_id=chat_id, text="Выберите предмет", reply_markup=reply_markup)



def button(update, context):
    query = update.callback_query

    command = query.data.split()

    if command[0] == 'set_obj':
        users[0][str(chat_id)]["current_object"] = command[1]

        msg = "Вы выбрали " + users[0][str(chat_id)]["current_object"] + " в качестве предмета для подготовки."  

        query.edit_message_text(text=msg)

    query.answer()

    elif command[0] == 'set_n_of_task':
        users[0][str(chat_id)]["current_task_number"] = command[1]

        msg = "Вы выбрали " + users[0][str(chat_id)]["current_task_number"] + " в качестве номера для подготовки."  

        query.edit_message_text(text=msg)

    query.answer()



#def echo(update, context):
#    chat_id = update.message.chat_id
#    if update.message.text == "Выбери предмет математика":
#        users[0][str(chat_id)]["current_object"] = "math"
#        context.bot.send_message(chat_id=update.effective_chat.id, text=users)
#    elif update.message.text == "Выбери предмет русский":
#        users[0][str(chat_id)]["current_object"] = "rus"
#        context.bot.send_message(chat_id=update.effective_chat.id, text=users)
#    elif update.message.text == "Выбери номер 1":
#        users[0][str(chat_id)]["current_task_number"] = "1"
#    elif update.message.text == "Выбери номер 2":
#       users[0][str(chat_id)]["current_task_number"] = "2"
#    elif update.message.text == "Выбери номер 3":
#        users[0][str(chat_id)]["current_task_number"] = "3"





def main():
    updater = Updater('1787533409:AAGiSxbovcVvYE4dElEfnx2dKm01Oz-BCmM', use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))

    dp.add_handler(CallbackQueryHandler(button))
    #dp.add_handler(MessageHandler(Filters.text & (~Filters.command), echo))
    #dp.add_handler(adding_user_handler)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()