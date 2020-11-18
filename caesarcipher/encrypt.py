def next_letter(letter, step=1):
    return chr((ord(letter) - 97 + step) % 26 + 97)


def encrypt(text, step=1):
    encrypted_text = ""
    for letter in text:
        encrypted_text += next_letter(letter, step)
    return encrypted_text
