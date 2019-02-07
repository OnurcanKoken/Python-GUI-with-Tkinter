from tkinter import * #imports tkinter library


class KokensButtons:

    #master means the root ot the main window
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text="Print Message", command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Quit", command=frame.quit) #breaks the main loop
        self.quitButton.pack(side=LEFT)
    
    def printMessage(self):
        print("Is this really worked?")


root = Tk() #to create the main window

"""
whenever you make a class you need two blank lines above it
remember that any time we want to use smt from a class 
we need to make an object
an object allows us to access inside the class
"""

k = KokensButtons(root) #an object
root.mainloop() #makes sure it is being shown continuously, on the screen
#for more info: https://www.youtube.com/watch?v=RJB1Ek2Ko_Y&t=1s&list=PL6gx4Cwl9DGBwibXFtPtflztSNPGuIB_d&index=2