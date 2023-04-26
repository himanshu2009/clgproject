from django.db import models

# Create your models here.










CATEGORY_CHOICES = (
 ('BCS', 'ComputerScience and Engineering '),
 ('BIT', 'Information Technology'),
 ('BET', 'Electronics and Telecommunication  Engineering'),
 ('BEC', 'Electrical Engineering'),
 ('BIN', ' Instrumentation Engineering'),
 ('BME', 'Mechanical Engineering'),
 ('BCV', 'Civil Engineering'),
 ('BPR', 'Production Engineering'),
 ('BCH', 'Chemical Engineering'),
 ('BTX', 'Textile Engineering'),
)

# modelform
class Subject(models.Model):
    subname=models.CharField(max_length=50)
    subcode=models.CharField(max_length=100)
    credit=models.IntegerField()
    semesterNo=models.IntegerField(default=0)
    departmentName=models.CharField(max_length=100,null=False,default='nodept',choices=CATEGORY_CHOICES)






class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    semester = models.IntegerField()
    subjects = models.JSONField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



