import io
import requests
from PyPDF2 import PdfFileReader
import re
import app.Scrapes.scrapeMananger as ScrapeManager

URL = 'http://www.bryggjan.is/static/files/menu/matsedill-is-70stk.pdf'


def scrape_bryggjan():
    f = io.BytesIO(requests.get(URL).content)
    reader = PdfFileReader(f)

    company_id = ScrapeManager.insert_or_get_company(name='Bryggjan', region='höfuðborgarsvæðið', delivers=False).id

    # Fixing few words for checks.
    contents = reader.getPage(0).extractText().replace('tún˚skur', 'túnfiskur').replace('Tor˚ærinn', 'Torfbærinn')
    manual_info = [
        {
            'name': 'Bátasmiðjan',
            'topping': 'Pepperoni, skinka, sveppir, aukaostur',
            'small': '2.090',
            'med': '2.740',
            'large': '3.590',
        }, {
            'name': 'Bankastjórinn',
            'topping': 'Pepperoni, nautahakk, beikon, sveppir, aukaostur',
            'small': '2.290',
            'med': '2.990',
            'large': '3.830',
        }, {
            'name': 'Bóndinn',
            'topping': 'Pepperoni, beikon, skinka, rjómaostur, svartur pipar',
            'small': '2.290',
            'med': ' 2.990',
            'large': '3.830',
        }, {
            'name': 'Búfræðingurinn',
            'topping': 'Gráðaostur, piparostur, parmesan, aukaostur, sulta',
            'small': '2.170',
            'med': '2.840',
            'large': '3.790',
        }, {
            'name': 'Bæjarstjórinn',
            'topping': 'Tómatar, paprika, laukur, sveppir',
            'small': '2.080',
            'med': '2.720',
            'large': '3.670',
        }, {
            'name': 'Innbæingurinn',
            'topping': 'Pepperoni, rjómaostur, oregano, svartur pipar, ananas, hvítlaukur, tómatar, parmesan',
            'small': '2.290',
            'med': '3.090',
            'large': '3.830',
        }, {
            'name': 'Rúvarinn',
            'topping': 'Pepperoni, sveppir, laukur, jalapeno, hvítlaukur, svartur pipar',
            'small': '2.070',
            'med': '2.840',
            'large': '3.790',
        }, {
            'name': 'Skipstjórinn',
            'topping': 'Rækjur, túnfiskur, laukur, tómatar',
            'small': '2.090',
            'med': '2.740',
            'large': '3.590',
        }, {
            'name': 'Þorparinn',
            'topping': 'Skinka, sveppir, ananas, hvítlaukur og piparostur',
            'small': '2.070',
            'med': '2.840',
            'large': '3.790',
        }, {
            'name': 'Torfbærinn',
            'topping': 'Parmaskinka, klettasalat, parmesanostur, olía',
            'small': '2.300',
            'med': '3.050',
            'large': '4.700',
        }, {
            'name': 'Hr. Akureyri',
            'topping': 'Nautakjöt, laukur, sveppir, bernaise og franskar',
            'small': '2.450',
            'med': '3.350',
            'large': '4.800',
        }, {
            'name': 'Margarita',
            'topping': None,
            'small': '1.490',
            'med': '1.650',
            'large': '2.170',
        },
    ]

    mContents = contents.replace('\n', '')

    for item in manual_info:
        valid = True
        pizza_name = item['name']
        toppings = item['topping']
        small_price = item['small']
        med_price = item['med']
        big_price = item['large']

        if pizza_name not in mContents:
            valid = False  # notify
        if toppings is not None:  # margarita edge case
            if item['topping'] not in mContents:
                valid = False  # notify
            else:
                toppings = toppings.lower().replace(' og', ',').split(', ')
        else:
            toppings = ['ostur', 'pizzusósa']
        if small_price not in mContents:
            valid = False  # notify
        if med_price not in mContents:
            valid = False  # notify
        if big_price not in mContents:
            valid = False  # notify

        if valid:
            small_price = re.sub(r"\D", "", small_price)
            med_price = re.sub(r"\D", "", med_price)
            big_price = re.sub(r"\D", "", big_price)
            ScrapeManager.add_scraped_pizza(pizza_name, toppings, company_id, small_price, med_price, big_price)
        else:
            break # TODO: notify breakage
