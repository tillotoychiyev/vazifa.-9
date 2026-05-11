from django.urls import path
from .views import home, student_detail, course_students

urlpatterns = [
    path('', home, name='home'),
    path('course/<int:course_id>/', course_students, name='course_students'),
    path('student/<int:student_id>/', student_detail, name='detail'),
]