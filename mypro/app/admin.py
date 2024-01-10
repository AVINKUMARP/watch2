from django.contrib import admin

from .models import Watch
from .models import Userlog

admin.site.register(Watch)
# Register your models here.
admin.site.register(Userlog)
