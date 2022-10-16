from django.urls import path

from ads.views.ad import AdUploadImageView, AdDetailView

urlpatterns = [
    path('<int:pk>/', AdDetailView.as_view(), name='ad_detail'),
    path('<int:pk>/upload_image/', AdUploadImageView.as_view(), name='upload_image'),
]
