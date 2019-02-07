from tkinter import * #imports tkinter library

root = Tk() #to create the main window

#one widget handle multiple events

def leftClick(evet):
    print("Left")

def middleClick(evet):
    print("Middle")

def rightClick(evet):
    print("Right")

#frame is just a blank empty container
frame = Frame(root, width=300, height=250) #set the width 300 pixels
frame.bind("<Button-1>", leftClick)
frame.bind("<Button-2>", middleClick)
frame.bind("<Button-3>", rightClick)
frame.pack()

"""
you may want to know this;
we adjusted 300x250 window,
what if we will make it larger by using mouse manually, not by code?
when the mouse icon is at 300x250 window, code will work fine
when the mouse icon is out of the 300x250 window, code will not work
"""

root.mainloop() #makes sure it is being shown continuously, on the screen
#for more info: https://www.youtube.com/watch?v=RJB1Ek2Ko_Y&t=1s&list=PL6gx4Cwl9DGBwibXFtPtflztSNPGuIB_d&index=2