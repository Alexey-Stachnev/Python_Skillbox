import requests
import json

my_req = requests.get('https://swapi.dev/api/starships/10/')

data_ship = {}
attributes_ship = ['name', 'max_atmosphering_speed', 'starship_class']
attributes_pilot = ['name', 'height', 'mass', 'homeworld']

for atrb in attributes_ship:
    data = json.loads(my_req.text)[atrb]
    data_ship[atrb] = data
data_ship['ship_name'] = data_ship['name']
data_ship.pop('name')

pilots_data = []
pilots = json.loads(my_req.text)['pilots']
for pilot in pilots:
    dict = {}
    pilot_data = requests.get(pilot).text
    for atrb in attributes_pilot:
        data = json.loads(pilot_data)[atrb]
        dict[atrb] = data
    dict['homeworld_url'] = dict['homeworld']
    home_world_data = requests.get(dict['homeworld_url']).text
    dict['homeworld'] = json.loads(home_world_data)['name']
    pilots_data.append(dict)

data_ship['pilots'] = pilots_data

with open('Falcon.json', 'w') as file:
    json.dump(data_ship, file, indent=4)

output = open('Falcon.json', 'r').read()
print(output)
