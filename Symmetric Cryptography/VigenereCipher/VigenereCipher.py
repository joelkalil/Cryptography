#########################################################################################
# Setting my alphabet (letters which will be shifted/encrypted)
# All characters usually used in US English
#alphabet = ''.join(chr(i) for i in range(31,127))
alphabet = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# If you want to see what we considered as alphabet.
# print(alphabet)

#########################################################################################
# Function to encryption the text
def vigenere_encryption(plain_text, private_key='LOVE IS WAR'):

    # It represents the index of the letters in the key
    key_index = 0

    # Starting the cipher_text
    cipher_text = ''

    # We have to consider all the characters in the plain_text
    for character in plain_text:
        # Number of shifts = index of character in the alphabet + index of the character in the key
        index = (alphabet.find(character) + alphabet.find(private_key[key_index])) % len(alphabet)

        # Keep appending the encrypted character to the cipher_text
        cipher_text = cipher_text + alphabet[index]

        # Increment the key index because we consider the next letter
        key_index += 1

        # If we've considered the last letter of the key we start again
        if key_index == len(private_key):
            key_index = 0 

    return cipher_text

#########################################################################################
# Function to encryption the text
def vigenere_decryption(cipher_text, private_key='LOVE IS WAR'):

    # It represents the index of the letters in the key
    key_index = 0

    # Starting the cipher_text
    plain_text = ''

    # We have to consider all the characters in the plain_text
    for character in cipher_text:
        # Number of shifts = index of character in the alphabet + index of the character in the key
        index = (alphabet.find(character) - alphabet.find(private_key[key_index])) % len(alphabet)

        # Keep appending the encrypted character to the cipher_text
        plain_text = plain_text + alphabet[index]

        # Increment the key index because we consider the next letter
        key_index += 1

        # If we've considered the last letter of the key we start again
        if key_index == len(private_key):
            key_index = 0 

    return plain_text

#########################################################################################
# Testing the cryptography functions

if __name__ == '__main__':
    # Test case :
    text = "LOREM IPSUM IS SIMPLY DUMMY TEXT OF THE PRINTING AND TYPESETTING INDUSTRY LOREM IPSUM HAS BEEN THE INDUSTRYS STANDARD DUMMY TEXT EVER SINCE THE 1500S WHEN AN UNKNOWN PRINTER TOOK A GALLEY OF TYPE AND SCRAMBLED IT TO MAKE A TYPE SPECIMEN BOOK IT HAS SURVIVED NOT ONLY FIVE CENTURIES BUT ALSO THE LEAP INTO ELECTRONIC TYPESETTING, REMAINING ESSENTIALLY UNCHANGED IT WAS POPULARISED IN THE 1960S WITH THE RELEASE OF LETRASET SHEETS CONTAINING LOREM IPSUM PASSAGES AND MORE RECENTLY WITH DESKTOP PUBLISHING SOFTWARE LIKE ALDUS PAGEMAKER INCLUDING VERSIONS OF LOREM IPSUM"

    # Crypted
    print("..." + vigenere_encryption(text, "COMIDA") + "...")
    # Decrypted
    #print(vigenere_decryption(vigenere_encryption(text)))