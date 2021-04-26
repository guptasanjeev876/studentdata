from django.shortcuts import render
from student.forms import StudentForm
from student.models import Student
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.
def homepage(request):
    if request.method =="POST":
        wd = StudentForm(request.POST, True)
        if wd.is_valid():
            wd.save()
            return HttpResponseRedirect( '/formsub/')
        
    else:
        wd=StudentForm()
    student = Student.objects.all()        
    return render(request, 'student/home.html', {"stu":wd, "stud": student} )

def formsubmitted(request):
    wordtx = Student.objects.all()
    return render(request, "student/success.html", {'word':wordtx})

def delete_data(request,id):
    if request.method == "POST":
        delstu = Student.objects.get(pk=id)
        delstu.delete()
    return render(request, "student/delete.html", )