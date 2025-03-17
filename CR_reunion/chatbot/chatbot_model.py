import openai
from django.conf import settings

class ChatBot:
    def __init__(self, api_key):
        self.client = openai.OpenAI(api_key=api_key)

    def generate_response(self, conversation_history):
        """
        conversation_history: Une liste de messages sous la forme :
        [
            {"role": "user", "content": "Bonjour"},
            {"role": "assistant", "content": "Bonjour ! Comment puis-je vous aider ?"},
            ...
        ]
        """
        try:
            completion = self.client.chat.completions.create(
                model="gpt-4",
                messages=conversation_history
            )
            return completion.choices[0].message.content
        except Exception as e:
            return f"Une erreur s'est produite : {str(e)}"
        
    def generate_summary(self, file_content):
        """
        Générer un résumé à partir du texte du fichier
        """
        try:
            conversation_history = [
                {"role": "system", "content": "Tu es un assistant qui génère des comptes rendus détaillés à partir du texte donné."},
                {"role": "user", "content": file_content}
            ]
            completion = self.client.chat.completions.create(
                model="gpt-4",
                messages=conversation_history
            )
            return completion.choices[0].message.content
        except Exception as e:
            return f"Une erreur s'est produite lors du résumé : {str(e)}"
