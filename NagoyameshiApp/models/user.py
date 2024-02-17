from django.db import models

class User(models.Model):
    USERNAME_FIELD = "username"
    username = models.CharField(max_length=50, default='')
    password1 = models.CharField(max_length=20, default='')
    password2 = models.CharField(max_length=20, default='')
    
    class Meta:
        app_label = 'NagoyameshiApp'

