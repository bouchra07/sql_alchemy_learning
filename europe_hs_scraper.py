import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
from random import randint

headers = {"Accept-Language": "en-US,en;q=0.5"}

codes = []
details = []

for page in range(98):

    page = requests.get("https://www.tariffnumber.com/2020/" + str(page),headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    all_div1 = soup.find_all('div', class_='col-sm-3 col-lg-2')
    sleep(randint(2, 10))
    for container in all_div1:
        code = container.a.text
        codes.append(code)

    all_div2 = soup.find_all('div', class_='col-sm-9 col-lg-10')
    sleep(randint(2, 10))
    for container in all_div2:
        detail = container.text
        details.append(detail)


tarif_df = pd.DataFrame({
'code': codes,
'description': details,

})

tarif_df['code'] = tarif_df.code.str.replace('\n', '')
tarif_df['description'] = tarif_df.description.str.replace('\n', '')
print(tarif_df)
tarif_df.to_csv('europe_hs.csv',index=None,sep = '\t')