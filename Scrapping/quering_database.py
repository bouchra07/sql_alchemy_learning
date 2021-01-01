from sqlalchemy import create_engine, select, MetaData, Table
from sqlalchemy.sql import and_
engine = create_engine("postgres://docker:docker@localhost:5432/docker")
metadata = MetaData(bind=None)
table = Table('tariffs', metadata, autoload = True, autoload_with = engine)
stmt = select([table]).where(table.columns.description == 'Baths, shower-baths, sinks and washbasins, of plastics')

connection = engine.connect()
results = connection.execute(stmt).fetchall()

# for result in results:
#     print(result)


s = select([table]).where(and_(table.c.section_id == 5, table.c.region_id == 3))
for row in connection.execute(s):
    print (row)