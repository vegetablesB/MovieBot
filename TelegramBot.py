import logging

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)

TOKEN='1090662742:AAG23JH9Xo_rdu6QaoYssBpmK0JxTXtglYk'

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

UNDERSTAND, PROCESSING= range(2)


def start(update: Update, context: CallbackContext) -> int:
    reply_keyboard = [['YES', 'NO']]

    update.message.reply_text(
        'Hi! My name is Professor Bot. I will hold a conversation with you. '
        'Send /cancel to stop talking to me.\n\n'
        'Do you understand?',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )

    return UNDERSTAND


def process(update: Update, context: CallbackContext) -> int:
    if (update.message.text == "bye"):
        update.message.reply_text(
            'Bye!.')
        cancel(update,update.message.text)
        return ConversationHandler.END

        # cancel1(update, update.message.text)
        # return ConversationHandler.END



    return PROCESSING



def cancel(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text(
        'you canceled the conversation.\n'
        'Bye! I hope we can talk again next time.')
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
        entry_points=[CommandHandler('start', start)],
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