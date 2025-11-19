from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


def hello_world (request):
    return HttpResponse("HELLO FROM FUNCTION-BASED! " )

class helloWorldView(View):
    def get (self,request):
        return HttpResponse("HELLO FROM CLASS-BASED VIEW !")
    
def student_profile (request):
   student = [
       {"name":"Coedy Dela Cruz", "age":20, "course":"BSIT"},
       {"name":"Nerjie Dela Cruz", "age":20, "course":"BSIT"},
       {"name":"John Dela Cruz", "age":20, "course":"BSIT"},
       {"name":"Ralph Dela Cruz", "age":20, "course":"BSIT"},
   ]
   return render(request, "student_profile.html", {"student":student})

def student_list(request):
    students = [
        {"name": "Coedy", "age": 32},
        {"name": "Nerjie", "age": 32},
        {"name": "Ralph", "age": 32},
    ]
    return render(request, 'student_list.html', {"students": students})
# Create your views here.
