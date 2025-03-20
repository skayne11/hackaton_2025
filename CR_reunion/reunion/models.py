from django.db import models
from django.utils import timezone


class Reunion(models.Model):
    titre = models.CharField(max_length=255)
    date = models.DateTimeField()
    participants = models.TextField()
    fichier_retranscription = models.FileField(upload_to='retranscriptions/', blank=True, null=True)

    def __str__(self):
        return self.titre