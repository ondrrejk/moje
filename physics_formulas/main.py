from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
import tkinter.ttk as ttk

window = Tk()
window.geometry("420x420")
window.title("Python app 123")

icon = PhotoImage(file='physics_formulas/logo.png')
window.iconphoto(True,icon)
window.config(background="#ffffff")

label1 = Label(window, text="Hello world!", font=("Arial Bold", 10))
label1.grid(column=0, row=0)

def message():
    messagebox.showinfo("Success", "Successfully clicked a button.")

bt = Button(window, text="Click me", command=message)
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

rad1 = Radiobutton(window, text="Volkswagen", value=1)
rad2 = Radiobutton(window, text="Ferrari", value=2)
rad3 = Radiobutton(window, text="Lotus", value=3)
rad1.grid(column=0, row=4)
rad2.grid(column=1, row=4)
rad3.grid(column=2, row=4)

scr_txt = scrolledtext.ScrolledText(window, width=40, height=10)
scr_txt.insert(INSERT, "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque consectetur augue sit amet mi dignissim dapibus. Maecenas rhoncus, nisl sed mollis varius, orci arcu tempor metus, eget scelerisque leo eros a ex. Nam molestie nisl ut eros varius congue. Mauris posuere ullamcorper cursus. Quisque sit amet purus blandit, dictum eros et, lobortis nisi. Phasellus nibh massa, sagittis et odio facilisis, dictum cursus tortor. Etiam enim leo, vulputate dictum turpis sed, malesuada venenatis eros. Sed dignissim venenatis tortor sit amet malesuada. Duis posuere ac justo non iaculis. Nulla vehicula risus condimentum dolor accumsan scelerisque.")
scr_txt.grid(column=0, row=5)

spin = Spinbox(window, from_=0, to=100, width=5)
spin.grid(column=0, row=6)

window.mainloop()