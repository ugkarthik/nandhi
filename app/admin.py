from django.contrib import admin

# Register your models here.

from .models import Membership, Contact

admin.site.register(Membership)
admin.site.register(Contact)