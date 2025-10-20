from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.show_students, name="students"),
    path('student/show/<int:id>/', views.get_student, name="student_details"), 
    path('student/delete/<int:id>/', views.student_delete, name="student_delete"), 
    path('student/create/', views.create_student, name="create_student"),
    path('student/update/<int:id>/', views.update_student, name="update_student"),
]
