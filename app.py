## RAG Q&A Conversation With PDF Including Chat History
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_community.document_loaders import PyPDFLoader
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_classic.chains import create_history_aware_retriever, create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
import chromadb
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["STREAMLIT_WATCHER_TYPE"] = "poll"
os.environ['HF_TOKEN'] = os.getenv("HF_TOKEN", "")

api_key = os.getenv("GROQ_API_KEY")

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
client = chromadb.PersistentClient(path="./chroma_db")

st.title("💬 Conversational RAG With PDF & Chat History")
st.write("Upload PDFs and chat with their content using Groq AI")

if not api_key:
    st.error("GROQ_API_KEY not found in .env file. Please add it and restart the app.")
    st.stop()

llm = ChatGroq(groq_api_key=api_key, model_name="llama-3.3-70b-versatile")
session_id = st.text_input("Session ID", value="default_session")

if 'store' not in st.session_state:
    st.session_state.store = {}

uploaded_files = st.file_uploader("Choose PDF file(s)", type="pdf", accept_multiple_files=True)

if uploaded_files:
    documents = []
    for uploaded_file in uploaded_files:
        temppdf = "./temp.pdf"
        with open(temppdf, "wb") as file:
            file.write(uploaded_file.getvalue())
        loader = PyPDFLoader(temppdf)
        docs = loader.load()
        documents.extend(docs)

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=5000, chunk_overlap=500)
    splits = text_splitter.split_documents(documents)

    vectorstore = Chroma.from_documents(
        documents=splits,
        embedding=embeddings,
        client=client,
        collection_name="ragpdfcollection"
    )
    retriever = vectorstore.as_retriever()

    contextualize_q_prompt = ChatPromptTemplate.from_messages([
        ("system", "Given a chat history and the latest user question which might reference context in the chat history, formulate a standalone question. Do NOT answer, just reformulate if needed."),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ])

    history_aware_retriever = create_history_aware_retriever(llm, retriever, contextualize_q_prompt)

    qa_prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an assistant for question-answering tasks. Use the retrieved context to answer. If you don't know, say so. Keep answers concise (3 sentences max).\n\n{context}"),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ])

    question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)
    rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)

    def get_session_history(session: str) -> BaseChatMessageHistory:
        if session not in st.session_state.store:
            st.session_state.store[session] = ChatMessageHistory()
        return st.session_state.store[session]

    conversational_rag_chain = RunnableWithMessageHistory(
        rag_chain,
        get_session_history,
        input_messages_key="input",
        history_messages_key="chat_history",
        output_messages_key="answer"
    )

    user_input = st.text_input("Your question:")
    if user_input:
        session_history = get_session_history(session_id)
        response = conversational_rag_chain.invoke(
            {"input": user_input},
            config={"configurable": {"session_id": session_id}},
        )
        st.write("**Assistant:**", response['answer'])
        with st.expander("Chat History"):
            for msg in session_history.messages:
                st.write(f"**{msg.type.capitalize()}:** {msg.content}")
else:
    st.info("👆 Please upload a PDF to get started.")