from modules.vigenere import vigenere
import sys

#select encryption or decryption
mode = input('Select mode (valid options are "encrypt" and "decrypt"): ').lower()

#input text and key
if mode == 'encrypt':
    text = input('Enter plaintext: ')
    key = input('Enter encryption key: ')
    print('Encrypted text:')
elif mode == 'decrypt':
    text = input('Enter encrypted text: ')
    key = input('Enter decryption key: ')
    print('Plaintext:')
else:
    print('Invalid mode selected. Acceptable options are "encrypt" and "decrypt"')
    sys.exit()

#output final text
print(vigenere(mode, text, key))