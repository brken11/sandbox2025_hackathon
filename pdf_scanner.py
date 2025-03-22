from pdf2image import convert_from_path
import pytesseract
import typing

def extract_text_from_scanned_pdf(file_path)-> list[str]:
    """
    Extracting text from a pdf is easier, my random patient generator produces pdfs.
    So this will turn them into an image before proceeding.
    """
    text : list[str] = []
    # Convert PDF pages to images
    pages = convert_from_path(file_path)
    for page_num, image in enumerate(pages):
        page_text = pytesseract.image_to_string(image)
        text.append(page_text)
    return text

def extract_text_from_image(file_path) -> list[str]:
    """
    Extracts directly, no middle ground
    """
    text : list[str] = []
    pages = convert_from_path(file_path)
    for page_num, image in enumerate(pages):
        page_text = pytesseract.image_to_string(image)
        text.append(page_text)
    return text

if __name__ == "__main__":
    pdf_path = "patient_forms.pdf"
    extracted_text = extract_text_from_scanned_pdf(pdf_path)
    print("Extracted Text from Scanned PDF:")
    print(extracted_text)

