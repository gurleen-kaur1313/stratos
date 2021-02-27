from django.contrib import admin
from .models import HealthEmergency,HealthTest

admin.site.register(HealthEmergency)
admin.site.register(HealthTest)
