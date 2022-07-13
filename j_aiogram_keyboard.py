from aiogram import Bot, Dispatcher, executor, types

from a_token import token

bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btns_text = ['Yes!', 'Sure!']
    keyboard_markup.row(*(types.KeyboardButton(text) for text in btns_text))
    await message.reply('Do you like Telegram?', reply_markup=keyboard_markup)


@dp.message_handler(text=['Yes!', 'Sure!'])
async def very_well(message: types.Message):
    await message.reply('Very well!', reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler()
async def echo(message: types.Message):
    await message.reply(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
