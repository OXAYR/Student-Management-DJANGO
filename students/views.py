from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Teacher, Student, Course, Lesson, Enrollment
from .serializers import TeacherSerializer, StudentSerializer, CourseSerializer, LessonSerializer, EnrollmentSerializer

class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class EnrollStudentAPIView(APIView):
    def post(self, request):
        student_id = request.data.get('student_id')
        course_id = request.data.get('course_id')
        if not student_id or not course_id:
            return Response({'error': 'Student ID and Course ID are required'}, status=status.HTTP_400_BAD_REQUEST)
        student = Student.objects.get_object_or_404(id=student_id)
        course = Course.objects.get_object_or_404(id=course_id)
        if Enrollment.objects.filter(student=student, course=course).exists():
            return Response({'error': 'Already enrolled'}, status=status.HTTP_400_BAD_REQUEST)
        enrollment = Enrollment.objects.create(student=student, course=course)
        return Response({'message': 'Student enrolled in course'}, status=status.HTTP_201_CREATED)

class StudentCourseAPIView(APIView):
    def get(self, request, student_id):
        enrollments = Enrollment.objects.filter(student_id=student_id)
        courses = [en.course.title for en in enrollments]
        return Response(courses)


class CourseProgressAPIView(APIView):
    def get(self, request, student_id, course_id):
        total_lessons = Lesson.objects.filter(course_id=course_id).count()
        completed_lessons = 3  # assume for now

        progress = (completed_lessons / total_lessons) * 100 if total_lessons else 0

        return Response({
            "progress": progress
        })

class CreateTeacherAPIView(generics.CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class CreateStudentAPIView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CreateCourseAPIView(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CreateLessonAPIView(generics.CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

