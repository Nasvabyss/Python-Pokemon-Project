import pygame,time,math,random,requests,io;from pygame.locals import*;from urllib.request import urlopen
pygame.init()
game,black,gold,grey,green,red,white=pygame.display.set_mode((500,500)),(0,0,0),(218,165,32),(200,200,200),(0,200,0),(200,0,0),(255,255,255)
pygame.display.set_caption('Pokemon Battle')
class Move():
    def __init__(self,url):
        self.json=requests.get(url).json()
        self.name,self.power,self.type=self.json['name'],self.json['power'],self.json['type']['name']
class Pokemon(pygame.sprite.Sprite):
    def __init__(self,name,lvl,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.json,self.name,self.lvl,self.x,self.y,self.num_potions=requests.get(f'https://pokeapi.co/api/v2/pokemon/{name.lower()}').json(),name,lvl,x,y,3
        for stat in self.json['stats']:
            match (stat['stat']['name']):
                case'hp':self.current_hp,self.maxHp=stat['base_stat']+self.lvl,stat['base_stat']+self.lvl
                case'attack':self.attack=stat['base_stat']
                case'defense':self.defense=stat['base_stat']
                case'speed':self.speed=stat['base_stat']
        self.types,self.size=[self.json['types'][i]['type']['name']for i in range(len(self.json['types']))],150
        self.setSprite('front_default')
    def doAtk(self,other,move):
        displayMsg(f'{self.name} used {move.name}')
        time.sleep(2)
        dmg=(2*self.lvl+10)/250*self.attack/other.defense*move.power
        if move.type in self.types:dmg*=1.5
        if random.randint(1,10000)<=625:dmg*=1.5
        other.takeDmg(math.floor(dmg))
    def takeDmg(self,dmg):self.current_hp=max(self.current_hp-dmg,0)
    def usePotion(self):
        if self.num_potions>0:self.current_hp,self.num_potions=min(self.current_hp+30,self.maxHp),self.num_potions-1
    def setSprite(self,side):
        self.img=pygame.image.load(io.BytesIO(urlopen(self.json['sprites'][side]).read())).convert_alpha()
        scale=self.size/self.img.get_width()
        self.img=pygame.transform.scale(self.img,(self.img.get_width()*scale,self.img.get_height()*scale))
    def setMoves(self):
        self.moves=[]
        for i in range(len(self.json['moves'])):
            versions=self.json['moves'][i]['version_group_details']
            for j in range(len(versions)):
                if versions[j]['version_group']['name']!='red-blue':continue
                if versions[j]['move_learn_method']['name']!='level-up':continue
                if self.lvl>=versions[j]['level_learned_at']:
                    move=Move(self.json['moves'][i]['move']['url'])
                    if move.power!=None:self.moves.append(move)
        if len(self.moves)>4:self.moves=random.sample(self.moves,4)
    def draw(self,alpha=255):
        sprite=self.img.copy()
        sprite.fill((255,255,255,alpha),None,pygame.BLEND_RGBA_MULT)
        game.blit(sprite,(self.x,self.y))
    def drawHp(self):
        barScale=200//self.maxHp
        for i in range(self.maxHp):pygame.draw.rect(game,red,(self.hpX+barScale*i,self.hpY,barScale,20))
        for i in range(self.current_hp):pygame.draw.rect(game,green,(self.hpX+barScale*i,self.hpY,barScale,20))
        font=pygame.font.Font(pygame.font.get_default_font(),16)
        text=font.render(f'HP: {self.current_hp}/{self.maxHp}',True,black)
        textRect=text.get_rect()
        textRect.x,textRect.y=self.hpX,self.hpY+30
        game.blit(text,textRect)
    def getRect(self):return Rect(self.x,self.y,self.img.get_width(),self.img.get_height())
def displayMsg(message):
    pygame.draw.rect(game,white,(10,350,480,140))
    pygame.draw.rect(game,black,(10,350,480,140),3)
    font=pygame.font.Font(pygame.font.get_default_font(),20)
    text=font.render(message,True,black)
    textRect=text.get_rect()
    textRect.x,textRect.y=30,410
    game.blit(text,textRect)
    pygame.display.update()
def createBtn(width,height,left,top,textCx,textCy,label):
    button=Rect(left,top,width,height)
    pygame.draw.rect(game,gold if button.collidepoint(pygame.mouse.get_pos())else white,button)
    font=pygame.font.Font(pygame.font.get_default_font(),16)
    text=font.render(label,True,black)
    game.blit(text,text.get_rect(center=(textCx,textCy)))
    return button
bulbasaur,charmander,squirtle=Pokemon('Bulbasaur',30,25,150),Pokemon('Charmander',30,175,150),Pokemon('Squirtle',30,325,150)
pokemons,playerPokemon,rivalPokemon,gameStatus=[bulbasaur,charmander,squirtle],None,None,'select pokemon'
while gameStatus!='quit':
    for event in pygame.event.get():
        if event.type==QUIT:gameStatus='quit'
        if event.type==KEYDOWN:
            if event.key==K_y:
                bulbasaur=Pokemon('Bulbasaur',30,25,150)
                charmander=Pokemon('Charmander',30,175,150)
                squirtle=Pokemon('Squirtle',30,325,150)
                pokemons=[bulbasaur,charmander,squirtle]
                gameStatus='select pokemon'
            elif event.key==K_n:gameStatus='quit'
        if event.type==MOUSEBUTTONDOWN:
            mouseClick=event.pos
            if gameStatus=='select pokemon':
                for i in range(len(pokemons)):
                    if pokemons[i].getRect().collidepoint(mouseClick):
                        playerPokemon,rivalPokemon=pokemons[i],pokemons[(i+1)%len(pokemons)]
                        rivalPokemon.lvl=int(rivalPokemon.lvl*.75)
                        playerPokemon.hpX,playerPokemon.hpY,rivalPokemon.hpX,rivalPokemon.hpY,gameStatus=275,250,50,50,'prebattle'
            elif gameStatus=='playerTurn':
                if fight_button.collidepoint(mouseClick):gameStatus='player move'
                if potion_button.collidepoint(mouseClick):
                    if playerPokemon.num_potions==0:
                        displayMsg('No more potions left')
                        gameStatus='player move'
                    else:
                        playerPokemon.usePotion()
                        displayMsg(f'{playerPokemon.name} used potion')
                        gameStatus='rivalTurn'
                    time.sleep(2)
            elif gameStatus=='player move':
                for i in range(len(moveBtns)):
                    if moveBtns[i].collidepoint(mouseClick):
                        playerPokemon.doAtk(rivalPokemon,playerPokemon.moves[i])
                        gameStatus='fainted'if rivalPokemon.current_hp==0 else'rivalTurn'
    if gameStatus=='select pokemon':
        game.fill(white)
        bulbasaur.draw()
        charmander.draw()
        squirtle.draw()
        mouse_cursor=pygame.mouse.get_pos()
        for pokemon in pokemons:
            if pokemon.getRect().collidepoint(mouse_cursor):pygame.draw.rect(game,black,pokemon.getRect(),2)
        pygame.display.update()
    if gameStatus=='prebattle':
        game.fill(white)
        playerPokemon.draw()
        pygame.display.update()
        playerPokemon.setMoves()
        rivalPokemon.setMoves()
        playerPokemon.x=-50
        playerPokemon.y=100
        rivalPokemon.x=250
        rivalPokemon.y=-50
        playerPokemon.size=300
        rivalPokemon.size=300
        playerPokemon.setSprite('back_default')
        rivalPokemon.setSprite('front_default')
        gameStatus='start'
    if gameStatus=='start':
        alpha=0
        while alpha<255:
            game.fill(white)
            rivalPokemon.draw(alpha)
            displayMsg(f'Rival sent out {rivalPokemon.name}!')
            alpha+=.4
            pygame.display.update()
        time.sleep(1)
        alpha=0
        while alpha<255:
            game.fill(white)
            rivalPokemon.draw()
            playerPokemon.draw(alpha)
            displayMsg(f'Go {playerPokemon.name}!')
            alpha+=.4
            pygame.display.update()
        playerPokemon.drawHp()
        rivalPokemon.drawHp()
        gameStatus='rivalTurn'if rivalPokemon.speed>playerPokemon.speed else'playerTurn'
        pygame.display.update()
        time.sleep(1)
    if gameStatus=='playerTurn':
        game.fill(white)
        playerPokemon.draw()
        rivalPokemon.draw()
        playerPokemon.drawHp()
        rivalPokemon.drawHp()
        fight_button=createBtn(240,140,10,350,130,412,'Fight')
        potion_button=createBtn(240,140,250,350,370,412,f'Use Potion ({playerPokemon.num_potions})')
        pygame.draw.rect(game,black,(10,350,480,140),3)
        pygame.display.update()
    if gameStatus=='player move':
        game.fill(white)
        playerPokemon.draw()
        rivalPokemon.draw()
        playerPokemon.drawHp()
        rivalPokemon.drawHp()
        moveBtns=[]
        for i in range(len(playerPokemon.moves)):
            move=playerPokemon.moves[i]
            button_width=240
            button_height=70
            left=10+i%2*button_width
            top=350+i//2*button_height
            text_center_x=left+120
            text_center_y=top+35
            button=createBtn(button_width,button_height,left,top,text_center_x,text_center_y,move.name.capitalize())
            moveBtns.append(button)
        pygame.draw.rect(game,black,(10,350,480,140),3)
        pygame.display.update()
    if gameStatus=='rivalTurn':
        game.fill(white)
        playerPokemon.draw()
        rivalPokemon.draw()
        playerPokemon.drawHp()
        rivalPokemon.drawHp()
        displayMsg('')
        time.sleep(2)
        move=random.choice(rivalPokemon.moves)
        rivalPokemon.doAtk(playerPokemon,move)
        gameStatus='fainted'if playerPokemon.current_hp==0 else'playerTurn'
        pygame.display.update()
    if gameStatus=='fainted':
        alpha=255
        while alpha > 0:
            game.fill(white)
            playerPokemon.drawHp()
            rivalPokemon.drawHp()
            if rivalPokemon.current_hp==0:
                playerPokemon.draw()
                rivalPokemon.draw(alpha)
                displayMsg(f'{rivalPokemon.name} fainted!')
            else:
                playerPokemon.draw(alpha)
                rivalPokemon.draw()
                displayMsg(f'{playerPokemon.name} fainted!')
            alpha-=.4
            pygame.display.update()
        gameStatus='gameover'
    if gameStatus=='gameover':displayMsg('Play again (Y/N)?')
pygame.quit()