from django.contrib import admin
from .models import Address
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin


# @admin.register(Address)
class AddressAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Address)
