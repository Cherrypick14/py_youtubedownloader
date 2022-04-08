from tkinter import *
from tkinter import filedialog
from tkinter import font
from turtle import width
from PIL import Image,ImageTk
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube

#   define our function
def select_path():
    #choosing the path to select your files
    path = filedialog.askdirectory()
    path_field.config(text = path)

# define our download function
def download_file():
    get_link = link_field.get()
    user_path= path_field.cget("text")
    mp4_video =YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip=VideoFileClip(mp4_video)
    vid_clip.close()

#create a screen
screen = Tk()
title = screen.title("Welcome to youtube downloader")

#creating our canvas
canvas = Canvas(screen, width=500, height=500)

#run
canvas.pack()

#loading an image into script
img_logo = (Image.open("ytubelogo.png"))
#img_logo = PhotoImage(file="ytubelogo.png")

#resizing the image
logo_img = img_logo.resize((300,200), Image.ANTIALIAS)
new_Image=ImageTk.PhotoImage(logo_img)

#logo_img = img_logo.subsample(3, 3)
canvas.create_image(100,20, anchor=NW, image= new_Image)
#addign to canvas
#canvas.create_image(250,80, image=img_logo)

#adding inputs
link_field = Entry(screen, width=50)
link_label = Label(screen, text="You can download your file here! ", font=('Open Sarif', 12))

#creation of our paths for file download x buttons
path_field = Label(screen, text="Select path to download file", font=('Open Sarif', 12))
select_button = Button(screen, text="Select", command=select_path)


#adding them to our window
canvas.create_window(250,250, window= link_field)
canvas.create_window(250,290, window= link_label)
canvas.create_window(250, 330, window= select_button)
canvas.create_window(250, 360, window= path_field)



# download button
btn_download = Button(screen, text="Download")
canvas.create_window(250, 400, window = btn_download, command= download_file)

# a user gets to see the screen
screen.mainloop()