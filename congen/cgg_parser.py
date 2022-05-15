def parse_cgg(text):
    """
    Parses ConGenGroups text e.g.
    C: p, t, k, s
    """

    groups_text = text.replace(" ", "")
    groups = {}
    weights = {}

    for line in groups_text.split("\n"):
        if ":" not in line:
            continue
        group, letters = line.split(":", 1)
        groups[group] = []
        weights[group] = []

        for letter in letters.split(","):
            if "-" in letter:
                letter, weight = letter.split("-")
                weight = int(weight)
                groups[group].append(letter)
                weights[group].append(weight)
            else:
                groups[group].append(letter)
                weights[group].append(0)

        if not any(weights[group]):
            weights[group] = [1 for _ in weights[group]]

    return groups, weights