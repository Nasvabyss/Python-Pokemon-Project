# Pick 3 characters
# Player's characters from top down
# AI chooses player's characters, uses random position.
# Dmg Calc: Attacker Atk + (Attacker Special Atk Range) - Enemy Def - (Enemy Special Def Range) 
# Enemy HP reduced by calc dmg
# Own xp increased by calc dmg
# Enemy xp increased by def pt
# If dmg calc >10, xp gained = 120%
# If dmg calc <=0, xp gained = 150%
# Character evo at 100, add 1 for every stat if unable to
# Remove char if hp <=0
# Allow player to select which chars attack which enemy char
# AI randomly picks player char from AI char top down
fileName='pokemonInfoList-1673586123.txt'
class Pokemon:
    def __init__(self,name,atk,defe,satk,sdef,spd,types,weaknesses):
        if len(types)==1:types=str(types)
        if len(weaknesses)==1:weaknesses=str(weaknesses)
        self.name,self.atk,self.defe,self.satk,self.sdef,self.spd,self.types,self.weaknesses,self.evo=name,atk,defe,satk,sdef,spd,types,weaknesses,None
    def getName(self):return self.name
    def getAtk(self):return self.atk,satk
    def getDef(self):return self.defe,sdef
    def getSpd(self):return self.spd
    def getTypes(self):return self.types
    def getWeaknesses(self):return self.weaknesses
    def setEvo(self,evo):self.evo=evo
    def getEvo(self):return self.evo
class Player:
    def __init__(self,pokemon:__main__.Pokemon):
        Player.count=1 if hasattr(Player, 'count') else Player.count+1
        self.count,self.name,self.atk,self.defe,self.satk,self.sdef,self.spd,self.types,self.weaknesses,
        self.evo=Player.count,pokemon.getName(),pokemon.getAtk()[0],pokemon.getAtk()[1],pokemon.getDef()[0],
        pokemon.getDef()[1],pokemon.getSpd(),pokemon.getTypes(),pokemon.getWeaknesses(),pokemon.getevo()
    def evolvePokemon(self,nxtPokemon:__main__.Pokemon):
        if type(self.evo)is None: self.atk,self.defe,self.satk,self.sdef,self.spd=self.atk+1,self.defe+1,self.satk+1,self.sdef+1,self.spd+1
        else:
            self.name,self.atk,self.defe,self.satk,self.sdef,self.spd,self.types,self.weakness,
            self.evo=nxtPokemon.getName(),nxtPokemon.getAtk()[0],nxtPokemon.getAtk()[1],nxtPokemon.getDef()[0],
            nxtPokemon.getDef()[1],nxtPokemon.getSpd(),nxtPokemon.getTypes(),nxtPokemon.getWeaknesses(),nxtPokemon.getevo()
        
with open(fileName,'r',encoding='utf-8') as f:
    pokemons={}
    for pokemon in list(f):
        count=pokemon[:3]
        name=pokemon[4:23].strip()
        stats=pokemon[25:34].split(' ')
        types=pokemon[41:71].strip().split('|')
        weaknesses=pokemon[72:].replace('\n','').strip().split('|')
        pokemons[count]=Pokemon(name,stats[0],stats[1],stats[2],stats[3],stats[4],types,weaknesses)
        #print(count,name,stats,types,weaknesses)
    
