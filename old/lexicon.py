import json

dictionary = {}

with open("dictionary.json", "r") as f:
    dictionary = json.load(f)

def add_word(word, definition):
    global dictionary
    dictionary[word] = definition
    with open("dictionary.json", "w") as f:
        json.dump(dictionary, f)

while 1:
    opt = input("Conlanger\n\n1) display dictionary\n2) add word\n3) translate\n\n>> ")

    print("\n")
    if opt == "1":
        for word, definition in dictionary.items():
            print(f"{word} | {definition}")

    elif opt == "2":
        word = input("Enter a word >> ")
        definition = input("Enter definition >> ")
        dictionary[word] = definition
        print("Word added")

    print("\n")