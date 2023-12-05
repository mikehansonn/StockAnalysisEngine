import tkinter as tk

window = tk.Tk()  # create window

# create a label and pack it into the window
label = tk.Label(text="Hello, Tkinter")
label.pack()  # use side=tk.TOP, side=tk.LEFT, etc to pack to differnt sides

# create a button
button = tk.Button(text="Click me!", width=10, height=5)
button.pack()

# create a text box
entry = tk.Entry(width=30)
entry.pack()
data = entry.get()  # Get the data from the text box
entry.delete(0, tk.END)  # remove all text in entry
entry.insert(0, "Python")  # insert text into the entry
# window.destroy() to close the window

# frames are containers for objects
# frame = tk.Frame()
# label = tk.Label(master=frame)  # this is how to set an object in a frame
# frame.pack()

# grid packing
frame1 = tk.Frame()
for i in range(3):
    for j in range(3):
        frame = tk.Frame(
            master=frame1,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5)
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack()
frame1.pack()

# ensure window stays open
window.mainloop()
