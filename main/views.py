from django.shortcuts import render, redirect, get_object_or_404

from .models import Course, Student
from .forms import CourseForm, StudentForm

def home(request):
    students = Student.objects.order_by('-id')
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



def course_create(request):
    form = CourseForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'main/course_create.html', {'form': form})


def student_create(request):
    form = StudentForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'main/student_create.html', {'form': form})