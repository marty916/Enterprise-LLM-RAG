// src/services/api.js
import axios from 'axios';

export const sendMessage = async (message) => {
  try {
    const response = await axios.post('http://localhost:8000/chat', { message });
    return response.data.reply;
  } catch (error) {
    console.error('Error:', error);
    return 'Error occurred while chatting.';
  }
};

export const sendCustomerSupportMessage = async (message) => {
  try {
    const response = await axios.post('http://localhost:8000/customer-support', { message });
    return response.data.reply;
  } catch (error) {
    console.error('Error:', error);
    return 'Error occurred while chatting.';
  }
};

// src/services/api.js
export const sendChatWithDataMessage = async () => {
  try {
      const response = await fetch('http://localhost:8000/chat-with-data', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
          },
      });
      if (!response.ok) {
          throw new Error('Network response was not ok');
      }
      const data = await response.json();
      return data;
  } catch (error) {
      console.error('Error:', error);
      return { embeddings: [], metadata: [] };
  }
};
