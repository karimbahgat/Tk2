"""
Tk2
Tk2 is a convenience library for extending the functionality of Tkinter, 
to make it easier and more flexible to create GUI applications. 
"""

import tk2

# TEST

w = tk2.Tk()

# FRAME
f = tk2.Frame(w, width=200, height=200)
f.pack(fill="both", expand=True)

# LABEL
l = tk2.Label(f.interior, text="hello\nmy\nname\nis\ncoocoo")
l.bind_rightclick( [("one",lambda: 1), ("two",lambda: 2)] )
#l.bind("<B1-Motion>", lambda e: l.move_to(100*e.x//100, 100*e.y//100) )
l.bind_draggable()
l.pack()

# TEXT
#t = tk2.SuperText(f.interior)
#t.apply_theme("typewriter")
#t.pack()

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
c = tk2.Canvas(w, width=600, height=600)
c.pack(fill="both", expand=True)

w.mainloop()
