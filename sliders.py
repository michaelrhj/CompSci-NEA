from tkinter import *

def home():
    #window setup
    window = Tk()
    window.title("Sliders")
    window.minsize(800,500)
    window.configure(bg="#0394fc")
    velocitySlider = Scale(window, from_=0.0, to=30.0, orient=HORIZONTAL,length=600,resolution=0.1)
    velocitySlider.pack()
    window.mainloop()
"""
parent = Tk()
sli = Scale(parent, from_=0, to=30, orient=HORIZONTAL)
sli.pack()
mainloop()
"""
home()