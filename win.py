import tkinter as tk

root = tk.Tk()
root.title('Snake game')
root.geometry('300x400')
button1 = tk.Button(root, text="New game")
button2 = tk.Button(root, text="Exit", command=root.quit)
button1.pack(side = tk.TOP, pady = 40)
button2.pack(side = tk.TOP, pady = 40)


root.mainloop()
