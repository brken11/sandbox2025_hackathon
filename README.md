# Fax-to-Info Demo

This project demonstrates converting faxed patient forms into structured JSON data. The demo includes generating dummy records, scanning PDFs (or images) using OCR, and parsing the extracted text.

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/brken11/sandbox2025_hackathon.git
cd sandbox2025_hackathon
```

### 2. Create a Virtual Environment
Create a virtual enviroment to isolate your dependencies:
```
python3 -m venv venv
```
Activate the virtua environmnt:
 - Linux/macOS:
```
source venv/bin/activate
```
 - Windows
```
venv\Scripts\activate
```

### 3. Install the package
Install the package in editable mode:
```
pip install -e .
```

### 4. Run the Demo
After installation, run the demo using the console script:
```
fax_demo
```

## Project Structure
 - *main.py*: Main demo script that ties the modules together
 - *dummy_pdf_generator.py* : Generates dummy patien form PDFs
 - *pdf_scanner.py* : Extracts text from PDFs (or images) using OCR.
 - *text_to_json.py* : Parses the extracted text into structed JSOn data.

### setup.pt
Below is the `setup.py` used to create the console script:
from setuptools import setup, find_packages
```
setup(
    name="fax_to_info_demo",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "fax_demo = main:main",
        ],
    },
    install_requires=[
        "pytesseract",
        "pdf2image",
        "reportlab",
        "Faker"
    ]
)
```

## Overiew

This demo performs the following steps:
 - Dummy Record Generation: Optionally generates dummy ptient form PDFs
 - OCR Processor: Extracts text from PDF or imagefiles
 - Parsing : Converts the extracted text into JSON for further processing or integration.
Follow the instuctions above to set up your environment and run the demo cross platform :]


