from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('Axter',read_only=False,logic_adapters=[{'import_path':'chatterbot.logic.BestMatch','deafult_response':'I am sorry, but I do not understand. I am still learning.','maximum_similarity_threshold':0.90}])


list_to_train = [
    "Hi",
    "Hello",
    "Hi! How are you?",
    "I am good.",
    "That is good to hear.",
    "Thank you",
    "What is your name?",
    "My name is Axter.",
    "Who are you?",
    "I am Axter.",
    "Who created you?",
    "I was created by a dev who goes by vloneashwin",
    "Who made you?",
    "I was created by a dev who goes by vloneashwin",
    "What is your purpose?",
    "To help you with your doubts",
]

ListTrainer(bot).train(list_to_train)

def index(request):
    return render(request, "axter_chat/index.html")

def specific(request):
    return HttpResponse("Hello, world. You're at the axter_chat specific.")

def getResponse(request):
    userMessage = request.GET.get('userMessage') #get the user message and integrate with HTML
    chat_response = str(bot.get_response(userMessage))
    return HttpResponse(chat_response)