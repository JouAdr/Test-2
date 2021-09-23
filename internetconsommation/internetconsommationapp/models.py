from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class InternetConsumption(models.Model):

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    consumption_date = models.DateTimeField(auto_now_add=True)
    upload = models.FloatField()
    download = models.FloatField()