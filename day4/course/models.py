from django.db import models

class Course(models.Model):
    code = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name