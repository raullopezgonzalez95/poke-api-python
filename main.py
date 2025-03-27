from fastapi import FastAPI
from service.service import *

app = FastAPI()


@app.get("/")
async def root():
    return {"status": "OK"}


@app.get("/pokemon/ditto")
async def ditto():
    return get_ditto()


@app.get("/pokemon/{name}")
async def pokemon(name: str):
    return get_pokemon(name)


@app.get("/pokemon")
async def all_pokemon():
    return get_all_pokemon()


@app.get("/species")
async def all_pokemon_species():
    return get_all_pokemon_species()
