from django.shortcuts import render

def Test_counseling (request):
    services = [
        {"name":"Counseling","description":"Providing emotional and psychological support."},
        {"name":"Outreach","description":"Engaging with communities with activities."},
        {"name":"Education Support","description":"Helping students with learning resources."},
        {"name":"Health Assistance","description":"Promoting health and wellness programs."},
        {"name":"Volunteer program","description":"Organizing volunteers for social services."},
    ]
    return render(request,'services/templates.html',{'services': services})
           