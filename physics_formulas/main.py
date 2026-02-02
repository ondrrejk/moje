from tkinter import *

window = Tk()
window.geometry("420x420")
window.title("Python app 123")

icon = PhotoImage(file='physics_formulas/logo.png')
window.iconphoto(True,icon)
window.config(background="#ffffff")

label1 = Label(window, text="Hello world!", font=("Arial Bold", 50))
label1.grid(column=0, row=0)

bt = Button(window, text="Click me")
bt.grid(column=1, row=0)

window.mainloop()