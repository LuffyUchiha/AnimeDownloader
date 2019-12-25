import os
import subprocess
from tkinter import *

basePath = "F:\\Anime"


def addElements():
    animeList.delete(1, END)
    dir = os.listdir(os.getcwd())
    for index, folder in enumerate(dir):
        if os.path.isfile(os.getcwd() + "\\" + folder):
            animeList.insert(END, folder)
        else:
            animeList.insert(1, folder)


# def show():
# person_name = name_box.get()
# Label(window, text=person_name).grid(column=0, row=1)
# animeList.delete(0, END)
# animeList.grid(row=2, column=0)


def CurSelect(event):
    widget = event.widget
    selection = widget.curselection()
    picked = widget.get(selection[0])
    if picked == "..":
        os.chdir("..")
        addElements()
    elif os.path.isdir(os.getcwd() + "\\" + picked):
        os.chdir(os.getcwd() + '\\' + picked)
        addElements()
    else:
        p = subprocess.Popen(
            ["C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe", "--fullscreen", os.getcwd() + "\\" + picked])


os.chdir(basePath)
window = Tk()
window.title = "Anime Viewer"
window.geometry('1280x720')
name_box = Entry()
name_box.grid(row=0, column=0)
btn = Button(window, text="Search")
btn.grid(column=1, row=0)
animeList = Listbox(window, height=20, width=500)
animeList.bind('<Double-Button-1>', CurSelect)
animeList.insert(0, "..")
addElements()
animeList.grid(row=2, column=0)

# Code to add widgets will go here...
window.mainloop()
