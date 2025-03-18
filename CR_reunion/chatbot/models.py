from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# class Utilisateur(models.Model):

#     choices=[
#         ('candidat', 'Candidat'), 
#         ('coach', 'Coach'), 
#     ]

#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
#     role = models.CharField(max_length=20, choices=choices)
#     date_inscription = models.DateField(default=timezone.now)

#     def __str__(self) -> str:
#         return f"{self.user.first_name} {self.user.last_name}"

# class Metier(models.Model):

#     nom = models.CharField(max_length=50)
#     desciption = models.CharField(max_length=200)

#     def __str__(self) -> str:
#         return self.nom

# class Ton(models.Model):

#     nom = models.CharField(max_length=10)

#     def __str__(self) -> str:
#         return self.nom

# class Entreprise(models.Model):

#     nom = models.CharField(max_length=50)

#     def __str__(self) -> str:
#         return self.nom

# class Profils(models.Model):

#     utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='user_profil')
#     metier_vise = models.ForeignKey(Metier, on_delete=models.CASCADE, related_name='metier_profil')
#     type_entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE, related_name='type_entreprise')
#     preference_ton = models.ForeignKey(Ton, on_delete=models.CASCADE, related_name='preference_ton')

# class SessionChat(models.Model):

#     utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='user_session')
#     coach = models.ForeignKey(Utilisateur, null=True, blank=True, on_delete=models.SET_NULL, related_name='coach_sessions', limit_choices_to={'role': 'coach'})
#     date_heur_session = models.DateTimeField()
#     Transciption = models.CharField(max_length=100)
#     type_session = models.ForeignKey(Ton, on_delete=models.CASCADE, related_name='ton_session')
#     feedback = models.CharField(max_length=500)

# class ReglageChatBot(models.Model):
#     ton = models.ForeignKey(Ton, on_delete=models.CASCADE, related_name='ton_chatbot')
#     metier = models.ForeignKey(Metier, on_delete=models.CASCADE, related_name='metier_chatbot')
#     type_entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE, related_name='entreprise_chatbot')