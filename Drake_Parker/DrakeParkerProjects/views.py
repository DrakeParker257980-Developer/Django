from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'DrakeParkerProjects/Index.html')
# def DrakeForum(request):
#     return render(request, '/Index.html')
# def DrakeChat(request):
#     return render(request, 'IntroOfDrakeParker/Index.html')
# def About(request):
#     return render(request, 'IntroOfDrakeParker/Index.html')
# def Projects(request):
#     return render(request, 'IntroOfDrakeParker/Index.html')
# def Contact(request):
#     return render(request, 'IntroOfDrakeParker/Index.html')
# def Search(request):
#     return render(request, 'IntroOfDrakeParker/Index.html')