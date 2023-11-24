from students.apps import StudentsConfig

from django.urls import path

from students.views import StudentCreateAPIView, StudentPublishedListAPIView, StudentListAPIView, \
    StudentRetrieveAPIView, StudentUpdateAPIView, StudentDestroyAPIView

app_name = StudentsConfig.name


urlpatterns = [
    path('create/', StudentCreateAPIView.as_view(), name='student_create'),
    path('', StudentPublishedListAPIView.as_view(), name='students'),
    path('all/', StudentListAPIView.as_view(), name='students'),
    path('<int:pk>/', StudentRetrieveAPIView.as_view(), name='student'),
    path('update/<int:pk>/', StudentUpdateAPIView.as_view(), name='student_update'),
    path('delete/<int:pk>/', StudentDestroyAPIView.as_view(), name='student_delete'),
]
