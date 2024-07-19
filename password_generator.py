# This is my code for password generator 
import string
import random
from tkinter import *
root = Tk()

s_lower=string.ascii_lowercase
s_upper=string.ascii_uppercase
s_digit=string.digits
s_punctuation=string.punctuation
l=[]
l.extend(list(s_lower))
l.extend(list(s_upper))
l.extend(list(s_digit))
l.extend(list(s_punctuation ))
def stop():
    exit()
def generate():
    new_list=l
    random.shuffle(new_list)
    length = int(entry.get())
    if length>=8:
        password ="".join(new_list[:length])
        label3.config(text="Your password is : "+password)
    else:
        label3.config(text="Lenght should be 8 or greater")
    button1=Button(root,text="Close",font=("arial",20),command=stop,bg="white",fg="black")
    button1.grid(row=4,column=2,padx=20,pady=20)

root.title("Passowrd Generator ")
root.config(bg="white")
root.geometry("1050x500")

label1=Label(root,text="CodSoft Task",font=("arial",20),bg="white",fg="black")
label1.grid(row=0,column=1,pady=20)

label2=Label(root,text="Enter password length ",font=("arial",20),bg="black",fg="white")
label2.grid(row=1,column=0,padx=20,pady=20)
entry=Entry(root,font=("arial",20),bg="white",fg="black")
entry.grid(row=1,column=1,padx=20,pady=20)
button=Button(root,text="Generate password",font=("arial",20),command=generate,bg="white",fg="black")
button.grid(row=2,column=1,padx=20,pady=20)
label3=Label(root,text="",font=("arial",20),bg="white",fg="black")
label3.grid(row=3,column=1,padx=20,pady=20)
root.mainloop()
