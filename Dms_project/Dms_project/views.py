from django.shortcuts import render

def home(request):
    return render(request,"home.html")

def team(request):
    return render(request,"team.html")
def services(request):
    return render(request,"services.html")

def contactus(request):
    return render(request,"contactus.html")