import json

from django.http import JsonResponse

# Create your views here.
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView, CreateView
from rest_framework.generics import ListAPIView, RetrieveAPIView

from ads.models import Ad, Category
from ads.serializers_ad import AdSerializer
from users.models import User


class AdListView(ListAPIView):
    queryset = Ad.objects.order_by('-price').all()
    serializer_class = AdSerializer

    def get(self, request, *args, **kwargs):
        categories = request.GET.getlist('cat', [])
        if categories:
            self.queryset = self.queryset.filter(category_id__in=categories)
        text = request.GET.get('text')
        if text:
            self.queryset = self.queryset.filter(name__icontains=text)
        location = request.GET.get('location')
        if location:
            self.queryset = self.queryset.filter(author__location__name__icontains=location)
        price_from = request.GET.get('price_from')
        price_to = request.GET.get('price_to')
        if price_from:
            self.queryset = self.queryset.filter(price__gte=price_from)
        if price_to:
            self.queryset = self.queryset.filter(price__lte=price_to)

        return super().get(self, *args, **kwargs)


class AdDetailView(RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


@method_decorator(csrf_exempt, name='dispatch')
class AdCreateView(CreateView):
    model = Ad
    fields = ['name', 'author', 'price', 'description', 'is_published', 'category']

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)

        author = get_object_or_404(User, id=data['author_id'])
        category = get_object_or_404(Category, id=data['category_id'])

        new_ad = Ad.objects.create(
            name=data['name'],
            author=author,
            category=category,
            price=data['price'],
            description=data['description'],
            is_published=data['is_published'] if 'is_published' in data else False,
            image=data['image'] if 'image' in data else ''
        )

        return JsonResponse({
            'id': new_ad.id,
            'name': new_ad.name,
            'author': new_ad.author.username,
            'category': new_ad.category.name,
            'price': new_ad.price,
            'description': new_ad.description,
            'is_published': new_ad.is_published,
            'image': new_ad.image.url if 'image' in data else 'Без картинки'
        },
            safe=False,
            json_dumps_params={'ensure_ascii': False}
        )


@method_decorator(csrf_exempt, name='dispatch')
class AdUploadImageView(UpdateView):
    model = Ad
    fields = ['image']

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.image = request.FILES.get('image')
        self.object.save()
        return JsonResponse({
            'id': self.object.id,
            'name': self.object.name,
            'author': self.object.author.username,
            'category': self.object.category.name,
            'price': self.object.price,
            'description': self.object.description,
            'is_published': self.object.is_published,
            'image': self.object.image.url
        },
            safe=False,
            json_dumps_params={'ensure_ascii': False}
        )
