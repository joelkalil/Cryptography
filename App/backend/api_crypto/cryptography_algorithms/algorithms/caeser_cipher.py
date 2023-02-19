#########################################################################################
# Caeser Cipher                                                                         #
#########################################################################################
class CaeserCipher:
    # Defining attributes
    def __init__(self, key=1):
        # All attributes
        self.key = key
        self.alphabet = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,!?:; '

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
    
    #########################################################################################