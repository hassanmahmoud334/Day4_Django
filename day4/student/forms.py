from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age','image', 'date_of_birth', 'courses']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }
