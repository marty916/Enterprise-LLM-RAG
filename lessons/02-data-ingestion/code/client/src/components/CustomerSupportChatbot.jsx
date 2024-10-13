import React, { useState } from 'react';
import { sendCustomerSupportMessage } from '../services/api';

const CustomerSupportChatbot = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');

  const handleSend = async () => {
    const response = await sendCustomerSupportMessage(input);
    setMessages([
      ...messages,
      { role: 'user', content: input },
      { role: 'customer_support', content: response },
    ]);
    setInput('');
  };

  return (
    <div className="chat-window">
      <div className="chat-log">
        {messages.map((msg, idx) => (
          <div key={idx} className={msg.role}>
            <strong>{msg.role.replace('_', ' ').toUpperCase()}: </strong> {msg.content}
          </div>
        ))}
      </div>
      <input
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Ask customer support..."
      />
      <button onClick={handleSend}>Send</button>
    </div>
  );
};

export default CustomerSupportChatbot;
