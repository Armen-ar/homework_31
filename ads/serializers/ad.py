from rest_framework import serializers

from ads.models import Ad, Category
from users.models import User


class AdListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = "__all__"
