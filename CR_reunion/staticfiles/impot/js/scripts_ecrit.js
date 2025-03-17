let conversationHistory = [
    {
        role: "system",
        content: `Tu es une IA qui va aider la persnne pour ses impôts. 
                Tu devras guider la personne pas à pas et clairement afin de l'aidé au mieux. 
                Tu devras répondre que sur le domaine ce-dessus et sur aucun autre sujet qui ne touche pas au domaine.
                La discussion se fait en français.`
    }
];

const csrftoken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

    async function sendMessage() {
        const inputElement = document.getElementById('user-input');
        const userMessage = inputElement.value.trim();
        if (!userMessage) return;
    
        const messagesElement = document.getElementById('chatbox');
        const userMessageElement = document.createElement('div');
        userMessageElement.className = 'alert alert-primary mt-2';
        userMessageElement.innerText = userMessage;
        messagesElement.appendChild(userMessageElement);

        conversationHistory.push({ role: "user", content: userMessage });
    
        inputElement.value = '';
    
        try {
            const response = await fetch('/entretiens/chat/', {
                method: 'POST',
                headers: { 
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken 
                },
                body: JSON.stringify({ messages: conversationHistory })
            });
    
            if (response.ok) {
                const data = await response.json();
                const botMessageElement = document.createElement('div');
                botMessageElement.className = 'alert alert-secondary mt-2';
                botMessageElement.innerText = data.content;
                messagesElement.appendChild(botMessageElement);
                conversationHistory.push({ role: "assistant", content: data.content });
            } else {
                console.error("Erreur lors de la requête.");
            }
        } catch (error) {
            console.error("Erreur :", error);
        }
    
        messagesElement.scrollTop = messagesElement.scrollHeight;
    }