import requests, urllib, json
null = None ; true = True ; false = False

def start_data(name:str):
    '''Name needs the tag'''
    name, tag = name.split('#')

    encode = urllib.parse.quote(name)
    print(encode)
    puuid = requests.get(f'https://api.henrikdev.xyz/valorant/v1/account/{encode}/{tag}', timeout=10).json()
    region = puuid['data']['region']
    puuid = puuid['data']['puuid']
    matches = requests.get(f'https://api.henrikdev.xyz/valorant/v1/by-puuid/lifetime/matches/na/{puuid}?size=10', timeout=4).json()
    print(matches)



def cut_data(file:str):
    data = json.loads(open(file).read())
    match = data['data']

    user_stats = []
    
    for i in data['data']['players']['all_players']:
        user_stats.append({'username': i['name'], 'agent':i['character'], 'afk_rounds':i['behavior']['afk_rounds'], 'stats':i['stats'], 'team':i['team']})
    


    rounds_data = []
    for round in match['rounds']:
        for index, player in enumerate(round['player_stats']):
            if player['player_display_name'] == 'Apenas um nerd#2230':
                stats = round['player_stats'][index]
                break
        rounds_data.append({'winner_team':round['winning_team'], 'end_type':round['end_type'], 'analyzed_player_stats':stats})
        
        
    important_data =  {
        'match_summary':{
            'map':match['metadata']['map'],
            'mode':match['metadata']['mode'],
            'server':match['metadata']['cluster'],
        },
        'players':user_stats,
        'won_rounds':{'red':match['teams']['red']['rounds_won'], 'blue':match['teams']['blue']['rounds_won']},
        'rounds':rounds_data
    }
    return json.dumps(important_data)

if __name__ == '__main__':
    #start_data('Apenas um nerd#2230')
    formmated = cut_data('match_data.json')
    with open('formatted.json', 'w') as file:
        file.write(formmated)