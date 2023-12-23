import PyPDF2

def read_file(path):
    resume = open(path, 'rb')
    pages = PyPDF2.PdfReader(resume)
    page = pages.pages[0]
    return page.extract_text()