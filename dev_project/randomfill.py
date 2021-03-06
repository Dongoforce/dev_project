import faker
import random

fake = faker.Faker(['ru_RU'])
jobs = ["Assistant", "Developer", "Destroyer", "Communist"]
with open("Generated.csv", "w", encoding="utf-8") as file:
    file.write("name,surname,birth_date,position\n")
    for _ in range(500):
        date = fake.date_of_birth()
        name = fake.first_name()
        surname = fake.last_name()
        position = random.choice(jobs)
        #position = fake.job()
        file.write(f"{name},{surname},{date},{position}\n")