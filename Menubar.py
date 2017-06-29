from tkinter import *
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
        file.add_command(label='SAVE')
        file.add_command(label='EXIT',command=self.client_exit)
        menu.add_cascade(label='FILE',menu=file)
        edit=Menu(menu)
        edit.add_command(label='UNDO')
        menu.add_cascade(label='EDIT',menu=edit)
    def client_exit(self):
        exit()
root=Tk()
root.geometry("300x400")
app=Window(root)
root.mainloop()
