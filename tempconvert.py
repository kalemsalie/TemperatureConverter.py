from tkinter import *
from tkinter.messagebox import showinfo
#activating tkinter

win = Tk()
win.title("Temperature Coverter")
#Name of GUI

def c_to_f():
    value = int(entry.get())
    answer = (value * 9/5) + 32
    showinfo("Answer",f"{value} C = {answer} F")

def f_to_c():
    value = int(entry.get())
    answer = (value - 32) * 5/9
    showinfo("Answer",f"{value} F = {answer} C")
#giving program the formula and actions to take

label = Label(win,text="Enter Temperature Here :",font=('arial',15,'bold'))
label.grid(row=0,column=0)
#heading label of GUI

entry = Entry(win,font=('arial',20,'bold'))
entry.grid(row=1,column=0)
#entry space of GUI

button1 = Button(win,text="Celsius to Farenheit",font=('arial',15,'bold'),command=c_to_f)
button1.grid(row=3,column=0)
#celsius to farenheit button

button2 = Button(win,text="Farenheit to Celsius",font=('arial',15,'bold'),command=f_to_c)
button2.grid(row=4,column=0)
#farenheit to celsius button

win.mainloop()
