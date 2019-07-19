from django.contrib import admin
from .models import Order,OrderProduct

class OrderProductInLine(admin.TabularInline):
    model = OrderProduct
    extra = 0
 
 
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
 
    inlines = [
        OrderProductInLine
    ]
    
    list_display = ["date","supplier","user","status", "display_order_product","takeout"]

    # readonly_fields = ["total_price"]


