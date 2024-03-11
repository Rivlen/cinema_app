from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy


class MemberSignUpView(generic.CreateView):
    template_name = 'register.html'
