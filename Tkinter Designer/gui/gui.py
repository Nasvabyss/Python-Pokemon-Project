import re,sys,os,tkinter as tk,tkinter.messagebox as tk1,tkinter.filedialog;from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent.parent)),
try:from tkdesigner.designer import Designer
except ModuleNotFoundError:raise RuntimeError('Couldn\'t add tkdesigner to the PATH.')
ASSETS_PATH=Path(__file__).resolve().parent/'assets'
path=getattr(sys,'_MEIPASS',os.getcwd())
os.chdir(path)
output_path=''
def btn_clicked():
    token=token_entry.get()
    URL=URL_entry.get()
    output_path=path_entry.get()
    output_path=output_path.strip()
    if not token:
        tk.messagebox.showerror(title='Empty Fields!',message='Please enter Token.')
        return
    if not URL:
        tk.messagebox.showerror(title='Empty Fields!',message='Please enter URL.')
        return
    if not output_path:
        tk.messagebox.showerror( title='Invalid Path!',message='Enter a valid output path.')
        return
    match=re.search(r'https://www.figma.com/file/([0-9A-Za-z]+)',URL.strip())
    if match is None:
        tk.messagebox.showerror('Invalid URL!','Please enter a valid file URL.')
        return
    file_key=match[1].strip()
    token=token.strip()
    output=Path(output_path+'/build').expanduser().resolve()
    if output.exists() and not output.is_dir():tk1.showerror(f'Exists! {output} already exists and is not a directory.\nEnter a valid output directory.')
    elif output.exists()and output.is_dir()and tuple(output.glob('*')):
        if not tk1.askyesno(f'Continue? Directory {output} is not empty.\nDo you want to continue and overwrite?'): return
    Designer(token,file_key,output).design()
    tk.messagebox.showinfo('Success!',f'Project successfully generated at {output}.')
def select_path():
    global output_path
    output_path=tk.filedialog.askdirectory()
    path_entry.delete(0,tk.END)
    path_entry.insert(0,output_path)
def make_label(master,x,y,h,w,*args,**kwargs):
    f=tk.Frame(master,height=h,width=w)
    f.pack_propagate(0)
    f.place(x=x,y=y)
    return tk.Label(f,*args,**kwargs).pack(fill=tk.BOTH,expand=1)
window=tk.Tk()
logo=tk.PhotoImage(file=ASSETS_PATH/'iconbitmap.gif')
window.call('wm','iconphoto',window._w,logo)
window.title('Tkinter Designer')
window.geometry('862x519')
window.configure(bg='#3A7FF6')
canvas=tk.Canvas(window,bg='#3A7FF6',height=519,width=862,bd=0,highlightthickness=0,relief='ridge')
canvas.place(x=0,y=0)
canvas.create_rectangle(431,0,862,519,fill='#FCFCFC',outline='')
canvas.create_rectangle(40,160,100,160 + 5,fill='#FCFCFC',outline='')
tk.PhotoImage(file=ASSETS_PATH/'TextBox_Bg.png')
canvas.create_image(650.5,167.5,image=text_box_bg)
canvas.create_image(650.5,248.5,image=text_box_bg)
canvas.create_image(650.5,329.5,image=text_box_bg)
token_entry=tk.Entry(bd=0,bg='#F6F7F9',fg='#000716',highlightthickness=0)
token_entry.place(x=490.0,y=137+25,width=321.0,height=35)
token_entry.focus()
tk.Entry(bd=0,bg='#F6F7F9',fg='#000716',highlightthickness=0).place(x=490.0,y=218+25,width=321.0,height=35)
tk.Entry(bd=0,bg='#F6F7F9',fg='#000716',highlightthickness=0).place(x=490.0,y=299+25,width=321.0,height=35)
path_picker_img=tk.PhotoImage(file=ASSETS_PATH / 'path_picker.png')
tk.Button(image=path_picker_img,text='',compound='center',fg='white',borderwidth=0,highlightthickness=0,command=select_path,relief='flat').place(x=783,y=319,width=24,height=22)
canvas.create_text(490.0,156.0,text='Token ID',fill='#515486',font=('Arial-BoldMT',int(13.0)),anchor='w')
canvas.create_text(490.0,234.5,text='File URL',fill='#515486',font=('Arial-BoldMT',int(13.0)),anchor='w')
canvas.create_text(490.0,315.5,text='Output Path',fill='#515486',font=('Arial-BoldMT',int(13.0)),anchor='w')
canvas.create_text(646.5,428.5,text='Generate',fill='#FFFFFF',font=('Arial-BoldMT',int(13.0)))
canvas.create_text(573.5,88.0,text='Enter the details.',fill='#515486',font=('Arial-BoldMT',int(22.0)))
tk.Label(text='Welcome to Tkinter Designer',bg='#3A7FF6',fg='white',font=('Arial-BoldMT',int(20.0))).place(x=27.0,y=120.0)
tk.Label(text='Tkinter Designer uses the Figma API\nto analyse a design file,then creates\nthe respective code and files needed\nfor your GUI.\n\nEven this GUI was created\nusing Tkinter Designer.',bg='#3A7FF6',fg='white',justify='left',font=('Georgia',int(16.0))).place(x=27.0,y=200.0)
generate_btn_img=tk.PhotoImage(file=ASSETS_PATH / 'generate.png')
tk.Button(image=generate_btn_img,borderwidth=0,highlightthickness=0,command=btn_clicked,relief='flat').place(x=557,y=401,width=180,height=55)
window.resizable(False,False)
window.mainloop()
