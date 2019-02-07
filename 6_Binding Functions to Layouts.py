from tkinter import * #imports tkinter library

root = Tk() #to create the main window

#binding a function to a widget

#define a function
def printName():
    print("My name is Koken!")

#create a button that calls a function
#make sure there is no parantheses of the function
button_1 = Button(root, text="Print my name", command=printName)
button_1.pack()

"""
there is another way to do this
we will deal with an evet
it is being used for smt that occurs
such as button click from the user or mouse movement or button click on the keyboard
smt that user can do
bind takes two parameters; 
what event are you waiting for to occur and what function do you want to call
"""
#define a function
#we have an event at this time
def printName2(event):
    print("Again, My name is Koken!")

#make sure there is no parantheses of the function
button_2 = Button(root, text="Again, Print my name")
button_2.bind("<Button-1>", printName2) #left mouse button
button_2.pack()

root.mainloop() #makes sure it is being shown continuously, on the screen
#for more info: https://www.youtube.com/watch?v=RJB1Ek2Ko_Y&t=1s&list=PL6gx4Cwl9DGBwibXFtPtflztSNPGuIB_d&index=2