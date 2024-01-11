import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path, start_page, end_page):
    try:
        # Open the PDF file
        pdf_document = fitz.open(pdf_path)

        # Initialize an empty string to store the extracted text
        text = ""

        # Iterate through the specified range of pages
        for page_number in range(start_page - 1, min(end_page, pdf_document.page_count)):
            # Get the current page
            page = pdf_document[page_number]

            # Extract text from the page
            text += page.get_text()

        # Close the PDF document
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

# Example usage
pdf_path = "/Users/arshad_221b/Documents/Documents - Arshad’s MacBook Pro - 1/Projects/Lanchain Pinecone/meidtations.pdf"  # Replace with the path to your PDF file
output_file = "/Users/arshad_221b/Documents/Documents - Arshad’s MacBook Pro - 1/Projects/Lanchain Pinecone/meditations.text"  # Replace with the desired output file path
start_page = 12
end_page = 109

extracted_text = extract_text_from_pdf(pdf_path, start_page, end_page)

if extracted_text:
    save_text_to_file(extracted_text, output_file)
