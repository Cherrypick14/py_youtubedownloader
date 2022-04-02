from tkinter import *
from tkinter import filedialog


#create a screen
screen = Tk()
title = screen.title("Welcome to youtube downloader")

#creating our canvas
canvas = Canvas(screen, width=500, height=500)

#run
canvas.pack()

#adding images and inputs
img_logo = PhotoImage(file="ytubelogo.png")

#resizing the image
logo_img = img_logo.subsample(2, 2)

#addign to canvas
canvas.create_image(250,80, image=img_logo)

# a user gets to see the screen
screen.mainloop()