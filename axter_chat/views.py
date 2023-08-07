from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('Axter',read_only=False,logic_adapters=['chatterbot.logic.MathematicalEvaluation','chatterbot.logic.BestMatch'])


list_to_train = [
    "Hi",
    "Hello",
    "How are you?",
    "I am good.",
    "That is good to hear.",
    "Thank you",
    "What is your name?",
    "My name is Axter.",
    "Who are you?",
    "I am Axter.",
    "Who created you?",
    "I was created by a dev who goes by ashwiniso",
    "What is your purpose?",
    "To help you with your doubts",
]


def index(request):
    return render(request, "axter_chat/index.html")

def specific(request):
    return HttpResponse("Hello, world. You're at the axter_chat specific.")

def getResponse(request):
    userMessage = request.GET.get('userMessage') #get the user message and integrate with HTML
    return HttpResponse(userMessage)