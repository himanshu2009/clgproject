from django import forms

from .models import Subject

import json
import os






class SubjectAddition(forms.ModelForm):
 class Meta:
  model=Subject

  fields=['subname','subcode','credit','semesterNo','departmentName']

  widgets={
   'subname':forms.TextInput(),
   'subcode':forms.TextInput(),
   'credit':forms.NumberInput(),
   'semesterNo':forms.NumberInput(),
   'departmentName':forms.TextInput(),

  }








class StudentForm(forms.Form):
    # Basic details
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    
    # Academic details
    semester = forms.ChoiceField(choices=[(1, 'Semester 1'), (2, 'Semester 2'), (3, 'Semester 3'), (4, 'Semester 4')])
    subjects = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, required=False)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Load the subjects data from the JSON file
        # json_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'sub.json')
        json_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'sub.json')

        with open(json_path) as f:
            subjects_data = json.load(f)
            
        # Set the choices for the subjects field based on the selected semester
        semester_choices = self.fields['semester'].choices
        selected_semester = int(self['semester'].value())
        selected_semester_name = dict(semester_choices)[selected_semester]
        self.fields['subjects'].choices = [(subject, subject) for subject in subjects_data[selected_semester_name]]


