from PIL import Image
import requests
from io import BytesIO
import pytesseract

#pytesseract.pytesseract.tesseract_cmd = r'C:\ProgramData\Anaconda3\Lib\site-packages\pytesseract'



imgurls = [
        'https://italiano.is/wp-content/uploads/2018/09/menu_isl_st%C3%A6kka%C3%B0ur-copy-740x1024.jpg',
        'https://italiano.is/wp-content/uploads/2018/09/menu_isl_st%C3%A6kka%C3%B0ur2-copy-740x1024.jpg',
        'https://italiano.is/wp-content/uploads/2018/09/menu_isl_st%C3%A6kka%C3%B0ur3-copy-740x1024.jpg',
        'https://www.pizzaking.is/images/69-72-veislu-ostabr.png',
        'https://www.pizzaking.is/images/65-68-pizza-ostabr.png',
        'https://www.pizzaking.is/images/mognud-var-gaeda.png',
        'https://www.pizzaking.is/images/party-tilbod.png',
        'https://i.kym-cdn.com/photos/images/newsfeed/001/471/117/521.jpg',
        'https://italiano.is/wp-content/uploads/2018/09/menu_eng-724x1024.jpg'
    ]
page = 1
for url in imgurls:
    print('----------------------------------------oOo----------------------------------------')
    print('page number: ' + str(page) + '\n')

    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    response.close()
    print(pytesseract.image_to_string(img, lang = 'isl'))
    page += 1
    print()

print('===================================================================================\ntesteroni\n\n')
img = Image.open('test.png')
print(pytesseract.image_to_string(img, lang = 'isl+eng'))

