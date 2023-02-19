#########################################################################################
# Vigenere Cipher                                                                         #
#########################################################################################
class VigenereCipher:
    # Defining attributes
    def __init__(self, key='default'):
        # All attributes
        self.key = key
        self.alphabet = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,!?:; '

    #########################################################################################
    # Function to encryption the text
    def encrypt(self, plain_text):
        
        # It represents the index of the letters in the key
        key_index = 0

        # Starting the cipher_text
        cipher_text = ''

        # We have to consider all the characters in the plain_text
        for character in plain_text:
            # Number of shifts = index of character in the alphabet + index of the character in the key
            index = (self.alphabet.find(character) + self.alphabet.find(self.key[key_index])) % len(self.alphabet)

            # Keep appending the encrypted character to the cipher_text
            cipher_text = cipher_text + self.alphabet[index]

            # Increment the key index because we consider the next letter
            key_index += 1

            # If we've considered the last letter of the key we start again
            if key_index == len(self.key):
                key_index = 0 

        return cipher_text

    #########################################################################################
    # Function to decryption the text
    def decrypt(self, cipher_text):

        # It represents the index of the letters in the key
        key_index = 0

        # Starting the cipher_text
        plain_text = ''

        # We have to consider all the characters in the plain_text
        for character in cipher_text:
            # Number of shifts = index of character in the alphabet + index of the character in the key
            index = (self.alphabet.find(character) - self.alphabet.find(self.key[key_index])) % len(self.alphabet)

            # Keep appending the encrypted character to the cipher_text
            plain_text = plain_text + self.alphabet[index]

            # Increment the key index because we consider the next letter
            key_index += 1

            # If we've considered the last letter of the key we start again
            if key_index == len(self.key):
                key_index = 0 

        return plain_text
    
    #########################################################################################