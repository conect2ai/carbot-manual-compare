from dotenv import load_dotenv
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback

def main():
    load_dotenv() # Load environment variables from .env file
    st.set_page_config(page_title='Ask your PDF') # Set Streamlit page title
    st.header('Ask your PDF') # Set Streamlit header

    # Upload PDF files
    pdfs = st.file_uploader('Upload your PDF files', type=['pdf'])

    # Extract text from the uploaded PDF
    if pdfs:
        pdf_reader = PdfReader(pdfs)
        text = ''
        for page in pdf_reader.pages:
            text += page.extract_text()
        
        # Split the text into chunks
        text_splitter = CharacterTextSplitter(
            separator = '\n',
            chunk_size = 1000, 
            chunk_overlap = 20,
            length_function = len
        )

        chunks = text_splitter.split_text(text)

        # Create embeddings
        embeddings = OpenAIEmbeddings()
        knowledge_base = FAISS.from_texts(chunks, embeddings)

        # Show user input
        user_question = st.text_input('Ask a question about your PDF:', key='text_input')

        if user_question:
            docs = knowledge_base.similarity_search(user_question)

            llm = OpenAI()
            chain = load_qa_chain(llm, chain_type="stuff")
            with get_openai_callback() as cb:
                response = chain.run(input_documents=docs, question=user_question)
                print(cb)
            
            st.write(response) # Display the response from the chatbot

if __name__ == '__main__':
    main()
