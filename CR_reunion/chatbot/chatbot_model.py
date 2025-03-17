from openai import OpenAI

class ChatBot:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

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

