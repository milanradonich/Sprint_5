import faker


def get_sing_up_data():
    fake = faker.Faker()
    email = fake.email()

    return email
