"""
Add multichoice widget,
multientry widget,
and maybe possibility to link these hierarchically (one depends on answers of previous)?
"""



def add_option_input(self, label, valuetype, argname=None, multi=False, length=None, default=None, minval=None, maxval=None, choices=None):
    optionrow = tk.Frame(self.mainoptions)
    optionrow.pack(fill="x", anchor="n", pady=5, padx=5)
    if multi:
        # make a list-type widget that user can add to
        inputlabel = tk.Label(optionrow, text=label, **style_options_labels)
        inputlabel.pack(side="left", anchor="nw", padx=3)
        inputwidget = tk.Listbox(optionrow, activestyle="none",
                                 highlightthickness=0, selectmode="extended",
                                 **style_options_labels)
        inputwidget.pack(side="right", anchor="ne", padx=3)
        
        if choices:
            # add a listbox of choices to choose from
            def addtolist():
                for selectindex in fromlist.curselection():
                    selectvalue = fromlist.get(selectindex)
                    inputwidget.insert(tk.END, selectvalue)
                for selectindex in reversed(fromlist.curselection()):
                    fromlist.delete(selectindex)
            def dropfromlist():
                for selectindex in inputwidget.curselection():
                    selectvalue = inputwidget.get(selectindex)
                    fromlist.insert(tk.END, selectvalue)
                for selectindex in reversed(inputwidget.curselection()):
                    inputwidget.delete(selectindex)
            # define buttons to send back and forth bw choices and input
            buttonarea = tk.Frame(optionrow)
            buttonarea.pack(side="right", anchor="n")
            addbutton = IconButton(buttonarea, command=addtolist,
                                   text="-->", **style_options_labels)
            addbutton.pack(anchor="ne", padx=3, pady=3)
            dropbutton = IconButton(buttonarea, command=dropfromlist,
                                   text="<--", **style_options_labels)
            dropbutton.pack(anchor="ne", padx=3, pady=3)
            # create and populate the choices listbox
            fromlist = tk.Listbox(optionrow, activestyle="none",
                                 highlightthickness=0, selectmode="extended",
                                 **style_options_labels)
            for ch in choices:
                fromlist.insert(tk.END, ch)
            fromlist.pack(side="right", anchor="ne", padx=3)
        else:
            # add a freeform entry field and button to add to the listbox
            def addtolist():
                entryvalue = addentry.get()
                inputwidget.insert(tk.END, entryvalue)
                addentry.delete(0, tk.END)
            def dropfromlist():
                for selectindex in reversed(inputwidget.curselection()):
                    inputwidget.delete(selectindex)
            buttonarea = tk.Frame(optionrow)
            buttonarea.pack(side="right", anchor="n")
            addbutton = IconButton(buttonarea, command=addtolist,
                                   text="-->", **style_options_labels)
            addbutton.pack(anchor="ne", padx=3, pady=3)
            dropbutton = IconButton(buttonarea, command=dropfromlist,
                                   text="<--", **style_options_labels)
            dropbutton.pack(anchor="ne", padx=3, pady=3)
            # place the freeform text entry widget
            addentry = tk.Entry(optionrow, **style_options_labels)
            addentry.pack(side="right", anchor="ne", padx=3)

    else:
        inputlabel = tk.Label(optionrow, text=label, **style_options_labels)
        inputlabel.pack(side="left", anchor="nw")
        if choices:
            # dropdown menu of choices
            choice = tk.StringVar()
            if default: choice.set(default)
            inputwidget = tk.OptionMenu(optionrow, choice, *choices)
            inputwidget.choice = choice
            inputwidget.pack(side="right", anchor="ne", padx=3)
        else:
            # simple number or string entry widget
            inputwidget = tk.Entry(optionrow, **style_options_labels)
            inputwidget.pack(side="right", anchor="ne")
            if default != None:
                inputwidget.insert(tk.END, str(default))
