import hashlib
from Crypto import Random
from Crypto.Cipher import AES
from base64 import b64encode, b64decode

class AESCipher:

    def __init__(self, key):

        self.block_size = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()


    def add_padding(self, plain_text):
        
        bytes_to_pad = self.block_size - len(plain_text) % self.block_size

        # PKCS or CMS "Cryptographic Message Syntax"
        ascii_string = chr(bytes_to_pad)
        padding_string = ascii_string * bytes_to_pad

        return plain_text + padding_string

    
    def remove_padding(self, txt):

        last_character = txt[len(txt) - 1:]
        return txt[:-ord(last_character)]


    def encrypt(self, plain_text):

        plain_text = self.add_padding(plain_text)

        # IV (Initialization Vector - Seed)
        iv = Random.new().read(self.block_size)
        
        cipher = AES.new(self.key, AES.MODE_CBC, iv)

        encrypted_text = cipher.encrypt(plain_text.encode())

        return b64encode(iv + encrypted_text).decode("utf-8")

    def decrypt(self, encrypted_text):

        encrypted_text = b64decode(encrypted_text)

        iv = encrypted_text[:self.block_size]
        
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        
        plain_text = cipher.decrypt(encrypted_text[self.block_size:]).decode('utf-8')

        return self.remove_padding(plain_text)


if __name__ == "__main__":

    aes = AESCipher('Viego')

    message = 'LOREM IPSUM IS SIMPLY DUMMY TEXT OF THE PRINTING AND TYPESETTING INDUSTRY LOREM IPSUM HAS BEEN THE INDUSTRYS STANDARD DUMMY TEXT EVER SINCE THE 1500S WHEN AN UNKNOWN PRINTER TOOK A GALLEY OF TYPE AND SCRAMBLED IT TO MAKE A TYPE SPECIMEN BOOK IT HAS SURVIVED NOT ONLY FIVE CENTURIES BUT ALSO THE LEAP INTO ELECTRONIC TYPESETTING, REMAINING ESSENTIALLY UNCHANGED IT WAS POPULARISED IN THE 1960S WITH THE RELEASE OF LETRASET SHEETS CONTAINING LOREM IPSUM PASSAGES AND MORE RECENTLY WITH DESKTOP PUBLISHING SOFTWARE LIKE ALDUS PAGEMAKER INCLUDING VERSIONS OF LOREM IPSUM'

    encrypted = aes.encrypt(message)
    print(encrypted)

    decrypted = aes.decrypt(encrypted)
    print(decrypted)