from tkinter import * #imports tkinter library

root = Tk() #to create a window with small,full screen and close buttons

#bg specifies the color of back ground
one = Label(root, text="One", bg="red", fg="white")
one.pack() #on the middle with default size
two = Label(root, text="One", bg="green", fg="white")
two.pack(fill=X) #goes through X direction
three = Label(root, text="One", bg="blue", fg="white")
three.pack(side=LEFT, fill=Y) #goes through Y direction and text is on the left side

root.mainloop() #makes sure it is being shown continuously, on the screen
#for more info: https://www.youtube.com/watch?v=RJB1Ek2Ko_Y&t=1s&list=PL6gx4Cwl9DGBwibXFtPtflztSNPGuIB_d&index=2