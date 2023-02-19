#########################################################################################
# Vernam Cipher                                                                         #
#########################################################################################
# Imports
import random

#########################################################################################
class VernamCipher:
    # Defining attributes
    def __init__(self, key='default'):
        # All attributes
        self.key = key
        self.random = random
        self.alphabet = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,!?:; '

        self.set_seed()

    #########################################################################################
    # Converting the key passed in a seed for the random function
    def set_seed(self):
        seed = 0
        for i in self.key:
            seed += self.key.find(i) 
        self.random.seed(seed)

    #########################################################################################
    # Function to generate the random key with the size of the text.
    def random_sequence(self, text):
        random_seq = ''

        for _ in range(len(text)):
            random_seq += self.alphabet[self.random.randint(0, len(self.alphabet)-1)]

        return random_seq

    #########################################################################################
    # Function to encryption the text
    def encrypt(self, plain_text):

        self.key = self.random_sequence(plain_text)
        
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

        self.key = self.random_sequence(cipher_text)

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