import io
import requests
from PyPDF2 import PdfFileReader

url = 'https://irp-cdn.multiscreensite.com/c20b6e4b/files/uploaded/flatey_matse%C3%B0ill_v9_IS.pdf'

r = requests.get(url)
f = io.BytesIO(r.content)

reader = PdfFileReader(f)
contents = reader.getPage(0).extractText()

print(contents)