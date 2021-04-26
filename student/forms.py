from django import forms
from student.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'textarea']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'textarea' : forms.Textarea(attrs={'class':'form-control', 'rows':3, 'cols':5}),
        }