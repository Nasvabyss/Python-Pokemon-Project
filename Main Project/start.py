from func import path
class Player():
    def __init__(self):self.pokemonCount,self.pokemons=0,[]
    def getPokemonCount(self):return self.pokemonCount
    def setPokemonCount(self,count):self.pokemonCount=count
    def getPokemons(self):return self.pokemons
    def setPokemons(self,pokemons):self.pokemons=pokemons
class Pokemon():
    def __init__(self,name,count,atk,defe,satk,sdef,spd,imgPath):self.name,self.count,self.atk,self.defe,self.satk,self.sdef,self.spd,self.imgPath=name,count,atk,defe,satk,sdef,spd,imgPath
    def evol(self):
        pass
charizard=Pokemon('Charizard',0,0,0,0,0,0,path('charizard.png'))
def getStarterPokemon():
    return charizard
def confirmPokemon():
    pass
def changePokemon():
    pass