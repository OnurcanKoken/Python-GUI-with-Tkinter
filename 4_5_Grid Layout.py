from tkinter import * #imports tkinter library

root = Tk() #to create main window

label_1 = Label(root, text="Name")
label_2 = Label(root, text="Password")
entry_1 = Entry(root)
entry_2 = Entry(root)

label_1.grid(row=0, sticky=E) #place it to the right alined by sticky=E (E means east so we have also N, S and W)
label_2.grid(row=1, sticky=E) #default column is equal to zero

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

#keep me logged in checkbox
c = Checkbutton(root, text="Keep me logged in") #create a checkbox
c.grid(columnspan=2)

root.mainloop() #makes sure it is being shown continuously, on the screen
#for more info: https://www.youtube.com/watch?v=RJB1Ek2Ko_Y&t=1s&list=PL6gx4Cwl9DGBwibXFtPtflztSNPGuIB_d&index=2