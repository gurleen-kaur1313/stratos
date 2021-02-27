from django.db import models
from django.conf import settings
import uuid

class HealthEmergency(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)
    problem = models.TextField(help_text="Problem : ")
    locality = models.CharField(null=True,blank=True,max_length=250)
    city = models.CharField(null=True,blank=True,max_length=250)
    state = models.CharField(null=True,blank=True,max_length=250)
    date = models.CharField(null=True,blank=True, max_length=250)

    def __str__(self):
        return self.user.email

    def save(self, *args, **kwargs):
        super(HealthEmergency, self).save(*args, **kwargs)