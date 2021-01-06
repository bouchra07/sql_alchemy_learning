import pandas as pd

df = pd.read_csv('/home/bouchra/PycharmProjects/ECP_scraper/Scrapping/data/new_australia_test.csv', sep=',')

# print(df.hs_code.str[:2].values)

parents =[]
for index, row in df.iterrows():
    parent = row['parent']
    hs_code = row['hs_code']
    if parent not in df['hs_code'].values:
        parents.append(hs_code[:4])
    else:
        parents.append(parent)

df['parent'] = parents

parents = []

for index, row in df.iterrows():
    parent = row['parent']
    hs_code = row['hs_code']
    if parent not in df['hs_code'].values:
        parents.append(hs_code[:2])
    else:
        parents.append(parent)

df['parent'] = parents

df.to_csv('/home/bouchra/PycharmProjects/ECP_scraper/Scrapping/data/new_australia.csv',index = None)





# mask = df['hs_code'].values == '0101'
# print(df[mask].id)
# df['parent_id'] = df[mask].id
# print(df['parent_id'])
#
# parents_ids = []
#
# for index, row in df.iterrows():
#     parent = row['parent']
#     if df['hs_code'].values == parent:
#         parents_ids.append(row2['id'])
#     else:
#         continue
#     for index2,row2 in df.iterrows():