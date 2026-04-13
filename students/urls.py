from django.urls import path
from .views import (
    CourseListCreateView,
    EnrollStudentAPIView,
    StudentCourseAPIView,
    CourseProgressAPIView
)

urlpatterns = [
    path('courses/', CourseListCreateView.as_view(), name='course-list-create'),
    path('enroll/', EnrollStudentAPIView.as_view(), name='enroll-student'),
    path('student-courses/<int:student_id>/', StudentCourseAPIView.as_view(), name='student-courses'),
    path('course-progress/<int:student_id>/<int:course_id>/', CourseProgressAPIView.as_view(), name='course-progress'),
]
