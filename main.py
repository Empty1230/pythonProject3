from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("tic tac toe")
root.resizable(False, False)


clicked = True
count = 0
def checkif1():
    global winner
    winner = False
    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner = True
        messagebox.showinfo("tic tac toe", "x wins!!!")
    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner = True
        messagebox.showinfo("tic tac toe", "x wins!!!")
    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("tic tac toe", "x wins!!!")
    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("tic tac toe", "x wins!!!")
    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("tic tac toe", "x wins!!!")
    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("tic tac toe", "x wins!!!")
    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("tic tac toe", "x wins!!!")
    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner = True
        messagebox.showinfo("tic tac toe", "x wins!!!")
    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("tic tac toe", "0 wins!!!")
    elif b1["text"] == "0" and b2["text"] == "0" and b3["text"] == "0":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner = True
        messagebox.showinfo("tic tac toe", "0 wins!!!")
    elif b4["text"] == "0" and b5["text"] == "0" and b6["text"] == "0":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner = True
        messagebox.showinfo("tic tac toe", "0 wins!!!")
    elif b7["text"] == "0" and b8["text"] == "0" and b9["text"] == "0":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("tic tac toe", "0 wins!!!")
    elif b1["text"] == "0" and b5["text"] == "0" and b9["text"] == "0":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("tic tac toe", "0 wins!!!")
    elif b3["text"] == "0" and b5["text"] == "0" and b7["text"] == "0":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("tic tac toe", "0 wins!!!")
    elif b3["text"] == "0" and b5["text"] == "0" and b7["text"] == "0":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("tic tac toe", "0 wins!!!")
    elif b1["text"] == "0" and b4["text"] == "0" and b7["text"] == "0":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("tic tac toe", "0 wins!!!")
    elif b2["text"] == "0" and b5["text"] == "0" and b8["text"] == "0":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner = True
        messagebox.showinfo("tic tac toe", "0 wins!!!")
    elif b3["text"] == "0" and b6["text"] == "0" and b9["text"] == "0":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("tic tac toe", "0 wins!!!")
    elif count == 9:
        messagebox.showinfo("tic tac toe", "tie!")
def beclicked(b):
    global clicked, count
    if b["text"] == " " and  clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        checkif1()
    elif b["text"] == " " and  clicked == False:
        b["text"] = "0"
        clicked = True
        count += 1
        checkif1()
def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9, clicked, count
    clicked = True
    count = 0
    b1 = Button(root, text=" ", font="Arial 20", height=3, width=6, bg="SystemButtonFace", command=lambda:beclicked(b1))
    b2 = Button(root, text=" ", font="Arial 20", height=3, width=6, bg="SystemButtonFace",
                command=lambda: beclicked(b2))
    b3 = Button(root, text=" ", font="Arial 20", height=3, width=6, bg="SystemButtonFace",
                command=lambda: beclicked(b3))
    b4 = Button(root, text=" ", font="Arial 20", height=3, width=6, bg="SystemButtonFace", command=lambda:beclicked(b4))
    b5 = Button(root, text=" ", font="Arial 20", height=3, width=6, bg="SystemButtonFace", command=lambda: beclicked(b5))
    b6 = Button(root, text=" ", font="Arial 20", height=3, width=6, bg="SystemButtonFace", command=lambda: beclicked(b6))
    b7 = Button(root, text=" ", font="Arial 20", height=3, width=6, bg="SystemButtonFace", command=lambda: beclicked(b7))
    b8 = Button(root, text=" ", font="Arial 20", height=3, width=6, bg="SystemButtonFace",
                command=lambda: beclicked(b8))
    b9 = Button(root, text=" ", font="Arial 20", height=3, width=6, bg="SystemButtonFace",
                command=lambda: beclicked(b9))
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)
    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)
    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)


my_menu = Menu(root)
root.config(menu=my_menu)
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="options", menu=options_menu)
options_menu.add_command(label="reset", command=reset)
reset()


root.mainloop()