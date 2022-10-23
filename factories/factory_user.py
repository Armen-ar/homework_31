import factory


class UserFactory(factory.django.DjangoModelFactory):
    first_name = 'test',
    last_name = 'testyan',
    username = 'Test',
    email = 'jh@test.ru',
    password = '12345',
    birth_date = factory.Faker('date_object')

    class Meta:
        model = 'users.User'
