from nameInput import initName, getName
from startGUI import startGUI
from time import time  # Display startup time of program
from func import path
from classes import Pokemon
import logging
from battleGUI import battleGUI
logging.basicConfig(level=logging.INFO)
### INIT ###
chargesLeft = 3
FILE_PATH = path("pokemonInformation-1674801501.txt", ['assets'])
MAX_POKEMON = 240
# STORE POKEMON INFO IN POKEMONS VARIABLE
startTime=time()
with open(FILE_PATH, 'r', encoding='utf-8') as f:
    pokemons = {}
    for pokemon in list(f):
        if 'Program has finished.' in pokemon:
            break
        count = int(pokemon[:4])
        name = pokemon[5:23].strip()
        stats = list(pokemon[26:41].strip().split('|'))
        types = pokemon[43:74].strip().split('|')
        weaknesses = pokemon[74:128].strip().split('|')
        evolutions = pokemon[129:].strip().split('|')
        pokemons[count] = Pokemon(name, stats, types, weaknesses, evolutions)
logging.info(f'All Pokemon has been successfully initalized! ({time()-startTime}s)')
del startTime
### INIT ###

# Player Name GUI

# initName()
# playerName=getName()
# logging.info('Pokemon Trainer Name:',playerName)
# startGUI(playerName, time(), pokemons)
# logging.info('Player has finished choosing their pokemon.')
battleGUI()
