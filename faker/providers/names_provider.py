import pandas as pd
import random
from faker import Faker
from faker.providers import BaseProvider

mylist = []
with open('moroccan_names.csv') as f:
    for x in f:
        mylist.append(x)

fake = Faker()
class Provider(BaseProvider):
    names = mylist

    def name(self):
        return random.choice(self.names)

fake.add_provider(Provider)

for i in range(10):
    print(fake.name())

def create_fake_data(fake, no_of_rows):

    columns = ['name']
    data = {column: [getattr(fake, column)() for _ in range(no_of_rows)] for column in columns}
    df = pd.DataFrame(data=data)
    df = df[columns]

    return df

print(create_fake_data(fake, 10))