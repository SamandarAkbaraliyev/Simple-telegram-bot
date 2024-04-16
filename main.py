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

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)
MENU = "🍴 Menyu"
BASKET = "📥 Savat"
LOCATION = "KAFE LOKATSIYASI"
ABOUT_ORDER = "🚀 Buyurtma haqida"
FEEDBACK = "✍️ Fikr bildirish"
CONTACT = "☎️ Kontaktlar"
SETTINGS = "⚙️ Sozlamalar"
MAIN_MENU = "🏠 Bosh menu"
MAIN_KEYBOARD = [
    [
        MENU,
        BASKET,
    ],
    [LOCATION, ABOUT_ORDER],
    [FEEDBACK, CONTACT],
    [SETTINGS]
]

(FIKR_BILDIRISH,) = range(1)


def start(update: Update, context: CallbackContext) -> int:
    """Starts the conversation and asks the user about their gender."""

    update.message.reply_text(
        "Kerakli bo'limni tanlang",
        reply_markup=ReplyKeyboardMarkup(
            MAIN_KEYBOARD,
            one_time_keyboard=False,
            input_field_placeholder="Quyidagilardan birini tanlang",
        ),
    )


def menu(update: Update, context: CallbackContext) -> int:
    keyboard = [
        [BASKET],
        ['Pasta', "Qo'shimchalar"],
        ['Salatlar', "🆕 Taomlar"],
        ['Sovuq ichimliklar', '🆕 Tomato seti'],
        ['2 Kishilik set', '🆕 Ravioli ikki kishilik'],
        ['🔥 Kombo 4 kishilik', '🤩KIDS MENU'],
        [MAIN_MENU]
    ]

    update.message.reply_text(
        """Quyidagilardan birini tanlang""",
        reply_markup=ReplyKeyboardMarkup(
            keyboard,
            one_time_keyboard=False,
            input_field_placeholder="Quyidagilardan birini tanlang",
        ),
    )


def basket(update: Update, context: CallbackContext):
    update.message.reply_text(
        """Sizning savatingiz bo'sh""")


def location(update: Update, context: CallbackContext) -> int:
    update.message.reply_location(latitude=41.312082, longitude=69.292853)

    update.message.reply_text(
        """🤩 Pastani kafeimizga kelib to'g'ridan-to'g'ri skovorodkadan ta'tib ko'ring - aynan shu uchun ham shaharning markazida joy ochdik, manzil Ц-1'da Ecopark va 64 maktab yonida

📌 Ish tartibi: du - pa 11:00 - 23:00 / ju 14:00 - 23:00 / sha - yak 11:00 - 23:00

Operator bilan aloqa 👉 @pastarobot""",
        reply_markup=ReplyKeyboardMarkup(
            MAIN_KEYBOARD,
            one_time_keyboard=False,
            input_field_placeholder="Quyidagilardan birini tanlang",
        ),
    )


def about_order(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        """🇮🇹 Italiyani yetkazib berish!
🍝 Italiyancha pasta korobochkalarda!
⏰ С 11:00 до 01:00 
🛵 Hoziroq buyurtma bering!

*Ob havo va yo'l tirbandliklar sababli yetkazish narxi o'zgarishi mumkin""",
        reply_markup=ReplyKeyboardMarkup(
            MAIN_KEYBOARD,
            one_time_keyboard=False,
            input_field_placeholder="Quyidagilardan birini tanlang",
        ),
    )


def feedback(update: Update, context: CallbackContext) -> int:
    keyboard = [
        ['😊Hammasi yoqdi ❤️'],
        ['☺️Yaxshi ⭐️⭐️⭐️⭐️'],
        ['😐 Yoqmadi ⭐️⭐️⭐️'],
        ['☹️ Yomon ⭐️⭐️'],
        ['😤 Juda yomon👎🏻'],
        [MAIN_MENU]
    ]
    update.message.reply_text(
        """Quyidagilardan birini tanlang""",
        reply_markup=ReplyKeyboardMarkup(
            keyboard,
            one_time_keyboard=False,
            input_field_placeholder="Quyidagilardan birini tanlang",

        ),
    )
    return FIKR_BILDIRISH


def marking(update: Update, context: CallbackContext):
    update.message.reply_text(
        """Bahoyingiz uchun raxmat""",
        reply_markup=ReplyKeyboardMarkup(
            MAIN_KEYBOARD,
            one_time_keyboard=False,
            input_field_placeholder="Quyidagilardan birini tanlang",
        )
    )
    return ConversationHandler.END


def contact(update: Update, context: CallbackContext):
    update.message.reply_text(
        """Buyurtma va boshqa savollar bo'yicha javob olish uchun 
@pastarobot'ga murojaat qiling, barchasiga javob beramiz :)"""
    )


LANG = "🌐 Tilni tanlash"
PHONE = "📱 Raqamni o'zgartirish"


def settings(update: Update, context: CallbackContext):
    keyboard = [
        [LANG],
        [PHONE],
        [MAIN_MENU]
    ]
    update.message.reply_text(
        f"""{SETTINGS}""",
        reply_markup=ReplyKeyboardMarkup(
            keyboard,
            one_time_keyboard=False,
            input_field_placeholder=f"{SETTINGS}",
        ),
    )


def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("7101272082:AAGnF5z-X6SeKrqB1Wy-E673oXFgmeZ5emk")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
    dispatcher.add_handler(CommandHandler("start", start))

    # Main menu
    dispatcher.add_handler(MessageHandler(Filters.text(MENU), menu)),
    dispatcher.add_handler(MessageHandler(Filters.text(BASKET), basket)),
    dispatcher.add_handler(MessageHandler(Filters.text(LOCATION), location)),
    dispatcher.add_handler(MessageHandler(Filters.text(ABOUT_ORDER), about_order)),
    dispatcher.add_handler(MessageHandler(Filters.text(FEEDBACK), feedback)),
    dispatcher.add_handler(MessageHandler(Filters.text(CONTACT), contact)),
    dispatcher.add_handler(MessageHandler(Filters.text(SETTINGS), settings))

    conv_handler = ConversationHandler(
        entry_points=[
            CommandHandler('start', start),
            MessageHandler(Filters.text(FEEDBACK), feedback)
        ],
        states={
            FIKR_BILDIRISH: [
                MessageHandler(Filters.regex(
                    '^(😊Hammasi yoqdi ❤️|☺️Yaxshi ⭐️⭐️⭐️⭐️|😐 Yoqmadi ⭐️⭐️⭐️|☹️ Yomon ⭐️⭐️|😤 Juda yomon👎🏻)$'), marking)
            ],
        },
        fallbacks=[CommandHandler('start', start)]
    )
    dispatcher.add_handler(conv_handler)

    # Settings menu
    dispatcher.add_handler(MessageHandler(Filters.text(MAIN_MENU), start))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == "__main__":
    main()
