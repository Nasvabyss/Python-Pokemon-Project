from json import load # Load json
from random import randint  # Randomize pokemon
from pathlib import Path # Resolve path issues
from urllib.error import URLError # Error that occurs if website is blocked
from urllib.request import urlopen # Get image from url
from PIL.ImageTk import PhotoImage # Convert photo data into image
from time import time # Logging
from logging import info,warn,error # Logging
def path(path,between):
    return f'{Path(__file__).parent.resolve()}/{"/".join(between)}/{path}' #Fix path issue

def imgCreator(pokemon):
    """Turn URLS into Images"""
    startTime=time()
    try:URL=urlopen(load(open(path('config.json',[])))['pokemonPaths'][pokemon[0].upper()+pokemon[1:]])
    except URLError:
        error('The website used to obtain essential images has been blocked by your network. If this error reoccurs, please try another network.')
        exit()
    DATA=URL.read()
    URL.close()
    endTime=time()
    info(f'Successfully retrieved photo for {pokemon} ({endTime-startTime}ms)')
    # if endTime-startTime>1000:
    warn('Your network is slow. This program might take longer to run.')
    return PhotoImage(data=DATA)
def generatePokemon():
    config=list(load(open(path('config.json',[])))['pokemonPaths'])
    count = randint(0, len(config)-1)
    return count,imgCreator(config[count])
def flipImg(img):
    """Horizontally flips images"""
    from PIL import Image, ImageTk
    image = Image.open(img)
    image = image.transpose(Image.FLIP_LEFT_RIGHT)
    return ImageTk.PhotoImage(image)