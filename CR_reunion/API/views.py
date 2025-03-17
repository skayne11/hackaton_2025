# chatbot/views.py
import logging
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from chatbot.chatbot_model import ChatBot
from django.conf import settings


logger = logging.getLogger(__name__)

chatbot = ChatBot(settings.OPENAI_API_KEY)

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

@csrf_exempt
def upload_txt_file(request):
    if request.method == 'POST':
        try:
            if 'file' not in request.FILES:
                return JsonResponse({'error': 'Aucun fichier envoyé'}, status=400)
            
            file = request.FILES['file']
            if not file.name.endswith('.txt'):
                return JsonResponse({'error': 'Format de fichier non supporté. Veuillez envoyer un fichier .txt'}, status=400)
            
            # Lire le contenu du fichier
            file_content = file.read().decode('utf-8')
            
            # Générer le compte rendu avec le chatbot
            summary = chatbot.generate_summary(file_content)

            return JsonResponse({'summary': summary})
        except Exception as e:
            logger.error(f"Erreur lors du résumé du fichier : {e}")
            return JsonResponse({'error': f'Erreur serveur : {str(e)}'}, status=500)
    
    return JsonResponse({'error': 'Méthode de requête invalide'}, status=400)
