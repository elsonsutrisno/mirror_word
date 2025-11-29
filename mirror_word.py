# mirror word
alphabet = list("abcdefghijklmnopqrstuvwxyz")

word = "elson"

# convert each character to its alphabet index
indexes = [alphabet.index(ch) for ch in word]

# mirror the index
for i, idx in enumerate(indexes):
    indexes[i] = len(alphabet) - (idx + 1)

# convert back to letters
mirrored = [alphabet[i] for i in indexes]

print(mirrored)