import React, { useState } from 'react';
import '../styles/Chatbot.css'; // Import the CSS file

function Chatbot() {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState([
    { sender: 'bot', text: 'Hi! I am Salu, I can assist you in finding the best tutor. Tell me the subject and location?' },
  ]);
  const [input, setInput] = useState('');
  const [isTyping, setIsTyping] = useState(false); // Typing indicator for bot
  const [userTyping, setUserTyping] = useState(false); // Typing indicator for user
  const [listening, setListening] = useState(false); // Audio listening state

  const toggleChat = () => {
    setIsOpen(!isOpen);
  };

  // Handle voice input using Web Speech API and auto-submit after recognition
  const handleVoiceInput = () => {
    if (!('webkitSpeechRecognition' in window)) {
      alert('Speech recognition is not supported in this browser.');
      return;
    }

    const recognition = new window.webkitSpeechRecognition();
    recognition.lang = 'en-US';
    recognition.interimResults = false; // If true, it will show partial results as the user speaks.
    recognition.maxAlternatives = 1;

    setListening(true); // Show the user that the bot is listening
    recognition.start();

    recognition.onresult = (event) => {
      const transcript = event.results[0][0].transcript;
      setInput(transcript); // Set the recognized speech as input text
      setListening(false); // Stop listening indication

      // Automatically send the recognized voice input like a regular text input
      handleMessageSendFromVoice(transcript);
    };

    recognition.onerror = (event) => {
      console.error('Voice recognition error:', event);
      setListening(false);
    };

    recognition.onend = () => {
      setListening(false); // Reset listening state when recognition ends
    };
  };

  // Detect when user is typing
  const handleInputChange = (e) => {
    setInput(e.target.value);
    setUserTyping(e.target.value.length > 0);
  };

  // This is used to auto-send the recognized speech input
  const handleMessageSendFromVoice = async (voiceInput) => {
    if (voiceInput.trim()) {
      // Add user message to the chat
      const newMessages = [...messages, { sender: 'user', text: voiceInput }];
      setMessages(newMessages);
      setIsTyping(true); // Show typing indicator for bot
      setUserTyping(false); // Hide user typing indicator

      // Send the recognized speech (converted text) to RASA
      setTimeout(async () => {
        const rasaResponse = await sendMessageToRasa(voiceInput);

        // Add bot response to the chat
        setMessages((prevMessages) => [
          ...prevMessages,
          { sender: 'bot', text: rasaResponse },
        ]);
        setIsTyping(false); // Hide typing indicator once bot responds
      }, 1000); // Simulate typing delay
    }
  };

  const handleMessageSend = async (e) => {
    e.preventDefault();
    if (input.trim()) {
      // Add user message to the chat
      const newMessages = [...messages, { sender: 'user', text: input }];
      setMessages(newMessages);
      setInput(''); // Clear input field
      setIsTyping(true); // Show typing indicator for bot
      setUserTyping(false); // Hide user typing indicator

      // Simulate bot response delay to show typing indicator
      setTimeout(async () => {
        const rasaResponse = await sendMessageToRasa(input);

        // Add bot response to the chat
        setMessages((prevMessages) => [
          ...prevMessages,
          { sender: 'bot', text: rasaResponse },
        ]);
        setIsTyping(false); // Hide typing indicator once bot responds
      }, 1000); // Simulate typing delay
    }
  };

  // Function to send the message to the RASA REST API
  const sendMessageToRasa = async (message) => {
    try {
      const response = await fetch('http://localhost:5005/webhooks/rest/webhook', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          sender: 'user', // The sender's unique identifier
          message: message, // The message sent by the user
        }),
      });

      const data = await response.json();
      if (data.length && data[0].text) {
        return data[0].text; // Return the bot's response from RASA
      } else {
        return 'Sorry, I didn’t understand that. Could you please clarify?';
      }
    } catch (error) {
      console.error('Error communicating with RASA:', error);
      return 'There was an issue connecting to the server. Please try again later.';
    }
  };

  return (
    <div className="chatbot-container">
      <div className={`chatbot-toggle ${isOpen ? 'open' : ''}`} onClick={toggleChat}>
        {isOpen ? '✖' : '💬'}
      </div>

      {isOpen && (
        <div className="chatbot-window">
          <div className="chatbot-header">
            <h4>Tutor Finder Bot</h4>
          </div>

          <div className="chatbot-body">
            <div className="chatbot-messages">
              {messages.map((message, index) => (
                <div
                  key={index}
                  className={`chatbot-message ${message.sender === 'user' ? 'user-message' : 'bot-message'}`}
                >
                  {message.text}
                </div>
              ))}
            </div>
            {/* Show bot typing indicator */}
            {isTyping && (
              <div className="typing-indicator bot-typing">
                <span className="bot-symbol">🤖</span> is typing...
              </div>
            )}
          </div>

          <div className="chatbot-footer">
            <form onSubmit={handleMessageSend}>
              <input
                type="text"
                value={input}
                onChange={handleInputChange}
                placeholder="Type a message..."
              />
              <button type="submit">Send</button>
              <button type="button" onClick={handleVoiceInput}>
                🎤 {listening ? 'Listening...' : 'Voice Input'}
              </button>
            </form>
            {/* Show user typing indicator */}
            {userTyping && (
              <div className="typing-indicator user-typing">
                You are typing...
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  );
}

export default Chatbot;
