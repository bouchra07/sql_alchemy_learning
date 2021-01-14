import pandas as pd

df = pd.read_csv('/home/bouchra/PycharmProjects/ECP_scraper/Scrapping/data/new_categories.csv')

# df.columns = ['id', 'name', 'parent_id', 'created_at', 'updated_at', 'children_count', 'cover', 'logo',
#               'product_template_id', 'state', 'status_text', "position", 'suppliers_count', 'post_tag',
#               'products_count', 'slug', 'certifiers_count', 'labels_count', 'cover_original_content_type',
#               'cover_original_filename', 'cover_original_filesize', 'logo_original_content_type',
#               'logo_original_filename', 'logo_original_filesize', 'cover_title', 'cover_alt', 'cover_description',
#               'logo_title', 'logo_alt', 'logo_description']
#
# df = df.dropna(axis=0, subset=['parent_id'])
# print(df)


for index, row in df.iterrows():
    parent_id = row['parent_id']
    if parent_id not in df['id'].values:
        i = df[((df.parent_id == parent_id))].index
        df = df.drop(i)
print(df)

df.to_csv('/home/bouchra/PycharmProjects/ECP_scraper/Scrapping/data/new_categories_x.csv',index=None)
