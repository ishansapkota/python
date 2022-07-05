

# ishan_root = Tk()   #this ishan_root chahi tk() class ko instance/object  ho

#gui logic yesma use huncha

# ishan_root.mainloop()   #this keeps you in gui window and makes the gui interactive and  remembers the logic   of the code

#LABEL
# A label in tkinter is a widget with which a user doesnot interact unlike the widget like button with which the user can interact

from tkinter import *
root = Tk()
root.geometry("640x480") #this sets the geometry of the GUI & geometry uses the argument of ("Width", "height")
root.minsize(580,360)  #this sets the minimum size of the GUI & uses the argument as (Width,Height)
root.maxsize(1024,720)  #this sets the maximum size of the GUI & uses the argument as (width, height)
root.mainloop()