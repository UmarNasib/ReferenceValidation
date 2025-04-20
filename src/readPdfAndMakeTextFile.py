import PyPDF2

pdfFileObj = open('inputFile1.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(pdfFileObj)
x = len(pdfReader.pages)
print(x)
for y in range(x):
    pageObj = pdfReader.pages[y]
    text = pageObj.extract_text()
    with open('processedTextFile1.txt', 'a') as f:
        f.write(text)