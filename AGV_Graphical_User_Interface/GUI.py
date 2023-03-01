from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image  
from tkinter import messagebox

#define variable to handle the class Tk
root = Tk()

root.geometry('800x600')
root.minsize(640,480)

def start_button_click():
    print("robot has started")

def stop_button_click():
    print("robot is stopped") 

def pause_button_click():
    print("robot process suspended")       



# load a picture1 and make it as a click button
im=PhotoImage(file="heading.png")
start_btn1=Button(root,text="Start",bg="yellow",fg="green",font=("arial",25,"bold"),activebackground="blue",
            width="250",height="250",anchor=NE,cursor="circle",activeforeground="black",bd=3,relief=RIDGE,
            image=im)

# load a picture2 and make it as a click button
im_1=PhotoImage(file="stop256.png")
start_btn2=Button(root,text="Start",bg="yellow",fg="green",font=("arial",25,"bold"),activebackground="blue",
            width="250",height="250",anchor=NE,cursor="circle",activeforeground="black",bd=3,relief=RIDGE,
            image=im_1)

# load a picture3 and make it as a click button
im_2=PhotoImage(file="pause.png")
start_btn3=Button(root,text="Start",bg="yellow",fg="green",font=("arial",25,"bold"),activebackground="blue",
            width="250",height="250",anchor=NE,cursor="circle",activeforeground="black",bd=3,relief=RIDGE,
            image=im_2)


# load a picture4 just for display
load = Image.open("demopic.png")
render = ImageTk.PhotoImage(load)
im_3 = Label(image=render)
im_3.place(x=420, y=320)

# Make the buttons interactive

button_start = tk.Button(root, start_btn1, command=start_button_click)
button_start.pack()
button_start.place(x=200,y=5)

button_stop = tk.Button(root, start_btn2, command=stop_button_click)
button_stop.pack()
button_stop.place(x=650,y=5)

button_pause = tk.Button(root, start_btn3, command=pause_button_click)
button_pause.pack()
button_pause.place(x=1080,y=5)

root.mainloop()
