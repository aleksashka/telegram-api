import requests

from b_urls import url_get_updates

# https://core.telegram.org/bots/api#getting-updates
# https://core.telegram.org/bots/api#getupdates
response = requests.get(url_get_updates).json()
print('-' * 80)
print(response)
print('-' * 80)

print('Open chat with the bot and press START')
input('When ready hit Enter to continue')

response = requests.get(url_get_updates).json()
print('-' * 80)
print(response)
print('-' * 80)
