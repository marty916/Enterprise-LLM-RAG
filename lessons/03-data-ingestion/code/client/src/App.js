// src/App.js
import React from 'react';
import Chatbot from './components/Chatbot';
import CustomerSupportChatbot from './components/CustomerSupportChatbot';
import ChatWithData from './components/ChatWithData'

const App = () => {
  return (
    <div>
      <h1>Enterprise LLM Chatbots</h1>
      <h2>Wikipedia Chat</h2>
      <ChatWithData />
      <h2>General Chatbot</h2>
      <Chatbot />
      <h2>Customer Support Chatbot</h2>
      <CustomerSupportChatbot />
    </div>
  );
};

export default App;
