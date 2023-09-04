import requests
import json
import random
import locations
import pokedata

pkm_count = int(input())
gsid = input()
location = random.choice(locations.locations)


g = requests.Session()
encounters = [{'species': pokedata.pkms[random.choice(location)['name']]['id'], 'move': 75, 'form': '0', 'gender': 'GENDERLESS', 'animation': 'LOOK_AROUND'} for i in range(pkm_count)]
print(g.post('http://127.0.0.1/dashboard/login', data={
    'gsid': gsid}))
print(g.post('http://127.0.0.1/dashboard/profile', data=json.dumps({'encounters': encounters,
                                                                    'items': [],
                                                                    'avenueVisitors': [],
                                                                    'cgearSkin': 'none',
                                                                    'dexSkin': 'none',
                                                                    'musical': 'none',
                                                                    'gainedLevels': 0})))
g.close()