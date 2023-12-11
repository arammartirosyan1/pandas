import pandas as pd
from random import randint
from faker import Faker


fake = Faker()
names = [fake.name() for x in range(20)]
age = [randint(18, 60) for y in range(20)]

data = {'names': names, 'age': age}

data = pd.DataFrame(data)
data.to_excel('Power.xlsx', index=False)

data_read = pd.read_excel('Power.xlsx')

new_data = data_read.head(6)
new_data.insert(1, "News", [12, 56, 93, 20, 44, 57])
new_data.to_excel("New.xlsx")

