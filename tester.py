"""
Tk2
Tk2 is a convenience library for extending the functionality of Tkinter, 
to make it easier and more flexible to create GUI applications. 
"""

import tk2

# TEST

w = tk2.Tk()

# FRAME
f = tk2.Frame(w, text="Input", labelanchor="nw", width=200, height=200)
f.pack(fill="both", expand=True)

# LABEL
l = tk2.Label(f.interior, text="hello\nmy\nname\nis\ncoocoo")
l.bind_rightclick( [("one",lambda: 1), ("two",lambda: 2)] )
#l.bind("<B1-Motion>", lambda e: l.move_to(100*e.x//100, 100*e.y//100) )
l.bind_draggable()
l.pack()

# BUTTONS
b = tk2.OkButton(f.interior, command=lambda: tk2.Window())
#b.set_icon("C:/Users/kimo/Desktop/ble.png", width=20, height=20)
b.pack()

# TEXT
t = tk2.Text(f.interior)
t.apply_theme("terminal")
t.pack()
t.insert("insert", "TITLE:\n Some introduction content blabla...")
t["state"] = "disabled"

## SLIDER
s = tk2.Slider(f.interior)
s.pack()

## MISC
r = tk2.Radiobutton(f.interior)
r.pack()
cb = tk2.Checkbutton(f.interior)
cb.pack()
dr = tk2.Dropdown(f.interior)
dr.pack()

# CANVAS
c = tk2.Canvas(f.interior, bg="dark green", width=600, height=600)
c.pack(fill="both", expand=True)

# PANES
panes = tk2.Panes(f.interior)
panes.pack(fill="both", expand=1)
p1 = panes.add_pane()
l1 = tk2.Label(p1, text="hello")
l1.pack()
p2 = panes.add_pane()
l2 = tk2.Label(p2, text="world")
l2.pack()

# LISTBOX
listbox = tk2.Listbox(f.interior, items=range(90))
listbox.insert("0", "fhjksdhfjsdkhfkjshdfjkshdfjkhdfkjsfh")
listbox.pack(fill="both", expand=True)

# MULTIS
multisel = tk2.Multiselect(f.interior, choices=range(100))
multisel.pack()
multient = tk2.Multientry(f.interior)
multient.pack()

w.mainloop()
