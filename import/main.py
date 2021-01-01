#import.py
from helpers import *
import sys


def import_pg():
    filename = sys.argv[1]
    tablename = sys.argv[2]

    if filename.endswith('.csv'):
        df = log_import(filename)

    elif filename.endswith('.zip'):
        df = zip_import(filename)

    elif filename.endswith('.gz'):
        df = gz_import(filename)

    implement_to_postgres(tablename, df)

if __name__ == '__main__':
    import_pg()


