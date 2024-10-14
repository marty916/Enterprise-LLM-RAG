// src/App.js
import React from 'react';
import ChatWithData from './components/ChatWithData'
import Chatbot from './components/Chatbot'

const App = () => {
  return (
    <div>
      <h1>Enterprise LLM Chatbots</h1>
      <h2>ACME BANK Rewards Program Chat</h2>
      <Chatbot />
      <ChatWithData />
    </div>
  );
};

export default App;
