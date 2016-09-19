from django.contrib import admin

from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "created", "bio", "github_url")


admin.site.register(Student, StudentAdmin)












