from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
import zlib



# Create your views here.
@csrf_exempt
def index(request):
    if request.method == 'POST':
        decompressed_data=zlib.decompress(request.body, 16+zlib.MAX_WBITS)
        data = json.loads(decompressed_data)
        return JsonResponse(data)
