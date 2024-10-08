from django.shortcuts import render
from accounts.models import CustomUser
from back.models import Subject, Formation, Domaine, Emploi, Achat
# from back.models import Subject, Formation, Domaine, Emploi
from django.contrib.auth import get_user_model

User = get_user_model()

def Dashboard(request):
    users = User.objects.all()
    subjects = Subject.objects.all()
    formations = Formation.objects.all()
    domaines = Domaine.objects.all()
    emplois = Emploi.objects.all()
    commandes = Achat.objects.all()
    template_name = 'back/dashboard.html'
    context = {
        'users': users.count(),
        'subjects': subjects.count(),
        'formations': formations.count(),
        'domaines': domaines.count(),
        'emplois': emplois.count(),
        'commandes': commandes.count(),
    }
    return render(request, template_name, context)


def Users(request):
    users = User.objects.all().order_by('id')
    template_name = 'back/users.html'
    context = {
        'users': users,
    }
    return render(request, template_name, context)


def Formations(request):
    subjects = Subject.objects.all().order_by('id')
    formations = Formation.objects.all().order_by('id')
    template_name = 'back/formations.html'
    context = {
        'subjects': subjects,
        'formations': formations,
    }
    return render(request, template_name, context)


def Commandes(request):
    commandes = Achat.objects.all().order_by('id')
    template_name = 'back/commandes.html'
    context = {
        'commandes': commandes,
    }
    return render(request, template_name, context)


def Emplois(request):
    emplois = Emploi.objects.all().order_by('id')
    template_name = 'back/emplois.html'
    context = {
        'emplois': emplois,
    }
    return render(request, template_name, context)


def Formulaires(request):
    template_name = 'back/formulaires.html'
    return render(request, template_name)
