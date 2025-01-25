from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
import os
TOKEN = "8007195842:AAG2sSDJZjDu41NO0bD3PVlVTlUQKNJSFzQ"

like_count = {
    "likes": 0 
    
}
dislike_count ={
    "dislikes": 0
}


def start(update: Update, context):
    photo = open('img.jpg', 'rb')
    keyboard = [
        [InlineKeyboardButton(f"👍 {like_count}", caallback_date="like")], 
        [InlineKeyboardButton(f"👎 {dislike_count}", callback_data="dislike")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_photo(photo=photo, reply_markup=reply_markup)




updater = Updater(TOKEN)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", start))

updater.start_polling()
updater.idle()
