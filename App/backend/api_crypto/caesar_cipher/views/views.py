from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from caesar_cipher.algorithms.main import CaeserCipher

# Create your views here.

@csrf_exempt
def encrypt(request, alphabet_type):
    # POST Method
    if request.method == 'POST':
        
        key = request.headers.get('key', None)
        text = request.POST.get('text', None)

        cipher = CaeserCipher(key=int(key), alphabet_type=alphabet_type)

        response = {
            "cipher_text": cipher.encrypt(text),
        }

        return JsonResponse(response, status=200)

    else:
        return HttpResponse(status=404)