from django.shortcuts import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    # return HttpResponse("Hello, world.")
    # return render(request, 'index.html')
    return render(request, 'postcard.html')
