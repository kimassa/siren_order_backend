from django.contrib import admin
from .models import Order,OrderProduct
from django.utils.html import format_html
from django.urls import reverse, path



class OrderProductInLine(admin.TabularInline):
    model = OrderProduct
    extra = 0
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
 
    inlines = [
        OrderProductInLine
    ]
    
    list_display = ["date","status","supplier","user", "display_order_product","total_price","takeout","account_actions"]

    readonly_fields = ["user","date","supplier","display_order_product","takeout","total_price"]

    def account_actions(self, obj):
        # import pdb; pdb.set_trace()

        return format_html(
            '<a class="button" href="{}">준비 완료</a>&nbsp;',
            reverse('admin:change-status', args=[obj.pk])
        )
    account_actions.short_description = 'Account Actions'
    account_actions.allow_tags = True

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                '<order_id>/change_status/',
                self.admin_site.admin_view(self.change_status),
                name='change-status',
            ),
        ]
        return custom_urls + urls

    def change_status(self, request, *args, **kwargs):
        # import pdb; pdb.set_trace()


        Order.objects.filter(id=kwargs["order_id"]).update(status='PRODUCT_READY')


        print("ffefffffffhb")
        return super(OrderAdmin, self).changelist_view(request)

