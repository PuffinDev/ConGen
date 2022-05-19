import random

def generate_pseudotext(words, max_sentance_len=15):
    pseudotext = ""
    sentence_len = random.randint(1, max_sentance_len)
    i = 0
    for j, word in enumerate(words):
        i += 1

        if i == 1:
            pseudotext += word.capitalize()

        elif i-1 >= sentence_len or j == len(words)-1:
            sentence_len = random.randint(1, max_sentance_len)
            pseudotext += word + random.choice(["!", ".", ".", ".", "?"])
            i = 0

        else:
            pseudotext += word

        pseudotext += " "

    return pseudotext