from django.contrib import admin

# Register your models here.
from Demo.models import  Region, City, Voie
admin.site.register(Region)
admin.site.register(City)
admin.site.register(Voie)



