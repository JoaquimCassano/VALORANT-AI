import requests, urllib


name = input('Seu username (Com tag):  ')
name, tag = name.split('#')

encode = urllib.parse.quote(name)
print(encode)
puuid = requests.get(f'https://api.henrikdev.xyz/valorant/v1/account/{encode}/{tag}', timeout=10).json()
region = puuid['data']['region']
puuid = puuid['data']['puuid']
matches = requests.get(f'https://api.henrikdev.xyz/valorant/v1/by-puuid/lifetime/matches/na/{puuid}?size=5', timeout=4).json()
print(matches)