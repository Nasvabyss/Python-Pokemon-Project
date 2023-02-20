from tkinter import Tk,Canvas,Entry,Text,Button,PhotoImage
from func import path
def initName():
    def setName(n):
        global name
        name=n
        window.destroy()
    # Init
    window=Tk()
    window.geometry("600x600")
    window.configure(bg="#FFFFFF")
    canvas=Canvas(window,bg="#FFFFFF",height=600,width=600,bd=0,highlightthickness=0,relief="ridge")
    canvas.place(x=0,y=0)

    # Background Img
    bg=PhotoImage(file=path("bg.png",['assets']))
    canvas.create_image(300,300,image=bg)

    # Name input
    name_input_img=PhotoImage(file=path("nameInput.png",['assets','nameInput']))
    canvas.create_image(300,300,image=name_input_img)
    name_input=Entry(bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0)
    name_input.place(x=110,y=291,width=380,height=30)

    #Make enter key submit the name
    name_input.bind('<Return>',lambda event:setName(name_input.get()))

    # Name input descriptor
    canvas.create_text(105,278,anchor="nw",text="Name",fill="#000000",font=("Inter Regular",-13))

    # Name input header
    canvas.create_text(114,108,anchor="nw",text="What is your name?",fill="#FFFFFF",font=("Inter",-40))

    # Settings
    window.resizable(False,False)
    window.mainloop()

# Get username
def getName():
    return name