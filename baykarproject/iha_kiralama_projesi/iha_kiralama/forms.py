from django import forms
from .models import Kiralama,IHA

class KiralamaFilterForm(forms.ModelForm):
    class Meta:
        model = Kiralama
        fields = ['tarih_ve_saat_araliklari', 'kiralayan_uye', 'iha']
        widgets = {
            'tarih': forms.DateInput(attrs={'type': 'date'}),
            
        }


class IHAForm(forms.ModelForm):
    class Meta:
        model = IHA
        fields = '__all__'

class KiralamaForm(forms.ModelForm):
    class Meta:
        model = Kiralama
        fields = '__all__'

