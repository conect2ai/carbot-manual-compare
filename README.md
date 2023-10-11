# Comparing Three AI-Powered Solutions for Car Manual Queries 🤖🚗

Welcome to the **Comparing Three AI-Powered Solutions for Car Manual Queries** project! This repository contains the codes and resources that have been used and adapted for the analysis and comparison of three leading AI-based solutions for answering technical questions related to car manuals in PDF format. Our goal is to help you make an informed decision about the best solution for your specific needs.

## 🤖 Solutions Overview

We've evaluated the following three AI-powered solutions:

1. **Doc Chatbot with LlamaIndex**: A chatbot that uses LlamaIndex and LangChain libraries to connect large language models (LLMs) to external data sources like PDF car manuals, enabling the creation of chatbots that can learn from diverse data sources and deliver good answers. The code for this solution can be found in the [doc-chatbot-with-llamaindex](./doc-chatbot-with-llamaindex) folder.

2. **Ask your PDF**: A graphical interface that combines Streamlit and Langchain to allow users to upload a PDF file and ask questions about its content. The application extracts text from the PDF, creates embeddings using the OpenAIEmbeddings library, and stores them in a FAISS database for similarity search. The code for this solution can be found in the [ask-your-pdf](./ask-your-pdf) folder.

3. **Question and answer system**: A system that combines LangChain and Large Language Models, such as OpenAI’s GPT-3, and uses React/Typescript for the frontend and Python FastAPI for the backend. QDrant is used to store embeddings and text documents for fast search. The code for this solution can be found in the [QA-system](./QA-system) folder.

For detailed documentation and resources for each solution, please refer to the `README.md` files inside each solution's folder. You will also find the 'How to Run' instructions within each solution's `README.md` file.

## 📊 Analysis and Comparison

Our analysis and comparison of the three solutions focused on the following criteria:

1. Response Accuracy
2. Cost
3. User Experience

| Criteria        | Doc Chatbot with LlamaIndex | Ask your PDF | Question and answer system
| :---------:     |:---------------------------:|:------------:|:-------------------------:|
| Response Accuracy | Medium                        | High         | Low
| Cost            | $$$                         | $$           | $
| User Experience | Bad                        | Good         | Good


## ✉️ Contact Information

If you have any questions or feedback, please feel free to reach out to the authors of this analysis:

- [Mariana Azevedo](mailto:mariana.brito.110@ufrn.edu.br)
- [Morsinaldo Medeiros](mailto:morsinaldo.medeiros.075@ufrn.edu.br)
- [Thaís Medeiros](mailto:thais.araujo.707@ufrn.edu.br)

The following are the links to the sources where the codes were taken from:

- [Doc Chatbot with LlamaIndex](https://levelup.gitconnected.com/how-to-create-a-doc-chatbot-that-learns-everything-for-you-in-15-minutes-364fef481307)
- [Ask your PDF](https://github.com/alejandro-ao/langchain-ask-pdf)
- [Question and answer system](https://github.com/mallahyari/drqa)