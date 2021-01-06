import pandas as pd


df = pd.read_csv('/home/bouchra/PycharmProjects/ECP_scraper/Scrapping/data/new_australia.csv', sep=',')


df.to_csv('/home/bouchra/PycharmProjects/ECP_scraper/Scrapping/data/new_australia.csv')