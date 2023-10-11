# Doc Chatbot with LlamaIndex
The Doc Chatbot with LlamaIndex is a chatbot that answers questions about a PDF document. It uses the [LlamaIndex](https://gpt-index.readthedocs.io/en/latest/) and [LangChain](https://langchain.readthedocs.io/en/latest/) libraries to connect large language models (LLMs) to external data sources like PDF car manuals, enabling the creation of chatbots that can learn from diverse data sources and deliver good answers.

## 📚 Documentation and Resources
  - [LlamaIndex Documentation](https://gpt-index.readthedocs.io/en/latest/)
  - [LangChain Documentation](https://langchain.readthedocs.io/en/latest/)
  - [Application Source Article](https://levelup.gitconnected.com/how-to-create-a-doc-chatbot-that-learns-everything-for-you-in-15-minutes-364fef481307)

## 💻 How to Run
Follow the instructions below to run the Doc Chatbot with LlamaIndex application on your machine:

1. Clone the repository to your local machine:
```
git clone https://github.com/conect2ai/carbot-manual-compare.git
```

2. Navigate to the cloned repository:
```
cd carbot-manual-compare
```

3. Enter the `doc-chatbot-with-llamaindex` folder:
```
cd doc-chatbot-with-llamaindex
```

4. Create an account at [OpenAI API](https://openai.com/blog/openai-api). You will need OpenAI credits to run the application, and in general, new users get $5 credits to test the API. This is enough to run the application;

5. Create an API key in the OpenAI API. To do this, click on the `View API keys` option and create a new API key. Copy the value from the key that was created;

6. In the same directory where the `index.py` file is located on your machine, create the `.env` file and paste the following code snippet, replacing `your-api-key` with the key you generated in step 5:

```
OPENAI_API_KEY='your-api-key'
```

7. In the same directory, create a folder called `data` and put the PDF car manual file, such as `Ford_Fiesta_2015.pdf`;

8. Run the `index.py` script, replacing the variable `query_str` with the question you wish to ask the chatbot.

```
from langchain.callbacks import get_openai_callback

query_engine = index.as_query_engine()

with get_openai_callback() as cb:
    query_str = "How does the air recycle button work?"
    response = query_engine.query(query_str)
    print(cb)
```
This will provide the chatbot's response to your question based on the information available in the car manual PDF file.