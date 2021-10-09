from django.contrib import admin
from .models import details,ChangeDet,Apply,Rest,Register

# Register your models here.
admin.site.register(details)
admin.site.register(Register)
admin.site.register(ChangeDet)
admin.site.register(Apply)
admin.site.register(Rest)
