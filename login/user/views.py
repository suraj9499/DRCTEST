from django.shortcuts import render
from . form import *
from django.views.generic.edit import FormView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.conf import settings
from django.views.generic import ListView

class RegisterFormView(CreateView):
  template_name = 'Register.html'
  form_class = Reg_Form
  success_url = '/register/'

class Home(CreateView):
  template_name = 'file_upload.html'
  form_class = File_upload_form
  success_url = '/home/'

class File_list(ListView):
    model = File_upload
    context_object_name = 'Files'
    # def get_context_data(self, **kwargs):
    #   ctx = super(File_list, self).get_context_data(**kwargs)
    #   # ctx['fields'] = [field for field in File_upload._meta.get_fields()]
    #   return ctx