# admin.py

from django.contrib import admin
from .models import IHA, Kiralama

class KiralamaAdmin(admin.ModelAdmin):
    list_filter = ("tarih_ve_saat_araliklari", 'kiralayan_uye', 'iha')
    search_fields = ('kiralayan_uye', "tarih_ve_saat_araliklari", 'iha__marka', 'iha__model')

class IHAAdmin(admin.ModelAdmin):
    list_filter = ("marka", 'model', 'agirlik', 'kategori')
    search_fields = ('marka', 'model', 'kategori')

admin.site.register(Kiralama, KiralamaAdmin)
admin.site.register(IHA, IHAAdmin)
