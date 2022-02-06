from django import forms
from .models import Intake
class Traineeinsert(forms.Form):
    username = forms.CharField(label='username',max_length=100)
    email = forms.EmailField(label='email', max_length=100)
    password = forms.CharField(label='password', max_length=100)



class Traineeinsert1(forms.ModelForm):

   class Meta:
       fields='__all__'
       model=Intake

