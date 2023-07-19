from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the axter_chat index.")

def specific(request):
    return HttpResponse("Hello, world. You're at the axter_chat specific.")

def article(request, article_id):
    return render(request, "axter_chat/index.html", {"article_id": article_id})
