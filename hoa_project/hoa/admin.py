from hoa.models import Agreement, Hoa, Address, Payment
from django.contrib import admin
from nested_inlines.admin import NestedModelAdmin, NestedTabularInline


class AddressInline(NestedTabularInline):
    model = Address
    extra = 0


class AgreementAdmin(NestedModelAdmin):
    list_display = ['number', 'ammount', 'date_start', 'comment', 'date_end']
    inlines = [AddressInline]


class AgreementInline(NestedTabularInline):
    model = Agreement
    can_delete = False
    extra = 0
    inlines = [AddressInline]


class HoaAdmin(NestedModelAdmin):
    list_display = ['name', 'location', 'phone', 'contact']
    inlines = [AgreementInline]


class PaymentAdmin(admin.ModelAdmin):
    list_display = ['agreement', 'ammount', 'date', 'period_start',
                    'period_end', 'comment']


admin.site.register(Hoa, HoaAdmin)
admin.site.register(Agreement, AgreementAdmin)
admin.site.register(Address)
admin.site.register(Payment, PaymentAdmin)
