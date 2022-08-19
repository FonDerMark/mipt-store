from django.contrib import admin
from app.models import Notebook, Smartphone, TV, Cleaners, ToCard

# Register your models here.
admin.site.register(Notebook)
admin.site.register(Smartphone)
admin.site.register(TV)
admin.site.register(Cleaners)
admin.site.register(ToCard)