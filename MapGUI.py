#Import the required Libraries
from tkinter import *
from PIL import ImageTk, Image

class mapGUI():
    def __init__(self, master):
        self.master = master
        self.floor = 1
        self.total = 3

        self.showFloorMap()
        self.button = Button(self.master, text="Change Current Floor",bg="blue", fg="white",anchor="center",command=self.cycleMap)
        self.button.grid(row=1,column=0,sticky="nesw")

    def showFloorMap(self):
        # Load image , resize it, and set the img variable to be used
        hold = f"image{self.floor}.png"
        use = Image.open(hold)

        use = use.resize((400, 400))

        self.img = ImageTk.PhotoImage(use)

        # Display the floor map image within the label being used
        self.floorMap = Label(self.master, image=self.img)
        self.floorMap.grid(row=0,column=0)

    def cycleMap(self):
        # cycle through the map images
        self.floor += 1
        if self.floor > self.total:
            self.floor = 1

        # Remove old label and show next map
        self.floorMap.destroy()
        self.showFloorMap()

window = Tk()
window.geometry("400x430")
gui = mapGUI(window)
window.mainloop()