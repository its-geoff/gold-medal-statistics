from django.contrib import admin

# Register your models here.
from .models import Mark, Athlete

class MarkAdmin(admin.ModelAdmin):
   fieldsets = [
      ('Athlete information', {'fields': ['name', 'gender', 'team']}),
      ('Mark information',    {'fields': ['event', 'mark']}),
      ('User Assignment', {'fields': ['user']}),
   ]

   list_display = ('name', 'gender', 'team', 'event', 'mark', 'points', 'id')
   list_filter = ['name', 'gender', 'team', 'event', 'user']
   search_fields = ['name', 'gender', 'team', 'event', 'user', 'id']

class AthleteAdmin(admin.ModelAdmin):
   fieldsets = [
      ('Athlete information', {'fields': ['name', 'gender', 'team']}),
      ('100m',    {'fields': ['one_mark', 'one_points']}),
      ('200m',    {'fields': ['two_mark', 'two_points']}),
      ('400m',    {'fields': ['four_mark', 'four_points']}),
      ('100mH/110mH',    {'fields': ['one_h_mark', 'one_h_points']}),
      ('400mH',    {'fields': ['four_h_mark', 'four_h_points']}),
      ('4x100m',    {'fields': ['one_r_mark', 'one_r_points']}),
      ('4x400m',    {'fields': ['four_r_mark', 'four_r_points']}),
      ('800m',    {'fields': ['eight_mark', 'eight_points']}),
      ('1600m',    {'fields': ['sixteen_mark', 'sixteen_points']}),
      ('3200m',    {'fields': ['thirtytwo_mark', 'thirtytwo_points']}),
      ('High Jump', {'fields': ['hj_mark', 'hj_points']}),
      ('Pole Vault', {'fields': ['pv_mark', 'pv_points']}),
      ('Long Jump', {'fields': ['lj_mark', 'lj_points']}),
      ('Triple Jump', {'fields': ['tj_mark', 'tj_points']}),
      ('Shot Put', {'fields': ['sp_mark', 'sp_points']}),
      ('Discus Throw', {'fields': ['dt_mark', 'dt_points']}),
      ('User Assignment', {'fields': ['user']}),
   ]

   list_display = ('name', 'gender', 'team')
   list_filter = ['name', 'gender', 'team', 'user']
   search_fields = ['name', 'gender', 'team', 'user']

admin.site.register(Mark, MarkAdmin)
admin.site.register(Athlete, AthleteAdmin)