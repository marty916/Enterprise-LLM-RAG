'''
/server/models/index.py 
Centralized third-party imports for the server models module.

Imports:
- ChatOpenAI from langchain_openai
- ChatPromptTemplate from langchain_core.prompts
- StrOutputParser from langchain_core.output_parsers

Exports:
- ChatOpenAI
- ChatPromptTemplate
- StrOutputParser
'''

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Export them as part of the module's namespace
__all__ = ["ChatOpenAI", "ChatPromptTemplate", "StrOutputParser"]
