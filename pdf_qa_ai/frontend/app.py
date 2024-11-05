import streamlit as st
from pdf_qa_ai.backend.main import read_pdf_document


# Set page config
st.set_page_config(
    page_title="PDF Q&A AI",
    page_icon=":material/article:",
    layout="wide",
)

# Set side bar
st.sidebar.title("PDF Q&A AI Assitant")
st.sidebar.markdown(
    "### This webapp can analyze the pdf documents and response to the user query"
)
st.sidebar.markdown("")
st.sidebar.image(
    image="https://static.vecteezy.com/system/resources/previews/017/196/581/large_2x/pdf-icon-on-transparent-background-free-png.png",
    width=120,
)
st.sidebar.markdown("")

# Main
st.title(":page_facing_up: PDF Q&A AI Assitant")
is_file_uploaded = st.file_uploader("Upload a PDF File", type="pdf")

if is_file_uploaded:
    st.success("pdf file uploaded successfully")
    extracted_data = read_pdf_document(is_file_uploaded)
    st.markdown("")
    st.text_area("Extracted data", extracted_data, height=250)
