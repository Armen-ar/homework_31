from rest_framework import serializers


def is_published_validator(value):
    if value:
        return serializers.ValidationError('is_published cannot be true')
    return value
