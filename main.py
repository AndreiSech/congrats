from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, ConversationHandler
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from random import randrange
from os import path
import time
import logging

BASE_DIR = path.join('C:\\', 'Users', 'Andrei', 'PycharmProjects', 'untitled', 'venv', 'assets')

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)
caption = "С Праздником!"

# Stages
FIRST, SECOND = range(2)
# Callback data
ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT = range(8)
ZERO = 10
# Flowers
# Tulips, Roses, Peonies, Chamomile, Lilies, Chrysanthemums, Orchids, Hyacinths, Violets, Crocuses, OTHERS

def start(update: Update, context: CallbackContext) -> None:
    """Send message on `/start`."""
    # Get user that sent /start and log his name
    user = update.message.from_user
    logger.info("User %s started the conversation.", user.full_name)
    keyboard = [
        [
            InlineKeyboardButton("1", callback_data=str(ONE)),
            InlineKeyboardButton("2", callback_data=str(TWO)),
            InlineKeyboardButton("3", callback_data=str(THREE)),
            InlineKeyboardButton("4", callback_data=str(FOUR)),
            InlineKeyboardButton("5", callback_data=str(FIVE)),
            InlineKeyboardButton("6", callback_data=str(SIX)),
            InlineKeyboardButton("7", callback_data=str(SEVEN)),
            InlineKeyboardButton("8", callback_data=str(EIGHT)),
        ],
        [InlineKeyboardButton("Я девочка и не хочу решать. Пусть будет сюрприз", callback_data=str(ZERO))],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send message with text and appended InlineKeyboard
    update.message.reply_text("Здравствуйте, " + update.message.from_user.first_name +
        '. Выберите свое персональное поздравление c Международным женским днем:', reply_markup=reply_markup)
    # Tell ConversationHandler that we're in state `FIRST` now
    return FIRST

def start_over(update: Update, context: CallbackContext) -> None:
    """Prompt same text & keyboard as `start` does but not as new message"""
    # Get CallbackQuery from Update
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Хочу еще", callback_data=str(ONE)),
            InlineKeyboardButton("До свидания", callback_data=str(TWO)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Instead of sending a new message, edit the message that
    # originated the CallbackQuery. This gives the feeling of an
    # interactive menu.
    #query.edit_message_text(text="Start handler, Choose a route", reply_markup=reply_markup)
    return FIRST

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Для начала разговора напишите /start. Поздравление только для девушек :)")

def one(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    logger.info(query.from_user.full_name + " selected 1 option")
    query.edit_message_text(caption)
    query.message.reply_text("Женщин неправильно называть „слабым полом“: есть научные свидетельства того, что они обладают более сильным иммунитетом, большей выносливостью и высоким болевым порогом, легче справляются с COVID-19 и по статистике живут дольше мужчин. Возможно, еще и потому, что умнее: совершают в своей жизни меньше глупостей, пренебрегая своим здоровьем. Но это не значит, к сожалению, что они неуязвимы")
    img = path.join(BASE_DIR, '1.bmp')
    query.message.reply_photo(open(img, 'rb'))
    query.message.reply_text("Желаем Вам самого ценного – крепкого и нерушимого амазонского здоровья! Пусть самочувствие будет прекрасным каждый день, а организм легко справляется с любыми нагрузками. Пусть жизненной энергии хватает на все, активность бьет ключом и эндорфины выливаются в обаятельную улыбку! Будьте здоровы и живите подольше!")
    query.answer()
    #time.sleep(10)
    #start_over(update,context)
    return FIRST

def two(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    logger.info(query.from_user.full_name + " selected 2 option")
    query.edit_message_text(caption)
    query.message.reply_text("Женщины обладают многими суперспособностями и видеть красоту окружающего мира в более ярких насыщенных красках одна из них")
    img = path.join(BASE_DIR, '2-1.bmp')
    query.message.reply_photo(open(img, 'rb'))
    query.message.reply_text("Бладаря Вам мужчины могут организовать окружающее пространство стильно и со вкусом. Вы способны облачаться в потрясающе красивые наряды, которые подчеркивают ваше природное совершенство. Спасибо за то, что дарите миру эту красоту. И помните: даже если любимый мужчина слегка профан в распознавании цветов, он все равно оценивает по-достоинству, когда Вы для него наряжаетесь в красное платье")
    img = path.join(BASE_DIR, '2-2.bmp')
    query.message.reply_photo(open(img, 'rb'))
    query.message.reply_text("С праздником, обаятельные и привлекательные!")
    query.answer()
    #time.sleep(10)
    return SECOND

def three(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    logger.info(query.from_user.full_name + " selected 3 option")
    query.edit_message_text(caption)
    query.message.reply_text("Женщины Вы безукоризненно безогововорчно прекрасны. И единственный Ваш недостаток в том, что Вы порой склонны в этом сомневаться")
    img = path.join(BASE_DIR, '3.bmp')
    query.message.reply_photo(open(img, 'rb'))
    query.message.reply_text("Желаем Вам, чтобы любимые мужчины почаще напоминали о Вашей очаровательности!")
    track = path.join(BASE_DIR, 'You are beautiful.mp3')
    audioFile = open(track, 'rb')
    query.message.reply_audio(audio=audioFile)
    query.answer()
    #time.sleep(10)
    return SECOND

def four(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    logger.info(query.from_user.full_name + " selected 4 option")
    query.edit_message_text(caption)
    query.message.reply_text("Этот светлый весенний женский празник начинался с борьбы женщин за свои права и до сих пор можно упрекнуть мужчин в том, что они не дают возможность больше зарабатывать, обращают внимание скорее на внешность, а не на интеллект и уникальный богатый внутренний мир. Но оглянитесь вокруг: в современном мире вы важны ничуть не меньше мужчин. По статистике женщины более образованны и начитанны, чем мужчины, реже подвержены вредным привычкам и деструктивному поведению, а руководители государств – женщины гораздо лучше справлялись с коронокризисом, потому что обладают тем, что неспособно дать „сильная“ мужская власть: эмпатией, способностью услышать и понять каждого. Вы невероятные!")
    img = path.join(BASE_DIR, '4.bmp')
    query.message.reply_photo(open(img, 'rb'))
    query.message.reply_text("Не будьте равными с мужчинами. Будьте лучше нас!")
    query.answer()
    #time.sleep(10)
    return SECOND

def five(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    logger.info(query.from_user.full_name + " selected 5 option")
    query.edit_message_text(caption)
    query.answer()
    query.message.reply_text("Уинстон Черчилль напутствовал: „Не желайте здоровья и богатства, а желайте удачи, ибо на Титанике все были богаты и здоровы, а удачливыми оказались единицы!“. И с этим трудно не согласиться. Желаем удачи во всех начинаниях, упорно следовать за своими мечтами, легко достигать поставленных целей и не сворачивать с верного пути")
    img = path.join(BASE_DIR, '5-1.bmp')
    query.message.reply_photo(open(img, 'rb'))
    query.message.reply_text("Верьте, что „когда чего-нибудь сильно захочешь, вся Вселенная будет способствовать тому, чтобы желание твое сбылось“")
    img = path.join(BASE_DIR, '5-2.bmp')
    query.message.reply_photo(open(img, 'rb'))
    return SECOND

def six(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    logger.info(query.from_user.full_name + " selected 6 option")
    query.edit_message_text(caption)
    query.answer()
    query.message.reply_text("Масса сердца у человека зависит от пола и обычно достигает 250-320 граммов у женщин и 300-360 граммов у мужчин. Но маленькое женское сердце на деле оказывается необъятным и включает в себя так много эмпатии и любви. А что же мужчины? „Любовь дарит возможность быть счастливым просто потому, что счастлива она“, Готфрид Лейбниц")
    img = path.join(BASE_DIR, '6.bmp')
    query.message.reply_photo(open(img, 'rb'))
    query.message.reply_text("Сделайте счастивым своего любимого человека: дайте возможность ему безгранично Вас любить и не забывать проявлять свою любовь и заботу!")
    return SECOND

def seven(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    logger.info(query.from_user.full_name + " selected 7 option")
    query.edit_message_text(caption)
    query.answer()
    query.message.reply_text("Существует стереотип, что мужчины более рациональные, а женщины – эмоциональные")
    img = path.join(BASE_DIR, '7-1.bmp')
    query.message.reply_photo(open(img, 'rb'))
    query.message.reply_text("Так ли это, не мне, бездушному боту, судить. Однако мне известно, что у женщин куда выше эмоциональный интеллект и способность справляться со многими задачами одновременно. Хотели бы пожелать, чтобы суперспособность „читать“ людей и оценивать их искренность в семейной жизни оказалось бы невостребованной: родные любили, доверяли, ценили, заботились о Вас и Вы испытывали исключительно пожительные эмоции! Искрите счастьем и дарите нам свои искренние обаятельные улыбки")
    img = path.join(BASE_DIR, '7-2.bmp')
    query.message.reply_photo(open(img, 'rb'))
    return SECOND

def eight(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    logger.info(query.from_user.full_name + " selected 8 option")
    query.edit_message_text(caption)
    query.answer()
    query.message.reply_text("Какие цветы обычно дарят женщинам на 8 марта? Правильно, из года в год все те же тюльпаны. С фантазией обычно у мужчин небогато. Но ведь каждая женщина уникальна и у нее свои предпочтения. В нашем цветочном бутике предлагаем выбрать себе в подарок персональный букет")
    flowerKeyboard = [
        [
            InlineKeyboardButton("Тюльпаны", callback_data='Tulips')
        ],
        [
            InlineKeyboardButton("Розы", callback_data='Roses')
        ],
        [
            InlineKeyboardButton("Пионы", callback_data='Peonies')
        ],
        [
            InlineKeyboardButton("Ромашки", callback_data='Chamomile')
        ],
        [
            InlineKeyboardButton("Лилии", callback_data='Lilies'),
        ],
        [
            InlineKeyboardButton("Хризантемы", callback_data='Chrysanthemums'),
        ],
        [
            InlineKeyboardButton("Орхидеи", callback_data='Orchids'),
        ],
        [
            InlineKeyboardButton("Гиацинты", callback_data='Hyacinths'),
        ],
        [
            InlineKeyboardButton("Фиалки", callback_data='Violets'),
        ],
        [
            InlineKeyboardButton("Крокусы", callback_data='Crocuses'),
        ],
        [
            InlineKeyboardButton("Другие цветы", callback_data='OTHERS'),
        ]
    ]
    flower_reply_markup = InlineKeyboardMarkup(flowerKeyboard)
    query.message.reply_text(
        text="Какие цветы Вы предпочитаете?", reply_markup=flower_reply_markup
    )
    return FIRST

def flowers(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    logger.info(query.from_user.full_name + " selected flowers: " + query.data)
    query.edit_message_text("Ваш букет цветов")
    img = path.join(BASE_DIR, query.data + '.bmp')
    query.message.reply_photo(open(img, 'rb'))
    if query.data == 'OTHERS':
        query.message.reply_text("К сожалению, у нас не оказалось подходящего для Вас букета, примите, пожалуйста, этот. Но мы убеждены, что любимые цветы сегодня подарят Ваши родные заботливые мужчины.")
    return SECOND

def surprise(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    logger.info(query.from_user.full_name + " wanted to be surprised")
    choice = randrange(1, 8)
    logger.info("Random selected " + str(choice) + " option for " + query.from_user.full_name)
    if choice == 1:
        one(update, context)
    if choice == 2:
        two(update, context)
    if choice == 3:
        three(update, context)
    if choice == 4:
        four(update, context)
    if choice == 5:
        five(update, context)
    if choice == 6:
        six(update, context)
    if choice == 7:
        seven(update, context)
    if choice == 8:
        eight(update, context)
    return SECOND

def end(update: Update, context: CallbackContext) -> None:
    """Returns `ConversationHandler.END`, which tells the
    ConversationHandler that the conversation is over"""
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="C Праздником! До свидания")
    return ConversationHandler.END

def main():
    # check for new messages --> polling
    updater = Updater(token="1638844288:AAGcMf4va4zFqKMuIFzFe6KJwH4JROdOOeY")

    # allows to register handler -> command, text, video, audio etc
    dispatcher = updater.dispatcher

    # Setup conversation handler with the states FIRST and SECOND
    # Use the pattern parameter to pass CallbackQueries with specific
    # data pattern to the corresponding handlers.
    # ^ means "start of line/string"
    # $ means "end of line/string"
    # So ^ABC$ will only allow 'ABC'
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            FIRST: [
                CallbackQueryHandler(one, pattern='^' + str(ONE) + '$'),
                CallbackQueryHandler(two, pattern='^' + str(TWO) + '$'),
                CallbackQueryHandler(three, pattern='^' + str(THREE) + '$'),
                CallbackQueryHandler(four, pattern='^' + str(FOUR) + '$'),
                CallbackQueryHandler(five, pattern='^' + str(FIVE) + '$'),
                CallbackQueryHandler(six, pattern='^' + str(SIX) + '$'),
                CallbackQueryHandler(seven, pattern='^' + str(SEVEN) + '$'),
                CallbackQueryHandler(eight, pattern='^' + str(EIGHT) + '$'),
                CallbackQueryHandler(surprise, pattern='^' + str(ZERO) + '$'),

                # Tulips, Roses, Peonies, Chamomile, Lilies, Chrysanthemums, Orchids, Hyacinths, Violets, Crocuses, OTHERS
                CallbackQueryHandler(flowers, pattern='^1(Tulips)|(Roses)|(Peonies)|(Chamomile)|(Lilies)|(Chrysanthemums)|(Orchids)|(Hyacinths)|(Violets)|(Crocuses)|(OTHERS)$'),
            ],
            SECOND: [
                CallbackQueryHandler(start_over, pattern='^' + str(ONE) + '$'),
                CallbackQueryHandler(end, pattern='^' + str(TWO) + '$'),
            ],
        },
        fallbacks=[CommandHandler('start', start)],
    )

    # Add ConversationHandler to dispatcher that will be used for handling
    # updates
    dispatcher.add_handler(conv_handler)

    help_handler = CommandHandler("help", help_command)
    dispatcher.add_handler(help_handler)

    # start polling
    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()