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
from . import scrollwidgets


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

class Scrollbar(mx.AllMixins, ttk.Scrollbar):
    def __init__(self, master, **kwargs):
        ttk.Scrollbar.__init__(self, master, **kwargs)
        mx.AllMixins.__init__(self, master)

class Menubutton(mx.AllMixins, ttk.Menubutton):
    # not sure what does/how differs from normal Menu()...
    def __init__(self, master, **kwargs):
        ttk.Menubutton.__init__(self, master, **kwargs)
        mx.AllMixins.__init__(self, master)

class Slider(ttk.Scale, mx.AllMixins):
    def __init__(self, master, *args, **kwargs):
        ttk.Scale.__init__(self, master, *args, **kwargs)
        mx.AllMixins.__init__(self, master)





# Unify Tk(), Window

class Tk(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        
class Window(tk.Toplevel):
    def __init__(self, master=None, **kwargs):
        # Make this class a subclass of tk.Menu and add to it
        tk.Toplevel.__init__(self, master, **kwargs)
        # Set its size to percent of screen size, and place in middle
        width = self.winfo_screenwidth() * 0.6
        height = self.winfo_screenheight() * 0.6
        xleft = self.winfo_screenwidth()/2.0 - width / 2.0
        ytop = self.winfo_screenheight()/2.0 - height / 2.0
        self.geometry("%ix%i+%i+%i"%(width, height, xleft, ytop))
        # Force and lock focus to the window
        self.grab_set()
        self.focus_force()

# Complete the button widgets!

class Button(mx.AllMixins, ttk.Button):
    def __init__(self, master, **kwargs):
        # initialize
        ttk.Button.__init__(self, master, **kwargs)

    def set_icon(self, filepath, **kwargs):
        """
        image given as filepath
        """
        import PIL, PIL.Image, PIL.ImageTk
        img = PIL.Image.open(filepath)
        # resize if necessary
        width,height = img.size
        if kwargs.get("width"): width = kwargs["width"]
        if kwargs.get("height"): height = kwargs["height"]
        img = img.resize((width, height), PIL.Image.ANTIALIAS)
        # resize button to have room for text if compound type
        if kwargs.get("compound"):
            def expand():
                self["width"] += width
                self["height"] += height/2
            self.after(100, expand)
        # convert to tkinter
        tk_img = PIL.ImageTk.PhotoImage(img)
        if not kwargs.get("anchor"): kwargs["anchor"] = "center"
        self.config(image=tk_img, **kwargs)
        self.img = tk_img

class OkButton(Button):
    def __init__(self, master, **kwargs):
        # initialize
        if kwargs.get("text") == None:
            kwargs["text"] = "OK"
        okfunc = kwargs.get("command")
        Button.__init__(self, master, **kwargs)

        # bind enter keypress to command function
        def runfunc(event):
            okfunc()
        self.winfo_toplevel().bind("<Return>", runfunc)

class CancelButton(Button):
    def __init__(self, master, **kwargs):
        # initialize
        if kwargs.get("text") == None:
            kwargs["text"] = "Cancel"
        cancelfunc = kwargs.get("command")
        Button.__init__(self, master, **kwargs)

        # bind escape keypress to command function
        def runfunc(event):
            cancelfunc()
        self.winfo_toplevel().bind("<Escape>", runfunc)




# Add PanedWindow as a method for the Frame widget??

class Panes(tk.PanedWindow):
    def __init__(self, master, panes=1, **kwargs):
        # initialize
        if "sashrelief" not in kwargs:
            kwargs["sashrelief"] = "ridge"
        tk.PanedWindow.__init__(self, master, **kwargs)

        # add all panes at startup
        #for _ in range(panes):
        #    fr = tk.Frame(self)
        #    self.add(fr)

    def add_pane(self):
        # panedwindow only takes pure tkinter widgets
        # so first create a normal frame to be added
        fr = tk.Frame(self)
        fr.pack(fill="both", expand=True)
        self.add(fr)
        # then nest a tk2 frame inside it and return it
        # ...
        return fr

    def get_pane(self, nameorindex):
        # get pane by name or index
        pass



# Toolbar (simply a draggable frame)

class Toolbar(mx.AllMixins, ttk.LabelFrame):
    # not sure what does/how differs from normal Menu()...
    def __init__(self, master, **kwargs):
        ttk.LabelFrame.__init__(self, master, **kwargs)
        mx.AllMixins.__init__(self, master)

        # make draggable
        self.bind_draggable()




##class Toolbar(tk.Frame):
##    """
##    Base class for all toolbars.
##    """
##    def __init__(self, master, toolbarname, **kwargs):
##        # get theme style
##        style = style_toolbar_normal.copy()
##        style.update(kwargs)
##        
##        # Make this class a subclass of tk.Frame and add to it
##        tk.Frame.__init__(self, master, **style)
##
##        # Divide into button area and toolbar name
##        self.buttonframe = tk.Frame(self, **style)
##        self.buttonframe.pack(side="top", fill="y", expand=True)
##        self.name_label = tk.Label(self, **style_namelabel_normal)
##        self.name_label["text"] = toolbarname
##        self.name_label.pack(side="bottom")
##
##    def add_button(self, icon=None, **kwargs):
##        button = IconButton(self.buttonframe)
##        options = {"text":"", "width":48, "height":32, "compound":"top"}
##        options.update(kwargs)
##        if icon:
##            button.set_icon(icon, **options)
##        else:
##            button.config(**options)
##        button.pack(side="left", padx=2, pady=0, anchor="center")
##        return button




###########
# LATER:
###########

# Tooltip (info box that follows mouse when hovering)

# Orderedlist

# Calendar, Clock, and Table...

# Add all other messageboxes in py3 structure
### http://stackoverflow.com/questions/673174/file-dialogs-of-tkinter-in-python-3/673309#673309


        
