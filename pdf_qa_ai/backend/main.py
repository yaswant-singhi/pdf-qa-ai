import pdfplumber


def read_pdf_document(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for p in pdf.pages:
            text += p.extract_text() or ""
    return text
