from django.shortcuts import render, redirect, get_object_or_404

from .models import Course, Student

def home(request):
    students = Student.objects.all()
    courses = Course.objects.all()
    context = {
        'students':students,
        'courses':courses
    }
    return render(request, 'main/index.html', context)



def course_students(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    students = Student.objects.filter(field=course)

    context = {
        'course': course,
        'students': students
    }

    return render(request, 'main/course_students.html', context)


def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    context = {
        'student': student
    }

    return render(request, 'main/detail.html', context)