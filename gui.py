from congen import wordgen, cgg_parser, pseudotextgen

from tkinter import *
from tkinter import filedialog, simpledialog

from threading import Thread

def gen_words():
    pattern = e1.get()
    if not pattern:
        return
    amt = s1.get()

    groups, weights, rewrites = cgg_parser.parse_cgg(t1.get("1.0", END))

    words = wordgen.generate_words(amt, pattern, groups, weights=weights, rewrites=rewrites)
    pseudotext = pseudotextgen.generate_pseudotext(words)

    t2.delete("1.0", END)
    t2.insert(END, pseudotext)

def highlight(*args):
    highlighting = {"->": "rewrite_arrow", "([A-Z]):": "group_name", "\d+": "weight", "-\d": "weight"}
    last_indexes = {}

    for text, tag in highlighting.items():
        done = []
        while True:
            index = t1.search(text, last_indexes[text] if text in last_indexes.keys() else "1.0", regexp=True)
            if not index or index in done:
                break

            line, char = index.split(".")
            end_index = f"{line}.{int(char)+2}"

            t1.tag_add(tag, index, end_index)
            last_indexes[text] = end_index
            done.append(index)

        done.clear()

def open_file():
    file = filedialog.askopenfilename(filetypes=(
        ('congen group files', '*.cgg'),
        ('All files', '*.*')
    ), initialdir="cggs/")
    if file == "":
        return

    try:
        with open(file) as f:
            text = f.read()
            t1.delete("1.0", END)
            t1.insert("1.0", text)
            highlight()
    except Exception as e:
        simpledialog.messagebox.showerror("Error", e)
        print(e)
        pass

def save_file():
    file = filedialog.asksaveasfile(filetypes=(
        ('congen group files', '*.cgg'),
        ('All files', '*.*')
    ), initialdir="cggs/")
    if not file:
        return

    try:
        with open(file.name, "w") as f:
            f.write(t1.get("1.0", END))
        simpledialog.messagebox.showinfo("Info", "Saved letter groups to " + file.name)
    except Exception as e:
        simpledialog.messagebox.showerror("Error", e)
        print(e)
        pass

root = Tk()
root.config()
root.title("ConGen word generator")

l1 = Label(text="ConGen", font=("", 17))
l1.grid(pady=(5, 5), row=0, columnspan=2)

t1 = Text(height=15, width=44, font=("", 13))
t1.tag_configure("rewrite_arrow", foreground="green")
t1.tag_configure("group_name", foreground="red")
t1.tag_configure("weight", foreground="blue")
t1.insert("1.0", "C: p, t, k, s, m, n\nV: a, i, u")
highlight()
t1.bind_all('<Key>', highlight)
t1.grid(pady=(5, 5), row=1, columnspan=2)

b2 = Button(text="Load", font=("", 10), command=open_file)
b2.grid(pady=(5, 5), column=0, row=2)

b3 = Button(text="Save", font=("", 10), command=save_file)
b3.grid(pady=(5, 5), column=1, row=2)

l2 = Label(text="Pattern", font=("", 11))
l2.grid(columnspan=2)

pat = IntVar()
e1 = Entry(font=("", 13), text=pat)
pat.set("CV(CV)(C)/VC(VC)(V)")
e1.grid(columnspan=2)

l2 = Label(text="Words", font=("", 11))
l2.grid(columnspan=2)

s1 = Scale(orient=HORIZONTAL, from_=1, to=300)
s1.set(50)
s1.grid(row=5, columnspan=2)

b1 = Button(text="Generate!", font=("", 13), command=gen_words)
b1.grid(pady=(0, 20), columnspan=2)

l4 = Label(text="Output", font=("", 13))
l4.grid(column=2, row=0, pady=(2, 0))

t2 = Text(wrap=WORD, font=("", 14), width=43)
t2.grid(column=2, row=1, padx=(10, 10), pady=(5, 10), rowspan=8)

root.mainloop()
