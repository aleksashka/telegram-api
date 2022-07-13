"""
Check if bot is authorized
"""
import requests

from b_urls import url_get_me

# https://core.telegram.org/bots/api#authorizing-your-bot 
# https://core.telegram.org/bots/api#getme
response = requests.get(url_get_me).json()

username = response['result']['username']
print('-' * 80)
print('I am alive!!!')
print('My name is @{0} (or https://t.me/{0})'.format(username))
print('-' * 80)
print(response)
print('-' * 80)
