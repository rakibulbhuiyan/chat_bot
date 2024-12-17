from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


bot = ChatBot('chatbot', read_only=False, logic_adapters=['chatterbot.logic.bestMatch'])

list_to_train=[
    "Hii",
    "Hii, there",
    "what's your name?",
    "i'm just chatbot"
    "what's your favourite food?",
    "i like cheese"
]

list_trainer = ListTrainer(bot) 

list_trainer.train(list_to_train)

def index(request):
    return render(request, 'index.html')

def specific(request):
    return HttpResponse('this is a chat app')


def getResponse(request):
    userMessage=request.GET.get('userMessage')
    return HttpResponse(userMessage)




