from classes import Player
from func import path, generatePokemon
from tkinter import Tk, Canvas, Button, PhotoImage  # For GUI
from time import time  # Display startup time of program
from logging import info


def startGUI(name, startTime, pokemons):
    global canvas, pokemonImg, generatedPokemon, player, pokemonList, currentPokemonCount, chargeText, counterText, pokemonPicker
    pokemonList = pokemons
    pokemonPicker = Tk()
    pokemonPicker.geometry('600x600')
    pokemonPicker.configure(bg='#FFF')
    player = Player(name=name)

    # Create Canvas
    canvas = Canvas(pokemonPicker, bg='#FFF', height=600,
                    width=600, bd=0, highlightthickness=0, relief='ridge')
    canvas.place(x=0, y=0)

    # Create GUI background
    bgImg = PhotoImage(file=path('bg.png', ['assets']))
    canvas.create_image(300, 300, image=bgImg)

    # Starter pokemon text
    counterText = canvas.create_text(
        60, 38, anchor='nw', text=f'Choose your {player.getPokemonCount()} starter pokemon!', fill='#FFF', font=('Inter', -31))

    # Create pokemon image
    currentPokemonCount, generatedPokemon = generatePokemon()
    pokemonImg = canvas.create_image(298, 200, image=generatedPokemon)

    # Create 'Confirm Pokemon' button
    coBtn = PhotoImage(file=path('coPoImg.png', ['assets', 'startGUI']))
    Button(image=coBtn, borderwidth=0, highlightthickness=0, command=lambda: togglePokemon(
        'Confirm'), relief='flat').place(x=60, y=325, width=193, height=45)

    # Create 'Change Pokemon' button
    chBtn = PhotoImage(file=path('chPoImg.png', ['assets', 'startGUI']))
    Button(image=chBtn, borderwidth=0, highlightthickness=0, command=lambda: togglePokemon(
        'Change'), relief='flat').place(x=347, y=325, width=193, height=45)

    # Change Pokemon's charges algorithm
    chargeText = canvas.create_text(397, 370, anchor='nw',
                                    text=f'Charges Left: {player.chargesLeft}', fill='#FFF', font=('Inter', -13))

    pokemonPicker.resizable(False, False)  # Disable resizing
    info(f'Start GUI has successfully started. ({time()-startTime}ms)')
    pokemonPicker.mainloop()  # Display GUI


def togglePokemon(button):
    info(f'The user has pressed the {button} button')
    if button.lower() == 'confirm':  # Check if user pressed the confirm button
        # Append pokemon object to player
        player.pokemons.append(pokemonList[currentPokemonCount])
        player.startIndex += 1  # Increment the index by 1
        if player.startIndex == 3:  # If they have chosen 3 pokemon
            del player.startIndex, player.chargesLeft  # Delete useless variables
            info('Player has successfully chosen their 3 pokemon.')
            return pokemonPicker.destroy()  # Exit the GUI
    elif button.lower() == 'change':
        if player.chargesLeft <= 0:
            return
        player.chargesLeft -= 1
        canvas.itemconfig(chargeText,
                          text=f'Charges Left: {player.chargesLeft}')
        info(f'Player has {player.chargesLeft} charges remaining')
    changePokemon()
    canvas.itemconfig(counterText,
                      text=f'Choose your {player.getPokemonCount()} starter pokemon!')


def changePokemon():
    global currentPokemonCount, generatedPokemon
    currentPokemonCount, generatedPokemon = generatePokemon()
    canvas.itemconfig(pokemonImg, image=generatedPokemon)
