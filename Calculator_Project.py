from tkinter import *
win=Tk()
win.geometry("800x600")
win.title("Impresive Calculator")
win.iconbitmap("C:\\Users\\start_saran.bat\\Downloads\\sum sub.ico")
win.config(bg="#303977")
label_1=Label(win, text="Use integer to calculate",bg="#FFF700",fg="#1919c5",height="2",width="30",font="Georgia 10 bold")
label_1.pack()
number_1=Label(win,text="Enter First Number ⤵",bg="#fff700",fg="#1919b0",padx=30,pady=30,font="Georgia 15 normal")
number_1.pack()

n1=Entry(win,text="First Number ", bg="#1919c3",fg="#ffffff",font="Georgia 10 bold",borderwidth=5,relief=SUNKEN)
n1.pack()

number_2=Label(win,text="Enter Second Number ⤵",bg="#fff700",fg="#1919b0",padx=30,pady=30,font="Georgia 15 normal")
number_2.pack()

n2=Entry(win,text="Second Number ", bg="#1919c4",fg="#ffffff",font="Georgia 10 bold",borderwidth=4,relief=SUNKEN)
n2.pack()

def sum():
    num_1=float(n1.get())
    num_2=float(n2.get())
    sum=num_1+ num_2
    result.config(text="Click For Substract : "+str(sum))

result=Button(win,text=" + ",bg="#ffff00",fg="#1919c5",font="Georgia 15 bold",command=sum)
result.pack()


def sub():
    num_1=float(n1.get())
    num_2=float(n2.get())
    sub=num_1 - num_2
    result.config(text=f"The Subtraction is : \t {sub}")

result=Button(win,text=" - ",bg="#1919c4",fg="#ffff00",font="Georgia 20 bold",command=sub)
result.pack()








win.mainloop()