#########################################################################################
# Imports

from random import randint

#########################################################################################
# Setting my alphabet (letters which will be shifted/encrypted)
# All characters usually used in US English
alphabet = ''.join(chr(i) for i in range(31,127))
#alphabet = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# If you want to see what we considered as alphabet.
# print(alphabet)

#########################################################################################
# Function to generate the random key with the size of the text.
def random_sequence(text):
    random = []

    for _ in range(len(text)):
        random.append(randint(0, len(alphabet)-1))

    return random

#########################################################################################
# Function to encryption the text
def vernam_encryption(plain_text, private_key):

    # It represents the index of the letters in the key
    key_index = 0

    # Starting the cipher_text
    cipher_text = ''

    # We have to consider all the plain_text letters: enumerate returns the item + it's index.
    for index, char in enumerate(text):
        # The value with which we shift the give letter
        key_index = private_key[index]

        # The given letter in the plain_text
        char_index = alphabet.find(char)

        cipher_text += alphabet[(char_index + key_index) % len(alphabet)]

    return cipher_text

#########################################################################################
# Function to decryption the text
def vernam_decryption(cipher_text, private_key=None):

    # It represents the index of the letters in the key
    key_index = 0

    # Starting the cipher_text
    plain_text = ''

    # We have to consider all the plain_text letters: enumerate returns the item + it's index.
    for index, char in enumerate(cipher_text):
        # The value with which we shift the give letter
        key_index = private_key[index]

        # The given letter in the cipher_text
        char_index = alphabet.find(char)

        plain_text += alphabet[(char_index - key_index) % len(alphabet)]

    return plain_text

#########################################################################################
# Version with XOR, which uses the same function to encryption and decryption
def vernam_xor(text, key=None):
    # Starting the text
    output = ''
    
    for i in range(len(text)):
        output += chr(key[i]^ord(text[i]))

    return output

#########################################################################################
# Testing the cryptography functions
if __name__ == '__main__':
    # Test case :
    text = "LOREM IPSUM IS SIMPLY DUMMY TEXT OF THE PRINTING AND TYPESETTING INDUSTRY LOREM IPSUM HAS BEEN THE INDUSTRYS STANDARD DUMMY TEXT EVER SINCE THE 1500S WHEN AN UNKNOWN PRINTER TOOK A GALLEY OF TYPE AND SCRAMBLED IT TO MAKE A TYPE SPECIMEN BOOK IT HAS SURVIVED NOT ONLY FIVE CENTURIES BUT ALSO THE LEAP INTO ELECTRONIC TYPESETTING, REMAINING ESSENTIALLY UNCHANGED IT WAS POPULARISED IN THE 1960S WITH THE RELEASE OF LETRASET SHEETS CONTAINING LOREM IPSUM PASSAGES AND MORE RECENTLY WITH DESKTOP PUBLISHING SOFTWARE LIKE ALDUS PAGEMAKER INCLUDING VERSIONS OF LOREM IPSUM"

    key = random_sequence(text)
    # Crypted
    print(vernam_encryption(text, key))
    print(vernam_xor(text, key))
    # Decrypted
    print(vernam_decryption(vernam_encryption(text, key), key))
    print(vernam_xor(vernam_xor(text,key), key))