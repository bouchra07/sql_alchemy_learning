import csv
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.morocco-guide.com/travel-tips/moroccan-names/"
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, "lxml")


tds = soup.find_all('td')

with open('moroccan_names.csv', mode='w') as names_file:
    names_writer = csv.writer(names_file, quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for name in tds:
        names_writer.writerow([name.text])


df = pd.read_csv('moroccan_names.csv', header = None)
df = pd.DataFrame(df.values, columns = ['names'])
df['names'] = df.names.str.replace('"', '')
df=df.dropna(axis=0,how='all')
df.to_csv('moroccan_names.csv',index=False,header = False)
