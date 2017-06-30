from tkinter import *

#window.init_window()

class window(Frame):

    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master=master
        self.init_window()

    def init_window(self):
        self.master.title("GUI")
        self.pack(fill=BOTH, expand=1)

        #button
        quitButton = Button(self,text = "quit",command=self.client_exit )
        quitButton.place(x=0, y=0)


#for event handling
    def client_exit(self):
        exit()
                    
    

root = Tk()
root.geometry("400x300")

app = window(root)

root.mainloop()
