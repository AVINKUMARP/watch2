from django.contrib import admin

from .models import Watch

from .models import CartItem
admin.site.register(Watch)
# Register your models here.

admin.site.register(CartItem)