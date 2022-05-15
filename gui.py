from congen import wordgen, cgg_parser

from tkinter import *
from tkinter import filedialog

def gen_words():
    pattern = e1.get()
    if not pattern:
        return
    amt = s1.get()

    groups, weights = cgg_parser.parse_cgg(t1.get("1.0", END))

    words = wordgen.generate_words(amt, pattern, groups, weights=weights)
    pseudotext = wordgen.generate_pseudotext(words)

    t2.delete("1.0", END)
    t2.insert(END, pseudotext)

def open_file():
    file = filedialog.askopenfilename(filetypes=(
        ('congen group files', '*.cgg'),
        ('All files', '*.*')
    ), initialdir="cggs/")
    with open(file) as f:
        text = f.read()
        t1.delete("1.0", END)
        t1.insert("1.0", text)

root = Tk()
root.geometry("500x600")
root.resizable(False, False)

l1 = Label(text="ConGen", font=("", 17))
l1.pack(pady=(5, 10))

l2 = Label(text="Pattern", font=("", 13))
l2.pack()

pat = IntVar()
e1 = Entry(font=("", 13), text=pat)
pat.set("CV(CV)(C)/VC(VC)(V)")
e1.pack(pady=(5, 5))

s1 = Scale(orient=HORIZONTAL, from_=1, to=150)
s1.set(50)
s1.pack(pady=(5, 5))

b2 = Button(text="Open a file", font=("", 10), command=open_file)
b2.pack(pady=(5, 5))

t1 = Text(height=5, width=60, font=("", 13))
t1.insert("1.0", "C: p, t, k, s, m, n\nV: a, i, u")
t1.pack(pady=(5, 5))

b1 = Button(text="Generate!", font=("", 13), command=gen_words)
b1.pack(pady=(0, 20))

t2 = Text(wrap=WORD, font=("", 14))
t2.pack()


root.mainloop()
