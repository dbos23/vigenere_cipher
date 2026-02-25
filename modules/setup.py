def set_up_vars(text, key):
    '''
    Extends or shortens a key until its length exactly matches that of the text it's encrypting or decrypting.
    Also creates two alphabets that are used to identify the shift applied by each letter of the key.
    Having two of them allows for the preservation of the case in the original text
    '''

    #two alphabets are created to preserve the case during encryption
    alph_l = 'abcdefghijklmnopqrstuvwxyz'
    alph_u = alph_l.upper()

    #the key is repeated until it matches or exceeds the length of the text
    key = key.lower()
    full_key = key
    while len(text) > len(full_key):
        full_key += key

    #if the key is longer than the plaintext, it's truncated to match its length exactly
    if len(full_key) > len(text):
        diff = len(full_key) - len(text)
        full_key = full_key[:len(full_key) - diff]

    #create dictionary of variables used for both encryption and decryption
    output = {
        'full_key': full_key,
        'alph_l': alph_l,
        'alph_u': alph_u
    }

    return output