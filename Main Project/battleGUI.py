from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from PIL import Image
from func import path, flipImg, imgCreator
from time import time
from logging import info

def battleGUI():
    startTime=time()
    window = Tk()
    window.geometry("600x600")
    window.configure(bg="#FFFFFF")
    canvas = Canvas(window, bg="#FFFFFF", height=600, width=600,
                    bd=0, highlightthickness=0, relief="ridge")
    canvas.place(x=0, y=0)
    # Background
    background = PhotoImage(file=path("bg.png", ['assets']))
    image_1 = canvas.create_image(300, 300, image=background)
    # Render Self Pokemon
    # my_pokemon=flipImg(imgCreator('bulbasaur',True))
    # canvas.create_image(107, 107, image=my_pokemon)
    # enemy_pokemon = imgCreator('bulbasaur')
    # canvas.create_image(492, 107, image=enemy_pokemon)

    # HP Display
    canvas.create_text(228, 61, anchor="nw", text="100/100",
                       fill="#0c38c8", font=("Inter", -30))
    canvas.create_text(228, 27, anchor="nw", text="Your HP:",
                       fill="#0c38c8", font=("Inter", -28))
    canvas.create_text(228, 153, anchor="nw", text="100/100",
                       fill="#0c38c8", font=("Inter", -30))
    canvas.create_text(228, 119, anchor="nw", text="Enemy HP:",
                       fill="#0c38c8", font=("Inter", -28))

    # Ability 1 Button
    Button(text='Ability 1',font=("Inter",22),bg='#607EEB',fg="#fff",borderwidth=0, highlightthickness=0,command=lambda: print(
        "Ability 1 used!",), relief="flat").place(x=5, y=217, width=290, height=80)

    # Ability 2 Button
    Button(text='Ability 2',font=("Inter",22),bg='#607EEB',fg="#fff", borderwidth=0, highlightthickness=0, command=lambda: print(
        "Ability 2 used!"), relief="flat").place(x=305, y=217, width=290, height=80)

    # Ability 3 Button
    Button(text='Ability 3',font=("Inter",22),bg='#607EEB',fg="#fff", borderwidth=0, highlightthickness=0, command=lambda: print(
        "Ability 3 used!"), relief="flat").place(x=5, y=309, width=290, height=80)

    # Ability 4 Button
    Button(text='Ability 4',font=("Inter",22),bg='#607EEB',fg="#fff", borderwidth=0, highlightthickness=0, command=lambda: print(
        "Ability 4 used!"), relief="flat").place(x=305, y=309, width=290, height=80)

    # History box
    canvas.create_rectangle(0, 394, 600, 600, fill="#D9D9D9", outline="")
    for i in range(1, 10):
        canvas.create_text(1, 372.5+22.5*i, anchor="nw",
                           text=f"History line {i}", fill="#000000", font=("Inter", -22))

    window.resizable(False, False)
    info(f'Battle GUI has successfully started ({time()-startTime}ms)')
    window.mainloop()
battleGUI()