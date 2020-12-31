import requests
from bs4 import BeautifulSoup
import pandas as pd
headers = {"Accept-Language": "en-US, en;q=0.5"}

url = "https://www.abf.gov.au/importing-exporting-and-manufacturing/tariff-classification/current-tariff/schedule-3"

results = requests.get(url, headers=headers)

soup = BeautifulSoup(results.text, "html.parser")

section_numbers = []
section_titles = []


for tr in soup.find_all('tr')[1:]:
    tds = tr.find_all('td')
    section_number = tr.th.a.text
    section_numbers.append(section_number)
    section_title = tds[1].a.text
    section_titles.append(section_title)


section_ids = list(range(1, 22))
print(section_ids)
df = pd.DataFrame({
'section_id' : section_ids,
'section_number': section_numbers,
'section_title': section_titles,

})

print(df)

df.to_csv('australia_sections.csv',index=None,sep = '\t')


