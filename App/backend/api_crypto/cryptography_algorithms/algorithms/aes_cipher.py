#########################################################################################
# AES Cipher                                                                            #
#########################################################################################
# Imports
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
from base64 import b64encode, b64decode

#########################################################################################
class AESCipher:
    # Defining attributes
    def __init__(self, key='default'):
        # All attributes
        self.block_size = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    #########################################################################################
    # Function to add padding in the text
    def add_padding(self, plain_text):
        
        bytes_to_pad = self.block_size - len(plain_text) % self.block_size

        # PKCS or CMS "Cryptographic Message Syntax"
        ascii_string = chr(bytes_to_pad)
        padding_string = ascii_string * bytes_to_pad

        return plain_text + padding_string

    #########################################################################################
    # Function to remove padding in the text
    def remove_padding(self, txt):

        last_character = txt[len(txt) - 1:]
        return txt[:-ord(last_character)]

    #########################################################################################
    # Function to encrypt the text
    def encrypt(self, plain_text):

        plain_text = self.add_padding(plain_text)

        # IV (Initialization Vector - Seed)
        iv = Random.new().read(self.block_size)
        
        cipher = AES.new(self.key, AES.MODE_CBC, iv)

        encrypted_text = cipher.encrypt(plain_text.encode())

        return b64encode(iv + encrypted_text).decode("utf-8")

    #########################################################################################
    # Function to decrypt the text
    def decrypt(self, encrypted_text):

        encrypted_text = b64decode(encrypted_text)

        iv = encrypted_text[:self.block_size]
        
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        
        plain_text = cipher.decrypt(encrypted_text[self.block_size:]).decode('utf-8')

        return self.remove_padding(plain_text)
    
    #########################################################################################