import django_filters
from .models import IHA, Kiralama

# IHA modeli için filtreleme işlemi
class IHAFilter(django_filters.FilterSet):
    class Meta:
        model = IHA
        fields = ['marka', 'model', 'agirlik', 'kategori']
        # IHA modeli için filtrelemek istediğimiz alanları belirtiyoruz.
        # Kullanıcılara "marka", "model", "agirlik" ve "kategori" alanlarını filtreleme seçenekleri olarak sunacağız.

# Kiralama modeli için filtreleme işlemi
class KiralamaFilter(django_filters.FilterSet):
    class Meta:
        model = Kiralama
        fields = ['iha__marka', 'tarih_ve_saat_araliklari', 'teslim_tarihi', 'kiralayan_uye']
        # Kiralama modeli için filtrelemek istediğimiz alanları belirtiyoruz.
        # Kullanıcılara "iha__marka", "tarih_ve_saat_araliklari", "teslim_tarihi" ve "kiralayan_uye" alanlarını filtreleme seçenekleri olarak sunacağız.
        # "iha__marka" alanı, Kiralama nesnesine bağlı IHA nesnesinin marka alanıdır ve "iha__" ile belirtilmiştir.
        # Bu şekilde ForeignKey ile bağlı alanları filtrelemek için "__" kullanılır.
