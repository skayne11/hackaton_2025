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

let recognition;
let recognizing = false;

// Vérification de la disponibilité de la reconnaissance vocale
if (!('SpeechRecognition' in window || 'webkitSpeechRecognition' in window)) {
    alert("La reconnaissance vocale n'est pas supportée par votre navigateur.");
}

function startListening() {
    if (recognizing) {
        recognition.stop();
        return;
    }

    recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = 'fr-FR';
    recognition.continuous = false;

    recognition.onstart = function () {
        recognizing = true;
        document.getElementById('mic-button').innerText = 'Arrêter';
    };

    recognition.onend = function () {
        recognizing = false;
        document.getElementById('mic-button').innerText = '🎤 Parler';
    };

    recognition.onresult = function (event) {
        const transcript = event.results[0][0].transcript;
        document.getElementById('voice-input').value = transcript;
        sendVoiceMessage(transcript);
    };

    recognition.start();
}

async function sendVoiceMessage(transcript) {
    const messagesElement = document.getElementById('voice-chatbox');
    const userMessageElement = document.createElement('div');
    userMessageElement.className = 'alert alert-primary mt-2';
    userMessageElement.innerText = transcript;
    messagesElement.appendChild(userMessageElement);

    conversationHistory.push({ role: "user", content: transcript });

    try {
        const response = await fetch('/entretiens/chat/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ messages: conversationHistory })
        });

        if (response.ok) {
            const data = await response.json();
            const botMessageElement = document.createElement('div');
            botMessageElement.className = 'alert alert-secondary mt-2';
            botMessageElement.innerText = data.content;
            messagesElement.appendChild(botMessageElement);

            const utterance = new SpeechSynthesisUtterance(data.content);
            speechSynthesis.speak(utterance);

            conversationHistory.push({ role: "assistant", content: data.content });
        } else {
            console.error("Échec de la requête au chatbot.");
        }
    } catch (error) {
        console.error("Erreur :", error);
    }
    messagesElement.scrollTop = messagesElement.scrollHeight;
}
