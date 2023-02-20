from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
ASSETS_PATH=Path(f"{Path(__file__).parent}/assets/battleGUI")
def relative_to_assets(path: str) -> Path:return ASSETS_PATH / Path(path)
window=Tk()
window.geometry("600x600")
window.configure(bg="#FFFFFF")
canvas=Canvas(window,bg="#FFFFFF",height=600,width=600,bd=0,highlightthickness=0,relief="ridge")
canvas.place(x=0, y=0)

# Background
background=PhotoImage(file=relative_to_assets("background.png"))
image_1=canvas.create_image(300,300,image=background)

# Render Self & Enemy Pokemon
my_pokemon=PhotoImage(file=relative_to_assets("my_pokemon.png"))
canvas.create_image(107,107,image=my_pokemon)
enemy_pokemon=PhotoImage(file=relative_to_assets("enemy_pokemon.png"))
canvas.create_image(492,107,image=enemy_pokemon)

# HP Display
canvas.create_text(228,61,anchor="nw",text="100/100",fill="#030242",font=("Inter", -30))
canvas.create_text(228,27,anchor="nw",text="Your HP:",fill="#030242",font=("Inter",-28))
canvas.create_text(228,153,anchor="nw",text="100/100",fill="#030242",font=("Inter", -30))
canvas.create_text(228,119,anchor="nw",text="Enemy HP:",fill="#030242",font=("Inter",-28))

# Ability 1 Button
ability_1=PhotoImage(file=relative_to_assets("Ability_1.png"))
Button(image=ability_1,borderwidth=0,highlightthickness=0,command=lambda: print("Ability 1 used!"),relief="flat").place(x=5,y=217,width=290,height=80)

# Ability 2 Button
ability_2=PhotoImage(file=relative_to_assets("Ability_2.png"))
Button(image=ability_2,borderwidth=0,highlightthickness=0,command=lambda: print("Ability 2 used!"),relief="flat").place(x=305,y=217,width=290,height=80)

# Ability 3 Button
ability_3=PhotoImage(file=relative_to_assets("Ability_3.png"))
Button(image=ability_3,borderwidth=0,highlightthickness=0,command=lambda: print("Ability 3 used!"),relief="flat").place(x=5,y=309,width=290,height=80)

# Ability 4 Button
ability_4=PhotoImage(file=relative_to_assets("Ability_4.png"))
Button(image=ability_4,borderwidth=0,highlightthickness=0,command=lambda: print("Ability 4 used!"),relief="flat").place(x=305,y=309,width=290,height=80)

# History box
canvas.create_rectangle(0,394,600,600,fill="#D9D9D9",outline="")
canvas.create_text(0,394,anchor="nw",text="History 1",fill="#000000",font=("Inter",-21))
canvas.create_text(0,418,anchor="nw",text="History 2",fill="#000000",font=("Inter",-21))
canvas.create_text(0,443,anchor="nw",text="History 3",fill="#000000",font=("Inter",-21))
canvas.create_text(0,468,anchor="nw",text="History 4",fill="#000000",font=("Inter",-21))
canvas.create_text(0,493,anchor="nw",text="History 5",fill="#000000",font=("Inter",-21))
canvas.create_text(0,517,anchor="nw",text="History 6",fill="#000000",font=("Inter",-21))
canvas.create_text(0,544,anchor="nw",text="History 7",fill="#000000",font=("Inter",-21))
canvas.create_text(0,569,anchor="nw",text="History 8",fill="#000000",font=("Inter",-21))

window.resizable(False, False)
window.mainloop()
