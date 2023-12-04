from django.urls import path
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

app_name = 'gms'
urlpatterns = [
   # /home/
   path('', views.home, name='home'),
   path('home/', views.home, name='home'),
   # /about/
   path('about/', views.about, name='about'),
   # /scores/
   path('scores/', views.scores, name='scores'),
   # /scores/new/
   path('scores/new/', views.new_entry, name='new_entry'),
   # /scores/delete/
   path('scores/delete/<int:index>', views.delete, name='delete'),
   # /stats/
   path('stats/', views.stats, name='stats'),
   # /stats/men/
   path('stats/men/', views.men, name='men'),
   # /stats/women/
   path('stats/women/', views.women, name='women'),
   # /stats/men/athlete
   path('stats/men/<str:name>', views.men_profile, name='men_profile'),
   # /stats/women/athlete
   path('stats/women/<str:name>', views.women_profile, name='women_profile'),
]

# change admin site url
admin.site.site_url = '/home'

urlpatterns += staticfiles_urlpatterns()