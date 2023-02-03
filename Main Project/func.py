from json import load # For imgCreator & generatePokemon function
from random import randint # Random evolutions choice evolutions' pokemon (For generatePokemon function)

def path(path,between):
    from pathlib import Path
    return f'{Path(__file__).parent.resolve()}/{"/".join(between)}/{path}' #Fix path issue

def imgCreator(pokemon):
    """Turn URLS into Images"""
    from PIL.ImageTk import PhotoImage;from urllib.request import urlopen # Image Creator from URLS
    from urllib.error import URLError
    try:URL=urlopen(load(open(path('config.json',[])))['pokemonPaths'][pokemon[0].upper()+pokemon[1:]])
    except URLError:
        print('The website has been blocked by your network. Please try another network.')
        exit()
    DATA=URL.read()
    URL.close()
    return PhotoImage(data=DATA)

def generatePokemon():
    config=list(load(open(path('config.json',[])))['pokemonPaths'])
    return imgCreator(config[randint(0,len(config)-1)])