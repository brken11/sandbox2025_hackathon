from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from faker import Faker

def generate_patient_form_pdf(output_filename, num_records=5):
    """
    Generates a PDF file with pseudo-random, but realistic patient form data.
    """
    c = canvas.Canvas(output_filename, pagesize=letter)
    _, height = letter
    fake = Faker()

    for i in range(num_records):
        name = fake.name()
        dob = fake.date_of_birth(minimum_age=0, maximum_age=100)
        address = fake.address().replace("\n", ", ")
        phone = fake.phone_number()
        email = fake.email()
        patient_id = fake.random_number(digits=6, fix_len=True)
        appointment_date = fake.date_this_year()
        doctor = fake.name()
        diagnosis = fake.sentence(nb_words=6)

        y = height - 50
        c.setFont("Helvetica-Bold", 16)
        c.drawString(50, y, f"Patient Form #{i+1}")
        y -= 30

        c.setFont("Helvetica", 12)
        c.drawString(50, y, f"Patient ID: {patient_id}")
        y -= 20;
        c.drawString(50, y, f"Name: {name}")
        y -= 20
        c.drawString(50, y, f"Date of Birth: {dob}")
        y -= 20
        c.drawString(50, y, f"Address: {address}")
        y -= 20
        c.drawString(50, y, f"Phone: {phone}")
        y -= 20
        c.drawString(50, y, f"Email: {email}")
        y -= 20
        c.drawString(50, y, f"Appointment Date: {appointment_date}")
        y -= 20
        c.drawString(50, y, f"Doctor: {doctor}")
        y -= 20
        c.drawString(50, y, f"Diagnosis: {diagnosis}")
        y -= 40

        c.showPage()

    c.save()
    print(f"PDF generated: {output_filename}")

if __name__ == "__main__":
    generate_patient_form_pdf("patient_forms.pdf", num_records=5)

