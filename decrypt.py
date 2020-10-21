def next_letter(letter, step=1):
    return chr((ord(letter) - 97 - step) % 26 + 97)


def decrypt(encrypted_text, step=1):
    decrypted_text = ''
    for letter in encrypted_text:
        decrypted_text += next_letter(letter, step)
    return decrypted_text
