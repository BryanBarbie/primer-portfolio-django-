from django.shortcuts import render
from .models import Project

# Create your views here.
def portfolio(request):
    #traigo todos los datos de la base de datos para el apartado de proyectos
    projects = Project.objects.all()
    return render(request, 'portafolio/portfolio.html', {'projects':projects})
