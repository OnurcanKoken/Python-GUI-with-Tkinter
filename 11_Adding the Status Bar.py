from tkinter import * #imports tkinter library

#we will not deal with the function here
def doNothing():
    print("so what?")

root = Tk() #to create the main window

# ***** Main Menu *****

#menu is at the top by default settings
#we want to add an item that has drop-down functinality
#drop-down functinality is called cascading

menu_name = Menu(root) #create a main menu and give a name
root.config(menu=menu_name)

subMenu = Menu(menu_name) #create a subMenu for the main menu
menu_name.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New File", command=doNothing)
subMenu.add_command(label="New Window", command=doNothing)
subMenu.add_separator() #separate groups of submenu commands
subMenu.add_command(label="Exit", command=doNothing)

editMenu = Menu(menu_name) #create another subMenu for the main menu
menu_name.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Undo", command=doNothing)

# ***** Toolbar *****

toolbar = Frame(root, bg="blue")

insertButton = Button(toolbar, text="Insert Image", command=doNothing)
insertButton.pack(side=LEFT, padx=2, pady=2) #padding means extra space for the button, padx=2 gives us 2 pixels of padding
printButton = Button(toolbar, text="Print", command=doNothing)
printButton.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

# ***** Status Bar *****

status = Label(root, text="Is that so?", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

"""
bd means border
whenever you have a label, you can have a border around it
relief=SUNKEN -> how you want you border or 
how you want this item to appear; sunken in the screen
we also need to anchor it, W means west 
"""

root.mainloop() #makes sure it is being shown continuously, on the screen
#for more info: https://www.youtube.com/watch?v=RJB1Ek2Ko_Y&t=1s&list=PL6gx4Cwl9DGBwibXFtPtflztSNPGuIB_d&index=2