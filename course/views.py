from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Course

@login_required
def course_list(request):
    courses = Course.objects.all()

    # Tambahkan atribut dinamis `is_unlocked` untuk tiap course
    for course in courses:
        course.is_unlocked = request.user in course.subscribers.all()

    return render(request, "course_list.html", {"courses": courses})

@login_required
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    # Hanya subscriber yang boleh lihat detail kursus
    if request.user not in course.subscribers.all():
        return redirect("course_list")

    return render(request, "course_detail.html", {"course": course})
