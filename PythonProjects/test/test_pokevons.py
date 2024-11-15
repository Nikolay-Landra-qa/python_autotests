import requests
import pytest

URL='https://api.pokemonbattle.ru/v2'
TOKEN='476f3cd986a62b6dcfde1064ea5604ec'
HEADER={'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID=18166

def test_status_code():
    response = requests.get(url=f'{URL}/pokemons',params={'traner_id': TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url=f'{URL}/pokemons',params={'traner_id': TRAINER_ID})
    assert response_get.json()["data"][0]["name"] == 'bellossom'



  




