from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from .models import Student
from .pagination import StudentPagination
from .serializers import StudentSerializer, StudentSmallSerializer
from users.permissions import IsModeratorPermission, IsTeacherPermission, IsStudentPermission


class StudentCreateAPIView(generics.CreateAPIView):
    """ Создание  или добавление студента """

    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated & (IsModeratorPermission | IsStudentPermission)]


class StudentPublishedListAPIView(generics.ListAPIView):
    """ Вывод списка студентов по имени и фамилии"""

    serializer_class = StudentSmallSerializer
    pagination_class = StudentPagination
    permission_classes = [IsAuthenticated & (IsTeacherPermission | IsModeratorPermission | IsStudentPermission)]

    def get_queryset(self):
        return Student.objects.all()


class StudentListAPIView(generics.ListAPIView):
    """ Вывод списка студентов со всей информацией о них"""

    serializer_class = StudentSerializer
    pagination_class = StudentPagination
    permission_classes = (IsModeratorPermission, )

    def get_queryset(self):
        return Student.objects.all()


class StudentRetrieveAPIView(generics.RetrieveAPIView):
    """Вывод одного студента"""
    serializer_class = StudentSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return Student.objects.all()

    def get_object(self):
        return get_object_or_404(Student, pk=self.kwargs.get('pk'))


class StudentUpdateAPIView(generics.UpdateAPIView):
    """ Обновление данных о студенте"""

    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated & IsModeratorPermission]

    def get_queryset(self):
        return Student.objects.all().order_by('first_name', 'last_name')


class StudentDestroyAPIView(generics.DestroyAPIView):
    """ Удаление  студента"""

    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated & IsModeratorPermission]

    def get_queryset(self):
        return Student.objects.all()
