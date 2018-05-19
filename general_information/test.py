import json
import random

with open('name_and_sex.json') as file:
    data = json.load(file)
    names = data.keys()
    sexs = data.values()

for i in range(0, len(names)):
    print(names[i])

for i in range(0, len(sexs)):
    print(sexs[i])

age = []
for i in range(0, 400):
    age.append(random.randint(20, 60))

print age