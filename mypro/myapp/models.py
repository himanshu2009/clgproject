from django.db import models

# Create your models here.


class Student(models.Model):
    Name = models.CharField(max_length=40,default=True,null=True)
    RegNo = models.CharField(max_length=40,default=True,null=True)
    Year_of_Joining = models.DateField(max_length=40,default=True,null=True)
    Passing_year = models.DateField(null=True)
    Email = models.EmailField(default=True,null=True)
    Phone_Number = models.IntegerField(default=True,null=True)
    Address = models.TextField(max_length=120,default=True,null=True)
    No_of_Transcript_R = models.IntegerField(default=True,null=True)

class Markss(models.Model):
    sem1 = models.IntegerField(default=True,null=True)
    sem2 = models.IntegerField(default=True,null=True)
    sem3 = models.IntegerField(default=True,null=True)
    sem4 = models.IntegerField(default=True,null=True)
    sem5 = models.IntegerField(default=True,null=True)
    sem6 = models.IntegerField(default=True,null=True)
    sem7 = models.IntegerField(default=True,null=True)
    sem8 = models.IntegerField(default=True,null=True)


class Department(models.Model):
    departmentName = models.CharField(max_length=40)
    departmentId = models.CharField(max_length=40)


class Semester(models.Model):
    semesterNo = models.IntegerField()
    semesterId = models.IntegerField()


class Subjects(models.Model):
    subjecttName = models.CharField(max_length=40)
    departmentId = models.CharField(max_length=40)
    semesterId = models.IntegerField()
    departmentId = models.IntegerField()
    subCode=models.CharField(max_length=10,null=False,default='')
    
