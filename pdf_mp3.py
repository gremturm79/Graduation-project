import PyPDF3
import pyttsx3
import pdfplumber

file = 'Agile.pdf'

path = open(file, 'rb')

pdf_reader = PyPDF3.PdfFileReader(path)
from_page = pdf_reader.numPages
finalText = " "
with pdfplumber.open(file) as pdf:
    for i in range(0, from_page):
        page = pdf.pages[i]
        text = page.extract_text()
        finalText += text


engine = pyttsx3.init()
engine.say(finalText)
engine.runAndWait()


