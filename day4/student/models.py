from django.db import models
from course.models import Course

class Student(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='student/' , null = True , blank=True)
    date_of_birth = models.DateField()
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.name
    