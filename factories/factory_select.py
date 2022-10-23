import factory

from factories.factory_user import UserFactory


class SelectionFactory(factory.django.DjangoModelFactory):
    name = 'test name'
    owner = factory.SubFactory(UserFactory)

    class Meta:
        model = 'ads.Selection'
