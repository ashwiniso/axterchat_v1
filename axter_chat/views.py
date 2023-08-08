from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
# Create your views here.

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

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

#ListTrainer(bot).train(list_to_train)

chatterbotCorpusTrainer = ChatterBotCorpusTrainer(bot)
chatterbotCorpusTrainer.train("chatterbot.corpus.english")

def index(request):
    return render(request, "axter_chat/index.html")

def getResponse(request):
    userMessage = request.GET.get('userMessage') #get the user message and integrate with HTML
    chat_response = str(bot.get_response(userMessage))
    return HttpResponse(chat_response)

def about(request):
    return render(request, "axter_chat/about.html")

def axter(request):
    return render(request, "axter_chat/axter.html")

def contact(request):
    return render(request, "axter_chat/contact.html")

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('axter_chat:index')  # Redirect to chatbot page after login
    else:
        form = AuthenticationForm()
    return render(request, 'axter_chat/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # You can log in the user here if desired
            return redirect('axter_chat:index')  # Redirect to chatbot page after registration
    else:
        form = UserCreationForm()
    return render(request, 'axter_chat/register.html', {'form': form})