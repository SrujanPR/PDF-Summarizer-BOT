# PDF Summarizer BOT 📄✨

Your interactive PDF assistant powered by cutting-edge Gemini's Generative AI language model! This Bot enables you to interact with your PDFs in a whole new way, extracting information, summarizing content, and much more.

## Getting Started 🚀

### Step 1: Obtain Your API Key 🔑

To interact with the Gemini model, you will need an API key. Follow these steps to obtain one:

1. Visit the [Gemini Website](https://aistudio.google.com/).
2. Sign up for an account if you don't already have one.
3. Navigate to the API section and follow the instructions to generate your API key.

### Step 2: Set Your API Key 🛠️

Once you have your API key, you'll need to configure this in a .env file with the variable ["GOOGLE_API_KEY"] and then import it in the `app.py` file. In the `app.py` file, find the line that looks like this:

```python
api_key=os.getenv("GOOGLE_API_KEY")
```

Place your actual API key in the .env file and save it.

### Step 3: Install Dependencies 📦

The Project requires several dependencies to run. Install them using the provided `requirements.txt` file with the following command:

```bash
pip install -r requirements.txt
```

### Step 4: Launch the Application 🌟

With your API key set and dependencies installed, you're ready to start the application. Navigate to the root folder of the directory and run:

```bash
streamlit run app.py
```

The application should now be up and running on your local server. Open your web browser and go to the address indicated by Streamlit (usually `http://localhost:8501`) to start using PDF Summarizer BOT.

## Features:

ChatPDF comes with a plethora of features designed to make your interaction with PDF documents as smooth as possible:

- **Information Extraction**: Pull out key details or data from your PDF files.
- **Content Summarization**: Get concise summaries of lengthy documents.
- **Q&A with your PDF**: Ask questions and get answers based on the content of your PDFs.

## Technologies Used:

- **LangChain**: LangChain is a framework for developing applications powered by large language models (LLMs).
- **PyPDF2**: PyPDF2 is a free and open source pure-python PDF library capable of splitting, merging, cropping, and transforming the pages of PDF files.
- **FAISS**: FAISS (Facebook AI Similarity Search) is a library that allows developers to quickly search for embeddings of multimedia documents that are similar to each other.
- **Google Gemini GenAI Model**: The Gemini model is a groundbreaking multimodal language model developed by Google AI, capable of extracting meaningful insights from a diverse array of data formats, including images, and video. 
- **Streamlit**: Streamlit is a promising open-source Python library, which enables developers to build attractive user interfaces in no time

