from django.shortcuts import render
from .models import Fiche

# Create your views here.


def list_fiche(request):

    sort = request.GET.get('sort')
    if sort == "client":
        fiches = Fiche.objects.all().order_by('client__name')
    elif sort == "project_title":
        fiches = Fiche.objects.all().order_by('project_title')

    context = {
        "fiches": fiches
    }
    return render(request, 'home.html', context=context)
