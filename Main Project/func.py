# For imgCreator & generatePokemon function
from json import load
# Random evolutions choice evolutions' pokemon (For generatePokemon function)
from random import randint


def path(path,between):
    from pathlib import Path
    return f'{Path(__file__).parent.resolve()}/{"/".join(between)}/{path}' #Fix path issue

def imgCreator(pokemon):
    """Turn URLS into Images"""
    from urllib.error import URLError
    from urllib.request import urlopen  # Image Creator from URLS

    from PIL.ImageTk import PhotoImage
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
def flipImg(img):
    from PIL import Image, ImageTk
    image = Image.open(img)
    image = image.transpose(Image.FLIP_LEFT_RIGHT)
    return ImageTk.PhotoImage(image)