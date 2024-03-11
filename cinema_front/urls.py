from django.urls import path
from cinema_front.views import LandingPageView, CurrentCinemaRepertoire

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing-page'),
    path('', CurrentCinemaRepertoire.as_view(), name='current-cinema-repertoire'),
]
