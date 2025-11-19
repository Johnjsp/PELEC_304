from django.urls import path
from . import views

urlpatterns =[
    path('',views.input_educbackground,name='educ_background_form'),
    path('success/',views.success,name='success')

    ]