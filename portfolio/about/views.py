from django.shortcuts import render
from .models import Course, Skill

# Create your views here.

def about(request):
    courses = Course.objects.all()
    skills = Skill.objects.all()
    return render(request, 'about/about.html', {'courses':courses, 'skills':skills})


