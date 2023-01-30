from func import path;from tkinter import Tk, Canvas, Button, PhotoImage # Library Imports
import start,func
def startGUI():
    # Initialization
    window=Tk()
    window.geometry('600x600')
    window.configure(bg='#FFF')

    # Create Canvas
    canvas=Canvas(window,bg='#FFF',height=600,width=600,bd=0,highlightthickness=0,relief='ridge')
    canvas.place(x=0, y=0)

    # Create GUI background
    bgImg=PhotoImage(file=path('bg.png'))
    canvas.create_image(300, 300, image=bgImg)

    # Starter pokemon
    canvas.create_text(60,38,anchor='nw',text=f'Choose your {start.getPokemonCount()} starter pokemon!',fill='#FFF',font=('Inter',-31))

    # Create pokemon image
    POKEMON_IMAGE=start.generatePokemon()
    img=canvas.create_image(298,200,image=POKEMON_IMAGE)

    # Create 'Confirm Pokemon' button
    coBtn=PhotoImage(file=path('coPoImg.png'))
    Button(image=coBtn,borderwidth=0,highlightthickness=0,command=lambda: start.coBtn(canvas,img),relief='flat').place(x=60,y=325,width=193,height=45)

    # Create 'Change Pokemon' button
    chBtn=PhotoImage(file=path('chPoImg.png'))
    Button(image=chBtn,borderwidth=0,highlightthickness=0,command=lambda:start.chBtn(canvas,img),relief='flat').place(x=347,y=325,width=193,height=45)

    # Change Pokemon's charges algorithm
    canvas.create_text(397,370,anchor='nw',text=f'Charge Left: {start.getCharge()}',fill='#FFF',font=('Inter',-13))

    window.resizable(False,False)# Disable resizing
    window.mainloop() # Display GUI