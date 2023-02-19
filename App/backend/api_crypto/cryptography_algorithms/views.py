###########################################################################################
# Imports                                                                                 #
###########################################################################################
from cryptography_algorithms.algorithms.caeser_cipher import CaeserCipher
from cryptography_algorithms.algorithms.vigenere_cipher import VigenereCipher
from cryptography_algorithms.algorithms.vernam_cipher import VernamCipher
from cryptography_algorithms.algorithms.aes_cipher import AESCipher



from django.http import Http404
from rest_framework.response import Response
from rest_framework.decorators import api_view

###########################################################################################
# Requests Classes                                                                        #
###########################################################################################
###########################################################################################
# Caesar Cipher                                                                           #
###########################################################################################
# .../caesar_cipher/encrypt/
@api_view(['POST'])
def caesar_cipher_encrypt(request):
    key = request.headers.get('key', None)
    text = request.POST.get('text', None)

    cipher = CaeserCipher(key=int(key))

    response = {
        "cipher_text": cipher.encrypt(text),
    }

    return Response(response)

###########################################################################################
# .../caesar_cipher/decrypt/
@api_view(['POST'])
def caesar_cipher_decrypt(request):
    key = request.headers.get('key', None)
    text = request.POST.get('text', None)

    cipher = CaeserCipher(key=int(key))

    response = {
        "plain_text": cipher.decrypt(text),
    }

    return Response(response)

###########################################################################################
# Vigenere Cipher                                                                         #
###########################################################################################
# .../vigenere_cipher/encrypt/
@api_view(['POST'])
def vigenere_cipher_encrypt(request):
    key = request.headers.get('key', 'default')
    text = request.POST.get('text', None)

    cipher = VigenereCipher(key=str(key))

    response = {
        "cipher_text": cipher.encrypt(text),
    }

    return Response(response)

###########################################################################################
# .../vigenere_cipher/decrypt/
@api_view(['POST'])
def vigenere_cipher_decrypt(request):
    key = request.headers.get('key', 'default')
    text = request.POST.get('text', None)

    cipher = VigenereCipher(key=str(key))

    response = {
        "plain_text": cipher.decrypt(text),
    }

    return Response(response)

###########################################################################################
# Vernam Cipher                                                                           #
###########################################################################################
# .../vernam_cipher/encrypt/
@api_view(['POST'])
def vernam_cipher_encrypt(request):
    key = request.headers.get('key', 'default')
    text = request.POST.get('text', None)

    cipher = VernamCipher(key=str(key))

    response = {
        "cipher_text": cipher.encrypt(text),
    }

    return Response(response)

###########################################################################################
# .../vernam_cipher/decrypt/
@api_view(['POST'])
def vernam_cipher_decrypt(request):
    key = request.headers.get('key', 'default')
    text = request.POST.get('text', None)

    cipher = VernamCipher(key=str(key))

    response = {
        "plain_text": cipher.decrypt(text),
    }

    return Response(response)

###########################################################################################
# AES Cipher                                                                              #
###########################################################################################
# .../vernam_cipher/encrypt/
@api_view(['POST'])
def aes_cipher_encrypt(request):
    key = request.headers.get('key', 'default')
    text = request.POST.get('text', None)

    cipher = AESCipher(key=str(key))

    response = {
        "cipher_text": cipher.encrypt(text),
    }

    return Response(response)

###########################################################################################
# .../vernam_cipher/decrypt/
@api_view(['POST'])
def aes_cipher_decrypt(request):
    key = request.headers.get('key', 'default')
    text = request.POST.get('text', None)

    cipher = AESCipher(key=str(key))

    response = {
        "plain_text": cipher.decrypt(text),
    }

    return Response(response)

###########################################################################################