from django.urls import path

from ads.views.ad import AdListView, AdDetailView, AdUploadImageView, AdCreateView

urlpatterns = [
    path('', AdListView.as_view(), name='ad_all'),
    path('<int:pk>/', AdDetailView.as_view(), name='ad_detail'),
    path('create/', AdCreateView.as_view(), name='ad_create'),
    path('<int:pk>/upload_image', AdUploadImageView.as_view(), name='upload_image'),
]
