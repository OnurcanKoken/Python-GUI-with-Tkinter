from tkinter import * #imports tkinter library

root = Tk() #to create a window with small,full screen and close buttons

#we will create two rectangules, one of them is on the top the other one is on the bottom
#invisible containers
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM) #no need to specify for topFrame, this is enough

#buttons
#fg specifies the color of the text
button1 = Button(topFrame, text="hello 1", fg="red")
button2 = Button(topFrame, text="hello 2", fg="purple")
button3 = Button(topFrame, text="hello 3", fg="yellow")
button4 = Button(bottomFrame, text="hello 4", fg="blue")
button5 = Button(bottomFrame, text="hello 5", fg="green")
button6 = Button(topFrame, text="hello 6", fg="black")

#we need to dispay the widgets
button1.pack()
button2.pack(side=LEFT) #put it as left as possiable
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)
button5.pack()
button6.pack()

root.mainloop() #makes sure it is being shown continuously, on the screen
#for more info: https://www.youtube.com/watch?v=RJB1Ek2Ko_Y&t=1s&list=PL6gx4Cwl9DGBwibXFtPtflztSNPGuIB_d&index=2