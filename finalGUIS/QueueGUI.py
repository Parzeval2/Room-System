from tkinter import *

class GUITest(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.master = master

    def setupGUI(self):
        label = Label(self.master,text="Label Man")

        scrollBar = Scrollbar(self.master, bg="gray")


window = Tk()
t = GUITest(window)
t.setupGUI()
window.mainloop()