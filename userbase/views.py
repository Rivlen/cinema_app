from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .forms import MemberRegistrationForm


class MemberSignUpView(generic.CreateView):
    form_class = MemberRegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'
