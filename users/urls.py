from django.urls import path

from users.views_user import UserListView, UserCreateView, UserDetailView

urlpatterns = [
    path('', UserListView.as_view(), name='user'),
    path('<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    # path('update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('create/', UserCreateView.as_view(), name='user_create'),
    # path('delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),
]
