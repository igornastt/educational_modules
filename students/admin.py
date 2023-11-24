from django.contrib import admin

from students.models import Student

# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name")
    list_filter = ("first_name", "last_name")
    search_fields = ("email", "id")
    