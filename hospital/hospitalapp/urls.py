from django.urls import path

from hospitalapp import views

urlpatterns = [
    path('',views.Home,name='Home'),
    path('about/',views.about,name='about'),
    path('booking/',views.booking,name='booking'),
    path('doctors/',views.doctors,name='doctors'),
    path('contact/',views.contact,name='contact'),
    path('department/',views.department,name='department'),
]
