"""
Run this code to confirm all unconfirmed messages
"""
import requests

from b_urls import url_get_updates

# https://core.telegram.org/bots/api#getupdates
response = requests.get(url_get_updates).json()
if len(response['result']):
    print('Confirming message(s)...')
    update_id = max(item['update_id'] for item in response['result'])
    params = {
        'offset': update_id + 1,
    }
    response = requests.get(url_get_updates, params=params).json()
    if len(response['result']):
        print(response)
    else:
        print('You are good to go')
else:
    print('You are good to go')
