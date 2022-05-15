def text_to_ipa(text, phonetics):
    text = text.lower()
    ipa_text = ""
    for char in text:
        ipa_text += phonetics[char] if char in phonetics else char

    return ipa_text
