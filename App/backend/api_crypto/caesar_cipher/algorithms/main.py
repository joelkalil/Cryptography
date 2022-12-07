#########################################################################################
# 
#########################################################################################

class CaeserCipher:

    # Defining attributes
    def __init__(self, key=1, alphabet_type='ascii'):
        # All attributes
        self.key = key
        self.alphabet = alphabet_type
        
        self.define_alphabet()

    #########################################################################################
    # Setting my alphabet (letters which will be shifted/encrypted)
    def define_alphabet(self):

        if self.alphabet == 'ascii':
            alphabet = ''.join(chr(i) for i in range(0,127))
        elif self.alphabet == 'ascii_extended':
            alphabet = ''.join(chr(i) for i in range(0,255))
            
        self.alphabet = alphabet

    #########################################################################################
    # Function to encryption the text
    def encrypt(self, plain_text):
        
        # Starting the cipher_text
        cipher_text = ''

        for letter in plain_text:

            # Getting the index of each letter
            index = self.alphabet.index(letter)

            # Getting the new index for this letter
            index = (index + self.key) % len(self.alphabet)

            # Adding the letter in the cipher text
            cipher_text = cipher_text + self.alphabet[index]
        
        return cipher_text

    #########################################################################################
    # Function to decryption the text
    def decrypt(self, cipher_text):

        # Starting the plain_text
        plain_text = ''

        for letter in cipher_text:

            # Getting the index of each letter
            index = self.alphabet.index(letter)

            # Getting the new index for this letter
            index = (index - self.key) % len(self.alphabet)

            # Adding the letter in the cipher text
            plain_text = plain_text + self.alphabet[index]
        
        return plain_text