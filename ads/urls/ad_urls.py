from django.urls import path

from ads.views_ad import AdListView, AdDetailView, AdUploadImageView, AdCreateView

urlpatterns = [
    path('', AdListView.as_view(), name='ad'),
    path('<int:pk>/', AdDetailView.as_view(), name='ad_detail'),
    # path('update/<int:pk>/', AdUpdateView.as_view(), name='ad_update'),
    path('create/', AdCreateView.as_view(), name='ad_create'),
    # path('delete/<int:pk>/', AdDeleteView.as_view(), name='ad_delete'),
    path('<int:pk>/upload_image', AdUploadImageView.as_view(), name='upload_image'),
]
