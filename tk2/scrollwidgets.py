#
# create scrolled canvas
# straight from http://effbot.org/zone/tkinter-autoscrollbar.htm
# changed to being a class

import sys
if sys.version.startswith("2"):
    import Tkinter as tk
else:
    import tkinter as tk
import ttk
from . import mixins as mx

class _AutoScrollbar(ttk.Scrollbar):
    # a scrollbar that hides itself if it's not needed.  only
    # works if you use the grid geometry manager.
    def set(self, lo, hi):
        if float(lo) <= 0.0 and float(hi) >= 1.0:
            # grid_remove is currently missing from Tkinter!
            self.tk.call("grid", "remove", self)
        else:
            self.grid()
        ttk.Scrollbar.set(self, lo, hi)
    def pack(self, **kw):
        raise tk.TclError, "cannot use pack with this widget"
    def place(self, **kw):
        raise tk.TclError, "cannot use place with this widget"

class Listbox(tk.Frame, mx.AllMixins):
    def __init__(self, master, items=[], *args, **kwargs):
        tk.Frame.__init__(self, master)
        mx.AllMixins.__init__(self, master)

        vscrollbar = _AutoScrollbar(self, orient=tk.VERTICAL)
        vscrollbar.grid(row=0, column=1, sticky="ns")
        hscrollbar = _AutoScrollbar(self, orient=tk.HORIZONTAL)
        hscrollbar.grid(row=1, column=0, sticky="ew")
        
        self.listbox = tk.Listbox(self,
                                 yscrollcommand=vscrollbar.set,
                                 xscrollcommand=hscrollbar.set)

        # default list box behavior
        if "activestyle" not in kwargs: kwargs["activestyle"] = "none"
        if "highlightthickness" not in kwargs: kwargs["highlightthickness"] = 0
        if "selectmode" not in kwargs: kwargs["selectmode"] = "extended"
        self.listbox.config(*args, **kwargs)
        
        vscrollbar.config(command=self.listbox.yview)
        hscrollbar.config(command=self.listbox.xview)
        self.listbox.grid(row=0, column=0, sticky="nsew")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        vscrollbar.grid_rowconfigure(0, weight=1)
        hscrollbar.grid_columnconfigure(0, weight=1)

        for item in items:
            self.listbox.insert("end", str(item))

    # ADD CUSTOM OVERRIDE METHODS THAT REDIRECT TO self.listbox
    # ...

    def insert(self, *args, **kwargs):
        return self.listbox.insert(*args, **kwargs)

##class Listbox(tk.Listbox, mx.AllMixins):
##    def __init__(self, master, items=[], *args, **kwargs):
##
##        tk.Listbox.__init__(self, master)
##        mx.AllMixins.__init__(self, master)
##
##        vscrollbar = _AutoScrollbar(self, orient=tk.VERTICAL)
##        vscrollbar.grid(row=0, column=1, sticky="ns")
##        #vscrollbar.grid_configure(rowspan=2)
##        hscrollbar = _AutoScrollbar(self, orient=tk.HORIZONTAL)
##        hscrollbar.grid(row=1, column=0, sticky="ew")
##
##        # default list box behavior
##        if "activestyle" not in kwargs: kwargs["activestyle"] = "none"
##        if "highlightthickness" not in kwargs: kwargs["highlightthickness"] = 0
##        if "selectmode" not in kwargs: kwargs["selectmode"] = "extended"
##        self.config(yscrollcommand=vscrollbar.set,
##                     xscrollcommand=hscrollbar.set,
##                     *args, **kwargs)
##        print kwargs
##        print self.config
##    
##        vscrollbar.config(command=self.yview)
##        hscrollbar.config(command=self.xview)
##        
####        self.grid_rowconfigure(0, weight=1)
####        self.grid_columnconfigure(0, weight=1)
####        vscrollbar.grid_rowconfigure(0, weight=1)
####        hscrollbar.grid_columnconfigure(0, weight=1)
##
##        for item in items:
##            self.insert("end", str(item))

class Canvas(mx.AllMixins, tk.Canvas):
    def __init__(self, parent, *args, **kwargs):

        # control main frame widget args
        frameargs = kwargs.copy()
        anchor = frameargs.pop("anchor", None)

        # subclass
        tk.Canvas.__init__(self, parent, *args, **frameargs)
        mx.AllMixins.__init__(self, parent)
        
        # begin
        vscrollbar = _AutoScrollbar(self)
        vscrollbar.grid(row=0, column=1, sticky="ns")
        hscrollbar = _AutoScrollbar(self, orient=tk.HORIZONTAL)
        hscrollbar.grid(row=1, column=0, sticky="ew")

        self.config(yscrollcommand=vscrollbar.set,
                    xscrollcommand=hscrollbar.set)
        vscrollbar.config(command=self.yview)
        hscrollbar.config(command=self.xview)

        # make the canvas expandable
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        vscrollbar.grid_rowconfigure(0, weight=1)
        hscrollbar.grid_columnconfigure(0, weight=1)

        size = (self.cget("width"), self.cget("height"))
        self.config(scrollregion="0 0 %s %s" % size)

        # ALSO ALLOW PANNING
        self.bind("<Button-1>",
                  lambda event: self.scan_mark(event.x, event.y),
                  "+")
        self.bind("<Button1-Motion>",
                  lambda event: self.scan_dragto(event.x, event.y, 1),
                  "+")

    def zoom(self, event, level):
        # NOT SURE IF WORKS CORRECTLY
        
        # scale
        value = level * (1 / float(self._zoomlevel))
        self._zoomlevel = level
        # offset
        x1,y1,x2,y2 = self.bbox("all")
        width = max((x1,x2))-min((x1,x2))
        height = max((y1,y2))-min((y1,y2))
        xoff,yoff = min((x1,x2))+width/2.0, min((y1,y2))+height/2.0
        # execute
        self.scale("all",xoff,yoff,value,value)

class Frame(mx.AllMixins, ttk.LabelFrame):
    """
    This "super frame" combines the features of normal frames and labelframes,
    and making it all automatically scrollable.
    
    Use the 'interior' attribute to place widgets inside the scrollable frame.
    All inserted widgets are unified with the kwargs to make it all appear as one widget.

    - anchor: Where to anchor the interior frame. Any of n, s, e, w, or combination of two of them. 
    
    Note: Currently only pack and place are scrollable, grid does not work for some reason (TODO, fix and cleanup internal placement)
    Note: For anchor to work when using pack, must use fill=both, expand=True
    
    """
    def __init__(self, parent, *args, **kwargs):

        # control main frame widget args
        frameargs = kwargs.copy()
        anchor = frameargs.pop("anchor", None)
        if not "relief" in frameargs and not frameargs.get("text",None) and not "labelwidget" in frameargs:
            frameargs["relief"] = "flat"
            frameargs["borderwidth"] = 0

        # control interior frame for inserted widget args
        interiorargs = kwargs.copy()
        interiorargs.pop("anchor", None)
        interiorargs.pop("width", None)
        interiorargs.pop("height", None)

        # also filter out labelframe options for the regular frame interior
        interiorargs.pop("text", None)
        interiorargs.pop("labelanchor", None)
        interiorargs.pop("labelwidget", None)
        
        # subclass
        ttk.LabelFrame.__init__(self, parent, *args, **frameargs)
        mx.AllMixins.__init__(self, parent)

        # begin
        vscrollbar = _AutoScrollbar(self)
        vscrollbar.grid(row=0, column=1, sticky="ns")
        hscrollbar = _AutoScrollbar(self, orient=tk.HORIZONTAL)
        hscrollbar.grid(row=1, column=0, sticky="ew")

        canvas = tk.Canvas(self,
                        yscrollcommand=vscrollbar.set,
                        xscrollcommand=hscrollbar.set,
                        bg=kwargs.get("bg"),
                        #bd=0, highlightthickness=0,
                        )
        canvas.grid(row=0, column=0, sticky=anchor)

        vscrollbar.config(command=canvas.yview)
        hscrollbar.config(command=canvas.xview)

        # make the canvas expandable
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        vscrollbar.grid_rowconfigure(0, weight=1)
        hscrollbar.grid_columnconfigure(0, weight=1)

        # create canvas contents

        self.interior = ttk.Frame(canvas, **interiorargs)
        #self.interior.rowconfigure(1, weight=1)
        #self.interior.columnconfigure(1, weight=1)

        interior_id = canvas.create_window(0, 0, window=self.interior, anchor="nw")

        # on resize
        def _configure_interior(event):
            # update the scrollbars to match the size of the inner frame
            size = (self.interior.winfo_reqwidth(), self.interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if self.interior.winfo_reqwidth() != canvas.winfo_width():
                # update the canvas's width to fit the inner frame
                canvas.config(width=self.interior.winfo_reqwidth())
            if self.interior.winfo_reqheight() != canvas.winfo_height():
                # update the canvas's height to fit the inner frame
                canvas.config(height=self.interior.winfo_reqheight())
        self.interior.bind('<Configure>', _configure_interior)

    # ADD CUSTOM OVERRIDE METHODS THAT REDIRECT TO self.interior
    # ...




