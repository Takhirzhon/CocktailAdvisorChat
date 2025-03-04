async function sendMessage() {
    const question = document.getElementById('question').value;
    const chatWindow = document.getElementById('chat-window');

    chatWindow.innerHTML += `<div><strong>You:</strong> ${question}</div>`;

    const response = await fetch('/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question })
    });

    const data = await response.json();
    chatWindow.innerHTML += `<div><strong>Bot:</strong> ${data.response}</div>`;

    document.getElementById('question').value = '';
    chatWindow.scrollTop = chatWindow.scrollHeight;
}