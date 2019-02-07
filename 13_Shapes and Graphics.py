from tkinter import * #imports tkinter library

root = Tk() #to create the main window

canvas = Canvas(root, width=200, height=100)
canvas.pack()

blackLine = canvas.create_line(0, 0, 200, 50) #beginning point and ending point
redLine = canvas.create_line(0, 100, 200, 50, fill="red") #makes the line red
greenBox = canvas.create_rectangle(25, 25, 130, 60, fill="blue") #top left point, width, height parameters

#to delete an object
#canvas.delete(redLine)

#to delete them all
#canvas.delete(ALL)

root.mainloop() #makes sure it is being shown continuously, on the screen
#for more info: https://www.youtube.com/watch?v=RJB1Ek2Ko_Y&t=1s&list=PL6gx4Cwl9DGBwibXFtPtflztSNPGuIB_d&index=2