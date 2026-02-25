from modules.setup import set_up_vars
import sys

def vigenere(mode, text, key):
    '''
    Encrypts plaintext or decrypts ciphertext using a Vigenere cipher with a provided key
    '''

    #match key's length to that of the text. create two alphabets to allow for case preservation
    vars = set_up_vars(text, key)
    full_key = vars['full_key']
    alph_l = vars['alph_l']
    alph_u = vars['alph_u']

    #l will hold the final list of characters. count is used to track the current position within the key
    l = []
    count = 0

    #encryption
    if mode.lower() == 'encrypt':
        
        #add each character from the plaintext to l
        for i in range(len(text)):
            l.append(text[i])
            
            #encrypt the plaintext character, leaving non-letters as they are and preserving case
            if l[i].isalpha():
                if l[i].islower():
                    l[i] = alph_l[(alph_l.index(text[i]) + alph_l.index(full_key[count])) % 26]
                else:
                    l[i] = alph_u[(alph_u.index(text[i]) + alph_u.index(full_key[count].upper())) % 26]
        
                #increment count to move to the next letter of the key
                count += 1

    #decryption
    elif mode.lower() == 'decrypt':
        
        #add each character from the plaintext to l
        for i in range(len(text)):
            l.append(text[i])

            #decrypt the encrypted character, leaving non-letters as they are and preserving case
            if l[i].isalpha():
                if l[i].islower():
                    l[i] = alph_l[(alph_l.index(text[i]) - alph_l.index(full_key[count])) % 26]
                else:
                    l[i] = alph_u[(alph_u.index(text[i]) - alph_u.index(full_key[count].upper())) % 26]
                
                #increment count to move to the next letter of the key
                count += 1
    
    return ''.join(l)