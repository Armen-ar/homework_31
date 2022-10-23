import pytest
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.test import APIClient
from pytest_factoryboy import register

from factories.factory_user import UserFactory
from users.models import User

register(UserFactory)


@pytest.fixture
def api_client(db, user):
    client = APIClient()
    token = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token.access_token}')
    return client
