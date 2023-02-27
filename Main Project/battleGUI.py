from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from PIL import Image
from func import path, flipImg, imgCreator
from time import time
from logging import info
from random import shuffle, randint, random


def battleGUI(player):
    # sourcery skip: bin-op-identity, inline-variable, move-assign-in-block
    global playerAbilities, abilityBtn, playerPokemons, hp, canvas, playerPokeCount, compPokemons, history, compPokeCount, gameOver, playerPokemonId, compPokemonId, compAbilities
    startTime = time()
    playerPokemons = player.pokemons
    playerPokeCount = 1  # Set player's current pokemon to their first pokemon
    compPokeCount = 1  # Set computer's current pokemon to first pokemon
    gameOver = False
    playerAbilities = [
        [
            {
                'name': moveset['name'],
                'type': moveset['type'],
                'power':moveset['power'],
                'accuracy':moveset['accuracy']
            }
            for moveset in pokemon.movesets
        ]
        for pokemon in playerPokemons
    ]
    # Get a randomized integer list
    randomIntList = list(range(3))
    shuffle(randomIntList)
    # Initialize computer pokemon and abilities
    compAbilities = [playerAbilities[_] for _ in randomIntList]
    compPokemons = [playerPokemons[_] for _ in randomIntList]
    # Battle GUI
    window = Tk()
    window.geometry('600x600')
    window.configure(bg='#FFFFFF')
    canvas = Canvas(window, bg='#FFFFFF', height=600, width=600,
                    bd=0, highlightthickness=0, relief='ridge')
    canvas.place(x=0, y=0)

    # Background
    background = PhotoImage(file=path('bg.png', ['assets']))
    canvas.create_image(300, 300, image=background)

    # Render pokemon images
    playerPokemonImg = flipImg(imgCreator(
        playerPokemons[playerPokeCount-1].name, True))
    playerPokemonId = canvas.create_image(107, 107, image=playerPokemonImg)
    compPokemonImg = imgCreator(compPokemons[compPokeCount-1].name)
    compPokemonId = canvas.create_image(492, 107, image=compPokemonImg)

    # HP Headers
    canvas.create_text(228, 27, anchor='nw', text='Your HP:',
                       fill='#000', font=('Inter', -28))
    canvas.create_text(228, 119, anchor='nw', text='Enemy HP:',
                       fill='#000', font=('Inter', -28))
    # HP variables
    hp = {
        'player': canvas.create_text(228, 61, anchor='nw', text='100/100',
                                     fill='#040243', font=('Inter', -30)),
        'comp': canvas.create_text(228, 153, anchor='nw', text='100/100',
                                   fill='#040243', font=('Inter', -30))
    }

    # Ability Buttons
    abilityBtn = [Button(text='Ability 1', font=('Inter', 22), bg='#6383F6', fg='#fff', borderwidth=0,
                         highlightthickness=0, command=lambda:useAbility(1), relief='flat'),
                  Button(text='Ability 2', font=('Inter', 22), bg='#6383F6', fg='#fff', borderwidth=0,
                         highlightthickness=0, command=lambda: useAbility(2), relief='flat'),
                  Button(text='Ability 3', font=('Inter', 22), bg='#6383F6', fg='#fff', borderwidth=0,
                         highlightthickness=0, command=lambda: useAbility(3), relief='flat'),
                  Button(text='Ability 4', font=('Inter', 22), bg='#6383F6', fg='#fff', borderwidth=0,
                         highlightthickness=0, command=lambda: useAbility(4), relief='flat')]
    abilityBtn[0].place(x=5, y=217, width=290, height=80)
    abilityBtn[1].place(x=305, y=217, width=290, height=80)
    abilityBtn[2].place(x=5, y=309, width=290, height=80)
    abilityBtn[3].place(x=305, y=309, width=290, height=80)

    # History box
    canvas.create_rectangle(0, 394, 600, 600, fill='#D9D9D9', outline='')
    history = [
        canvas.create_text(1, 372.5 + 22.5 * i, anchor='nw', text=f'History line {i}',
                           fill='#000000', font=('Inter', -22))for i in range(1, 10)
    ]
    window.resizable(False, False)

    # Final initializations
    initPokemon(1, 'player')
    initPokemon(1, 'comp')
    info(f'Started Battle GUI. ({time()-startTime}ms)')
    window.mainloop()


def useAbility(no: int):
    global compPokeCount, gameOver, playerPokeCount
    if gameOver:
        return
    # Random chance to deal damage (Based on accuracy)
    # Damage calculation: Ability Power + Random int (From 0 to Pokemon special atk dmg * Pokemon atk dmg)
    # Player damage algorithm
    dmgDealt = int(playerAbilities[playerPokeCount-1][no-1]['power']) + randint(0, int(playerPokemons[playerPokeCount-1].stats[1])*int(
        playerPokemons[playerPokeCount-1].stats[3])) if random() < int(playerAbilities[playerPokeCount-1][no-1]['accuracy'])/100 else 0
    info(
        f"(Player) {playerPokemons[playerPokeCount-1].name}'s {playerAbilities[playerPokeCount-1][no-1]['name']} dealt {dmgDealt} dmg!")
    historyUpdate(
        f"(Player) {playerPokemons[playerPokeCount-1].name}'s {playerAbilities[playerPokeCount-1][no-1]['name']} dealt {dmgDealt} dmg!")
    compCurrHp = int(canvas.itemcget(
        hp['comp'], 'text').split('/')[0])-dmgDealt
    # If computer hp goes below 0
    if compCurrHp <= 0:
        # Send out pokemon fainted message
        info(f'(Comp) {compPokemons[compPokeCount-1].name} has fainted.')
        historyUpdate(
            f'(Comp) {compPokemons[compPokeCount-1].name} has fainted.')
        if compPokeCount >= 3:
            gameOver = True
            canvas.itemconfig(
                hp['comp'], text=f"0/{int(canvas.itemcget(hp['comp'], 'text').split('/')[1])}")
            info('(Comp) Computer has no usable pokemon. Player wins!')
            return historyUpdate('(Comp) Computer has no usable pokemon. Player wins!')
        compPokeCount += 1  # Increase counter by 1
        # Configure computer's next pokemon
        return initPokemon(compPokeCount, 'comp')
    # Update text with computer's new current hp
    canvas.itemconfig(
        hp['comp'], text=f"{compCurrHp}/{int(canvas.itemcget(hp['comp'], 'text').split('/')[1])}")

    # Computer damage algorithm
    # Computer selects a random ability between 1 and 4
    randomAbility = randint(1, 4)
    if random() < int(compAbilities[compPokeCount-1][randomAbility-1]['accuracy'])/100:
        dmgDealt = int(compAbilities[compPokeCount-1][randomAbility-1]['power']) + randint(0, int(compPokemons[compPokeCount-1].stats[1])*int(
            compPokemons[compPokeCount-1].stats[3]))
    else:
        dmgDealt = 0
    info(f"(Comp) {compPokemons[compPokeCount-1].name}'s {compAbilities[compPokeCount-1][randomAbility-1]['name']} dealt {dmgDealt} dmg!")
    historyUpdate(
        f"(Comp) {compPokemons[compPokeCount-1].name}'s {compAbilities[compPokeCount-1][randomAbility-1]['name']} dealt {dmgDealt} dmg!")
    playerCurrHp = int(canvas.itemcget(
        hp['player'], 'text').split('/')[0])-dmgDealt
    # If player hp goes below 0
    if playerCurrHp <= 0:
        # Send out pokemon fainted message
        info(f'(Player) {playerPokemons[playerPokeCount-1].name} has fainted.')
        historyUpdate(
            f'(Player) {playerPokemons[playerPokeCount-1].name} has fainted.')
        if playerPokeCount >= 3:
            gameOver = True
            canvas.itemconfig(
                hp['player'], text=f"0/{int(canvas.itemcget(hp['player'], 'text').split('/')[1])}")
            info('(Player) Player has no usable pokemon. Computer wins!')
            return historyUpdate('(Player) Player has no usable pokemon. Computer wins!')
        playerPokeCount += 1  # Increase counter by 1
        # Configure computer's next pokemon
        return initPokemon(playerPokeCount, 'player')
    # Update text with computer's new current hp
    canvas.itemconfig(
        hp['player'], text=f"{playerCurrHp}/{int(canvas.itemcget(hp['player'], 'text').split('/')[1])}")


def initPokemon(no: int, trainer: str):  # sourcery skip: remove-pass-elif, switch
    global canvas,playerPokemonId,compPokemonId
    if trainer == 'player':
        # Player initialization
        for count, initName in enumerate(playerAbilities[no-1]):
            abilityBtn[count].config(text=initName['name'])
        # Set current hp to max hp
        playerCurrHp = int(playerPokemons[no-1].stats[0])*100
        # Update hp text
        canvas.itemconfig(
            hp['player'], text=f'{playerCurrHp}/{playerCurrHp}')
        canvas.update()
        
    elif trainer == 'comp':
        compCurrHp = int(compPokemons[no-1].stats[0])*100
        canvas.itemconfig(
            hp['comp'], text=f'{compCurrHp}/{compCurrHp}')
        canvas.update()


def historyUpdate(text: str):
    # Requires its own variable to prevent all lines of history to be overwritten
    newHistory = [canvas.itemcget(history[count], 'text')
                  for count in range(len(history)-1)]
    # Put the new text ontop, push the rest of history text below
    canvas.itemconfig(history[0], text=text)
    for count, rewriteHistory in enumerate(newHistory):
        canvas.itemconfig(history[count+1], text=rewriteHistory)
