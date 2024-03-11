from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from cinema_front.models import Movie


class LandingPageView(View):
    def get(self, request):
        return render(request, 'landing-page.html')


class CurrentCinemaRepertoire(ListView):
    model = Movie

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["now"] = timezone.now()
    #     return context
