import random
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk

main_win=Tk()
main_win.title("HANGMAN")
main_win.minsize(height=600,width=1000)
main_win.maxsize(height=600,width=1000)
image1=Image.open("hanging.png")
v1=ImageTk.PhotoImage(image1)
image2=Image.open("hanged.png")
v2=ImageTk.PhotoImage(image2)
image3=Image.open("happy.png")
v3=ImageTk.PhotoImage(image3)

def start():
   lab.config(image=v1)
   messagebox.showinfo("HANGMAN","you have to guess in three chances")
   animal=["horse","donkey","goat","dog","cat","cow","ox","tiger","lion","elephant","fox","rabbit","rat"]
   fruit=["orange","pineapple","banana","mango","corn","papaya","water melon","kiwi"]
   vehicle=["car","bike","train","flight","helicopter","jet","submerine"]
   thing=["furit","animal","vehicle"]
   randthing=thing[random.randrange(len(thing))]
   print(randthing)
   global rand
   global j
   j=0
   if randthing=="animal":
       
        rand=animal[random.randrange(len(animal))]
        ln=len(rand)
        hint.config(text=f"It is a {randthing} name of {ln} letters length")
   elif randthing=="fruit":
       
        rand=fruit[random.randrange(len(fruit))]
        ln=len(rand)
        hint.config(text=f"It is a {randthing} name of {ln} letters length")
   else:
        rand=vehicle[random.randrange(len(vehicle))]
        ln=len(rand)
        hint.config(text=f"It is a {randthing} name of {ln} letters length")

def check():
    global j
    j=j+1
    if j>=3:
        lab.config(image=v2)
        messagebox.showinfo("HANGMAN",f"you hav used your three chances\n hanged \n and answer is \n{rand}")
        j=0
        
        start()
    else:
        ggu=gue.get()
        if ggu==rand:

            print("you have done")
            lab.config(image=v3)
            
            messagebox.showinfo("HANGMAN","you got it ")

            start()
            j=0
        else:
            print("try again")
            messagebox.showwarning("HANGMAN",f"try again\nremaining {3-j} chances")

child1=Frame(main_win,height=500,width=500,bg="orange")
child1.pack(side='left')
hint=Label(child1,bg="black",height=3,width=40,fg="white",font=(18))
hint.place(x=30,y=30)
lab1=Label(child1,height=2,width=28,font=(15),text="enter your guess below",fg="white",bg="orange")
lab1.place(x=100,y=200)
gue=StringVar()
guess=Entry(child1,width=35,font=(20),bd=5,textvariable=gue)
guess.place(x=50,y=250)
but=Button(child1,bg="black",text="check",fg="white",cursor="hand2",width=10,command=check)
but.place(x=260,y=300)
but2=Button(child1,bg="black",text="start",fg="white",cursor="hand2",width=10,command=start)
but2.place(x=160,y=300)
child2=Frame(main_win,height=750,width=500)
child2.pack(side='right')
lab=Label(child2,image=v1,height=750,width=500)
lab.pack()
main_win.mainloop()


