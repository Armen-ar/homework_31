from django.http import JsonResponse

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from ads.models import Category
from ads.serializers.cat import CategorySerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def root(request):
    return JsonResponse({'status': 'ok'})


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
