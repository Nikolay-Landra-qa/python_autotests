import requests

URL='https://api.pokemonbattle.ru/v2'
TOKEN='0f831c1451ee3d9c4bfc4ce44bbf78b6'
HEADER={'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email": "nikolajlandra123@gmail.com",
    "password": "810647KK"
}
body_confirmation = {"trainer_token": TOKEN}

body_create = {
    "name": "Бульбазавр",
    "photo_id": "1"
}

body_Change = {
    "pokemon_id": "133857",
    "name": "Стив",
    "photo_id": 14
}
body_battle = {
    "attacking_pokemon": "133851",
    "defending_pokemon": "133801"
}

body_Catch = {
    "pokemon_id": "133857"
}

'''respons = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(respons.text)'''

'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers=HEADER,json=body_confirmation)
print(response_confirmation.text)'''

'''respons_create = requests.post(url=f'{URL}/pokemons', headers=HEADER,json=body_create)
print (respons_create.text)'''

respons_Change = requests.put(url=f'{URL}/pokemons', headers=HEADER,json=body_Change)
print (respons_Change.text)

'''respons_Catch = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER,json=body_Catch)
print (respons_Catch.text)'''

'''respons_battle = requests.post(url=f'{URL}/pokemons', headers=HEADER,json=body_battle)
print (respons_battle.text)'''