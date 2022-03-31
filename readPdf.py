# The purpose of this project is to read aloud Pdf files..

from PyPDF2 import pdf
import pyttsx3
import PyPDF2

#Write the text you want to read as "name.pdf".
metin=open("PDF.pdf","rb")

pdfOkuyucu=PyPDF2.PdfFileReader(metin)


#Setting sound options

engine=pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty("voices",voices[0].id)

#Reading pages with a for loop
for sayfa_numarasi in range(0, pdfOkuyucu.numPages):
    sayfa=pdfOkuyucu.getPage(sayfa_numarasi)
    yazi=sayfa.extractText()
    engine.say(yazi)
    engine.runAndWait()
