import requests

from b_urls import url_get_updates, url_send_message, url_delete_message

response = requests.get(url_get_updates).json()
if len(response['result']) == 0:
    print('It looks like no updates are present')
    print('Open chat with bot and press START')
    input('When ready hit Enter to continue')
    response = requests.get(url_get_updates).json()

result = response['result'][0]
update_id = result['update_id']
message_id = result['message']['message_id']
chat_id = result['message']['chat']['id']

input("Press Enter to reply with 'Replying to your message'")

# https://core.telegram.org/bots/api#sendmessage
params = {
    'chat_id': chat_id,
    'reply_to_message_id': message_id,
    'text': 'Replying to your message',
}
response = requests.get(url_send_message, params=params).json()

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
if response['ok']:
    print('Successfully deleted the message')
else:
    print('Oops, something went wrong')
