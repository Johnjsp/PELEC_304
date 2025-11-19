from django.shortcuts import render
from .forms import EducationalBackgroundforms

def input_educbackground (request):
    if request.method == 'POST':
        form = EducationalBackgroundforms(request.POST)
        if form.is_valid():
            form.save()
            return render ('success')
    else:
        form = EducationalBackgroundforms()
    return render (request,'educ_background/forms.html'),{'forms':form}

def success (request):
    return render (request,'educ_background/success.html')
        

# Create your views here.
