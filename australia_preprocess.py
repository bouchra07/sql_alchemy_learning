import pandas as pd

df = pd.read_csv('data/australia_hs.csv', sep='\t')


# df = df.rename(columns = {'country_id': 'region_id'}, inplace = False)
df['description'] = df.description.str.replace('-','')
df['hs_code2'] = df.hs_code.str.replace('.','')
df['hs_code2'] = df.hs_code2.str.replace(' ','')

df['hs_code'] = df.hs_code.str.replace(' ','')
df['description'] = df.description.str.replace(':','')
df['level'] = df['hs_code2'].str.len()

parents = []
for index, row in df.iterrows():
    level = row['level']
    hs_code = row['hs_code']
    if level == 2 :
        parents.append('TOTAL')
    elif level == 4:
        parents.append(hs_code[:2])
    elif level == 5:
        parents.append(hs_code[:4])
    elif level == 6:
        parents.append(hs_code[:6])
    elif level == 7:
        parents.append(hs_code[:6])
    elif level == 8:
        parents.append(hs_code[:6])
    else:
        parents.append('None')

df['parent'] = parents



df['chapter'] = df.hs_code2.astype(str).str[:2].astype(int)
df['region_id'] = 1




section_ids = []
for index, row in df.iterrows():
    chapter = row['chapter']
    if chapter in range(1,6) :
        section_ids.append(1)
    elif chapter in range(6, 15):
        section_ids.append(2)
    elif chapter == 15:
        section_ids.append(3)
    elif chapter in range(16, 25):
        section_ids.append(4)
    elif chapter in range(25, 28):
        section_ids.append(5)
    elif chapter in range(28, 39):
        section_ids.append(6)
    elif chapter in range(39, 41):
        section_ids.append(7)
    elif chapter in range(41, 44):
        section_ids.append(8)
    elif chapter in range(44, 47):
        section_ids.append(9)
    elif chapter in range(47, 50):
        section_ids.append(10)
    elif chapter in range(50, 64):
        section_ids.append(11)
    elif chapter in range(64, 68):
        section_ids.append(12)
    elif chapter in range(68, 71):
        section_ids.append(13)
    elif chapter == 71:
        section_ids.append(14)
    elif chapter in range(72, 84):
        section_ids.append(15)
    elif chapter in range(84, 86):
        section_ids.append(16)
    elif chapter in range(86, 90):
        section_ids.append(17)
    elif chapter in range(90, 93):
        section_ids.append(18)
    elif chapter == 93:
        section_ids.append(19)
    elif chapter in range(94, 97):
        section_ids.append(20)
    elif chapter == 97:
        section_ids.append(21)
    else:
        section_ids.append(0)

df['section_id'] = section_ids
del df["hs_code2"]
# df['depth'] = depths

df.to_csv('data/new_australia.csv',index =None)
