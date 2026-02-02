from tkinter import *

window = Tk()
window.geometry("420x420")
window.title("Python app 123")

icon = PhotoImage(file='physics_formulas/logo.png')
window.iconphoto(True,icon)
window.config(background="#ffffff")

window.mainloop()

label1 = Label(window, text="Hello world!", font="Arial Bold", height=50)
label1.grid(column=0, row=0)