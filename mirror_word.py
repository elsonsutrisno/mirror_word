# mirror word
def mirror(word):
    if not word.isalpha():
        return "Invalid: only letters allowed"

    alphabet = list("abcdefghijklmnopqrstuvwxyz")

    # convert each character to its alphabet index
    indexes = [alphabet.index(ch) for ch in word.lower()]

    # mirror the index
    for i, idx in enumerate(indexes):
        indexes[i] = len(alphabet) - (idx + 1)

    # convert back to letters
    mirrored = [alphabet[i] for i in indexes]

    result = "".join(mirrored)
    return result

if __name__ == "__main__": 
    word = input("Input Word: ")
    mirrored_word = mirror(word)
    print(mirrored_word)
