from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from oscar.core.loading import get_model

Partner = get_model('partner', 'Partner')
StockRecord = get_model('partner', 'StockRecord')
StockAlert = get_model('partner', 'StockAlert')


class PartnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'list_users']

    def list_users(self, obj):
        return ', '.join([a.username for a in obj.users.all()])

    list_users.short_description = _('Users')
    list_users.allow_tags = True


class StockRecordAdmin(admin.ModelAdmin):
    list_display = ['product', 'partner', 'partner_sku', 'price_excl_tax',
                    'cost_price', 'num_in_stock']
    list_filter = ['partner', 'product']


class StockAlertAdmin(admin.ModelAdmin):
    list_display = ['stockrecord', 'threshold', 'status', 'date_created', 'date_closed']
    list_filter = ['threshold', 'status']


admin.site.register(Partner, PartnerAdmin)
admin.site.register(StockRecord, StockRecordAdmin)
admin.site.register(StockAlert, StockAlertAdmin)

