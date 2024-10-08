from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from .forms import UserUpdateForm
from django.contrib.auth.decorators import login_required
from .models import Commissionaire
from back.models import Formation, Emploi, Achat
from django.contrib.auth import get_user_model


User = get_user_model()


def Register(request):
    template_name = 'accounts/register.html'
    if request.method == "POST":
        form = UserUpdateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            messages.error(request, "Données incorrectes! Réessayez")
            form = UserUpdateForm()
            context = {
                'form': form,
            }
            return render(request, template_name, context)
    form = UserUpdateForm()
    context = {
        'form': form,
    }
    return render(request, template_name, context)


def Login(request):
    username_email = request.POST.get('username_email')
    password = request.POST.get('password')
    if request.method=='POST':
        if(User.objects.filter(username=username_email).exists()):
            user = authenticate(username=username_email, password=password)
        elif(User.objects.filter(email=username_email).exists()):
            user = User.objects.get(email=username_email)
            user = authenticate(username=user.username, password=password)
        else:
            messages.error(request, "Données incorrects! Réessayez")
            return redirect('home:home')
        if user is not None:
            login(request, user)
            return redirect('home:home')
        else:
            messages.error(request, "Mot de passe incorrects! Réessayez")
            return redirect('home:home')
    else:
        return render(request, 'home/index.html')


@login_required
def Logout(request):
    logout(request)
    return redirect('home:home')


@login_required
def Profile(request, username):
    user = get_object_or_404(User, username=username)
    comms = Commissionaire.objects.all()
    is_comm = False
    for item in comms:
        if item.user == request.user:
            is_comm = True
    context = {
        'user': user,
        'comms': comms,
        'is_comm': is_comm,
    }
    return render(request, 'accounts/profile.html', context)


@login_required
def UpdateProfile(request, username):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('accounts:profile', args=[username]))
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'accounts/update_profile.html', {'form': form})
    

@login_required
def MesFormations(request):
    current_user = request.user
    formations = current_user.formation_set.all()
    template_name = 'accounts/formations.html'
    context = {
        'formations': formations,
    }
    return render(request, template_name, context)


@login_required
def MesCommandes(request):
    current_user = request.user
    commandes = Achat.objects.filter(user=current_user, livraison='en cours')
    template_name = 'accounts/commandes.html'
    context = {
        'commandes': commandes,
    }
    return render(request, template_name, context)


@login_required
def MesCommissions(request):
    current_user = request.user
    commissions = Commissionaire.objects.filter(user=current_user)
    template_name = 'accounts/commissions.html'
    context = {
        'commissions': commissions,
    }
    return render(request, template_name, context)
    