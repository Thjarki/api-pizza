import io
import requests
from PyPDF2 import PdfFileReader

URL = 'https://irp-cdn.multiscreensite.com/c20b6e4b/files/uploaded/flatey_matse%C3%B0ill_v9_IS.pdf'

# TODO: insert into database
def scrape_flatey():
    f = io.BytesIO(requests.get(URL).content)
    reader = PdfFileReader(f)
    # Fixing few words for checks.
    contents = reader.getPage(0).extractText().replace('kartö˚ur', 'kartöflur').replace('truf˚uolía',
                                                                                        'truffluolía').replace('˚ögur',
                                                                                                               'flögur')
    manual_info = [
        {
            'name': 'MARINARA',
            'topping': 'San Marzano tómatar, fersk basilíka, ólífuolía, hvítlaukur, oregano (enginn ostur)',
            'small': None,
            'med': '1.750',
            'large': None,
        }, {
            'name': 'MARGHERITA',
            'topping': 'San Marzano tómatar, fersk basilíka, ólífuolía, ferskur mozzarella',
            'small': None,
            'med': '1.950',
            'large': None,
        }, {
            'name': 'DIAVOLA',
            'topping': 'San Marzano tómatar, fersk basilíka, ólífuolía, ferskur mozzarella, pepperoni',
            'small': None,
            'med': '2.150',
            'large': None,
        }, {
            'name': 'PARMA',
            'topping': 'San Marzano tómatar, fersk basilíka, ólífuolía,  ferskur mozzarella, hráskinka, klettasalat,  parmesan',
            'small': None,
            'med': '2.750',
            'large': None,
        }, {
            'name': 'PADRINO',
            'topping': 'San Marzano tómatar, fersk basilíka, ólífuolía, ferskur mozzarella, pepperoni, pikklaður chili pipar, hunang',
            'small': None,
            'med': '2.450',
            'large': None,
        }, {
            'name': 'NDUJA',
            'topping': 'San Marzano tómatar, ólífuolía, fersk basilíka,   ferskur mozzarella, n™duja kryddpylsa (sterk)',
            'small': None,
            'med': '2.500',
            'large': None,
        }, {
            'name': 'UMBERTO',
            'topping': 'San Marzano tómatar, fersk basilíka, ólífuolía, ferskur mozzarella, pepperoni, döðlur, mascarpone '
                       'rjómaostu',
            'small': None,
            'med': '2.550',
            'large': None,
        }, {
            'name': 'TARTUFO',
            'topping': 'Fersk basilíka, ólífuolía, ferskur mozzarella, ricotta ostur, íslenskar kartöflur, truffluolía, sjávarsalt (engir tómatar)',
            'small': None,
            'med': '2.550',
            'large': None,
        }, {
            'name': 'VEGANA',
            'topping': 'San Marzano tómatar, fersk basilíka, ólífuolía, íslenskar kartöflur, ferskt rósmarín, rauðlaukur, svartar og grænar ólífur (enginn ostur)',
            'small': None,
            'med': '1.950',
            'large': None,
        }, {
            'name': 'MONELLA',
            'topping': 'San Marzano tómatar, ólífuolía, fersk basilíka,  ferskur mozzarella, pecorino, oregano, chili flögur',
            'small': None,
            'med': '2.150',
            'large': None,
        }
    ]

    mContents = contents.replace('\n', '')

    for item in manual_info:
        print(item['name'] in mContents)
        if item['topping'] is not None:
            print(item['topping'] in mContents)
        if item['small'] in mContents:
            print(item['small'] in mContents)
        if item['med'] in mContents:
            print(item['med'] in mContents)
        if item['large'] in mContents:
            print(item['large'] in mContents)
