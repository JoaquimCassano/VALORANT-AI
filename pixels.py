import requests
from bs4 import BeautifulSoup

agente = input('Nome do agente:  ')
mapa = input('Mapa:  ')

lineups = requests.get(f'https://tracker.gg/valorant/guides/clips?agent={agente.lower()}&map={mapa.lower()}')
soup = BeautifulSoup(lineups.content, 'html.parser')
guides = []

for guide in soup.select('div.guide-tile'):
    title = guide.select_one('p.guide-tile__title a')['href']
    author = guide.select_one('span.guide-tile__author a').text
    views = guide.select_one('span.views').text
    timestamp = guide.select_one('span.guide-tile__timestamp').text
    
    guide_data = {
        'title': title,
        'author': author,
        'views': views,
        'timestamp': timestamp
    }
    
    guides.append(guide_data)



for guide in guides:
    print(f'Vídeo: https://tracker.gg{guide.get("title")}/')