import logging

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, InputMediaPhoto
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)
from NLUbasedRasa import(extract,getresponse)
from MovieAPI import(
    Respond,
    RespondGenres,
    RespondPoster,
    RespondPopular,
)

params={}
neg_params={}
TOKEN='1090662742:AAG23JH9Xo_rdu6QaoYssBpmK0JxTXtglYk'

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

UNDERSTAND, PROCESSING= range(2)



def start(update: Update, context: CallbackContext) -> int:
    global params
    params={}
    global neg_params
    neg_params={}
    global id
    id=""
    reply_keyboard = [['YES', 'NO']]

    update.message.reply_text(
        'Hi! I am MovieSearch Bot. I will hold a conversation with you. '
        'Send /cancel to stop talking to me,or say something same as "bye".\n\n'
        'And please type the initial word of movie name word as bigletter.\n\n'
        'Do you understand?',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )

    return UNDERSTAND


def process(update: Update, context: CallbackContext) -> int:
    global params
    global neg_params
    global id
    print(params)
    print(neg_params)
    update.message.reply_text("Robot in processing")
    intent,entities,ent_vals=extract(update.message.text)

    if (intent == "goodbye"):
        update.message.reply_text('Bye!')
        cancel(update,update.message.text)
        return ConversationHandler.END
    if (intent == "movie_search"):
        update.message.reply_text("Robot is workinnnnng!")
        logger.info("movie search of the conversation.")
        response, params, neg_params, id, imageUrl = getresponse(update.message.text, params, neg_params)
        update.message.reply_text(response)
        update.message.reply_text("And here is the poster,wait a moment...")
        try:
            update.message.reply_photo(imageUrl)
        except :
            update.message.reply_document(imageUrl)

    if (intent == "images_get"):
        update.message.reply_text("Robot is looking for images")
        logger.info("poster search of the conversation.")
        url=RespondPoster(id)
        update.message.reply_text("Here you are")
        try:
            update.message.reply_photo(url[0]["url"])
            update.message.reply_photo(url[1]["url"])
            update.message.reply_photo(url[2]["url"])
        except :
            # print(url[0])
            # print(type(url[0]))
            update.message.reply_document(url[0]["url"])
            update.message.reply_document(url[1]["url"])
            update.message.reply_document(url[2]["url"])

    if (intent == "genre_get"):
        update.message.reply_text("Robot is searching for genres")
        logger.info("poster search of the conversation.")
        genre=RespondGenres(id)
        update.message.reply_text(genre)
    return PROCESSING

def echo(update: Update, context: CallbackContext) -> None:
    global params
    params = {}
    global neg_params
    neg_params = {}
    global id
    id = ""
    """Echo the user message."""
    intent,entities,ent_vals=extract(update.message.text)
    if (intent == "greet"):
        reply_keyboard = [['YES', 'NO']]

        update.message.reply_text(
            'Hi! I am MovieSearch Bot. I will hold a conversation with you.\n\n '
            'Send /cancel to stop talking to me,or say something same as "bye".\n\n'
            'And please type the initial word of movie name word as bigletter.\n\n'
            'Do you understand?',
            reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
        )
    else:
        update.message.reply_text(
            'Hi! I am MovieSearch Bot.\n'
            'Send /start to start talking to me or say something same as "hi".\n',
        )
        return ConversationHandler.END

    return UNDERSTAND

def cancel(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text(
        'You canceled the conversation.\n'
        'I hope we can talk again next time.\n\nHUMAN')
    print(ConversationHandler.END)
    return ConversationHandler.END


def main() -> None:
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher


    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start),
                      MessageHandler(Filters.text, echo)],
        states={
            UNDERSTAND: [
                MessageHandler(Filters.regex('^(YES)$'), process),
                MessageHandler(Filters.regex('^(NO)$'), cancel)],
            PROCESSING: [MessageHandler(Filters.text, process)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )


    dispatcher.add_handler(conv_handler)
    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()