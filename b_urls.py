from a_token import token

url_bot_api = 'https://api.telegram.org/bot'
url_token = url_bot_api + token

url_get_me = url_token + '/getMe'
url_get_updates = url_token + '/getUpdates'
url_send_message = url_token + '/sendMessage'
url_delete_message = url_token + '/deleteMessage'
