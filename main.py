import requests
import json
from pprint import pprint

url = 'https://superheroapi.com/api/2619421814940190/search/'

intellects = {}

def intelligence(superhero):
    link = url + superhero
    response = requests.get(link)

    data = response.json()

    results = data.get('results')[0]
    powerstats = results.get('powerstats')
    intelligence = powerstats.get('intelligence')

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

