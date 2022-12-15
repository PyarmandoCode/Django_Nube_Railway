from django.shortcuts import render
from .models import Departamentos


def index(request):
    template_name = "index.html"
    departamentos = Departamentos.objects.all()
    context = {
        "dep": departamentos
    }
    return render(request, template_name, context)
