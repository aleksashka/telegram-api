import requests

from b_urls import url_get_updates, url_send_message, url_delete_message

# https://core.telegram.org/bots/api#getupdates
# Make sure there is at least one unconfirmed update
response = requests.get(url_get_updates).json()
if len(response['result']) == 0:
    print('It looks like no updates are present')
    print('Open chat with the bot and press START')
    input('When ready hit Enter to continue')
    response = requests.get(url_get_updates).json()
print('-' * 80)
print(response)
print('-' * 80)

result = response['result'][0]
update_id = result['update_id']
message_id = result['message']['message_id']
chat_id = result['message']['chat']['id']
from_id = result['message']['from']['id']
message = result['message']['text']

print(f'There is an update with the following properties:')
print(f'{update_id=}, {message_id=}, {chat_id=}, {from_id=}, {message=}')
input("Press Enter to send back 'Hello!'")

# https://core.telegram.org/bots/api#sendmessage
params = {
    'chat_id': chat_id,
    'text': 'Hello!',
}
response = requests.get(url_send_message, params=params).json()
print('-' * 80)
print(response)
print('-' * 80)

result = response['result']
sent_message_id = result['message_id']
sent_chat_id = result['chat']['id']

print(f'We just sent a message with the following:')
print(f'{sent_message_id=}, {sent_chat_id=}')
input('Press Enter to delete this message')

# https://core.telegram.org/bots/api#deletemessage
params = {
    'chat_id': sent_chat_id,
    'message_id': sent_message_id,
}
response = requests.get(url_delete_message, params=params).json()
print('-' * 80)
print(response)
print('-' * 80)
