from django.urls import path
from caesar_cipher.views import views

urlpatterns = [
    path('<str:alphabet_type>/encrypt/', views.encrypt)
]