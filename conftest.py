from factories.factory_ad import AdFactory
from factories.factory_select import SelectionFactory
from pytest_factoryboy import register

register(SelectionFactory)
register(AdFactory)

pytest_plugins = 'fixtures.fixtures'


