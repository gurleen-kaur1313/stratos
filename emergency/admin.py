from django.contrib import admin
from .models import HealthEmergency,HealthTest,Announcement

admin.site.register(HealthEmergency)
admin.site.register(HealthTest)
admin.site.register(Announcement)