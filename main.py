from paddleocr import PaddleOCRVL
from pypdf import PdfReader, PdfWriter
import os

# Extract first 2 pages from source.pdf
reader = PdfReader("source.pdf")
writer = PdfWriter()

# Add first 2 pages (or fewer if PDF has less than 2 pages)
for page_num in range(min(2, len(reader.pages))):
    writer.add_page(reader.pages[page_num])

# Save to temporary file
temp_pdf = "temp_first_2_pages.pdf"
with open(temp_pdf, "wb") as f:
    writer.write(f)

# Process the temporary PDF
pipeline = PaddleOCRVL()
output = pipeline.predict(temp_pdf)
for res in output:
    res.save_to_markdown("output.md")

# Clean up temporary file
os.remove(temp_pdf)
