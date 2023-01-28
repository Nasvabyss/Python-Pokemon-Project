from pathlib import Path
def path(path):return f'{Path(__file__).parent.resolve()}/assets/{path}' #Resolve path
# Image Creator from URLS
from PIL import ImageTk
from urllib.request import urlopen
from json import load
def imgCreator(pokemon):
    URL=urlopen(load(open(path('config.json')))['pokemonPaths'][pokemon[0].upper()+pokemon[1:]])
    DATA=URL.read()
    URL.close()
    return ImageTk.PhotoImage(data=DATA)