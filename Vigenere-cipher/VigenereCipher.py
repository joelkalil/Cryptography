#########################################################################################
# Setting my alphabet (letters which will be shifted/encrypted)
alphabet = ''.join(chr(i) for i in range(31,255))

# If you want to see what we considered as alphabet.
# print(alphabet)

#########################################################################################
# Function to encryption the text
def vigenere_encryption(plain_text, private_key='Love is War'):

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
def vigenere_decryption(cipher_text, private_key='Love is War'):

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
    text = 'O Lorem Ipsum é um texto modelo da indústria tipográfica e de impressão. O Lorem Ipsum tem vindo a ser o texto padrão usado por estas indústrias desde o ano de 1500, quando uma misturou os caracteres de um texto para criar um espécime de livro. Este texto não só sobreviveu 5 séculos, mas também o salto para a tipografia electrónica, mantendo-se essencialmente inalterada. Foi popularizada nos anos 60 com a disponibilização das folhas de Letraset, que continham passagens com Lorem Ipsum, e mais recentemente com os programas de publicação como o Aldus PageMaker que incluem versões do Lorem Ipsum.'
    
    # Crypted
    print(vigenere_encryption(text))
    # Decrypted
    print(vigenere_decryption(vigenere_encryption(text)))