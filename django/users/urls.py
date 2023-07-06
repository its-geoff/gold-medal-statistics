from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

app_name = 'accts'
urlpatterns = [
   # /signup/
   path('signup/', views.signup, name='signup'),
   # /login/
   path('login/', views.login, name='login'),
   # /logout/
   path('logout/', views.logout, name='logout'),
   # /password-change/
   path('password-change/', views.password_change, name='password_change'),
   # /password-change-done/
   path('password-change/done/', views.password_change_done, name='password_change_done'),
   # # /password-reset/
   # path('password-reset/', views.password_reset, name='password_reset'),
   # # /password-reset-done/
   # path('password-reset/done/', views.password_reset_done, name='password_reset_done'),
   # # /reset/userid/token/
   # path('reset/<uidb64>/token/', views.password_reset_confirm, name='password_reset_confirm'),
   # # /reset/done/
   # path('reset/done/', views.password_reset_complete, name='password_reset_complete'),
   # /profile/user
   path('profile/<str:username>', views.profile, name='profile'),
]

urlpatterns += staticfiles_urlpatterns()