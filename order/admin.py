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

    # readonly_fields = ["user","date","supplier","display_order_product","takeout","total_price"]

    def account_actions(self, obj):
        # import pdb; pdb.set_trace()

        return format_html(
            '<a class="button" href="{}">제품 완료</a>&nbsp;'
            '<a class="button" href="{}">취소</a>&nbsp;'
            ,
            reverse('admin:change-to-ready', args=[obj.pk]),
            reverse('admin:change-to-paid', args=[obj.pk])
        )
    account_actions.short_description = 'Account Actions'
    account_actions.allow_tags = True

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                '<order_id>/change_to_ready/',
                self.admin_site.admin_view(self.change_to_ready),
                name='change-to-ready',
            ),
            path(
                '<order_id>/change_to_paid/',
                self.admin_site.admin_view(self.change_to_paid),
                name='change-to-paid',
            ),
        ]
        return custom_urls + urls

    def change_to_ready(self, request, *args, **kwargs):

        Order.objects.filter(id=kwargs["order_id"]).update(status='PRODUCT_READY')
        return super(OrderAdmin, self).changelist_view(request)


    def change_to_paid(self, request, *args, **kwargs):

        Order.objects.filter(id=kwargs["order_id"]).update(status='PAID')
        return super(OrderAdmin, self).changelist_view(request)


    def get_queryset(self, request):
        qs = super(OrderAdmin, self).get_queryset(request)

        if request.user.is_superuser:
            return qs

        # import ipdb;
        # ipdb.set_trace();

        # if request.user.owner.exists():
        #     supplier = request.user.owner.all()
        #     return qs.filter(supplier__in=supplier)
        #
        # if request.user.manager.exists():
        #     supplier = request.user.manager.all()
        #     return qs.filter(supplier__in=supplier)


        return qs.filter(supplier__in=request.user.owner.all()|request.user.manager.all())

