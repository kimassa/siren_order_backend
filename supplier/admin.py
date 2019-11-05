from django.contrib import admin
from .models import Supplier


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    search_fields = ["branch"]
    list_display = ["branch","owner","manager", "products_count"]


