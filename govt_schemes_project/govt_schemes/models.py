from django.db import models

class Schema(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    eligibility_criteria=models.TextField()
    application_process=models.TextField()
    deadline=models.DateTimeField(auto_now_add=True)
