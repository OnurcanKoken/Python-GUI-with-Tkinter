from tkinter import * #imports tkinter library


#we will not deal with the function here
def doNothing():
    print("so what?")

root = Tk() #to create the main window

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

root.mainloop() #makes sure it is being shown continuously, on the screen
#for more info: https://www.youtube.com/watch?v=RJB1Ek2Ko_Y&t=1s&list=PL6gx4Cwl9DGBwibXFtPtflztSNPGuIB_d&index=2