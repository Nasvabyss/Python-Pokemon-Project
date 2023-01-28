# Pick 3 characters
# Player's characters from top down
# AI chooses player's characters, uses random position.

# Enemy HP reduced by calc dmg
# Own xp increased by calc dmg
# Enemy xp increased by def pt
# If dmg calc >10, xp gained = 120%
# If dmg calc <=0, xp gained = 150%
# Character evo at 100, add 1 for every stat if unable to
# Remove char if hp <=0
# Allow player to select which chars attack which enemy char
# AI randomly picks player char from AI char top down

# Dmg Calc: Attacker Atk + (Attacker Special Atk Range) - Enemy Def - (Enemy Special Def Range) 
# Exp calculation: Dmg Dealt
# Extra exp is given if the enemy has fainted: 
# Level calculation is taken from the 'fluctuating' evolution version. The source can be found here: (https://bulbapedia.bulbagarden.net/wiki/Experience)
# Level calculation:
# Before level 15: (n**3 * (((n+1)/3)+24))/50
# Level 15-35: (n**3 * (n+14))/50
# Level 36-100: (n**3 * ((n*2)+32))/50
# Pokemon evolves every 20 levels till max evolution (20,40,60)
# If pokemon is unable to evolve due to max evolution, add 1 to every stat

from random import randint # For randomizing evolutions for pokemon with choice evolutions
from func import path,imgCreator
from json import load
from random import randint
fileName = path('pokemonInformation-1674801501.txt')
MAX_POKEMON=240
class Pokemon:
    def __init__(self,name,stats,types,weaknesses,evol):self.name,self.stats,self.types,self.weaknesses,self.evol=name,stats,types,weaknesses,evol
    def getName(self):return self.name
    def getStats(self):return self.stats
    def getTypes(self):return self.types
    def getWeaknesses(self):return self.weaknesses
    def getEvol(self):return self.evol

class Player:
    def __init__(self,name,pokemon1:Pokemon,pokemon2:Pokemon,pokemon3:Pokemon):pass

def getPokemonCount():return '1st'

chargeLeft=3
def getCharge():return chargeLeft

def coBtn(canvas,img):
    """Confirm Button Algorithm"""
    print('Confirm Button clicked!')
    canvas.delete(img) # Delete the pokemon image
    # TODO
    # Get the pokemon info that was confirmed and process it
    # If it was the 3rd pokemon, show the next screen
    # Else, regenerate the image and change the title text to its approprate amount

def chBtn(canvas,img):
    """Change Button Algorithm"""
    print('Change Button clicked!')
    canvas.delete(img) # Delete the pokemon image
    chargeLeft=getCharge()
    chargeLeft-=1
    # TODO
    # Regenerate a new image
    # Remove a charge from the user
    # Change the 'Charge Left' text to its approprate amount
    # If charges are 0, do not allow the user to regenerate a new pokemon

def generatePokemon():
    generateName=list(load(open(path('config.json')))['pokemonPaths'])[randint(0, MAX_POKEMON-1)]
    return imgCreator(generateName)
if __name__ == '__main__':
    with open(fileName,'r',encoding='utf-8') as f:
        pokemons={}
        for pokemon in list(f):
            if'Program has finished.'in pokemon:break
            count=int(pokemon[:4])
            name=pokemon[5:23].strip()
            stats=list(pokemon[26:41].strip().split('|'))
            types=pokemon[43:74].strip().split('|')
            weaknesses=pokemon[74:128].strip().split('|')
            evolutions=pokemon[129:].strip().split('|')
            pokemons[count]=Pokemon(name,stats,types,weaknesses,evolutions)
            a=pokemons[count]
            #print(a.getName(),a.getStats(),a.getTypes(),a.getWeaknesses(),a.getEvol())