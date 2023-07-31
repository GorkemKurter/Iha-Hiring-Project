from django.db import models

class IHA(models.Model):
    marka = models.CharField(max_length=100)  # IHA'nın markası, en fazla 100 karakter uzunluğunda bir metin alanıdır.
    model = models.CharField(max_length=100)  # IHA'nın modeli, en fazla 100 karakter uzunluğunda bir metin alanıdır.
    agirlik = models.FloatField()  # IHA'nın ağırlığı, ondalık sayıları tutan bir alan.
    kategori = models.CharField(max_length=100)  # IHA'nın kategorisi, en fazla 100 karakter uzunluğunda bir metin alanıdır.

    def __str__(self):
        return f"{self.marka} {self.model}"  # IHA nesnesi bir stringe dönüştürüldüğünde döndürülecek değeri belirler.

class Kiralama(models.Model):
    iha = models.ForeignKey(IHA, on_delete=models.CASCADE)  # Kiralamanın hangi IHA'ya ait olduğu, ForeignKey kullanılarak belirtilir.
    tarih_ve_saat_araliklari = models.DateField()  # Kiralama için tarih ve saat aralıklarını tutan bir alan.
    kiralayan_uye = models.CharField(max_length=100)  # Kiralayan kullanıcının adını tutan bir metin alanı (en fazla 100 karakter).
    teslim_tarihi = models.DateField()  # Kiralama için teslim tarihini tutan bir alan.

    def __str__(self):
        return f"{self.iha} - {self.tarih_ve_saat_araliklari} - {self.kiralayan_uye}"  # Kiralama nesnesi bir stringe dönüştürüldüğünde döndürülecek değeri belirler.
