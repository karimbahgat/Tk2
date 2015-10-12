"""
Tk2
Tk2 is a convenience library for extending the functionality of Tkinter, 
to make it easier and more flexible to create GUI applications. 
"""


# Imports

import sys
if sys.version.startswith("2"):
    import Tkinter as tk
else: import tkinter as tk
import ttk
from . import mixins as mx


# Classes

class Label(mx.AllMixins, ttk.Label):
    def __init__(self, master, **kwargs):
        ttk.Label.__init__(self, master, **kwargs)
        mx.AllMixins.__init__(self, master)
        
        ## self.bind_rightclick( [("Edit", self.edit_text)] )

##    def edit_text(self):
##        # doesnt work, maybe remove...
##        entry = Entry(self)
##        entry.insert(0, self["text"])
##        entry.pack()
##        def dropentry(event):
##            entry.destroy()
##        def acceptentry(event):
##            self["text"] = entry.get()
##            entry.destroy()
##        entry.bind_once("<Escape>", dropentry)
##        entry.bind_once("<Return>", acceptentry)

class Entry(mx.AllMixins, ttk.Entry):
    def __init__(self, master, **kwargs):
        ttk.Entry.__init__(self, master, **kwargs)
        mx.AllMixins.__init__(self, master)

class Checkbutton(mx.AllMixins, tk.Checkbutton):
    def __init__(self, master, **kwargs):
        tk.Checkbutton.__init__(self, master, **kwargs)
        mx.AllMixins.__init__(self, master)

class Radiobutton(mx.AllMixins, tk.Radiobutton):
    def __init__(self, master, **kwargs):
        tk.Radiobutton.__init__(self, master, **kwargs)
        mx.AllMixins.__init__(self, master)

class Dropdown(mx.AllMixins, ttk.Combobox):
    def __init__(self, master, **kwargs):
        ttk.Combobox.__init__(self, master, **kwargs)
        mx.AllMixins.__init__(self, master)

class Separator(mx.AllMixins, ttk.Separator):
    def __init__(self, master, **kwargs):
        ttk.Separator.__init__(self, master, **kwargs)
        mx.AllMixins.__init__(self, master)

class Sizegrip(mx.AllMixins, ttk.Sizegrip):
    def __init__(self, master, **kwargs):
        ttk.Sizegrip.__init__(self, master, **kwargs)
        mx.AllMixins.__init__(self, master)

class Treeview(mx.AllMixins, ttk.Treeview):
    def __init__(self, master, **kwargs):
        ttk.Treeview.__init__(self, master, **kwargs)
        mx.AllMixins.__init__(self, master)

# Menubutton??

# LabelFrame??




# Unify Tk(), Window and all other messageboxes

# Separate Scrollbar...?

# Complete the button widgets!




# Add PanedWindow as a method for the Frame widget??



# NativeProgressBar and (custom) ProgressBar. 




# Toolbar (simply a draggable frame)

# Multiwidgets

# Orderedlist




# Calendar, Clock, and Table...




        
