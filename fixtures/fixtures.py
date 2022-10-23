import pytest
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.test import APIClient

from users.models import User


@pytest.fixture
def api_client(db, user):
    client = APIClient()
    token = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token.access_token}')
    return client


@pytest.fixture
def user(db):
    user = User.objects.create_user(
        first_name='test',
        last_name='testyan',
        username='Test',
        email='us@test.ru',
        password='12345'
    )
    return user

