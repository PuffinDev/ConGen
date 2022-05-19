import random

PROBIBILITY = 0.5 # probability of including values inside parentheses
WORD_AMOUNT = 100 # amount of words to genarate
FILTER_DUPLICATES = True

def push(obj, l, depth):
    while depth:
        l = l[-1]
        depth -= 1

    l.append(obj)

def parse_parentheses(s):
    groups = []
    depth = 0

    try:
        for char in s:
            if char == '(':
                push([], groups, depth)
                depth += 1
            elif char == ')':
                depth -= 1
            else:
                push(char, groups, depth)
    except IndexError:
        raise ValueError('Parentheses mismatch')

    if depth > 0:
        raise ValueError('Parentheses mismatch')
    else:
        return groups

def apply_rewrites(text, rewrites):
    for original, rewriten in rewrites.items():
        text = text.replace(original, rewriten)

    return text

def evaluate(value, letter_groups, probability=PROBIBILITY, weights=False, first_level=False):
    result = ""

    if type(value) == str:
        if value in letter_groups:
            if weights == True:
                weights = list(range(len(letter_groups[value]), 0, -1))
                result += random.sample(letter_groups[value], k=1, counts=weights)[0]
            elif weights:
                result += random.sample(letter_groups[value], k=1, counts=weights[value])[0]
            else:
                result += random.choice(letter_groups[value])
        else:
            result += value
    else:
        if random.random() < probability or first_level:
            if "/" in value:
                index = value.index("/")
                v1, v2 = value[:index], value[index+1:]

                if random.randint(0, 1) == 1:
                    value = v1
                else:
                    value = v2

            for subval in value:
                result += evaluate(subval, letter_groups, weights=weights)

    return result

def generate_word(pattern, letter_groups, weights=False, rewrites={}):
    pattern = parse_parentheses(pattern)
    result = ""
    result += apply_rewrites(evaluate(pattern, letter_groups, weights=weights, first_level=True), rewrites)
    return result

def generate_words(amount, pattern, letter_groups, weights=False, rewrites={}):
    words = []
    for i in range(amount):
        words.append(generate_word(pattern, letter_groups, weights=weights, rewrites=rewrites))

    return words

