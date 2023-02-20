from json import load  # Load json
from random import randint  # Randomize pokemon
from pathlib import Path  # Resolve path issues
from urllib.error import URLError  # Error that occurs if website is blocked
from urllib.request import urlopen  # Get image from url
from PIL.ImageTk import PhotoImage  # Convert photo data into image
from time import time  # Logging
from logging import info, warn, error  # Logging
from io import BytesIO # Flip Image
from PIL import Image # Convert byte object to image object

def path(path, between):
    # Fix path issue
    return f'{Path(__file__).parent.resolve()}/{"/".join(between)}/{path}'


def imgCreator(pokemon, data=False):
    """Turn URLS into Images"""
    startTime = time()
    try:
        URL = urlopen(load(open(path('config.json', [])))[
                      'pokemonPaths'][pokemon[0].upper()+pokemon[1:]])
    except URLError:
        error('The website used to obtain essential images has been blocked by your network. If this error reoccurs, please try another network.')
        exit()
    DATA = URL.read()
    URL.close()
    endTime = time()
    info(f'Successfully retrieved photo for {pokemon} ({endTime-startTime}ms)')
    if endTime-startTime>100:
        warn('Your network is slow. This program might take longer to run.')
    return DATA if data else PhotoImage(data=DATA)


def generatePokemon():
    config = list(load(open(path('config.json', [])))['pokemonPaths'])
    count = randint(0, len(config)-1)  # Get pokemon count
    # Return pokemon count and photo image object
    return count, imgCreator(config[count])


def flipImg(byteImg):
    """Horizontally flips images"""
    with BytesIO(byteImg) as f:
        img = Image.open(f)  # Create a PIL image object from the byte data
        # Get the byte data of the flipped image
        with BytesIO() as output:
            # Flip the image horizontally and save the flipped image to the output stream
            img.transpose(Image.FLIP_LEFT_RIGHT).save(
                output, format=img.format)
            imgData = output.getvalue()
    return PhotoImage(data=imgData)
