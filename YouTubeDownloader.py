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

Label(root, text = 'Paste link Here:', font = 'arial 15 bold').pack()#.place(x = 200 , y = 60)
link_enter = Entry(root, width = 70, textvariable = link).pack()#.place(x = 60, y = 90)


# Create Function to Start Downloading
def Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').pack()#.place(x = 180, y = 210)

Button(root, text = 'DOWNLOAD', font = 'arial 15 bold' , bg = 'pale violet red', padx = 2, command = Downloader).place(x = 180, y = 150)
root.mainloop()
