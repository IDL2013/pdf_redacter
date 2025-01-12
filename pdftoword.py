# Convert PDF to Word

from pdf2docx import Converter

# Keeping the PDF's location in a separate variable
pdf_file = input("Enter the location of the PDF file: ")

# Maintaining the Document's path in a separate variable
if (input("Do you want to save the file in the same directory? (Y/N): ").upper() == "Y"):
    docx_file = pdf_file.replace(".pdf", ".docx")
else: docx_file = input("Enter the location of the DOCX file: ")

# Using the built-in function, convert the PDF file to a document file by saving it in a variable.
cv = Converter(pdf_file)

# Converting the PDF file to a Word document
cv.convert(docx_file)

cv.close()
