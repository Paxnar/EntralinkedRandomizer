import requests
import json
import random

g = requests.Session()
encounters = [{'species': random.randint(1, 649), 'move': 75, 'form': '0', 'gender': 'GENDERLESS', 'animation': 'LOOK_AROUND'} for i in range(random.randint(1, 10))]
print(g.post('http://127.0.0.1/dashboard/login', data={
    'gsid': 'LGKK8TS6YH'}))
print(g.post('http://127.0.0.1/dashboard/profile', data=json.dumps({'encounters': encounters,
                                                                    'items': [],
                                                                    'avenueVisitors': [],
                                                                    'cgearSkin': 'none',
                                                                    'dexSkin': 'none',
                                                                    'musical': 'none',
                                                                    'gainedLevels': 1})))
g.close()