from tkinter import *
class Window(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master=master
        self.init_window()
    def init_window(self):
        self.master.title('GUI window using tkinter')
        self.pack(fill='both',expand=1)
        quitBut=Button(self,text='QUIT',command=self.client_exit)
        quitBut.place(x=0,y=0)
    def client_exit(self):
        exit()
root=Tk()
root.geometry("300x400")
app=Window(root)
root.mainloop()
