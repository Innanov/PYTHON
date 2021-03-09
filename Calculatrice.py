#INNAN Nouhaila 
#Calculatrice using tkinter 
from tkinter import *
import tkinter.messagebox
test = Tk()
my_frame = Frame(test, height = 200)
my_frame.pack()

def sum() :
  result = int(E1.get()) + int(E2.get())
  tkinter.messagebox.showinfo('answer',result)
def div() :
  result = int(E1.get()) / int(E2.get())
  tkinter.messagebox.showinfo('answer',result)
def sous() :
  result = int(E1.get()) - int(E2.get())
  tkinter.messagebox.showinfo('answer',result)    
def mult() :
  result = int(E1.get()) * int(E2.get())
  tkinter.messagebox.showinfo('answer',result)
B1 = Button (my_frame, text = "+", command = sum)
B1.pack()
B2 = Button (my_frame, text = "/", command = div)
B2.pack()
B3 = Button (my_frame, text = "-", command = sous)
B3.pack()
B4 = Button (my_frame, text = "x", command = mult)
B4.pack()
L1 = Label(my_frame, text="number1")
L1.pack(side = LEFT)
E1 = Entry(my_frame, bd = 5)
E1.pack()
L2 = Label(my_frame, text="number2")
L2.pack(side = RIGHT)
E2 = Entry(my_frame, bd = 5)
E2.pack()
test.mainloop()
