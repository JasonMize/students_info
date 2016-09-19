from django.shortcuts import render, get_object_or_404

from .models import Student


def index (request):
    students = Student.object()

    context = {
        "students": students
    }

    return render (request, "students/index.html", context)





