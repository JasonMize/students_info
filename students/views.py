from django.shortcuts import render, get_object_or_404

from .models import Student


def index (request):
    students = Student.objects.all()

    context = {
        "students": students
    }

    return render (request, "students/index.html", context)


def students (request, id):
    students = get_object_or_404(Student, pk=id)

    context = {
        "students":students
    }

    return render (request, "students/student.html", context)
