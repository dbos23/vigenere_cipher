def vig_encrypt(message, key):
    '''Encrypts plaintext using a Vigenere cipher with a given key.'''

    alph_l = 'abcdefghijklmnopqrstuvwxyz'
    alph_u = alph_l.upper()
    key = key.lower()
    full_key = key

    while len(message) > len(full_key):
        full_key += key

    if len(full_key) > len(message):
        diff = len(full_key) - len(message)
        full_key = full_key[:len(full_key) - diff]

    l = []
    count = 0
    for i in range(len(message)):
        l.append(message[i])
        if l[i].isalpha():
            if l[i].islower():
                l[i] = alph_l[(alph_l.index(message[i]) + alph_l.index(full_key[count])) % 26]
            else:
                l[i] = alph_u[(alph_u.index(message[i]) + alph_u.index(full_key[count].upper())) % 26]
            count += 1

    return ''.join(l)


def vig_decrypt(text, key):
    '''Decrypts ciphertext using a Vigenere cipher with a given key.'''

    alph_l = 'abcdefghijklmnopqrstuvwxyz'
    alph_u = alph_l.upper()
    key = key.lower()
    full_key = key

    while len(text) > len(full_key):
        full_key += key

    if len(full_key) > len(text):
        diff = len(full_key) - len(text)
        full_key = full_key[:len(full_key) - diff]

    l = []
    count = 0
    for i in range(len(text)):
        l.append(text[i])
        if l[i].isalpha():
            if l[i].islower():
                l[i] = alph_l[(alph_l.index(text[i]) - alph_l.index(full_key[count])) % 26]
            else:
                l[i] = alph_u[(alph_u.index(text[i]) - alph_u.index(full_key[count].upper())) % 26]
            count += 1

    return ''.join(l)
