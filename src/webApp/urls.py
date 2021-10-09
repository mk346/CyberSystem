from django.urls import path
from .import views


urlpatterns = [
    path('',views.home,name='home'),
    path('form',views.form,name='form'),
    path('registration',views.registration,name='registration'),
    path('change',views.change,name='change'),
    path('application',views.application,name='application'),
    path('other',views.other,name='other'),
    path('contact',views.contact,name='contact'),

]
