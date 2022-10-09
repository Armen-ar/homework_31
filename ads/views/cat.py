from django.http import JsonResponse

# Create your views here.
from rest_framework import viewsets

from ads.models import Category
from ads.serializers.cat import CategorySerializer


def root(request):
    return JsonResponse({'status': 'ok'})


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
