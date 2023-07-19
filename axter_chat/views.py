from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "axter_chat/index.html")

def specific(request):
    return HttpResponse("Hello, world. You're at the axter_chat specific.")