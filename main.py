import text_to_json
import json
import pdf_scanner
import dummy_pdf_generator

def main():
    user_input : str = "";
    file_path : str = ""
    is_pdf : bool = True
    extracted_text_list : list[str] = []

    while user_input.lower() not in ('y', 'n', 'q'):
        print("Would you like the program to generate you dummy records? (y/n)")
        user_input = input();

    user_input = user_input.lower();
    if user_input == 'q':
        return


    if user_input == 'y':
        file_path = "patient_forms.pdf"
        dummy_pdf_generator.generate_patient_form_pdf(file_path, num_records= 5)
    else:
        print("Please input the file path")
        file_path = input()

        while user_input.lower() not in ('p', 'i', 'q'):
            print("Is this a pdf or an image?")
            user_input = input("Type 'p' for pdf or 'i' for image").strip().lower()

            try:
                if user_input[0] == 'p' or user_input[0] == 'q':
                    is_pdf = user_input[0] == 'p'
                else:
                    print("Please enter 'p' or 'i', or enter just 'q' to quit")
                    continue
            except:
                print("You enter 'q' to quit")
                continue
        if user_input == 'q':
            return

    if is_pdf:
        extracted_text_list = pdf_scanner.extract_text_from_scanned_pdf(file_path)
    else:
        extracted_text_list = pdf_scanner.extract_text_from_image(file_path)

    parsed_data = []
    for page_text in extracted_text_list:
        parsed_page = text_to_json.parse_patient_form(page_text)
        parsed_data.append(parsed_page)

    print(f"Parsed Data:\n{json.dumps(parsed_data, indent = 4)}\n")

if __name__ == "__main__":
    main()
