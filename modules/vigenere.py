from modules.setup import set_up_vars

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
        
    #add each character from the plaintext to l
    for i in range(len(text)):
        l.append(text[i])

        #only encrypt/decrypt letters
        if l[i].isalpha():

            #alphabetic positions of the letters from the text and key
            text_index = alph_l.index(text[i].lower())
            key_index = alph_l.index(full_key[count].lower())

            #lowercase letters
            if l[i].islower():

                #encrypt or decrypt character
                if mode.lower() == 'encrypt':
                    l[i] = alph_l[(text_index + key_index) % 26]
                elif mode.lower() == 'decrypt':
                    l[i] = alph_l[(text_index - key_index) % 26]
            
            #capital letters
            else:
                
                #encrypt or decrypt character
                if mode.lower() == 'encrypt':
                    l[i] = alph_u[(text_index + key_index) % 26]
                elif mode.lower() == 'decrypt':
                    l[i] = alph_u[(text_index - key_index) % 26]
        
            #increment count to move to the next letter of the key
            count += 1
    
    return ''.join(l)