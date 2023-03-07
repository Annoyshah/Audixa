import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os


root = Tk()
root.title("Text to speech")
root.geometry("900x450")
root.resizable(False,False)
root.configure(bg="#305065")

engine = pyttsx3.init()

def speaknow():
    global engine 
    text=text_area.get(1.0,END)
    gender = gender_combobox.get()
    speed = speed_comobobox.get()
    voices = engine.getProperty('voices')
    
    def setvoice():
        if(gender=='Male'):
            engine.setProperty('voice',voices[0].id)
            engine.say(text)
            engine.runAndWait()
            
        else:
            engine.setProperty('voice',voices[1].id)
            engine.say(text)
            engine.runAndWait()
    
    if(text):
        if(speed=='Fast'):
            engine.setProperty('rate',250)
            setvoice()
        elif(speed=='Normal'):
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine.setProperty('rate',60)
            setvoice()
            
            
            
def download():
    global engine
    text=text_area.get(1.0,END)
    gender=gender_combobox.get()
    speed = speed_comobobox.get()
    voices = engine.getProperty('voices')
    
    def setvoice():
        if(gender=='Male'):
            engine.setProperty('voice',voices[0].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()
            
        else:
            engine.setProperty('voice',voices[1].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()
    
    if(text):
        if(speed=='Fast'):
            engine.setProperty('rate',250)
            setvoice()
        elif(speed=='Normal'):
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine.setProperty('rate',60)
            setvoice()
    

        
    
    
    
    
    

#icon
image_icon = PhotoImage(file="love.png")
root.iconphoto(False,image_icon)

#Top frame 
Top_frame = Frame(root,bg="white",width=900,height=100)
Top_frame.place(x=0 , y=0)

Logo = PhotoImage(file="love.png",height=100,width=300)
Label(Top_frame,image=Logo,bg="white").place(x=0,y=0)

Label(Top_frame,text="Text to speech",font=("Arial",20,"bold"),bg="white",fg="black").place(x=500,y=30)

text_area = Text(root,font="Robote 20",bg="white",relie=GROOVE,wrap=WORD)
text_area.place(x=10 , y=150 , width = 500 , height = 250)

Label(root,text="VOICE",font="arial 15 bold",bg="#305065",fg="white").place(x=580,y=160)
Label(root,text="VOICE",font="arial 15 bold",bg="#305065",fg="white").place(x=760,y=160)


gender_combobox = Combobox(root,values=['Male','Female'],font='arial 14',state='r',width=10)
gender_combobox.place(x=550 , y=200)
gender_combobox.set('Male')

speed_comobobox = Combobox(root , values=['Fast','Normal','Slow'],font='arial 14',state='r',width=10)
speed_comobobox.place(x=730,y=200)
speed_comobobox.set('Normal')

imageicon = PhotoImage(file="love.png", height=20 , width = 20)
btn = Button(root,text="Speak",compound=LEFT,image=imageicon,width=130,height=50,font="arial 14 bold",bg="blue",command=speaknow)
btn.place(x=550 , y=280)

imageicon2 = PhotoImage(file="love.png" , height=20 , width = 20)
save = Button(root,text="Save",compound=LEFT,image=imageicon2,width=130,height=50,font="arial 14 bold", bg="#39c790",command=download)
save.place(x=730,y=280)








root.mainloop()