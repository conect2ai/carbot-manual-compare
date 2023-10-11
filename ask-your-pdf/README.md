# Ask your PDF
The Ask your PDF application is a graphical interface that combines Streamlit and Langchain to allow users to upload a PDF file and ask questions about its content. The application extracts text from the PDF, creates embeddings using the OpenAIEmbeddings library, and stores them in a FAISS database for similarity search.

## 📚 Documentation and Resources
  - [Streamlit Documentation](https://docs.streamlit.io/en/stable/)
  - [LangChain Documentation](https://langchain.readthedocs.io/en/latest/)
  - [Application Source Repository](https://github.com/alejandro-ao/langchain-ask-pdf)

## 💻 How to Run
1. Clone the repository to your local machine:
```
https://github.com/conect2ai/carbot-manual-compare.git
```

2. Navigate to the cloned repository:
```
cd carbot-manual-compare
```

3. Enter the `ask-your-pdf` folder:
```
cd ask-your-pdf
```

4. Install the required packages and dependencies using pip:
```
pip install -r requirements.txt
```

5. Create a file named ".env" in the root directory of the `ask-your-pdf` folder and add the following environment variable:
```
OPENAI_API_KEY=<your_openai_api_key>
```
Replace `<your_openai_api_key>` with your actual OpenAI API key. If you don't have an API key, you can sign up for one  [here](https://beta.openai.com/signup/).

6. Run the code using the following command:
```
streamlit run app.py
```
A new tab will be opened in your default web browser, displaying the "Ask your PDF" app. Upload a PDF (for instance, the Ford Ka owner's manual, which can be found in the root directory of the repository) by clicking the "Upload your PDF files" button, and enter a question about the uploaded file in the text box below it. Then click the "Submit" button to see the answer to your question.
