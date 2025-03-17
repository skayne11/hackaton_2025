# chatbot/views.py
import logging
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .chatbot_model import ChatBot

logger = logging.getLogger(__name__)

def home(request):
    return render(request, 'home.html')

def chat_page_ecrit(request):
    return render(request, 'chat_ecrit.html')

def chat_page_vocal(request):
    return render(request, 'chat_vocal.html')

def chat_page_file(request):
    return render(request, 'file_to_CR.html')


