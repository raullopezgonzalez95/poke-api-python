import requests
from starlette import status

from constants.constants import BASE_URL_POKE_API
from dto.dto import ResponseData
from exception.custom_exceprtion import PokeException


def get_ditto():
    url = f"{BASE_URL_POKE_API}/pokemon/ditto"
    return response_json(requests.get(url))


def get_pokemon(name: str):
    url = f"{BASE_URL_POKE_API}/pokemon/{name}"
    return response_json(requests.get(url))


def get_all_pokemon():
    params = { "limit": 50, "offset": 0 }
    url = f"{BASE_URL_POKE_API}/pokemon"
    response = requests.get(url, params=params)
    return ResponseData(**response_json(response))


def get_all_pokemon_species():
    params = { "limit": 50, "offset": 0 }
    url = f"{BASE_URL_POKE_API}/pokemon-species"
    response = requests.get(url, params=params)
    return ResponseData(**response_json(response))


def response_json(response):
    if response.status_code != status.HTTP_200_OK:
        raise PokeException("ERROR", "GET DATA", status.HTTP_500_INTERNAL_SERVER_ERROR)

    return response.json()