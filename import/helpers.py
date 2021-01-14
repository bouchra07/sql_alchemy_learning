#helpers.py
import pandas as pd
from zipfile import ZipFile
import fnmatch
import gzip
import sqlalchemy
import os

def log_import(filename):
    df = pd.read_csv(filename, sep=',')
    print(df)
    return df

def zip_import(filename):
    with ZipFile(filename) as zipfiles:
        file_list = zipfiles.namelist()
        txt_files = fnmatch.filter(file_list, "*.log")
        data = [pd.read_csv(zipfiles.open(file_name), sep="\t", header=None) for file_name in txt_files]
    df = pd.concat(data)
    return df


def gz_import(filename):
    df = pd.read_csv(gzip.open(filename, 'r'), sep="\t", header=None)
    return df

def preprocess(df):
    # df = df.drop([24, 25, 26, 27, 28, 29, 30, 31, 32], axis=1)
    # df = df.drop([7], axis=0)
    df.columns = ['id', 'name', 'parent_id', 'created_at', 'updated_at', 'children_count', 'cover', 'logo', 'product_template_id', 'state', 'status_text', "position", 'suppliers_count', 'post_tag', 'products_count', 'slug', 'certifiers_count', 'labels_count', 'cover_original_content_type', 'cover_original_filename', 'cover_original_filesize', 'logo_original_content_type', 'logo_original_filename', 'logo_original_filesize', 'cover_title', 'cover_alt', 'cover_description', 'logo_title', 'logo_alt', 'logo_description']
    return df

def connect():
    engine = sqlalchemy.create_engine("postgres://docker:docker@localhost:5432/docker")
    con = engine.connect()
    return con

def implement_to_postgres(tablename,df):
    con = connect()
    # df=preprocess(df)
    df.to_sql(tablename, con, if_exists='append', index=False)
    con.close()
    print('The import to postgresql was successfully done!')
