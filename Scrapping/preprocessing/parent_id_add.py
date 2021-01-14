import pandas as pd

dtypes = {'hs_code': 'str', 'description': 'str'}
df = pd.read_csv('/home/bouchra/PycharmProjects/ECP_scraper/Scrapping/data/australia_final.csv', dtype=dtypes)

df['id']=df['id']-1
df['parent_id'] = df['parent_id']
print(df)


# print(df.loc[df['hs_code'] == '01'].id.item())

parent_ids = []



for index, row in df.iterrows():
    parent_id = row['parent_id']
    id = row['id']
    if parent_id == id:
        parent_ids.append(None)
    else:
        parent_ids.append(parent_id)

print(parent_ids)


# for i in parents:
#     parent_ids.append(df.loc[df['hs_code'] == i].id.item())
# print(parent_ids)


# del df["parent"]
# del df["parent_id"]
# df['parent_id'] = parent_ids
#
#
df.to_csv('/home/bouchra/PycharmProjects/ECP_scraper/Scrapping/data/australia_final.csv',index = None)