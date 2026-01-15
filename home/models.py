# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Ganado(models.Model):

    #__Ganado_FIELDS__
    tag = models.CharField(max_length=255, null=True, blank=True)
    tnombre = models.CharField(max_length=255, null=True, blank=True)
    sexo = models.CharField(max_length=255, null=True, blank=True)
    nacimiento = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Ganado_FIELDS__END

    class Meta:
        verbose_name        = _("Ganado")
        verbose_name_plural = _("Ganado")



#__MODELS__END
