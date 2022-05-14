import wordgen

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

# specifies how words will be selected
# anything in (parentheses) has a 50% chance of being included
# /slashes indicate either the stuff on the left or the right will be included, but not both
# e.g. CV/VC indicates the word will either be CV or VC
pattern = "CV(C)/VC(VC)(V)"

# generates a list of words
words = wordgen.generate_words(10, pattern, groups, weights=weights, rewrites=rewrites)
# creates fake sentances
pseudotext = wordgen.generate_pseudotext(words)

print(pseudotext)
