# Pokemon Class
class Pokemon:
    def __init__(self,name:str,stats:list,types:list,weaknesses:list,evol:list):self.name,self.stats,self.types,self.weaknesses,self.evol=name,stats,types,weaknesses,evol
    def getName(self)->str:return self.name
    def getStats(self)->list:return self.stats
    def getTypes(self)->list:return self.types
    def getWeaknesses(self)->list:return self.weaknesses
    def getEvol(self)->list:return self.evol

class Player:
    def __init__(self,name:str):
        self.chargesLeft=3 # Charges Left
        self.name=name # Player's username
        self.pokemons=[]
        self.startIndex=0
    def addPokemon(self,pokemon:Pokemon):self.pokemons.append(pokemon)
    def setcharge(self,charge:int)->int:self.chargesLeft=charge
    def getCharge(self):return self.chargesLeft
    def setStartIndex(self,index:int):self.startIndex=index
    def returnStartIndex(self)->int:return self.startIndex
    def getPokemonCount(self)->str:return ['1st','2nd','3rd'][self.startIndex]