from fastapi import FastAPI
from pydantic import BaseModel

import requests

app = FastAPI()

db = []

# 클래스 선언


class City(BaseModel):
    name: str
    timezone: str


@app.get('/')
def root():
    return {"hello": "world"}
    # 8000 port

# list


@app.get('/cities')
def get_cities():
    results = []
    for city in db:
        strs = f"https://worldtimeapi.org/api/timezone/{city['timezone']}"
        r = requests.get(strs)
        cur_time = r.json()['datetime']
        results.append([{'name': city['name']}, {'timezone': city['timezone']}, {
                       'current_time': cur_time}])

    return results

# GET read


@app.get('/cities/{city_id}')
def get_city(city_id: int):
    city = db[city_id-1]
    strs = f"https://worldtimeapi.org/api/timezone/{city['timezone']}"
    r = requests.get(strs)
    cur_time = r.json()['datetime']

    return {'name': city['name'], 'timezone': city['timezone'], 'current_time': cur_time}


# POST creatae

@app.post('/cities')
def create_city(city: City):
    db.append(city.dict())
    return db[-1]


# Delete delete

@app.delete('/cities/{city_id}')
def delete_city(city_id: int):
    db: pop(city_id-1)

    return {}
