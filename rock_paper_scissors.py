#This is my code for Rock Paper Scissor Game
from tkinter import *
import random
choice_list=["rock","paper","scissor"]
def new():
    #Game Rule
    def rules(a):
        b=random.choice(choice_list)
        if a==b:
            label2.config(text="Computer's choice is also "+b)
            label3.config(text="Tie !")
        elif a=="rock" and b=="paper":
            label2.config(text="Computer's choice is "+b)
            label3.config(text="Computer Won !")
        elif a=="paper" and b=="scissor":
            label2.config(text="Computer's choice is "+b)
            label3.config(text="Computer Won !")
        elif a=="scissor" and b=="rock":
            label2.config(text="Computer's choice is "+b)
            label3.config(text="Computer Won !")
        else:
            label2.config(text="Computer's choice is "+b)
            label3.config(text="You Won !")
        reset=Button(root,text="New Game",bg="white",fg="black",font=("arial",30),command=new)
        reset.grid(row=8,column=3,pady=10)
    #Choices
    def choice_1():
        a="rock"
        rules(a)
    def choice_2():
        a="paper"
        rules(a)
    def choice_3():
        a="scissor"
        rules(a)
    def st():
        label1.config(text="Welcome "+entry.get())

    #GUI
    root=Tk()
    root.title("Rock Paper Scissor Game ")
    root.config(bg="black")
    root.geometry("1300x900")
    label=Label(root,text="Enter your name",bg="white",fg="black",font=("arial",30))
    label.grid(row=1,column=1,pady=20)
    entry=Entry(root,font=("arial",30),bg="white",fg="black")
    entry.grid(row=2,column=1,pady=50)
    start=Button(root,text="Start",bg="white",fg="black",font=("arial",30),command=st)
    start.grid(row=3,column=1)
    label1=Label(root,text="",font=("arial",30),bg="white",fg="black")
    label1.grid(row=4,column=1,pady=10)
    choice1=Button(root,text="Rock",bg="white",fg="black",font=("arial",30),command=choice_1,height=4,width=8)
    choice1.grid(row=5,column=0,padx=10,pady=50)
    choice2=Button(root,text="Paper",bg="white",fg="black",font=("arial",30),command=choice_2,height=4,width=8)
    choice2.grid(row=5,column=1,padx=10,pady=50)
    choice3=Button(root,text="Scissors",bg="white",fg="black",font=("arial",30),command=choice_3,height=4,width=8)
    choice3.grid(row=5,column=2,padx=10,pady=50)
    label2=Label(root,text="",bg="white",fg="black",font=("arial",30))
    label2.grid(row=6,column=1)
    label3=Label(root,text="",bg="white",fg="black",font=("arial",30))
    label3.grid(row=7,column=1)
    root.mainloop()
new()
