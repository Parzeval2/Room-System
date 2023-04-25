#Import the required Libraries
""""
from tkinter import *
from PIL import Image,ImageTk

class GUITest(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.master = master
        self.floor = 1
        self.canvas= Canvas(self.master, width= 600, height= 400)
        self.canvas.pack()

        self.one = "floorOne.jpg"
        self.two = "floorTwo.jpg"
        self.three = "floorThree.jpg"

    def setupGUI(self):
        buttonRight = Button(self, text = ">", command =  self.changeRoom(self.floor, "up"))
        buttonRight.pack(side=RIGHT)

        buttonLeft = Button(self.master, text = "<", command = self.changeRoom(self.floor, "down"))
        buttonLeft.pack(side=LEFT)

        img= ImageTk.PhotoImage(Image.open(self.one))
        self.canvas.create_image(10,10,anchor=NW,image=img)

    def changeRoom(self, current, change):
        if change == "up":
            if current == 1:
                self.floor = 2
                
            elif current == 2:
                self.floor = 3

            elif current == 3:
                self.floor = 1
        
        if change == "down":
            if current == 1:
                self.floor = 3
                
            elif current == 2:
                self.floor = 1

            elif current == 3:
                self.floor = 2
                
window = Tk()
t = GUITest(window)
t.setupGUI()
window.mainloop()
"""



import tkinter as tk
from PIL import Image,ImageTk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.floor = 1

        self.one = "floorOne.jpg"
        self.two = "floorTwo.jpg"
        self.three = "floorThree.jpg"

        self.pack(fill=tk.BOTH, expand=True)

    def setUpGUI(self):
        # create left frame for buttons
        self.left_frame = tk.Frame(self, width=100, bg='gray')
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y)

        # create right frame for buttons
        self.right_frame = tk.Frame(self, width=100, bg='gray')
        self.right_frame.pack(side=tk.RIGHT, fill=tk.Y)

        # create middle frame for canvas
        self.middle_frame = tk.Frame(self)
        self.middle_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # create canvas object in the middle frame
        self.canvas = tk.Canvas(self.middle_frame)
        img = ImageTk.PhotoImage(Image.open("floorOne.jpg"))
        self.canvas.create_image(10,10,image=img)
        self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # create left button
        self.button1 = tk.Button(self.left_frame, text="<", command = self.changeRoom(self.floor, "down"))
        self.button1.pack(side=tk.TOP, padx=10, pady=10)

        # create right button
        self.button3 = tk.Button(self.right_frame, text=">", command = self.changeRoom(self.floor, "up"))
        self.button3.pack(side=tk.TOP, padx=10, pady=10)

    def changeRoom(self, floor, direc):
        if direc == "up":
            if floor == 1:
                self.floor = 2
                img = ImageTk.PhotoImage(Image.open("floorTwo.jpg"))
                self.canvas.create_image(10,10,image=img)
            elif floor == 2:
                self.floor = 3
                img = ImageTk.PhotoImage(Image.open("floorThree.jpg"))
                self.canvas.create_image(10,10,image=img)
            elif floor == 3:
                self.floor = 1
                img = ImageTk.PhotoImage(Image.open("floorOne.jpg"))
                self.canvas.create_image(10,10,image=img)
        elif direc == "down":
            if floor == 1:
                self.floor = 3
                img = ImageTk.PhotoImage(Image.open("floorThree.jpg"))
                self.canvas.create_image(10,10,image=img)
            elif floor == 2:
                self.floor = 1
                img = ImageTk.PhotoImage(Image.open("floorOne.jpg"))
                self.canvas.create_image(10,10,image=img)
            elif floor == 3:
                self.floor = 2
                img = ImageTk.PhotoImage(Image.open("floorTwo.jpg"))
                self.canvas.create_image(10,10,image=img)


root = tk.Tk()
app = Application(master=root)
app.setUpGUI()
app.mainloop()