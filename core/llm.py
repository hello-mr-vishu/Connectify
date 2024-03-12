import os

from .token import secret_key

from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
os.environ["OpenAI_API_kEY"]=secret_key
llm=OpenAI(temperature=0.7)

def retrieve_data(pdf,query):
    pdf_reader=PdfReader(pdf)
    text=""
    for page in pdf_reader.pages:
        text+=page.extract_text()
    text_splitters=RecursiveCharacterTextSplitter(
        separators=['\n\n','\n'],
        chunk_size=200,
        chunk_overlap=0
    )
    chunks=text_splitters.split_text(text)
    vector_store=FAISS.from_texts(chunks,OpenAIEmbeddings())
    docs=vector_store.similarity_search(query)
    chain=load_qa_chain(llm,chain_type="stuff")
    response=chain.run(input_documents=docs,question=query)
    return response

