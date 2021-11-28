# Bu projede Pdflerin sesli olarak okutulması sağlanmıştır.

from PyPDF2 import pdf
import pyttsx3
import PyPDF2

#Okutmak istediğiniz metini isim.pdf olarak yazınız.
metin=open("PDF.pdf","rb")

pdfOkuyucu=PyPDF2.PdfFileReader(metin)


#Ses seçeneklerini ayarlama
engine=pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty("voices",voices[0].id)

#For döngüsü ile sayfaları okutma
for sayfa_numarasi in range(0, pdfOkuyucu.numPages):
    sayfa=pdfOkuyucu.getPage(sayfa_numarasi)
    yazi=sayfa.extractText()
    engine.say(yazi)
    engine.runAndWait()
