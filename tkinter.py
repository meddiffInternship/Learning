
# coding: utf-8

# # Creating window using tkinter module

# In[2]:

from tkinter import *
from PIL import Image, ImageTk


# In[4]:

#Creating class window inherting from class Frame in Tkinter module 
class Window(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master = master
        self.init_Window()
    def init_Window(self):
        self.master.title("window")
        self.pack(fill = BOTH,expand = 1)
        quitButton = Button(self,text = "Exit",command = self.client_exit)
        quitButton.place(x=1,y=1)
    def client_exit(self):
        exit()
        
root = Tk()
#size of window
root.geometry("400x300")
app = Window(root)
root.mainloop()


# # creating menu bar 

# In[ ]:


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
    def init_window(self):
        self.master.title("GUI")
        self.pack(fill=BOTH, expand=1)
        menu = Menu(self.master)
        self.master.config(menu = menu)
        file = Menu(menu)
        file.add_command(label = "exit",command = self.client_exit)
        menu.add_cascade(label = "file",menu = file)
        edit = Menu(menu)
        edit.add_command(label="Undo")
        menu.add_cascade(label = "edit",menu = edit)
    def client_exit(self):
        exit()
root = Tk()
root.geometry("400x400")
app = Window(root)
root.mainloop()


# # showing images

# In[8]:

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
    def init_window(self):
        self.master.title("GUI")
        self.pack(fill=BOTH, expand=1)
        menu = Menu(self.master)
        self.master.config(menu = menu)
        file = Menu(menu)
        file.add_command(label = "exit",command = self.client_exit)
        menu.add_cascade(label = "file",menu = file)
        edit = Menu(menu)
        edit.add_command(label = "Image display",command = self.showImage)
        edit.add_command(label = "show messsage",command = self.showText)
        menu.add_cascade(label = "edit",menu = edit)
    def showImage(self):
        Load = Image.open("/home/aayushi/Desktop/ab.jpg")
        render = ImageTk.PhotoImage(Load)
        img = Label(self,image = render)
        img.image = render
        img.place(x = 0,y = 0)
    def showText(self):
        text =Label(self,text  = "hey! ")
        text.pack()
    def client_exit(self):
        exit()
root = Tk()
root.geometry("300x400")
app = Window(root)
root.mainloop()
        

