# chatbot/views.py
import logging
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from chatbot.chatbot_model import ChatBot

logger = logging.getLogger(__name__)
api_key = "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"  # Remplacez par votre clé API

chatbot = ChatBot(api_key)

def home(request):
    return render(request, 'home.html')

def chat_page_ecrit(request):
    return render(request, 'chat_ecrit.html')

def chat_page_vocal(request):
    return render(request, 'chat_vocal.html')

@csrf_exempt
def chat_response(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            conversation_history = data.get('messages', [])

            if not conversation_history:
                return JsonResponse({'error': "L'historique des messages est requis"}, status=400)

            # Appeler le modèle avec l'historique des messages
            response_text = chatbot.generate_response(conversation_history)

            return JsonResponse({'content': response_text})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Requête JSON invalide'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Méthode de requête invalide'}, status=400)

