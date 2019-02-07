from tkinter import * #imports tkinter library

root = Tk() #to create the main window

photo = PhotoImage(file="an_icon.png") #make sure that the phote is in the same file
label = Label(root, image=photo) #you need to set them in side a label
label.pack()

root.mainloop() #makes sure it is being shown continuously, on the screen
#for more info: https://www.youtube.com/watch?v=RJB1Ek2Ko_Y&t=1s&list=PL6gx4Cwl9DGBwibXFtPtflztSNPGuIB_d&index=2