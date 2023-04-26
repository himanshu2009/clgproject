from django.contrib import admin

from myapp.models import Student, Markss, Subjects, Department, Semester

# Register your models here.


class StudentAdmin(admin.ModelAdmin):

    list_display = ('id', 'Name', 'RegNo', 'Year_of_Joining', 'Email',
                    'Phone_Number', 'Passing_year', 'Address', 'No_of_Transcript_R')


admin.site.register(Student, StudentAdmin)


class MarkssAdmin(admin.ModelAdmin):
    list_display = ('sem1', 'sem2', 'sem3', 'sem4',
                    'sem5', 'sem6', 'sem7', 'sem8')


admin.site.register(Markss, MarkssAdmin)


admin.site.register(Subjects)
admin.site.register(Department)
admin.site.register(Semester)
