from django import forms

from .models import Student

class StudentForm(forms.ModelForm):
    class meta:
        model=Student
        fields=['first_name', 'last_name', 'age','grade','school','percentage']