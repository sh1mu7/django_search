import datetime
from django import forms

from test1.models import Posts


class StudentForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = '__all__'

