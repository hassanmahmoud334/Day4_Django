from django.shortcuts import render, redirect, get_object_or_404
from .models import Course

def show_courses(request):
    courses = Course.objects.all()
    return render(request, 'course/index.html', {'courses': courses})

def get_course(request, id):
    course = get_object_or_404(Course, pk=id)
    return render(request, 'course/course_details.html', {'course': course})

def create_course(request):
    if request.method == "POST":
        name = request.POST.get('name')
        if name and len(name.strip()) > 0:
            Course.objects.create(name=name.strip())
            return redirect('courses')
        else:
            error = "Course name cannot be empty."
            return render(request, 'course/create_course.html', {'error': error, 'title': 'Create Course'})
    
    return render(request, 'course/create_course.html', {'title': 'Create Course'})

def update_course(request, id):
    course = get_object_or_404(Course, pk=id)

    if request.method == "POST":
        name = request.POST.get('name')
        if name and len(name.strip()) > 0:
            course.name = name.strip()
            course.save()
            return redirect('courses')
        else:
            error = "Course name cannot be empty."
            return render(request, 'course/create_course.html', {'error': error, 'title': 'Edit Course', 'course': course})
    
    return render(request, 'course/create_course.html', {'title': 'Edit Course', 'course': course})

def course_delete(request, id):
    course = get_object_or_404(Course, pk=id)
    course.delete()
    return redirect('courses')
