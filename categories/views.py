from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from categories.models import Category
from categories.pagination import CategoriesPagination
from categories.serializers import CategoriesSerializer
from users.permissions import IsModeratorPermission, IsTeacherPermission


class CategoriesCreateAPIView(generics.CreateAPIView):
    """ Создание категории """

    serializer_class = CategoriesSerializer
    permission_classes = [IsAuthenticated & (IsModeratorPermission | IsTeacherPermission)]



class CategoriesListAPIView(generics.ListAPIView):
    """ Вывод списка обучающих модулей для авторизованных пользователей с ограниченными данными"""

    serializer_class = CategoriesSerializer
    pagination_class = CategoriesPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Category.objects.all()


class CategoriesRetrieveAPIView(generics.RetrieveAPIView):
    """ Вывод одного обучающего модуля"""

    serializer_class = CategoriesSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Category.objects.all()


class CategoriesUpdateAPIView(generics.UpdateAPIView):
    """ Обновление обучающего модуля"""

    serializer_class = CategoriesSerializer
    permission_classes = [IsAuthenticated & (IsModeratorPermission | IsTeacherPermission)]

    def get_queryset(self):
        return Category.objects.all()


class CategoriesDestroyAPIView(generics.DestroyAPIView):
    """ Удаление обучающего модуля"""

    serializer_class = CategoriesSerializer
    permission_classes = [IsAuthenticated & IsModeratorPermission]

    def get_queryset(self):
        return Category.objects.all()
