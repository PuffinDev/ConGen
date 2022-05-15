from congen import wordgen, cgg_parser

from tkinter import *
from tkinter import filedialog

from threading import Thread

def gen_words():
    pattern = e1.get()
    if not pattern:
        return
    amt = s1.get()

    groups, weights, rewrites = cgg_parser.parse_cgg(t1.get("1.0", END))

    words = wordgen.generate_words(amt, pattern, groups, weights=weights, rewrites=rewrites)
    pseudotext = wordgen.generate_pseudotext(words)

    t2.delete("1.0", END)
    t2.insert(END, pseudotext)

def highlight():
    highlighting = {"->": "rewrite_arrow", "([A-Z]):": "group_name", "\d+": "weight", "-\d": "weight"}
    last_indexes = {}
    while True:
        for text, tag in highlighting.items():
            index = t1.search(text, last_indexes[text] if text in last_indexes.keys() else "1.0", regexp=True)
            if not index:
                continue

            line, char = index.split(".")
            end_index = f"{line}.{int(char)+2}"

            t1.tag_add(tag, index, end_index)
            last_indexes[text] = end_index


def open_file():
    file = filedialog.askopenfilename(filetypes=(
        ('congen group files', '*.cgg'),
        ('All files', '*.*')
    ), initialdir="cggs/")
    try:
        with open(file) as f:
            text = f.read()
            t1.delete("1.0", END)
            t1.insert("1.0", text)
    except Exception:
        pass

root = Tk()
root.geometry("500x698")
root.resizable(False, False)
root.title("ConGen word generator")

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
s1.pack(pady=(5, 10))

b2 = Button(text="Open a file", font=("", 10), command=open_file)
b2.pack(pady=(5, 5))

t1 = Text(height=5, width=44, font=("", 13))
t1.tag_configure("rewrite_arrow", foreground="green")
t1.tag_configure("group_name", foreground="red")
t1.tag_configure("weight", foreground="blue")
t1.insert("1.0", "C: p, t, k, s, m, n\nV: a, i, u")
t1.pack(pady=(5, 5))

b1 = Button(text="Generate!", font=("", 13), command=gen_words)
b1.pack(pady=(0, 20))

t2 = Text(wrap=WORD, font=("", 14), width=43, height=10)
t2.pack()


thread = Thread(target=highlight, daemon=True)
thread.start()

root.mainloop()
