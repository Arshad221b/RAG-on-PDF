import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path, start_page, end_page):
    
    try:
        pdf_document = fitz.open(pdf_path)
        text = ""

        for page_number in range(start_page - 1, min(end_page, pdf_document.page_count)):
            page = pdf_document[page_number]
            text += page.get_text()

        pdf_document.close()

        return text

    except Exception as e:
        print(f"Error extracting text: {e}")
        return None

def save_text_to_file(text, output_file):
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(text)
        print(f"Text saved to {output_file}")

    except Exception as e:
        print(f"Error saving text to file: {e}")

pdf_path = ""  
output_file = ""  
start_page = 12
end_page = 109

extracted_text = extract_text_from_pdf(pdf_path, start_page, end_page)

if extracted_text:
    save_text_to_file(extracted_text, output_file)
