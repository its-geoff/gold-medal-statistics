from django.contrib import admin

# Register your models here.
from .models import Mark, Athlete

class MarkAdmin(admin.ModelAdmin):
   fieldsets = [
      ('Athlete information', {'fields': ['name', 'gender', 'team']}),
      ('Mark information',    {'fields': ['event', 'mark']}),
   ]

   list_display = ('name', 'gender', 'team', 'event', 'mark', 'points')
   list_filter = ['name', 'gender', 'team', 'event']
   search_fields = ['name', 'gender', 'team', 'event']

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
   ]

   list_display = ('name', 'gender', 'team')
   list_filter = ['name', 'gender', 'team']
   search_fields = ['name', 'gender', 'team']

admin.site.register(Mark, MarkAdmin)
admin.site.register(Athlete, AthleteAdmin)