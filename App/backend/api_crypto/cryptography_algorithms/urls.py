from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from cryptography_algorithms import views

urlpatterns = [
    path('caesar_cipher/encrypt/', views.caesar_cipher_encrypt),
    path('caesar_cipher/decrypt/', views.caesar_cipher_decrypt),
    
    path('vigenere_cipher/encrypt/', views.vigenere_cipher_encrypt),
    path('vigenere_cipher/decrypt/', views.vigenere_cipher_decrypt),

    path('vernam_cipher/encrypt/', views.vernam_cipher_encrypt),
    path('vernam_cipher/decrypt/', views.vernam_cipher_decrypt),

    path('aes_cipher/encrypt/', views.aes_cipher_encrypt),
    path('aes_cipher/decrypt/', views.aes_cipher_decrypt)
]

urlpatterns = format_suffix_patterns(urlpatterns)