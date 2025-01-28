from unstructured.partition.pdf import partition_pdf
from llama_index import SimpleDirectoryReader
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
import os

def extract_text_from_pdf(file_path):
    elements = partition_pdf(filename=file_path)
    return "\n".join([str(e) for e in elements])


# Load documents from a directory (previously extracted documents)
def load_documents(directory):
    reader = SimpleDirectoryReader(directory)
    docs = reader.load_data()
    return docs

# Create a vector index using LlamaIndex
def create_index(docs):
    index = GPTVectorStoreIndex.from_documents(docs)
    return index

# Query using the RAG model
def query_rag_agent(query_text, index):
    retriever = index.as_retriever()
    qa_chain = RetrievalQA.from_chain_type(
        llm=ChatOpenAI(temperature=0.2, model_name="gpt-4"),
        chain_type="stuff",
        retriever=retriever
    )
    response = qa_chain.run(query_text)
    return response

if __name__ == "__main__":
    # Load documents from stored directory
    docs = load_documents("./documents")
    
    # Create index
    index = create_index(docs)
    
    # Test Query
    query = "What is the main topic of the document?"
    response = query_rag_agent(query, index)
    print("Response:", response)

