import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import * 

# this is a function to check the status of the checkbox (1 means checked, and 0 means unchecked)
def getCheckboxValue():
	checkedOrNot = CheeseVariable.get()
	return checkedOrNot


# this is a function to check the status of the checkbox (1 means checked, and 0 means unchecked)
def getCheckboxValue():
	checkedOrNot = gpVariable.get()
	return checkedOrNot


# this is a function to check the status of the checkbox (1 means checked, and 0 means unchecked)
def getCheckboxValue():
	checkedOrNot = OnionVariable.get()
	return checkedOrNot


# this is a function to check the status of the checkbox (1 means checked, and 0 means unchecked)
def getCheckboxValue():
	checkedOrNot = PepperoniVariable.get()
	return checkedOrNot


# this is a function to check the status of the checkbox (1 means checked, and 0 means unchecked)
def getCheckboxValue():
	checkedOrNot = SausagesVariable.get()
	return checkedOrNot


# this is a function to check the status of the checkbox (1 means checked, and 0 means unchecked)
def getCheckboxValue():
	checkedOrNot = MushroomsVariable.get()
	return checkedOrNot


# this is a function to check the status of the checkbox (1 means checked, and 0 means unchecked)
def getCheckboxValue():
	checkedOrNot = SmallVariable.get()
	return checkedOrNot


# this is a function to check the status of the checkbox (1 means checked, and 0 means unchecked)
def getCheckboxValue():
	checkedOrNot = LargeVariable.get()
	return checkedOrNot


# this is a function to check the status of the checkbox (1 means checked, and 0 means unchecked)
def getCheckboxValue():
	checkedOrNot = MediumVariable.get()
	return checkedOrNot


# this is the function called when the button is clicked
def orderfunc():
    messagebox.showinfo('Success','ordered Successfully!')
	# print('clicked')



root = Tk()
#this is the declaration of the variable associated with the checkbox
CheeseVariable = tk.IntVar()


#this is the declaration of the variable associated with the checkbox
gpVariable = tk.IntVar()


#this is the declaration of the variable associated with the checkbox
OnionVariable = tk.IntVar()


#this is the declaration of the variable associated with the checkbox
PepperoniVariable = tk.IntVar()


#this is the declaration of the variable associated with the checkbox
SausagesVariable = tk.IntVar()


#this is the declaration of the variable associated with the checkbox
MushroomsVariable = tk.IntVar()


#this is the declaration of the variable associated with the checkbox
SmallVariable = tk.IntVar()


#this is the declaration of the variable associated with the checkbox
LargeVariable = tk.IntVar()


#this is the declaration of the variable associated with the checkbox
MediumVariable = tk.IntVar()



# This is the section of code which creates the main window
root.geometry('892x592')
root.configure(background='#ccd7ec')
root.title("Fernando's Pizza Ordering System")


# This is the section of code which creates the a label
Label(root, text='Fernando\'s Pizza make and sells pizza with different ingredients.', bg='#ccd7ec', font=('arial', 16, 'bold')).place(x=100, y=20)


# This is the section of code which creates a checkbox
Cheese=Checkbutton(root, text='Cheese', variable=CheeseVariable, bg='#ccd7ec', font=('arial', 13, 'normal'))
Cheese.place(x=135, y=98)


# This is the section of code which creates a checkbox
gp=Checkbutton(root, text='Green Pepper', variable=gpVariable, bg='#ccd7ec', font=('arial', 13, 'normal'))
gp.place(x=135, y=148)


# This is the section of code which creates a checkbox
Onion=Checkbutton(root, text='Onion', variable=OnionVariable, bg='#ccd7ec', font=('arial', 13, 'normal'))
Onion.place(x=135, y=198)


# This is the section of code which creates a checkbox
Pepperoni=Checkbutton(root, text='Pepperoni', variable=PepperoniVariable, bg='#ccd7ec', font=('arial', 13, 'normal'))
Pepperoni.place(x=417, y=97)


# This is the section of code which creates a checkbox
Sausages=Checkbutton(root, text='Sausage', variable=SausagesVariable, bg='#ccd7ec', font=('arial', 13, 'normal'))
Sausages.place(x=417, y=147)


# This is the section of code which creates a checkbox
Mushrooms=Checkbutton(root, text='Mushrooms', variable=MushroomsVariable, bg='#ccd7ec', font=('arial', 13, 'normal'))
Mushrooms.place(x=417, y=197)


# This is the section of code which creates the a label
Label(root, text='Pizza with one or more combinations:', bg='#ccd7ec', font=('arial', 14, 'normal')).place(x=134, y=60)


# This is the section of code which creates the a label
Label(root, text='Select the size:', bg='#ccd7ec', font=('arial', 14, 'normal')).place(x=135, y=270)


# This is the section of code which creates a checkbox
Small=Checkbutton(root, text='Small', variable=SmallVariable, bg='#ccd7ec', font=('arial', 13, 'normal'))
Small.place(x=135, y=317)


# This is the section of code which creates a checkbox
Large=Checkbutton(root, text='Large', variable=LargeVariable, bg='#ccd7ec', font=('arial', 13, 'normal'))
Large.place(x=135, y=367)


# This is the section of code which creates a checkbox
Medium=Checkbutton(root, text='Medium', variable=MediumVariable, bg='#ccd7ec', font=('arial', 13, 'normal'))
Medium.place(x=135, y=417)


# This is the section of code which creates a button
Button(root, text=' Order ', bg='#F0F8FF', font=('arial', 14, 'normal'), command=orderfunc).place(x=380, y=490)


root.mainloop()
