import json
import os
from pathlib import Path
import sqlite3 as db


path = Path(os.path.join('files', 'city.list.json'))
data_city = json.loads(path.read_text(encoding='utf-8'))

class City:
    def __init__(self, id, name, country):
        self.id = id
        self.name = name
        self.country = country

    def get_full_info(self):
        return self.id + self.name + self.country

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_country(self):
        return self.country

cities = []
for i in data_city:
    cities.append(City(i['id'], i['name'], i['country']))

data_country = sorted(set([val.get_country() for val in cities]))

