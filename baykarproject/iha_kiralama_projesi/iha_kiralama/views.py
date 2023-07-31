from django.shortcuts import render, redirect
from rest_framework import generics
from .models import IHA, Kiralama
from .forms import IHAForm, KiralamaForm
from .serializers import IHASerializer, KiralamaSerializer
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .filters import IHAFilter, KiralamaFilter
from django_filters.views import FilterView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse


# Anasayfa görünümü
def home(request):
    ihalar = IHA.objects.all()
    kiralama = Kiralama.objects.all()
    return render(request, 'home.html', {'ihalar': ihalar, 'kiralama': kiralama})


# Kullanıcı kayıt formu işleme
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


# Kullanıcı giriş formu işleme
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


# Kullanıcı oturum kapatma
@login_required
def user_logout(request):
    logout(request)
    return redirect('login')


# IHA modeli için liste oluşturma ve oluşturma görünümü
class IHAList(generics.ListCreateAPIView):
    queryset = IHA.objects.all()
    serializer_class = IHASerializer


# IHA modeli için detay görünümü
class IHADetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = IHA.objects.all()
    serializer_class = IHASerializer


# Kiralama modeli için liste oluşturma ve oluşturma görünümü
class KiralamaList(generics.ListCreateAPIView):
    queryset = Kiralama.objects.all()
    serializer_class = KiralamaSerializer


# Kiralama modeli için detay görünümü
class KiralamaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kiralama.objects.all()
    serializer_class = KiralamaSerializer


# IHA modeli için ListView
class IHAListView(ListView):
    model = IHA
    template_name = 'iha_list.html'
    context_object_name = 'ihalar'
    paginate_by = 10


# Kiralama modeli için ListView
class KiralamaListView(ListView):
    model = Kiralama
    template_name = 'kiralama_list.html'
    context_object_name = 'kiralamalar'
    paginate_by = 10

    def get_queryset(self):
        return Kiralama.objects.all().values('id', 'iha__marka', 'kiralayan_uye')


# IHA oluşturma görünümü
class IHACreateView(CreateView):
    model = IHA
    form_class = IHAForm
    template_name = 'iha_form.html'

    def get_success_url(self):
        return reverse('iha-ekle')


# Kiralama oluşturma görünümü
class KiralamaCreateView(CreateView):
    model = Kiralama
    form_class = KiralamaForm
    template_name = 'kiralama_form.html'

    def get_success_url(self):
        return reverse('kiralama-ekle')


# Filtrelenmiş verileri görüntüleme işlemleri
def filtered_data(request):
    # Burada yapılacak işlemleri ekleyin
    return render(request, 'filtered_data.html')


# IHA modeli için filtreleme işlemi
def iha_list(request):
    ihalar = IHA.objects.all()
    iha_filter = IHAFilter(request.GET, queryset=ihalar)
    return render(request, 'iha_list.html', {'filter': iha_filter})


# Kiralama modeli için filtreleme işlemi
class KiralamaListView(FilterView):
    model = Kiralama
    template_name = 'kiralama_list.html'
    context_object_name = 'kiralamalar'
    filterset_class = KiralamaFilter
    paginate_by = 10


# IHA modeli için güncelleme işlemi
class IHAUpdateView(LoginRequiredMixin, UpdateView):
    model = IHA
    form_class = IHAForm
    template_name = 'iha_form.html'
    success_url = reverse_lazy('iha-list')


# IHA modeli için silme işlemi
class IHADeleteView(LoginRequiredMixin, DeleteView):
    model = IHA
    template_name = 'iha_confirm_delete.html'
    success_url = reverse_lazy('iha-list')


# Kiralama modeli için güncelleme işlemi
class KiralamaUpdateView(LoginRequiredMixin, UpdateView):
    model = Kiralama
    form_class = KiralamaForm
    template_name = 'kiralama_form.html'
    success_url = reverse_lazy('kiralama-list')


# Kiralama modeli için silme işlemi
class KiralamaDeleteView(LoginRequiredMixin, DeleteView):
    model = Kiralama
    template_name = 'kiralama_confirm_delete.html'
    success_url = reverse_lazy('kiralama-list')  
    