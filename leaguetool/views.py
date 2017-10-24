from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def index(request):
    if request.method == 'POST':
        print(type(request.body))
        ustr_to_load = str(request.body, "ISO-8859-1")
        print(ustr_to_load)
        data = json.loads(ustr_to_load)
        return JsonResponse(data)
