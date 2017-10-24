from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def index(request):
    if request.method == 'POST':
        print(request.body)
        data = json.loads(request.body)
        return JsonResponse(data)
