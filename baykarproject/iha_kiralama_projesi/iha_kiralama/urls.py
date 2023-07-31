from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import KiralamaListView,IHAUpdateView, IHADeleteView,KiralamaUpdateView, KiralamaDeleteView


urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('ihalar/', views.IHAList.as_view(), name='iha-list'),
    path('ihalar/<int:pk>/', views.IHADetail.as_view(), name='iha-detail'),
    path('kiralamalar/', views.KiralamaList.as_view(), name='kiralama-list'),
    path('kiralamalar/<int:pk>/', views.KiralamaDetail.as_view(), name='kiralama-detail'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('iha_ekle/', views.IHACreateView.as_view(), name='iha-ekle'),
    path('kiralama_ekle/', views.KiralamaCreateView.as_view(), name='kiralama-ekle'),
    path('home/', views.home, name='home'),
    path('logout/', views.user_logout, name='logout'),
    path('filtered_data/', views.filtered_data, name='filtered_data'),
    path('home/ihalar/', views.iha_list, name='iha-list'),
    path('kiralama/', KiralamaListView.as_view(), name='kiralama-list'),
    path('iha/<int:pk>/update/', IHAUpdateView.as_view(), name='iha-update'),
    path('kiralama/<int:pk>/update/', KiralamaUpdateView.as_view(), name='kiralama-update'),
    path('kiralama/<int:pk>/delete/', KiralamaDeleteView.as_view(), name='kiralama-delete'),
    path('iha/<int:pk>/delete/', IHADeleteView.as_view(), name='iha-delete'), 
]
