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
