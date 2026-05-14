from faker import Faker

faker = Faker()


class UserFactory:

    @staticmethod
    def create_user():
        return {
            "name": faker.name(),
            "email": faker.unique.email(),
            "password": "Qa@123456",
            "first_name": faker.first_name(),
            "last_name": faker.last_name(),
            "address": faker.street_address(),
            "state": faker.state(),
            "city": faker.city(),
            "zipcode": faker.postcode(),
            "mobile_number": faker.phone_number()
        }