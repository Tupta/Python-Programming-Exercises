# Ten skrypt działa jedynie w systemie Windows
# i trzeba mieć zainstalowaną aplikację Word.
import win32com.client  # Zainstaluj za pomocą polecenia "pip install pywin32==224".
import docx
wordFilename = 'nazwa_dokumentu_worda.docx'
pdfFilename = 'nazwa_pliku_pdf.pdf'

doc = docx.Document()
# Miejsce na kod tworzący dokument Worda.
doc.save(wordFilename)

wdFormatPDF = 17  # Liczbowy kod Worda dla formatu PDF.
wordObj = win32com.client.Dispatch('Word.Application')
docObj = wordObj.Documents.Open(wordFilename)
docObj.SaveAs(pdfFilename, FileFormat=wdFormatPDF)
docObj.Close()
wordObj.Quit()
