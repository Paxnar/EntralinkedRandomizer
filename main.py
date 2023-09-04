import requests
import json
import random
import locations
import pokedata

pkm_count = int(input())
gsid = input()
location = random.choice(locations.locations)

g = requests.Session()
encounters = []
for i in range(pkm_count):
    pkm = random.choice(location)
    pkm_d = pokedata.pkms[pkm['name']]
    pkm_id = pkm_d['id']
    move = pokedata.moves[random.choice(pkm['move'])]
    form = random.choice(pkm_d['forms']) if pkm['name'] \
                                           not in ['Deoxys', 'Rotom', 'Giratina', 'Shaymin', 'Arceus', 'Tornadus',
                                                   'Thundurus', 'Landorus', 'Kyurem', 'Keldeo',
                                                   'Meloetta', 'Genesect'] else 0
    animation = random.choice(["LOOK_AROUND", "WALK_AROUND", "WALK_LOOK_AROUND", "WALK_VERTICALLY",
                               "WALK_HORIZONTALLY", "WALK_LOOK_HORIZONTALLY", "SPIN_RIGHT", "SPIN_LEFT"])
    encounters.append(
        {'species': pkm_id, 'move': move, 'form': form, 'gender': pkm_d['gender'], 'animation': animation})
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
