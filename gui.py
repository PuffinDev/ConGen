import wordgen

from tkinter import *

# letter groups can be referenced with their identifiers in the pattern, 
# and a random char will be picked.
groups = {
    "V": ["a", "y", "e", "u", "aa", "o"],
    "C": ["v", "j", "z", "zh", "s", "r", "hg", "n", "d", "vv", "l", "g"]
}

# weights change the chances of a letter being picked.
weights = {
    "V": [8, 11, 4, 8, 5, 5],
    "C": [11, 4, 4, 3, 11, 3, 2, 10, 5, 2, 1, 5],
}

# replaces text in the generated words
rewrites = {
    "aa": "à",
    "hg": "ĥ",
    "zh": "ž"
}

# pattern = "CV(C)/VC(VC)(V)"


def gen_words():
    pattern = e1.get()
    if not pattern:
        return
    amt = s1.get()

    words = wordgen.generate_words(amt, pattern, groups, weights=weights, rewrites=rewrites)
    pseudotext = wordgen.generate_pseudotext(words)

    t1.delete("1.0", END)
    t1.insert(END, pseudotext)


root = Tk()
root.geometry("500x600")
root.resizable(False, False)

l1 = Label(text="ConGen", font=("", 17))
l1.pack(pady=(5, 10))

l2 = Label(text="Pattern", font=("", 13))
l2.pack()
e1 = Entry(font=("", 13))
e1.pack(pady=(5, 10))

s1 = Scale(orient=HORIZONTAL, from_=1, to=200)
s1.pack(pady=(5, 10))

b1 = Button(text="Generate!", font=("", 13), command=gen_words)
b1.pack(pady=(0, 20))

t1 = Text(font=("", 14))
t1.pack()


root.mainloop()
