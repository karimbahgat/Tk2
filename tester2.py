import tk2

window = tk2.Tk()





frame = tk2.Frame(window, text="Keesings Coder")
frame.pack(fill="both", expand=1)

title = tk2.Label(frame.interior, text="News article title: ...")
title.pack(fill="x", expand=1)

panes = tk2.Panes(frame.interior)
panes.pack(fill="both", expand=1)

leftpane = panes.add_pane()
for i in range(10):
    lbl = tk2.Label(leftpane, text=i)
    lbl.pack()

rightpane = panes.add_pane()
article = tk2.Text(rightpane)
article.insert("insert", "abcdefgejrksljfdsjfdsjfjfdskfjsdfdslfndsnfksdffdsjadkfajfkajdfkajdfafjadljfaskjfkfjsasdfkajsdfj")
article.pack()

navig = tk2.Frame(frame.interior)
navig.pack(fill="x", expand=1)
nextbut = tk2.Button(navig.interior, text="Next")
nextbut.pack(side="right")
prevbut = tk2.Button(navig.interior, text="Previous")
prevbut.pack(side="left")





window.mainloop()
