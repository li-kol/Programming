def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    keyword_index = 0
    for index, char in enumerate(plaintext):
        if char.isalpha():
            if char.isupper():
                base = ord("A")
            else:
                base = ord("a")
            key_shift = ord(keyword[index % len(keyword)]) - base
            char_shift = ord(char) - base
            shift = (char_shift + key_shift) % 26
            ciphertext += chr(shift + base)
            keyword_index += 1
        else:
            ciphertext += char

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""

    for index, char in enumerate(ciphertext):
        if char.isalpha():
            keyword_char = keyword[index % len(keyword)]
            if char.islower():
                base = ord("a")
            else:
                base = ord("A")
            key_shift = ord(keyword_char) - base
            char_shift = ord(char) - base
            shift = (char_shift - key_shift + 26) % 26

            decrypted_char = chr(shift + base)
            plaintext += decrypted_char
        else:
            plaintext += char

    return plaintext
