#########################################################################################
# Setting my alphabet (letters which will be shifted/encrypted)
alphabet = ''.join(chr(i) for i in range(31,255))

# If you want to see what we considered as alphabet.
# print(alphabet)

#########################################################################################
# Function to encryption the text
def caesar_encryption(plain_text, private_key):
    
    # Starting the cipher_text
    cipher_text = ''

    for letter in plain_text:

        # Getting the index of each letter
        index = alphabet.index(letter)

        # Getting the new index for this letter
        index = (index + private_key) % len(alphabet)

        # Adding the letter in the cipher text
        cipher_text = cipher_text + alphabet[index]
    
    return cipher_text

#########################################################################################
# Function to decryption the text
def caesar_decryption(cipher_text, private_key):

    # Starting the plain_text
    plain_text = ''

    for letter in cipher_text:

        # Getting the index of each letter
        index = alphabet.index(letter)

        # Getting the new index for this letter
        index = (index - private_key) % len(alphabet)

        # Adding the letter in the cipher text
        plain_text = plain_text + alphabet[index]
    
    return plain_text

#########################################################################################
# Testing the cryptography functions
if __name__ == '__main__':
    # Test case :
    text = 'Lorem Ipsum is a text template for the typographic and printing industry. Lorem Ipsum has been the standard text used by these industries since the 1500s, when one mixed characters from a text to create a book specimen. This text not only survived 5 centuries, but also the leap into electronic typography, remaining essentially unchanged. It was popularized in the 1960s with the availability of Letraset sheets, which contained passages with Lorem Ipsum, and more recently with publishing programs such as Aldus PageMaker that include versions of Lorem Ipsum.'
    
    # Crypted
    print(caesar_encryption(text,220))
    # Decrypted
    print(caesar_decryption(caesar_encryption(text,220), 220))