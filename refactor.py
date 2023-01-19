from pathlib import Path;from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
def path(path: str) -> Path:return Path(f"{Path(__file__).parent}\assets{path}")
def startGUI():