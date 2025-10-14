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







win.mainloop()