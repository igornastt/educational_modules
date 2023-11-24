from students.models import Student

from rest_framework import serializers

from students.validators import FullnameValidator


class StudentSerializer(serializers.ModelSerializer):
    """ Класс сериализатор для студента """

    class Meta:
        model = Student
        fields = ("id", "first_name", "last_name", "avatar", "email", "phone", "is_active", "modul",)
        validators = [FullnameValidator(fields=("first_name", "last_name"))]


class StudentSmallSerializer(serializers.ModelSerializer):
    """ Класс сериализатора который показывает краткую информацию о студенте """

    class Meta:
        model = Student
        fields = ("id", "first_name", "last_name")
        