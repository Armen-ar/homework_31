from rest_framework import serializers

from ads.models import Ad, Category
from ads.validators.cat import is_published_validator
from users.models import User


class AdListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = "__all__"


class AdCreateSerializer(serializers.ModelSerializer):
    is_published = serializers.BooleanField(validators=[is_published_validator])

    class Meta:
        model = Ad
        fields = "__all__"


class AdDetailSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field="username", queryset=User.objects.all())
    category = serializers.SlugRelatedField(slug_field="name", queryset=Category.objects.all())

    class Meta:
        model = Ad
        fields = "__all__"


class AdUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = "__all__"
