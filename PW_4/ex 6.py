# Required libraries for each file type
import PyPDF2  # For PDF files
import pytesseract  # For image files
import pandas as pd  # For Excel files
from docx import Document  # For Word files

# Extract data from PDF file
pdf_file = 'близкие синонимы.pdf'
pdf_text = ''
with open(pdf_file, 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    for page in range(reader.numPages):
        pdf_text += reader.getPage(page).extract_text()

# Extract data from image file
image_file = 'pi.png'
image_text = pytesseract.image_to_string(image_file)

# Extract data from Excel file
excel_file = 'группировка.xlsx'
df = pd.read_excel(excel_file)
excel_data = df.to_dict()

# Extract data from Word file
word_file = "Mentor's bot.docx"
doc = Document(word_file)
word_text = ' '.join([p.text for p in doc.paragraphs])

# Print the extracted data
print("PDF Text:", pdf_text)
print("Image Text:", image_text)
print("Excel Data:", excel_data)
print("Word Text:", word_text)