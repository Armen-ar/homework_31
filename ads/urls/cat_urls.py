from django.urls import path
from ads.views_cat import CategoryView, CategoryDetailView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView

urlpatterns = [
    path('', CategoryView.as_view(), name='cat'),
    path('<int:pk>/', CategoryDetailView.as_view(), name='cat_detail'),
    path('update/<int:pk>/', CategoryUpdateView.as_view(), name='cat_update'),
    path('create/', CategoryCreateView.as_view(), name='cat_create'),
    path('delete/<int:pk>/', CategoryDeleteView.as_view(), name='cat_delete'),
]
