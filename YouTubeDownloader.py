# YouTube Downloader

# Import Libraries
from tkinter import *
from pytube import YouTube


# Create Display Window
root = Tk()
root.geometry('600x300')
root.resizable(0,0)
root.title("Chisoft-YouTube-Downloader")
Label(root, text = 'Youtube Video Downloader', font = 'arial 20 bold').pack()

# Create Field to Enter Link
link = StringVar()

Label(root, text = 'Paste link Here:', font = 'arial 15 bold').place(x = 160 , y = 60)
link_enter = Enter(root, width = 70, textvariable = link).place(x = 32, y = 90)
