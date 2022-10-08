from django.urls import path
from ads.views_cat import CategoryView, CategoryDetailView, CategoryDeleteView, CategoryUpdateView, CategoryCreateView

urlpatterns = [
    path('', CategoryView.as_view(), name='cat_all'),
    path('<int:pk>/', CategoryDetailView.as_view(), name='cat_detail'),
    path('<int:pk>/update/', CategoryUpdateView.as_view(), name='cat_update'),
    path('create/', CategoryCreateView.as_view(), name='cat_create'),
    path('<int:pk>/delete/', CategoryDeleteView.as_view(), name='cat_delete'),
]
