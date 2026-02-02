import tkinter as tk

window = tk.Tk()
window.title("Title")
window.geometry("600x600")

top_frame = tk.Frame(window).pack()
bottom_frame = tk.Frame(window).pack(side="bottom")

btn1 = tk.Button(top_frame, text="Button 1", fg="red").pack()
btn2 = tk.Button(top_frame, text="Button 2", fg="green").pack()
btn3 = tk.Button(bottom_frame, text="Button 3", fg="blue").pack(side="left")
btn4 = tk.Button(bottom_frame, text="Button 4", fg="purple").pack(side="left")

window.mainloop()