import requests
from bs4 import BeautifulSoup
import pandas as pd


headers = {"Accept-Language": "en-US,en;q=0.5"}

hs_codes = []
descriptions = []

for page in range(1,98):
    if page < 10:
        page = requests.get("https://www.cbsa-asfc.gc.ca/trade-commerce/tariff-tarif/2020/html/02/ch0" + str(page) +'-eng.html', headers=headers)
    elif page == 77:
        continue
    else:
        page = requests.get("https://www.cbsa-asfc.gc.ca/trade-commerce/tariff-tarif/2020/html/02/ch" + str(page) +'-eng.html', headers=headers)


    soup = BeautifulSoup(page.text, 'html.parser')


#wb-tables table table-striped table-hover wb-init wb-tables-inited dataTable no-footer



    for tr in soup.find('table',{'class':'wb-tables table table-striped table-hover'}).find_all('tr')[2:]:
        tds = tr.find_all('td')
        hs_code = tds[0].text
        hs_codes.append(hs_code)
        description = tds[2].text
        descriptions.append(description)


tarif_df = pd.DataFrame({
'hs_code': hs_codes,
'description': descriptions,

})

print(tarif_df)
tarif_df.to_csv('canada_hs_test.csv',index=None)