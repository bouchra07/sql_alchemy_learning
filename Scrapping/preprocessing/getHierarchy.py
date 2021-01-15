from tariff import Tariff
import pandas as pd


child_ids = []
parent_ids = []
generations = []


def get_tree(tariff,i) :
    i = i + 1
    if tariff.children == [] :
        return
    else :
        for child in tariff.children :
            child_ids.append(child.id)
            parent_ids.append(parent_id)
            generations.append(i)
            get_tree(child,i)

tariffs = Tariff.query.all()

for tariff in tariffs:
    i = 0
    parent_id = tariff.id
    child_ids.append(tariff.id)
    parent_ids.append(parent_id)
    generations.append(i)

    get_tree(tariff,i)



print(child_ids)
print('--------------------------------------------------------------------------------------------')
print(parent_ids)
print('--------------------------------------------------------------------------------------------')
print(generations)
print(len(child_ids))
print(len(parent_ids))

df = pd.DataFrame(parent_ids, columns =['ancestor_id'])
df['descendant_id'] = child_ids
df['generation'] = generations

print(df)

df.to_csv("tariff_hierarchy.csv",index=None)


