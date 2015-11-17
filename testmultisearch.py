import tk2

win = tk2.Tk()


src = tk2.texteditor.MultiTextSearch(win, "blue", {"background":(0,222,222)})
src.pack(side="left", fill="y")

src2 = tk2.texteditor.MultiTextSearch(win, "green", {"background":(0,222,0)})
src2.pack(side="left", fill="y")

txt = tk2.Text(win)
txt.insert("1.0", "hello my name is")
txt.pack(side="right")

def _update_highlight():
    txt.clear_highlights()
    src.highlight(txt)
    src2.highlight(txt)
    src.after(500, _update_highlight)
src.after(500, _update_highlight)

win.mainloop()
