from django.urls import path
from .views import Logout, Register, Login, Profile, UpdateProfile, MesCommandes, MesFormations, MesCommissions

app_name = 'accounts'

urlpatterns = [
    path('login/', Login, name='login'),
    path('register/', Register, name='register'),
    path('logout/', Logout, name='logout'),
    path('profile/<str:username>', Profile, name='profile'),
    path('update_profile/<str:username>', UpdateProfile, name='update_profile'),
    path('commandes/', MesCommandes, name='commandes'),
    path('formations/', MesFormations, name='formations'),
    path('commissions/', MesCommissions, name='commissions'),
]
