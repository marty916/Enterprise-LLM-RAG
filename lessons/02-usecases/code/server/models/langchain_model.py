# server/models/langchain_model.py
# Import all necessary components from index.py
from models.index import ChatOpenAI, ChatPromptTemplate, StrOutputParser

def setup_chatbot():
    # Setup OpenAI API (You need to have OPENAI_API_KEY in the environment)
    """
    Setup a chatbot using the OpenAI API.

    The chatbot is created using a simple system prompt and the OpenAI
    `ChatOpenAI` model.

    The chatbot is then returned as a LangChain `chain` object

    :return: A LangChain `chain` object that acts as a chatbot
    """
    model = ChatOpenAI(temperature=0.7)
    
    # Create a conversation chain with a simple system prompt
    system_template = """
    You are a helpful assistant. Answer the following question.
    
    Question:
    """
    ## prompt_template = ChatPromptTemplate(input_variables=["message"], template=template)
    prompt_template = ChatPromptTemplate.from_messages(
        [("system", system_template), ("user", "{message}") ]
        )

    # JSON response gets returned so we want to turn it into a string
    chatbot = prompt_template | model | StrOutputParser()
    
    return chatbot


def setup_customer_support_chatbot():
    """
    Setup a customer support chatbot using the OpenAI API.
    """
    model = ChatOpenAI(temperature=0.5)

    system_prompt = """
    You are a customer support assistant. Help customers with their inquiries about our products and services.
    """

    user_prompt = "{message}"

    prompt_template = ChatPromptTemplate.from_messages(
        [("system", system_prompt), ("user", user_prompt)]
    )

    chatbot = prompt_template | model | StrOutputParser()

    return chatbot

