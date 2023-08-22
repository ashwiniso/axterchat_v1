from telnetlib import LOGOUT
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,logout
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import openai

# Create your views here.

openai.api_key = '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'

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
    "My name is Axter.",
    "I am Axter.",
    "Who created you?",
    "I was created by a dev who goes by vloneashwin",
    "Who made you?",
    "I was created by a dev who goes by vloneashwin",
    "What is your purpose?",
    "To help you with your doubts",
    "I'll keep that in mind.",
    "I am glad to hear that.",
    "I am sorry to hear that.",
    "I am sorry, but I do not understand. I am still learning.",
    "I am sorry, but I do not understand.",
    "Thats okay.",
    "I am an AI chatbot.",
    "I am an AI chatbot. I am still learning.",
    "This is a great conversation. I am enjoying this.",
    "This is a great conversation. I am enjoying this. I hope you are too.",
]

ListTrainer(bot).train(list_to_train)

chatterbotCorpusTrainer = ChatterBotCorpusTrainer(bot)
chatterbotCorpusTrainer.train("chatterbot.corpus.english")


def index(request):
    return render(request, "axter_chat/index.html")

import openai

def get_openai_response(prompt_text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt_text}
        ]
    )
    # Extract the assistant's response from the returned messages
    return response.choices[0].message['content']

def getResponse(request):
    userMessage = request.GET.get('userMessage')

    # If user input starts with "act:", we use GPT for the response
    if userMessage.startswith("act:"):
        userMessage = userMessage.replace("act:", "").strip()
        chat_response = get_openai_response(userMessage)
    else:
        chat_response = str(bot.get_response(userMessage))
    
    return HttpResponse(chat_response)



def about(request):
    return render(request, "axter_chat/about.html")

@login_required(login_url='/login/')
def axter(request):
    return render(request, "axter_chat/axter.html")

def contact(request):
    return render(request, "axter_chat/contact.html")

@login_required(login_url='/login/')
def about2(request):
    return render(request, "axter_chat/about2.html")

@login_required(login_url='/login/')
def contact2(request):
    return render(request, "axter_chat/contact2.html")

@login_required(login_url='/login/')
def index2(request):
    return render(request, "axter_chat/index2.html")

def register_view(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1 != pass2:
            messages.error(request, "Passwords do not match")
        elif User.objects.filter(username=uname).exists():
            messages.error(request, "Username already exists")
        else:
            my_user = User.objects.create_user(uname, None, pass1)
            my_user.save()
            return redirect('axter_chat:axter')
    return render(request, "axter_chat/index.html")
        
def login_view(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=uname, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('axter_chat:axter')
        else:
            messages.error(request, "Invalid Credentials")
    return render(request, "axter_chat/axter.html")

def logout_view(request):
    logout(request)
    return redirect('axter_chat:index')

    
        
