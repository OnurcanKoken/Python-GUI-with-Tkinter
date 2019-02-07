from tkinter import * #imports tkinter library
import tkinter.messagebox #the class that allows you to pop a message box up

root = Tk() #to create the main window

tkinter.messagebox.showinfo('Window Title', 'Just click on the OK button!') #define a title and a message

answer = tkinter.messagebox.askquestion('Question 1', 'Yes or No ?') # yes or no question

if answer == 'yes':
    print('answer was No, you lost!')
if answer == 'no':
    print('answer was Yes, you lost!')

root.mainloop() #makes sure it is being shown continuously, on the screen
#for more info: https://www.youtube.com/watch?v=RJB1Ek2Ko_Y&t=1s&list=PL6gx4Cwl9DGBwibXFtPtflztSNPGuIB_d&index=2