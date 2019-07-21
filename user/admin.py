from django.contrib import admin

from .models import User, UserFrequency


admin.site.register(User)
admin.site.register(UserFrequency)