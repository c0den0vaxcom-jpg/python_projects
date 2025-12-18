from tkinter import *
win=Tk()
win.geometry("700x500")
win.title("My Test GUI")
win.config(bg="#090040")

l1=Label(win ,text="This is for Success",bg="#471396",fg="#FFCC00",font="Math_italic 20 bold",padx=10,pady=10)
l1.pack()

heading=Label(text=" Simple Calculator ",fg="#471396",bg="#FFCC00",height="2",width="25",font="Georgia 18 bold")
heading.pack()

n1=Label(text="Enter First Number : ",fg="#471396",bg="#FFCC00",font="Georgia 14 bold")
n1.pack()

num1=Entry(win ,bg="#471396",fg="#B13BFF",font="Georgia 14 bold",borderwidth=5,relief=SUNKEN)
num1.pack()

n2=Label(text="Enter Second Number : ",fg="#471396",bg="#FFCC00",font="Georgia 14 bold")    
n2.pack()

num2=Entry(win ,bg="#471396",fg="#B13BFF",font="Georgia 14 bold",borderwidth=5,relief=SUNKEN)
num2.pack()

def add():
    n1=float(num1.get())
    n2=float(num2.get())
    sum=n1+n2
    result.config(text="Result is : "+str(sum))
def sub():
    n1=float(num1.get())
    n2=float(num2.get())
    sub=n1-n2
    result.config(text="Result is : "+str(sub))
def mul():
    n1=float(num1.get())
    n2=float(num2.get())
    mul=n1*n2
    result.config(text="Result is : "+str(mul))         
def div():
    n1=float(num1.get())
    n2=float(num2.get())
    div=n1/n2
    result.config(text="Result is : "+str(div))
result=Label(win ,bg="#090040",fg="#FFCC00",font="Georgia 14 bold")
result.pack()
b1=Button(win ,text=" + ",bg="#471396",fg="#FFCC00",font="Georgia 14 bold",command=add)
b1.pack()
b2=Button(win ,text=" - ",bg="#471396",fg="#FFCC00",font="Georgia 14 bold",command=sub)
b2.pack()
b3=Button(win ,text=" * ",bg="#471396",fg="#FFCC00",font="Georgia 14 bold",command=mul)
b3.pack()
b4=Button(win ,text=" / ",bg="#471396",fg="#FFCC00",font="Georgia 14 bold",command=div)
b4.pack()


win.mainloop()