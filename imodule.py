import tkinter as tk

master=tk.Tk()
root=tk.Canvas(master, width=500, height=350, bg="black")
root.pack()

root.create_text(250, 175, fill="gray6", text="The cake is a lie", font="Arial 60")
root.create_text(250, 175, fill="white", text="The cake is a lie", font="Arial 40")

tk.mainloop()
