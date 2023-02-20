from tkinter import Tk,Canvas,Entry,Text,Button,PhotoImage
from func import path
from time import time
from logging import info
def initName():
    global name
    startTime=time()
    def setName(n):
        global name
        name=n
        nameGUI.destroy()
    
    # Init
    nameGUI=Tk()
    nameGUI.title('Enter your Pokemon Trainer Name')
    nameGUI.geometry("600x600")
    nameGUI.configure(bg="#FFFFFF")

    # Create and place canvas
    canvas=Canvas(nameGUI,bg="#FFFFFF",height=600,width=600,bd=0,highlightthickness=0,relief="ridge")
    canvas.place(x=0,y=0)

    # Background Img
    bg=PhotoImage(file=path("bg.png",['assets']))
    canvas.create_image(300,300,image=bg)

    # Name input
    nameInputImg=PhotoImage(file=path("nameInput.png",['assets','nameInput'])) # For input bg
    canvas.create_image(300,300,image=nameInputImg) # Input bg
    nameInput=Entry(bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0) # Input box
    nameInput.place(x=110,y=291,width=380,height=30) # Place input box
    nameInput.bind('<Return>',lambda event:setName(nameInput.get())) #Make enter key submit the name
    canvas.create_text(105,278,anchor="nw",text="Name",fill="#000000",font=("Inter Regular",-13)) # Create input descriptor
    canvas.create_text(35,108,anchor="nw",text="Enter your Pokemon Trainer Name",fill="#FFFFFF",font=("Inter",-35)) # Create input header

    # Settings
    nameGUI.resizable(False,False)
    info(f'Name GUI has successfully started. ({time()-startTime}ms)')
    nameGUI.mainloop()

# Get username
def getName():
    return name