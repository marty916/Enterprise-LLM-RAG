import React, { useState } from 'react';
import { sendMessage } from '../services/api';

const Chatbot = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');

  const handleSend = async () => {
    const response = await sendMessage(input);
    setMessages([...messages, { role: 'user', content: input }, { role: 'codedaddy', content: response }]);
    setInput('');
  };

  return (
    <div className="chat-window">
      <div className="chat-log">
        {messages.map((msg, idx) => (
          <div key={idx} className={msg.role}>
            <strong>{msg.role}: </strong> {msg.content}
          </div>
        ))}
      </div>
      <input
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Ask something..."
      />
      <button onClick={handleSend}>Send</button>
    </div>
  );
};

export default Chatbot;
