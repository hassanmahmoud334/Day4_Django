from django.urls import path
from . import views

urlpatterns = [
    path('course/', views.show_courses, name="courses"),
    path('course/show/<int:id>/', views.get_course, name="course_details"), 
    path('course/delete/<int:id>/', views.course_delete, name="course_delete"), 
    path('course/create/', views.create_course, name="create_course"),
    path('course/update/<int:id>/', views.update_course, name="update_course"),
]
