from tkinter import *
import tkinter.ttk as ttk

window = Tk()
window.geometry("420x420")
window.title("Python app 123")

icon = PhotoImage(file='physics_formulas/logo.png')
window.iconphoto(True,icon)
window.config(background="#ffffff")

label1 = Label(window, text="Hello world!", font=("Arial Bold", 10))
label1.grid(column=0, row=0)

bt = Button(window, text="Click me")
bt.grid(column=1, row=0)

bt_orange = Button(window, text="Orange", fg="yellow", bg="orange")
bt_orange.grid(column=0, row=1)

txt = Entry(window, width=10)
txt.grid(column=0, row=2)

def clicked():
    res = "Welcome to "+txt.get()
    label1.configure(text=res)

bt_clickable = Button(window, text="CLICK ME!", command=clicked)
bt_clickable.grid(column=1, row=1)

combo = ttk.Combobox(window)
combo["values"] = (1,2,3,4,5,"Text")
combo.current(0)
combo.grid(column=0, row=3)

chk_state = BooleanVar()
chk_state.set(True)
chk = Checkbutton(window, text="select", var=chk_state)
chk.grid(column=1, row=3)

window.mainloop()