# ConGen

Congen genarates made-up words for conlangs using patterns and character groups.

# Examples

```py
groups = {
    "C": ["p", "t", "k", "s", "m", "n"],
    "V": ["a", "i", "u"]
}
```

```py
pattern = "CV(CV)(CV)/VCV(C)"
```

This pattern generates words with Either one consonant and one vowel with 2 optional repetitions, or a vowel, a consonant and a vowel with an optional last consonant.

Example output:

```
Ipum inap atu pusi ukat na ikup! Tusa apu iku apap tatimi anik asu. Usa pa! Apam upik sutata nisu uku ka amu sipu isu namu? Mu imi ikun nina ki aman pati kakita? Apip amu simuma tamu! Apim ku puti. Pa uki.
```
