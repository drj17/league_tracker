from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
import zlib



# Create your views here.
@csrf_exempt
def index(request):
    if request.method == 'POST':
        print(request.body)
        print(type(request.body))
        decompressed_data=zlib.decompress(request.body, 16+zlib.MAX_WBITS)
        print(decompressed_data)
        ustr_to_load = request.body.decode("ISO-8859-1")
        print(ustr_to_load)
        data = json.loads(ustr_to_load)
        return JsonResponse(data)
