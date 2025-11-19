from django.urls import path
from . import views

urlpatterns = [
    path('student_profile/', views.student_profile, name = "Student Profile"),
    path('student_list/', views.student_list, name = "Student List"),
    path('fbv/', views.hello_world, name = "function-bases"),
    path('cbv/', views.helloWorldView.as_view(), name = "Class-based"),

]