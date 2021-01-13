#helpers.py
import pandas as pd
from zipfile import ZipFile
import fnmatch
import gzip
import sqlalchemy
import os

def log_import(filename):
    dtypes = {'hs_code': 'str', 'description': 'str', 'parent': 'int'}
    df = pd.read_csv(filename, sep=',',dtype=dtypes)
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

# def preprocess(df):
#     # df = df.drop([24, 25, 26, 27, 28, 29, 30, 31, 32], axis=1)
#     # df = df.drop([7], axis=0)
#     df.columns = ['date', 'time', 'code1', 'code2', 'ip_address', 'method', 'hostname', 'image_path', 'status', 'url1',
#                   'user_agents', 'v_number', 'log_type',
#                   'url_identifier', 'hostname2', 'protocol', 'port_number', 'time_response1',
#                   'tls_versions', 'cypher_suite', 'http_version', 'amp_connector',
#                   'time_response2', 'content_type']
#     return df

def connect():
    engine = sqlalchemy.create_engine("postgres://docker:docker@localhost:5432/docker")
    con = engine.connect()
    return con

def implement_to_postgres(tablename,df):
    con = connect()
    df.to_sql(tablename, con, if_exists='append', index=False)
    con.close()
    print('The import to postgresql was successfully done!')
