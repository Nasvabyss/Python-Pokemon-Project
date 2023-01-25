from func import path;from tkinter import Tk, Canvas, Button, PhotoImage # Library Imports
import start
# Initialization
window=Tk()
player=start.Player()
window.geometry('600x600')
window.configure(bg='#FFF')

# Create Canvas
canvas=Canvas(window,bg='#FFF',height=600,width=600,bd=0,highlightthickness=0,relief='ridge')
canvas.place(x=0, y=0)

#Create GUI background
bgImg=PhotoImage(file=path('bg.png'))
canvas.create_image(300.0,300.0,image=bgImg)

# Create title
starterPokemon=player.getPokemonCount()
canvas.create_text(156.0,152.0,anchor='nw',text=f'Starter Pokemon: {starterPokemon}',fill='#FFF',font=('Inter',-32))

#Pokemon Generated
pokemonGenPath = start.getStarterPokemon()
pmGenImg=PhotoImage(file=pokemonGenPath)
canvas.create_image(299.0,270.0,image=pmGenImg)

# Create 'Confirm Pokemon' button
cfmPmImg=PhotoImage(file=path('button_2.png'))
Button(image=cfmPmImg,borderwidth=0,highlightthickness=0,command=start.confirmPokemon,relief='flat').place(x=208.0,y=349.0,width=193.0,height=45.0)

# Create 'Change Pokemon' button
button_image_1=PhotoImage(file=path('button_1.png'))
Button(image=button_image_1,borderwidth=0,highlightthickness=0,command=start.changePokemon,relief='flat').place(x=208.0,y=403.0,width=193.0,height=44.0)

# Change Pokemon's charges algorithm
chargeLeft=3
canvas.create_text(255.0,429.0,anchor='nw',text=f'Charge Left: {chargeLeft}',fill='#FFF',font=('Inter',-13))# Create 'Charge Left' text

window.resizable(False, False)# Disable resizing
window.mainloop() # Display GUI