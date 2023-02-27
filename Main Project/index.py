from classes import Player
from nameInput import initName, getName
from startGUI import startGUI, getPlayer
from time import time  # Display startup time of program
from func import path
from classes import Pokemon
import logging
from battleGUI import battleGUI
from json import load
logging.basicConfig(level=logging.DEBUG)
logging.getLogger("PIL.PngImagePlugin").setLevel(
    logging.INFO)  # Get rid of PIL debug messages
### INIT ###
FILE_PATH = path("pokemonInformation-1674801501.txt", ['assets'])
MOVESET_PATH = path('pokemonMoveset.json', ['assets'])
MAX_POKEMON = 240
startTime = time()
with open(MOVESET_PATH, 'r', encoding='utf-8') as f:  # Get Pokemon Movesets
    data = load(f)  # Get moveset data
# Construct a new moveset dictionary
movesets = {
    key: [
        {
            'name': moveset['name'],
            'type': moveset['type'],
            'power': moveset['power'],
            'accuracy': moveset['accuracy'],
        }
        for count, moveset in enumerate(data[key]['levelUp'])
        if count < 4
    ]
    for key in data
}
# Get pokemon data
with open(FILE_PATH, 'r', encoding='utf-8') as f:
    pokemons = {
        int(pokemon[:4]):
        Pokemon(int(pokemon[:4]), pokemon[5:23].strip(),
                list(pokemon[26:41].strip().split('|')),
                pokemon[43:74].strip().split('|'),
                pokemon[74:128].strip().split('|'),
                pokemon[129:].strip().split('|'),
                movesets[pokemon[5:23].strip()])
        for count, pokemon in enumerate(list(f))
        if count <= MAX_POKEMON-1
    }
logging.info(
    f'All Pokemon has been successfully initalized! ({time()-startTime}s)')
del startTime, FILE_PATH, MOVESET_PATH  # Delete useless variables
### INIT ###

# Player Name GUI
initName()
playerName = getName()
logging.info(f'Pokemon Trainer Name: {playerName}')
startGUI(playerName, time(), pokemons)
player=getPlayer()
# player = Player('John Doe')
# player.pokemons = [pokemons[1], pokemons[2], pokemons[3]]
logging.info(
    f'Player {player.name} has chosen {player.pokemons[0].name}, {player.pokemons[1].name}, {player.pokemons[2].name} as their pokemons.')
battleGUI(player)