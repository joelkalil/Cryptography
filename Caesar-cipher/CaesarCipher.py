#########################################################################################
# Setting my alphabet (letters which will be shifted/encrypted)
alphabet = ''.join(chr(i) for i in range(31,255))

#########################################################################################
# Function to encryption the text
def caesar_encryption(plain_text, private_key):

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

if __name__ == '__main__':
    # Test case :
    text = 'O Lorem Ipsum é um texto modelo da indústria tipográfica e de impressão. O Lorem Ipsum tem vindo a ser o texto padrão usado por estas indústrias desde o ano de 1500, quando uma misturou os caracteres de um texto para criar um espécime de livro. Este texto não só sobreviveu 5 séculos, mas também o salto para a tipografia electrónica, mantendo-se essencialmente inalterada. Foi popularizada nos anos 60 com a disponibilização das folhas de Letraset, que continham passagens com Lorem Ipsum, e mais recentemente com os programas de publicação como o Aldus PageMaker que incluem versões do Lorem Ipsum.'
    
    # Crypted
    print(caesar_encryption(text,220))
    # Decrypted
    print(caesar_decryption(caesar_encryption(text,220), 220))