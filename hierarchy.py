import pandas as pd

df = pd.read_csv('data/new_australia.csv', sep=',')

df2 = pd.DataFrame(columns = ['mapping_id', 'parent_id','depth'])
df2['mapping_id']=df['id']
df2['parent_id']=df['chapter']
df2['depth'] = df['depth']

df2.to_csv('data/tariffs_hierarchy.csv',index =None)