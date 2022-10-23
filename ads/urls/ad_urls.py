from django.urls import path

from ads.views.ad import AdUploadImageView, AdDetailView, AdCreateView, AdListView

urlpatterns = [
    path('', AdListView.as_view(), name='ad_list'),
    path('<int:pk>/', AdDetailView.as_view(), name='ad_detail'),
    path('create/', AdCreateView.as_view(), name='ad_create'),
    path('<int:pk>/upload_image/', AdUploadImageView.as_view(), name='upload_image'),
]
