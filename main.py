import requests
from pprint import pprint

url = 'https://superheroapi.com/api/2619421814940190/search/'

intellects = {}

def intelligence(superhero):
    link = url + superhero
    response = requests.get(link)

    import json
    dict = json.loads(response.content)

    results = dict['results'][0]
    powerstats = results['powerstats']
    intelligence = powerstats['intelligence']

    intellects[intelligence] = superhero

    return int(intelligence)


hulk = intelligence('Hulk')
captain_america = intelligence('Captain America')
thanos = intelligence('Thanos')

for k in intellects.keys():
    temp = 0
    if int(k) > temp:
        temp = k
print(f'Самый умный супергерой - {intellects[temp]}')

