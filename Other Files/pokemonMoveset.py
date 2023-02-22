# sourcery skip: identity-comprehension
from pathlib import Path
from json import load
CONFIG_PATH=f'{Path(__file__).parent.parent.resolve()}\\Main Project\\config.json'
POKEMON_INFO_PATH=f'{Path(__file__).parent.parent.resolve()}\\Main Project\\assets\\pokemonInformation-1674801501.txt'
with open(CONFIG_PATH) as f:
    data=load(f)['pokemonPaths']
names= []
print(data.keys())
name='Bulbasaur'.lower()
link=f'https://pokemondb.net/pokedex/{name}'
