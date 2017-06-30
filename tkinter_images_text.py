from tkinter import *

from PIL import Image,ImageTk

class window(Frame):

    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master=master
        self.init_window()

    def client_exit(self):
        exit()
        

    def init_window(self):
        
        self.master.title("GUI")
        self.pack(fill=BOTH, expand=1)

    
        #menubar
        
        menu = Menu(self.master)
        self.master.config(menu=menu)

#to create flie 
        file = Menu(menu)

        file.add_command(label='Exit',command=self.client_exit)
        

        menu.add_cascade(label='File',menu=file)
#to create edit button
        edit = Menu(menu)
        edit.add_command(label='show Image',command=self.showImg)
        
        edit.add_command(label='show Text',command=self.showTxt)
        menu.add_cascade(label='Edit',menu=edit)

    def showImg(self):
        load = Image.open('C:\\Users\\User\\Pictures\\indumathi-pic\\pic.jpg')
        render = ImageTk.PhotoImage(load)

        img = Label(self,image=render)
        img.image=render
        img.place(x=0,y=0)

    def showTxt(self):
        text = Label(self,text='hey there good lookng')
        text.pack()
        
        
          

    
    

root = Tk()
root.geometry("400x300")

app = window(root)

root.mainloop()
