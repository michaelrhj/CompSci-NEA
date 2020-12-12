import tkinter as tk

class Introduction:
    def __init__(self,isready):
        self.isready = isready
    def register(self):
        window = tk.Tk()
        window.title("Home")
        window.minsize(400,100)


        window.mainloop()
  
    def display(self):
        print(self.isready)



intro = Introduction(500)
intro.register()
print(intro.close())
