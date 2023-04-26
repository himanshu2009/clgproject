from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse
from .models import Subject,Student
from .forms import SubjectAddition
from django.http import HttpResponseRedirect, HttpResponse
import json
import os



# Create your views here.


# def index(request):
#   mymembers = Subject.objects.all().values()
#   template = loader.get_template('enroll/index.html')
#   context = {
#     'mymembers': mymembers
#   }
#   return HttpResponse(template.render(context, request))

# def add(request):
#   template = loader.get_template('enroll/add.html')
#   return HttpResponse(template.render({}, request))


# def addrecord(request):
#   x = request.POST['subname']
#   y = request.POST['subcode']
#   z=request.POST['credit']
#   member = Subject(subname=x, subcode=y,credit=z)
#   member.save()
#   return HttpResponseRedirect(reverse('index'))

# this funtion add and show data


# def add_show(request):
#     # m=""

#     if request.method == 'POST':

#         # creating  a object of class subjectaddition
#         fm = SubjectAddition(request.POST)
#         if fm.is_valid():
#             fm.save()
#             fm = SubjectAddition()

#     else:
#         fm = SubjectAddition()
#     stud = Subject.objects.all()  # get all the data

    # subname=request.POST.get('subname')
    # subcode=request.POST.get('subcode')
    # credit=request.POST.get('credit')
    # fm=Subject(subname=subname,subcode=subcode,credit=credit)

    #     fm.save()
    #     m="data inserted suceessfully"
    # else:
    #      fm=""
    # stud=Subject.objects.all()
    # return render(request, 'enroll/addandshow.html', {'form': fm, 'stu': stud})


# this function will update and delete subject


def update(request, id):
    mymember = Subject.objects.get(id=id)
    template = loader.get_template('updatesubject.html')
    context = {
        'mymember': mymember,
    }

    return HttpResponse(template.render(context, request))

# def updaterecord(request,id):
#     subname=request.POST['subname']
#     subcode=request.POST['subcode']
#     credit=request.POST['credit']
#     member=Subject.objects.get(id=id)
#     member.subname=subname
#     member.subcode=subcode
#     member.credit=credit
#     member.save()
#     return HttpResponseRedirect(reverse(''))


def update_data(request, id):

    if request.method == 'POST':
        pi = Subject.objects.get(pk=id)
        # collection of whole data of specific id or you can use of cleandata to save one field by one field
        fm = SubjectAddition(request.POST, instance=pi)

        if fm.is_valid():
            fm.save()
    else:
        pi = Subject.objects.get(pk=id)
        fm = SubjectAddition(instance=pi)

    return render(request, 'enroll/updatesubject.html', {'form': fm})


# this function will delete subject
# here we use dyanamic url
def delete_data(request, id):
    if request.method == 'POST':
        pi = Subject.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')


# def show_details(request, my_id):
#     return render(request, 'enroll/app.html', {'id': my_id})


def picksub(request, data):
    # department = get_object_or_404(Subject, name=departmentName)
    # records = Subject.objects.filter(department=department)
    # context = {'records': records}
    # return render(request, 'department_records.html', context)
   
    # if data == 'Chemical Engineering':
        subject = Subject.objects.filter(departmentName=data)
        # return render(request, 'enroll/student.html', {'subject': subject})
    # elif data == 'ComputerScience and Engineering':
        #  subject = Subject.objects.filter(departmentName='ComputerScience and Engineering')
        
    # elif data == 'nodpt':
        # subject = Subject.objects.filter(departmentName='nodpt')
        return render(request, 'enroll/student.html', {'subject': subject})


def picksem(request,d):
    semester=Subject.objects.filter(semesterNo=d)

    return render(request,'enroll/studentsubject.html',{'semester':semester})




def display_subjects(request):

    # Get the absolute path to the JSON file
    json_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'subjects.json')

    # Load the JSON data
    with open(json_path) as f:
        data = json.load(f)

    # Create a list of dictionaries containing the semester and its subjects
    semesters = [{'name': semester, 'subjects': data[semester]} for semester in data]

    # Render the HTML template with the semester-wise subjects
    return render(request, 'enroll/subjects.html', {'semesters': semesters})



from django.shortcuts import render
from .forms import StudentForm

def student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # Process the form data
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            semester = form.cleaned_data['semester']
            subjects = form.cleaned_data['subjects']
            # ...
            # Here you can process the form data and save it to the database or perform any other action needed.
            er=Student(first_name=first_name,last_name=last_name,email=email,semester=semester,subjects=subjects)
            er.save()
    else:
        form = StudentForm()
    return render(request, 'enroll/student_form.html', {'form': form})



