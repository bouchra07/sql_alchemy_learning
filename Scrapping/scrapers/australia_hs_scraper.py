import requests
from bs4 import BeautifulSoup
import pandas as pd
headers = {"Accept-Language": "en-US, en;q=0.5"}

url = "https://www.dfat.gov.au/trade/agreements/in-force/kafta/official-documents/Pages/schedule-of-tariff-commitments-australia"

results = requests.get(url, headers=headers)

soup = BeautifulSoup(results.text, "html.parser")

hs_codes = []
descriptions = []


for tr in soup.find_all('tr')[1:]:
    tds = tr.find_all('td')
    hs_code = tds[0].text
    hs_codes.append(hs_code)
    description = tds[1].text
    descriptions.append(description)



tarif_df = pd.DataFrame({
'hs_code': hs_codes,
'description': descriptions,

})
tarif_df['hs_code'] = tarif_df.hs_code.str.replace('\n', '')
tarif_df['description'] = tarif_df.description.str.replace('\n', '')
print(tarif_df)
tarif_df.to_csv('australia_hs.csv',index=None,sep = '\t',)


