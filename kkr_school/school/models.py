from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age=models.IntegerField()
    grade=models.CharField(max_length=2)
    school_name=models.CharField(max_length=100)
    percentage=models.DecimalField(max_digits=2,decimal_places=2)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"