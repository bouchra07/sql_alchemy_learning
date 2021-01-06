import pandas as pd

dtypes = {'hs_code': 'str', 'description': 'str','parent': 'str'}
df = pd.read_csv('/home/bouchra/PycharmProjects/ECP_scraper/Scrapping/data/new_australia.csv', dtype=dtypes)

# print(df.loc[df['hs_code'] == '01'].id.item())

parent_ids = []
parents = df['parent'].values

for i in parents:
    parent_ids.append(df.loc[df['hs_code'] == i].id.item())
print(parent_ids)

df['parent_id'] = parent_ids
del df["parent"]


df.to_csv('/home/bouchra/PycharmProjects/ECP_scraper/Scrapping/data/australia_final.csv',index = None)