from tkinter import *
def window_again():
    m1 = Question(350, 400, "QUESTIONS", "HELLO!", "METRO")
class Question:

    def __init__(self, width, lenght, text, t1, t2):
        self.width = width
        self.text = text
        self.lenght = lenght
        self.t1 = t1
        self.t2 = t2
        self.root = Tk()
        self.root.geometry(str(self.width)+"x"+str(self.lenght)+"+100+100")
        self.frame = Frame(self.root,width=200,height=150,bg="white")
        self.frame.place(x=100, y=100)
        self.l = Label(self.frame, text = self.text,font="Arial 16")
        self.l.pack()
        self.frame1 = Frame(self.root,width=200,height=150,bg="white")
        self.frame1.place(x = 100,y=200)
        self.task = StringVar()
        self.task_entry = Entry(self.frame1, width=18,font="Arial 20", bd=0)
        self.task_entry.place(x=10, y=7)
        self.task_entry.focus()
        self.root.mainloop()
m1 = Question(350, 400, "What country has the highest life expectancy?APPLE hello metro film", "HELLO!", "METRO")

