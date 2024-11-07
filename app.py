import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from html_template import *

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    return text_splitter.split_text(text)

def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")

def get_conversational_chain():
    # Adjust prompt for detailed, paragraph-style answers
    prompt_template = """
    Answer the question as thoroughly as possible using detailed paragraphs. Each paragraph should cover a distinct aspect of the answer. 
    If the answer is not available in the provided context, respond with: "The answer is not available in the context."

    Context:
    {context}

    Question:
    {question}

    Detailed Answer:
    """
    
    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3, max_tokens=750)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
    
    return chain

def user_input(user_question, text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    
    # Perform similarity search
    docs = vector_store.similarity_search(user_question)
    chain = get_conversational_chain()

    response = chain(
        {"input_documents": docs, "question": user_question},
        return_only_outputs=True
    )

    # Format the response to ensure paragraph readability in Streamlit
    st.markdown("### Summarized Answer:")
    st.markdown(f"{response['output_text']}")

def main():
    st.set_page_config("Chat PDF")
    st.write(css, unsafe_allow_html=True)
    st.header("PDF Summarizer Bot")

    user_question = st.text_input("Ask a Question from the PDF Files")
    
    if user_question and st.session_state.get("text_chunks"):
        user_input(user_question, st.session_state["text_chunks"])

    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your PDF Files and Click on Submit & Process Button", accept_multiple_files=True)

        if st.button("Submit & Process"):
            if pdf_docs:  # Check if files are uploaded
                with st.spinner("Processing..."):
                    # Process the PDFs only if files were uploaded
                    raw_text = get_pdf_text(pdf_docs)
                    text_chunks = get_text_chunks(raw_text)
                    st.session_state["text_chunks"] = text_chunks
                    st.success("Done")
            else:
                st.error("Please upload at least one PDF file.")

if __name__ == "__main__":
    main()
