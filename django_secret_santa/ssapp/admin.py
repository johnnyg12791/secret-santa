from django.contrib import admin

from .models import Family, Person, Gifts
# Register your models here.
admin.site.register(Family)
admin.site.register(Person)
admin.site.register(Gifts)
