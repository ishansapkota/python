

# ishan_root = Tk()   #this ishan_root chahi tk() class ko instance/object  ho

#gui logic yesma use huncha

# ishan_root.mainloop()   #this keeps you in gui window and makes the gui interactive and  remembers the logic   of the code

#LABEL
# A label in tkinter is a widget with which a user doesnot interact unlike the widget like button with which the user can interact

'''from tkinter import *

root = Tk()
root.geometry("640x480") #this sets the geometry of the GUI & geometry uses the argument of ("Width", "height")

root.minsize(580,360)  #this sets the minimum size of the GUI & uses the argument as (Width,Height)

root.maxsize(1024,720)  #this sets the maximum size of the GUI & uses the argument as (width, height)

ishan = Label(text = "WELCOME TO OUR HOSPITAL DATABASE")
ishan.pack()

root.mainloop()
'''

'''INSERTING PHOTOS USING LABEL


from tkinter import * 

root = Tk()
root.geometry("1024x720")

photo = PhotoImage(file="1.png")
ishan_label = Label(image = photo)
ishan_label.pack()
root.mainloop()
'''

#ATTRIBUTES OF LABEL

# from tkinter import * 

# root = Tk()

# root.geometry("960x480")
# root.title("HOSPITAL DATABASE ")
#IMPORTANT LABEL OPTIONS
'''
text = adds the text
bd = background (background nai bhanera use garda ni huncha re)
fg = foreground
font = sets the font and has the following two methods
        font="Arial 16 italic"
        font = ("Arial", 16,italic)
padx = x padding 
pady = y padding
relief = border styling, yesko examples chahi --> SUNKEN, RAISE, GROOVE, RIDGE
'''
# label = Label(text='''The project we're about to submit is about the hospital database \n management using the tkinter module of python where the database \n part of the project is handled with mySQL''',background="blue",fg="white",font="Arial 16 italic",padx = 30,pady = 25,borderwidth=5,relief=SUNKEN)

# '''
# #IMPORTANT PACK OPTIONS
# ''''
# anchor = nw --> this can be written as anchor = NW or, anchor = "nw" 
#         this anchor does not use SE(southeast) or SW for this we have to use side
# side = BOTTOM --> this is used along with the anchor tag and the example of it can be side = BOTTOM , anchor="se" (BOTTOM,UP,LEFT,RIGHT)
# fill = this fills when the window is dragged, this consists of fill = X or fill = Y
# padx = 
# pady = 

# '''
# label.pack(side=BOTTOM,anchor = "ne")
# root.mainloop()
# '''

#FRAME 
#it is like the div tag in webdev
# from tkinter import * 

# root = Tk()

# root.geometry("960x360")
# root.title("HOSPITAL DATABASE")

# f1 = Frame(root, background= "grey",borderwidth=6,relief=SUNKEN) #this is how you create frame and it must include the root it must be packed into

# f1.pack(side=LEFT,fill = Y)

# label1 = Label(f1,text = "WELCOME TO OUR HOSPITAL DATABASE") #putting the label in f1 yesley gardaa tyo frame ma bhaako kura dekhaidincha
# label1.pack(pady=10)

# f2 = Frame(root,bg="blue",borderwidth=10,relief = SUNKEN)
# f2.pack(fill = X,padx=10)

# label2 = Label(f2,text= "FUCK YOU", pady=20)
# label2.pack()


# f3 = Frame(root,background="red",borderwidth=10,relief=RIDGE)
# f3.pack(side=RIGHT,fill=Y)

# label3 = Label(f3, text= "Hello,There")
# label3.pack()

# root.mainloop()

#BUTTON 


# from tkinter import *

# root = Tk()
# root.geometry("960x480")

# f1 = Frame(root,bg ="grey",borderwidth=5,relief = SUNKEN)
# f1.pack(side=LEFT)
# #button ko creation is same as that of label
# button = Button(f1,text = "Press me",fg= "blue",font = 20)
# button.pack()

# #a button can also contain a command so we can use the command attribute with a function and by pressing the button it executes the function and the code goes like this

# def magic():
#     print("JAADU")
# button2 = Button(root,text = "Press me again to see magic",command = magic,fg="red",borderwidth=10,relief= SUNKEN)
# #while giving the function in command, we should just give the name not its call so () is not used in it.
# button2.pack(side=RIGHT)

# root.mainloop()


# #GRID LAYOUT
# #grid widget also works the pack attribute and in this we will have to give two arguments namely rows and column, at default stage if we leave the grid as is then the rows and colums are 0
# from tkinter import *
# from unittest import result 

# root = Tk()

# root.geometry("960x480")

# user = Label(root, text= "USERNAME")
# password = Label(root, text = "PASSWORD")
# user.grid(row=0)
# password.grid(row=1)

# user_value = StringVar()
# pass_value = StringVar()

# user_entry = Entry(root, textvariable= user_value) #entry widget helps to take in the value by using a certain variable along it
# pass_entry = Entry(root, textvariable= pass_value)

# user_entry.grid(row = 0,column = 1)
# pass_entry.grid(row = 1,column = 1)

# def resultdisplay():
#     print(user_value.get())
#     print(pass_value.get())

# button = Button(root, text = "Login",command = resultdisplay)
# button.grid()
# root.mainloop()

#VARIABLE classes in TKINTER
#BooleanVar,IntVar,StringVar,DoubleVar

#MAKING A HOSPITAL FORM USING VARIOUS WIDGETS

from tkinter import *
from tokenize import String 

root = Tk()
root.geometry("1024x720")

label = Label(text = "Welcome to Our Hospital!", bg = "grey", font=20,borderwidth = 10,relief = SUNKEN)
label.grid(row = 0, column = 3,pady = 20)

name = Label(text = "Patient Name ")
phone = Label(text = "Patient Phone")
address = Label(text = "Patient Address")

name.grid(row = 1, column = 2, pady =15)
phone.grid(row = 2, column = 2, pady =15)
address.grid(row = 3,column = 2, pady =15)

namevalue = StringVar()
phonevalue = StringVar()
addressvalue = StringVar()
checkvalue = IntVar()

nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable = phonevalue)
addressentry = Entry(root, textvariable=addressvalue)

nameentry.grid(row = 1, column = 3)
phoneentry.grid(row = 2, column = 3)
addressentry.grid(row = 3, column = 3)


checkbox = Checkbutton(text = "Want to register into the database?", variable = checkvalue)
checkbox.grid(row = 4, column = 3)

def getvalue(): 
   print(f"{namevalue.get(),phonevalue.get(),addressvalue.get(),checkvalue.get()}")

   with open("records.txt","a") as f:
    f.write(f"{namevalue.get(),phonevalue.get(),addressvalue.get(),checkvalue.get()}\n")


button = Button(text = "Submit the queries", fg = "red", bg = "black", command = getvalue)
button.grid(row = 5, column = 2, pady = 10)



root.mainloop()