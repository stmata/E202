import streamlit as st
import os
from config import opai_key
os.environ["OPENAI_API_KEY"] = opai_key()
from os.path import exists
# Indexing the Documents

from llama_index import SimpleDirectoryReader, GPTVectorStoreIndex, LLMPredictor, PromptHelper,  llm_predictor
# And since we are using OpenAI, import the ChatOpenAI class as well:
from langchain.chat_models import ChatOpenAI

def index_documents(folder):
    max_input_size = 4096
    num_outputs = 4000
    max_chunk_overlap = 20
    chunk_size_limit = 600
    
    prompt_helper = PromptHelper(max_input_size,
                                 num_outputs,
                                 max_chunk_overlap,
                                 chunk_size_limit)
    llm_predictor = LLMPredictor(
        llm= ChatOpenAI(temperature=0.7,
                        model_name = "gpt-3.5-turbo",
                        max_tokens=num_outputs)
    )
    documents = SimpleDirectoryReader(folder).load_data()
    
    index = GPTVectorStoreIndex.from_documents(documents,
                                               llm_predictor= llm_predictor,
                                               prompt_helper=prompt_helper)
    index.storage_context.persist(persist_dir=".") # save in current directory

# To start the indexing process, call the index_documents with the name of the folder containing your documents: 
doc_path = './Docs/'
Index_store_path = './vector_store.json'

file_exists = exists(Index_store_path)
if file_exists:
    pass
else:    
    index_documents(doc_path)
# Asking Questions
# You are now ready to pose questions to ChatGPT. 

# Define a function named my_chatGPT_bot():
from llama_index import StorageContext, load_index_from_storage

def my_chatGPT_bot(input_text):
    # Load the index from vector_store.json
    storage_context = StorageContext.from_defaults(persist_dir=".")
    index = load_index_from_storage(storage_context)    
    # create a query engine to ask question
    query_engine = index.as_query_engine()
    response = query_engine.query(input_text)
    return response.response
