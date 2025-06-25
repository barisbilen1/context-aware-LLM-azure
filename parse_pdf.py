import pdfplumber

# Path to your PDF file
pdf_path = "####/barisbilen_cv_2025.pdf"

# Initialize empty string to store text
full_text = ""

# Open and parse the PDF
with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        if text:  # Some pages may be empty
            full_text += text + "\n"

# Output the extracted text
print(full_text)

# Optionally save to a .txt file for inspection
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(full_text)
