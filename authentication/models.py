from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    CREATOR = 'ADMIN'
    SUBSCRIBER = 'UTILISATEUR'

    ROLE_CHOICES = (
        (CREATOR, 'Admin'),
        (SUBSCRIBER, 'Utilisateur'),
    )

    profile_photo = models.ImageField(verbose_name='photo de profil')
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Rôle')

   