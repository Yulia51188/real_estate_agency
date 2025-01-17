from django.contrib import admin

from .models import Appeal
from .models import Flat
from .models import Owner


class OwnersInline(admin.TabularInline):
    model = Flat.owners.through
    raw_id_fields = ['owner']


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'town_district', 'address']
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'new_building', 'construction_year', 
        'town']
    list_editable = ['new_building']
    list_filter = ['new_building']
    raw_id_fields = ['liked_by']
    inlines = [OwnersInline]


class AppealAdmin(admin.ModelAdmin):
    raw_id_fields = ['flat', 'user']


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ['flats']
    search_fields = ['full_name']
    list_display = ['full_name', 'phonenumber', 'pure_phone']


admin.site.register(Flat, FlatAdmin) 
admin.site.register(Appeal, AppealAdmin) 
admin.site.register(Owner, OwnerAdmin)
