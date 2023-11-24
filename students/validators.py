import re
from rest_framework import serializers


class FullnameValidator:
    def __init__(self, fields):
        self.fields = fields

    def __call__(self, attrs):
        reg = re.compile('^[А-Яа-я]+$')
        for field in self.fields:
            value = attrs.get(field)
            if value and not reg.match(value):
                raise serializers.ValidationError({field: 'Имя и фамилия должны быть указаны только на русском языке'})
            