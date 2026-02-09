import streamlit as st
from pdf_loader import extract_text
from pii_sanitizer import sanitize
from embeddings import create_vector_store
from rag_qa import ask_question
from translator import translate_to_english
from dashboard import generate_charts

st.set_page_config(page_title="Health Report Analyzer", layout="wide")

st.title("🩺 RAG-Based Health Report Analyzer")

uploaded_file = st.file_uploader("Upload Health Report (PDF)", type=["pdf"])

if uploaded_file:
    raw_text = extract_text(uploaded_file)
    clean_text = sanitize(raw_text)

    index, chunks = create_vector_store(clean_text)

    st.subheader("📊 Personalized Health Dashboard")
    fig = generate_charts(clean_text)
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("💬 Ask Questions About Your Report")
    query = st.text_input("Ask in any language")

    if query:
        translated = translate_to_english(query)
        answer = ask_question(translated, index, chunks)
        st.success(answer)
