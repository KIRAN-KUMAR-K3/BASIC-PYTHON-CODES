from PyPDF2 import PdfWriter, PdfReader
num = int(input("Enter page number you want combine from multiple documents "))
pdf1 = open('E:\\birds.pdf', 'rb')
pdf2 = open('E:\\birdspic.pdf', 'rb')
pdf3 = open('E:\\birdspic1.pdf', 'rb')
pdf_writer = PdfWriter()
pdf1_reader = PdfReader(pdf1)
page = pdf1_reader.pages[num - 3]
pdf_writer.add_page(page)
pdf2_reader = PdfReader(pdf2)
page = pdf2_reader.pages[num - 3]
pdf_writer.add_page(page)
pdf3_reader = PdfReader(pdf3)
page = pdf3_reader.pages[num - 3]
pdf_writer.add_page(page)
with open('E:\output.pdf', 'wb') as output:
    pdf_writer.write(output)