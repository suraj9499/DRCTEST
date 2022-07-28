

from dataclasses import fields
from django import forms
from .models import *


class Reg_Form(forms.ModelForm):
  class Meta:
    model=My_User
    fields='__all__'


class login_Form(forms.ModelForm):
  class Meta:
    model=My_User
    fields=['phone','password'] 

class File_upload_form(forms.ModelForm):
  class Meta:
    model=File_upload
    fields='__all__'
