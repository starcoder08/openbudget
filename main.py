from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from aiogram.utils import executor

TOKEN = "7665037882:AAGe2KWFII_hDoLF1BzYoFZDzd8BcWFrY_o"
VOTING_LINK = "https://openbudget.uz/boards/initiatives/initiative/50/e9630f65-e102-4c25-a169-262b1b50bdbd"  # Mahallang uchun linkni qo'y
VOTING_LINK2 = "https://t.me/ochiqbudjet_0010_bot?start=050374825011"  # Mahallang uchun linkni qo'y

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    # Rasmlar 1
    photo1 = "https://i.postimg.cc/Ls94LyjZ/1.jpg"  # 1-rasm linki yoki file_id
    photo2 = "https://i.postimg.cc/gJrYBnSz/2.jpg"  # 2-rasm linki yoki file_id

    media = [
        InputMediaPhoto(media=photo1, caption="sayt orqali berilgan ovozlar shunday bo'lishi kerak‼️."),
        InputMediaPhoto(media=photo2)
    ]
    await bot.send_media_group(message.chat.id, media)
     # Rasmlar 2
    photo3 = "https://i.postimg.cc/63N3jd2d/3.jpg"  # 1-rasm linki yoki file_id

    await bot.send_photo(message.chat.id, photo3, caption="telegram bot orqali berilgan ovozlar shunday bo'lishi kerak‼️")

    # Ovoz berish tugmasi
    keyboard = InlineKeyboardMarkup()
    vote_button = InlineKeyboardButton("🗳 Ovoz berish (telegram bot)", url=VOTING_LINK2)  # Bevosita tg linkga yo‘naltiradi
    vote_button2 = InlineKeyboardButton("🗳 Ovoz berish (sayt orqali)", url=VOTING_LINK)  # Bevosita linkga yo‘naltiradi
    keyboard.add(vote_button)
    keyboard.add(vote_button2)

    await message.answer("Hurmatli mijoz! ushbu tugmani bosib telegeram yoki sayt orqali mahallamizga ovoz berishingiz mumkin.\n "
                         "Berilgan ovozlarni yuqoridagidek holatda screenshot qilin adminga tashlasangiz pulingiz tolab beriladi✅ 1 ta ovoz=20 ming so'm\n"
                         "Admin: @oybek_code | Admin telefon raqami: 911532114 (telegram orqali javob berish kechiksa telefon qilishingiz mumkin🟢)", reply_markup=keyboard)

executor.start_polling(dp, skip_updates=True)