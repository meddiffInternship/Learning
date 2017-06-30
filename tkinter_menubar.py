from tkinter import *

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
        file.add_command(label='Open',command=self.client_exit)

        menu.add_cascade(label='File',menu=file)
#to create edit button
        edit = Menu(menu)
        edit.add_command(label='undo')
        menu.add_cascade(label='Edit',menu=edit)
          

    
    

root = Tk()
root.geometry("400x300")

app = window(root)

root.mainloop()
