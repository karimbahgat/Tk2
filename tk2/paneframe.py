from Tkinter import *
root = Tk()

top = Label(root, text="top")
top.pack()

panes = PanedWindow(root, sashrelief="raised")
panes.pack(fill="both", expand="yes")

left = Label(panes, text="Left Pane")
left.pack()

right = Label(panes, text="Right Pane")
right.pack()

panes.add(left)
panes.add(right)

root.after(5000, lambda: panes.remove(right))

root.mainloop()
