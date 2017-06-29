from tkinter import *
from PIL import Image, ImageTk

class Window(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master=master
        self.init_window()
    def init_window(self):
        self.master.title('GUI window using tkinter')
        self.pack(fill='both',expand=1)
        menu=Menu(self.master)
        self.master.config(menu=menu)
        file=Menu(menu)
        file.add_command(label='EXIT',command=self.client_exit)
        menu.add_cascade(label='FILE',menu=file)
        
        edit=Menu(menu)
        edit.add_command(label='Show image', command=self.showImg)
        edit.add_command(label='Show text', command=self.showTxt)
        menu.add_cascade(label='EDIT',menu=edit)

    def showImg(self):
        load=Image.open('C://Users//Anupama C//Pictures//Saved Pictures//lawwwww.PNG')
        render=ImageTk.PhotoImage(load)
        img=Label(self,image=render)
        img.image=render
        img.place(x=0,y=0)

    def showTxt(self):
        text=Label(self, text="Hey there!")
        text.pack()
        
    def client_exit(self):
        exit()
root=Tk()
root.geometry("300x400")
app=Window(root)
root.mainloop()
