from tkinter import *

def calculate(number1Entry,number2Entry):
    var1 = number1Entry.get()
    var2 = number2Entry.get()
    print(var1+var2)
    

window = Tk()
window.title("Addition")
window.minsize(400,50)

number1Label = Label(window, text = "Enter number 1: ").place(x=0,y=0)
number1Entry = Entry(window).place(x=100,y=0)

number2Label = Label(window, text = "Enter number 2: ").place(x=0,y=20)
number2Entry = Entry(window).place(x=100,y=20)


calculateButton = Button(window,text="Calculate",command=calculate(number1Entry,number2Entry)).place(x=0,y=50)


window.mainloop()
