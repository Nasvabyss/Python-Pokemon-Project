from tkinter import Tk, Canvas, Button, PhotoImage # For GUI
from func import path,imgCreator,generatePokemon
from datetime import datetime # Display startup time of program
from classes import Pokemon,Player
startTime=datetime.now().strftime('%H:%M:%S')
### INIT ###
chargesLeft=3
FILE_PATH=path("pokemonInformation-1674801501.txt",['assets'])
MAX_POKEMON=240

def togglePokemon(canvas,var,button):
    print(button,'pressed!')
    randomImage=generatePokemon()
    canvas.itemconfig(var,image=randomImage)


# STORE POKEMON INFO IN POKEMONS VARIABLE
with open(FILE_PATH,'r',encoding='utf-8') as f:
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
### INIT ###


### Pokemon Picker GUI ###

# Initialization

pokemonPicker=Tk()
pokemonPicker.geometry('600x600')
pokemonPicker.configure(bg='#FFF')
player=Player(name='John Doe')
pokemonList = [generatePokemon()for _ in range(6)] # Calculated 6 by (noOfStartingPokemon+chargesLeft)

# Create Canvas
canvas=Canvas(pokemonPicker,bg='#FFF',height=600,width=600,bd=0,highlightthickness=0,relief='ridge')
canvas.place(x=0, y=0)

# Create GUI background
bgImg=PhotoImage(file=path('bg.png',['assets']))
canvas.create_image(300, 300, image=bgImg)

# Starter pokemon text
canvas.create_text(60,38,anchor='nw',text=f'Choose your {player.getPokemonCount()} starter pokemon!',fill='#FFF',font=('Inter',-31))

# Create pokemon image
pokemonImg=generatePokemon()
img=canvas.create_image(298,200,image=pokemonImg)
canvas.itemconfig()

# Create 'Confirm Pokemon' button
coBtn=PhotoImage(file=path('coPoImg.png',['assets','startGUI']))
Button(image=coBtn,borderwidth=0,highlightthickness=0,command=lambda:togglePokemon(canvas,img,'Confirm Pokemon'),relief='flat').place(x=60,y=325,width=193,height=45)

# Create 'Change Pokemon' button
chBtn=PhotoImage(file=path('chPoImg.png',['assets','startGUI']))
Button(image=chBtn,borderwidth=0,highlightthickness=0,command=lambda:togglePokemon(canvas,img,'Change Pokemon'),relief='flat').place(x=347,y=325,width=193,height=45)

# Change Pokemon's charges algorithm
canvas.create_text(397,370,anchor='nw',text=f'Charge Left: {player.getCharge()}',fill='#FFF',font=('Inter',-13))

pokemonPicker.resizable(False,False)# Disable resizing
print(f'Took {datetime.strptime(datetime.now().strftime("%H:%M:%S"),"%H:%M:%S")-datetime.strptime(startTime,"%H:%M:%S")} to start the program.')
pokemonPicker.mainloop() # Display GUI
### START GUI ###