from django.urls import path

from ads.views.select import SelectionListView, SelectionDetailView, SelectionCreateView, SelectionUpdateView, \
    SelectionDeleteView

urlpatterns = [
    path('', SelectionListView.as_view(), name='select_all'),
    path('<int:pk>/', SelectionDetailView.as_view(), name='select_detail'),
    path('create/', SelectionCreateView.as_view(), name='select_create'),
    path('<int:pk>/update/', SelectionUpdateView.as_view(), name='select_update'),
    path('<int:pk>/delete/', SelectionDeleteView.as_view(), name='select_delete'),
]
