"""
Send many messages to the bot, run the script two times,
then uncomment the code to confirm processed messages
"""
import requests

from b_urls import url_get_updates, url_send_message


def get_user_info(user):
    fields = [
        'first_name',
        'last_name',
        'username',
        'language_code',
        'id',
    ]
    result = 'Some info about you:'
    for field in fields:
        if field in user:
            result += f'\n{field}: {user[field]}'
    return result


max_update_id = 0
response = requests.get(url_get_updates).json()

for update in response['result']:
    user_id = update['message']['from']['id']
    chat_id = update['message']['chat']['id']
    message_id = update['message']['message_id']
    text = get_user_info(update['message']['from'])
    params = {
        'chat_id': chat_id,
        'reply_to_message_id': message_id,
        'text': text
    }
    print(f'Replying to {user_id}... ', end='')
    response = requests.get(url_send_message, params=params).json()
    print('OK' if response['ok'] else 'Fail')
    max_update_id = max(update['update_id'], max_update_id)

if 0:  # Change to 1 to 'uncomment' the code below
    if max_update_id:
        print('Confirming all processed messages... ', end='')
        params = {
            'offset': max_update_id + 1,
        }
        response = requests.get(url_get_updates, params=params).json()
        print('OK' if response['ok'] else 'Fail')
