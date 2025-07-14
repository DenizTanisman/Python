
'''
PDF and Note Merger  
Merges multiple PDF files using `PyPDF2`.  
Optionally creates a cover page or note with a custom title using `reportlab`.
'''
from PyPDF2 import PdfMerger
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# Merge multiple PDFs into one
def merge_pdfs(files, output):
    merger = PdfMerger()
    for file in files:
        merger.append(file)
    merger.write(output)
    merger.close()

# Create a single-page note PDF
def create_note_pdf(text, filename):
    c = canvas.Canvas(filename, pagesize=letter)
    c.drawString(100, 750, text)
    c.save()

# Example usage:
# create_note_pdf("Note by Deniz", "note.pdf")
# merge_pdfs(["note.pdf", "doc1.pdf", "doc2.pdf"], "merged.pdf")

