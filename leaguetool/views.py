from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def index(request):
    if request.method == 'POST':
        data = json.loads(request.body, "ISO-8859-1")
        return JsonResponse(data)
