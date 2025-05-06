import requests
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '5a0a3e95b591ae8e429f7590b4f34968'
HEADER = {'Content-Type: application/json', TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email": "yanbarisova2705@yandex.ru",
    "password": "Bazanovo55"
}

body_conformation = {
    "trainer_token": TOKEN
}

body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)'''

'''response.conformation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_conformation)
print(response_conformation.text)'''

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_conformation)
print(response_create.status_code)

pokemon_id = response_create.json()['id']