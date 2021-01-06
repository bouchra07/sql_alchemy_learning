import csv
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd

url = "https://fr.wikipedia.org/wiki/Liste_des_villes_du_Maroc"
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, "lxml")


cities = soup.select('div.mw-parser-output > ul > li > a')
with open('cities.csv', mode='w') as city_file:
    city_writer = csv.writer(city_file, quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for city in cities:
        city_writer.writerow([city.text])

df = pd.read_csv('cities.csv', header = None)
df = df.drop([0,1,2,3,4,5,6,7,8,459,460,461,462,463,464,465], axis=0)

df.to_csv('cities.csv',index=False,header = False)
