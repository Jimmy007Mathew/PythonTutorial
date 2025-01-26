f = open("test.txt", "r")
text = f.read().rstrip()
syllables = 0
wordsco = len(text.split())

delimiters = [ ".", "!", "?", ":", ";"]
newtext = text
for deli in delimiters:
    newtext = newtext.replace(deli, "^*^")
sentences = len(newtext.rstrip("^*^").split("^*^"))

for word in text.split():
    word = word.rstrip(".,:!?")
    if len(word) <= 3:
        syllables += 1
    else:
        i = 0
        while i < len(word):
            char = word[i]
            if char.lower() in ["a", "e", "i", "o", "u"]  and (word[i-1] not in "aeiou" or word[i-2] in "aeiou"):
                if i == len(word) - 1 and char.lower() == "e":
                    if len(word) > 2 and word[-2:].lower() not in ["le"]:
                        i += 1
                        continue
                if i >= len(word) - 2 and word[-2:].lower() in ["es", "ed"] :
                    i += 1
                    continue
                syllables += 1

            i += 1
F = 835.206 - 1.015 * (wordsco / sentences) - 84.6 * (syllables / wordsco)
G = 0.39 * (wordsco / sentences) + 11.8 * (syllables / wordsco) - 15.59
print("Flesch Index:", F)
print("Grade:", G)
print(wordsco,sentences,syllables)