import pdfplumber
from groq import Groq

client = Groq(api_key="your_api_key")

def read_pdf_document(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for p in pdf.pages:
            text += p.extract_text() or ""
    return text

def generate_response(extracted_data, query):
    prompt = f"extracted_data:{extracted_data}\nQuestion: {query}\nAnswer:"
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama3-8b-8192",
    )
    response = chat_completion.choices[0].message.content
    return response