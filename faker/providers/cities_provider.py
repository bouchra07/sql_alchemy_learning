import pandas as pd
import random
from faker import Faker
from faker.providers import BaseProvider

mylist = []
with open('cities.csv') as f:
    for x in f:
        mylist.append(x)

fake = Faker()
class Provider(BaseProvider):
    cities = mylist

    def city(self):
        return random.choice(self.cities)

fake.add_provider(Provider)

for i in range(10):
    print(fake.city())

def create_fake_data(fake, no_of_rows):

    columns = ['city']
    data = {column: [getattr(fake, column)() for _ in range(no_of_rows)] for column in columns}
    df = pd.DataFrame(data=data)
    df = df[columns]

    return df

print(create_fake_data(fake, 10))