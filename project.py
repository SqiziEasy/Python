from telegram.ext import Updater, InlineQueryHandler, CommandHandler, MessageHandler, Filters
import requests
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

keyboard = ()

objects_btn = KeyboardButton('Начать')

keyboard.add(objects_btn)

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
    context.bot.send_message(chat_id=chat_id, text="Привет")
    users.append({
        str(chat_id): {
        "current_object": "",
        "current_task_number": "",
        "current_variant_of_task": "",
        "completed_question": []
        }
    })
    context.bot.send_message(chat_id=update.effective_chat.id, text=users)




def main():
    updater = Updater('1787533409:AAGiSxbovcVvYE4dElEfnx2dKm01Oz-BCmM')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    #adding_user_handler = MessageHandler(Filters.text & (~Filters.command), adding_user)
    #dp.add_handler(adding_user_handler)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()