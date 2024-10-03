from models.langchain_model import setup_customer_support_chatbot

def get_customer_support_response(message: str) -> str:
    chatbot = setup_customer_support_chatbot()
    response = chatbot.invoke({"message": message})
    return response
