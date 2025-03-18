from django.contrib import admin
from .models import *

# @admin.register(Utilisateur)
# class UtilisateurAdmin(admin.ModelAdmin):
#     list_display = ('user', 'role', 'date_inscription')

# @admin.register(Metier)
# class MetierAdmin(admin.ModelAdmin):
#     list_display = ('nom', 'desciption',)

# @admin.register(Ton)
# class TonAdmin(admin.ModelAdmin):
#     list_display = ('nom',)

# @admin.register(Entreprise)
# class EntrepriseAdmin(admin.ModelAdmin):
#     list_display = ('nom',)

# @admin.register(Profils)
# class ProfilsAdmin(admin.ModelAdmin):
#     list_display = ('utilisateur', 'metier_vise', 'type_entreprise', 'preference_ton')

# @admin.register(SessionChat)
# class SessionChatAdmin(admin.ModelAdmin):
#     list_display = ('utilisateur', 'coach', 'date_heur_session', 'Transciption', 'type_session', 'feedback')

# @admin.register(ReglageChatBot)
# class ReglageChatBotAdmin(admin.ModelAdmin):
#     list_display = ('ton', 'metier', 'type_entreprise',)
