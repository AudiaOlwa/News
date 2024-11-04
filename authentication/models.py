from django.contrib.auth.models import AbstractUser, Group
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

    # Ajoutez ces lignes pour résoudre les conflits
    groups = models.ManyToManyField(
        Group,
        verbose_name=('groups'),
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions granted to each of their groups'
        ),
        related_name='custom_user_group'
    )
    user_permissions = models.ManyToManyField(
        Group,
        verbose_name=('user permissions'),
        blank=True,
        help_text=('Specific Permissions for this user.'),
        related_name='custom_user_permission'
    )
