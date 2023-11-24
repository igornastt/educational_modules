from django.urls import path

from .apps import EducationalModulesConfig
from .views import ModulesCreateAPIView, ModulesListAPIView, ModulesRetrieveAPIView, ModulesUpdateAPIView, \
    ModulesDestroyAPIView, ModulesPublishedListAPIView

app_name = EducationalModulesConfig.name

urlpatterns = [
    path('create/', ModulesCreateAPIView.as_view(), name='educational_modules_create'),
    path('', ModulesPublishedListAPIView.as_view(), name='educational_modules'),
    path('all/', ModulesListAPIView.as_view(), name='educational_modules'),
    path('<int:pk>/', ModulesRetrieveAPIView.as_view(), name='educational_module'),
    path('update/<int:pk>/', ModulesUpdateAPIView.as_view(), name='educational_modules_update'),
    path('delete/<int:pk>/', ModulesDestroyAPIView.as_view(), name='educational_modules_delete'),
]
