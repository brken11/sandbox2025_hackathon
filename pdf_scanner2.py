import PyPDF2
import typing

def extract_text_from_pdf(file_path)->str:
    #text : list[str] = []
    text = ""
    with open(file_path, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page_num, page in enumerate(pdf_reader.pages):
            page_text = page.extract_text()
            if page_text:
                text += page_text
            else:
                print(f"No text found on page {page_num}. The page might be scanned.")
    return text

if __name__ == "__main__":
    pdf_path = "some_file_path_idk.pdf"
    extracted_text = extract_text_from_pdf(pdf_path)
    print("Extracted Text:")
    print(extracted_text)

