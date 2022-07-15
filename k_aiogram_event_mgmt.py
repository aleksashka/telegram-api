import random
from time import sleep

from aiogram import Bot, Dispatcher, executor, types

from a_token import token


circle_green = '\U0001F7E2'
circle_red = '\U0001F534'
bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    text = 'Send me <pre>/send N</pre> to send N events (1 by default)'
    help_message = await message.answer(text, parse_mode='HTML')
    await message.delete()
    sleep(1)
    await help_message.delete()


@dp.message_handler(commands=['send'])
async def send(message: types.Message):
    text = message.text
    chat_id = message.chat.id
    try:
        count = int(text.split()[1])
    except (ValueError, IndexError):
        count = 1
    for _ in range(count):
        event_id = random.randint(1_000_000, 9_000_000)
        text = f'{circle_red}\nEvent ID: {event_id}'
        keyboard_markup = kb_create_event(event_id, 'asd')
        await bot.send_message(chat_id, text, reply_markup=keyboard_markup)
    await message.delete()


# @dp.callback_query_handler(text='no')  # if cb.data == 'no'
# @dp.callback_query_handler(text='yes')  # if cb.data == 'yes'
@dp.callback_query_handler()
async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    cb_data = query.data
    event_id = cb_data.split('_')[1]
    old_text = query.message.text
    user_id = query.from_user.id
    if cb_data.startswith('a'):
        new_text = old_text + f'\n\nAcked by: {user_id}'
        buttons_str = 'sd'
        qa_text = f'Event {event_id} acknowledged '
    elif cb_data.startswith('s'):
        line = '\n' if '\nAcked by:' in old_text else '\n\n'
        new_text = old_text.replace(circle_red+'\n', '')
        new_text += f'{line}Solved by: {user_id}'
        buttons_str = 'd'
        qa_text = f'Event {event_id} solved'
    elif cb_data.startswith('d'):
        buttons_str = ''
        qa_text = f'Event {event_id} deleted'
    else:
        raise

    if buttons_str:
        keyboard_markup = kb_create_event(event_id, buttons_str)
        await query.message.edit_text(new_text, reply_markup=keyboard_markup)
    else:
        await query.message.delete()
    # always answer callback queries, even if you have nothing to say
    await query.answer(qa_text)


@dp.message_handler()
async def echo(message: types.Message):
    await message.reply(message.text)


def kb_create_event(event_id, buttons_str='asd'):
    keyboard_markup = types.InlineKeyboardMarkup(row_width=3)
    buttons = []
    for letter in buttons_str:
        if letter == 'a':
            buttons.append(('Ack', f'a_{event_id}'))
        if letter == 's':
            buttons.append(('Solve', f's_{event_id}'))
        if letter == 'd':
            buttons.append(('Delete', f'd_{event_id}'))
    row_buttons = []
    for (text, data) in buttons:
        row_buttons.append(
            types.InlineKeyboardButton(text, callback_data=data)
        )
    keyboard_markup.add(*row_buttons)
    return keyboard_markup


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
