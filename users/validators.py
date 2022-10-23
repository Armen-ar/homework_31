from dateutil.relativedelta import relativedelta
from datetime import date
from rest_framework import serializers

from django.core.exceptions import ValidationError

USER_MIN_AGE = 9


def birth_date_validator(value):
    diff_years = relativedelta(date.today(), value).years
    if diff_years < USER_MIN_AGE:
        raise ValidationError('User is underage')
    return value


def email_validator(value):
    if value.endswith('rambler.ru'):
        raise serializers.ValidationError(f'Can`t register email from this domain {value}')
    return value
