from factories.factory_ad import AdFactory
from factories.factory_select import SelectionFactory, UserFactory
from pytest_factoryboy import register

register(SelectionFactory)
register(UserFactory)
register(AdFactory)

pytest_plugins = 'fixtures.fixtures'


