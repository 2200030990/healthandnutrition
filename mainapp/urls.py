from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path("", myfunction, name='main'),
    path("about/", myabout, name='about'),
    path("login_view/about/", myabout1, name='about1'),
    path("login/", mylogin, name='login'),
    path("registaration/", myregistration, name='reg'),
    path("contact/", mycontact, name='contact'),
    path("login_view/contact1/", mycontact1, name='contact1'),
    path("adminhome/", adminhome, name='adminpage'),
    path("userhome/", userhome, name='homepage'),
    path("registration_view/", registration_view, name='registration_view'),
    path('registration/', views.registration_view, name='registration'),
    path("login_view/", login_view, name='login_view'),
    path('logout/', logout_view, name='logout'),
    path("login_view/nutrition/", show_nutrition, name='show_nutrition'),
    path("login_view/fitness/", show_fitness, name='show_fitness'),
    path("login_view/meditation/", show_meditation, name='show_mediation'),








 ]