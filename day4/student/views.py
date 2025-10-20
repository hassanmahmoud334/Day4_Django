from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

def show_students(request):
    students = Student.objects.all()
    return render(request, 'student/index.html', {'students': students})

def get_student(request, id):
    student = get_object_or_404(Student, pk=id)
    return render(request, 'student/student_details.html', {'student': student})

def create_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('students')
    else:
        form = StudentForm()
    return render(request, 'student/create_student.html', {'form': form})


def update_student(request, id):
    student = get_object_or_404(Student, pk=id)
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student/create_student.html', {'form': form, 'student': student})

def student_delete(request, id):
    student = get_object_or_404(Student, pk=id)
    student.delete()
    return redirect('students')
