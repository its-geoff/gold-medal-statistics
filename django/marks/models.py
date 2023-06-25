from django.db import models

# Create your models here.
class Mark(models.Model):
   name = models.CharField(max_length = 50)
   gender = models.CharField(max_length = 5)
   team = models.CharField(max_length = 50)
   event = models.CharField(max_length = 10)
   mark = models.FloatField(default = 0.0)
   points = models.IntegerField(default = 0)

   def __str__(self):
      mark_text = f"{self.name}, {self.team}, {self.event}, {self.mark}, {self.points}"
      return mark_text
   
   # makes each parameter accessible in html
   def get_name_text(self):
      return self.name

   def get_gender_text(self):
      if self.gender == "men":
         return "M"
      elif self.gender == "women":
         return "W"
   
   def get_team_text(self):
      return self.team

   def get_event_text(self):
      return self.event

   def get_mark_text(self):
      return f"{self.mark:.2f}"
   
   def get_points_text(self):
      return self.points
   
   @classmethod
   def create(cls, name, gender, team, event, mark):
      mark = cls(name = name, gender = gender, team = team, event = event, mark = mark, points = 0)
      return mark
   
class Athlete(models.Model):
   name = models.CharField(max_length = 50)
   gender = models.CharField(max_length = 50)
   team = models.CharField(max_length = 50)
   one_mark = models.FloatField(default = 0.0, verbose_name = "mark")
   one_points = models.IntegerField(default = 0, verbose_name = "points")
   two_mark = models.FloatField(default = 0.0, verbose_name = "mark")
   two_points = models.IntegerField(default = 0, verbose_name = "points")
   four_mark = models.FloatField(default = 0.0, verbose_name = "mark")
   four_points = models.IntegerField(default = 0, verbose_name = "points")
   one_h_mark = models.FloatField(default = 0.0, verbose_name = "mark")
   one_h_points = models.IntegerField(default = 0, verbose_name = "points")
   four_h_mark = models.FloatField(default = 0.0, verbose_name = "mark")
   four_h_points = models.IntegerField(default = 0, verbose_name = "points")
   one_r_mark = models.FloatField(default = 0.0, verbose_name = "mark")
   one_r_points = models.IntegerField(default = 0, verbose_name = "points")
   four_r_mark = models.FloatField(default = 0.0, verbose_name = "mark")
   four_r_points = models.IntegerField(default = 0, verbose_name = "points")
   eight_mark = models.FloatField(default = 0.0, verbose_name = "mark")
   eight_points = models.IntegerField(default = 0, verbose_name = "points")
   sixteen_mark = models.FloatField(default = 0.0, verbose_name = "mark")
   sixteen_points = models.IntegerField(default = 0, verbose_name = "points")
   thirtytwo_mark = models.FloatField(default = 0.0, verbose_name = "mark")
   thirtytwo_points = models.IntegerField(default = 0, verbose_name = "points")

   def __str__(self):
      athlete_text = f"{self.name}, {self.team}"
      return athlete_text

   # makes each parameter accessible in html
   def get_name_text(self):
      return self.name

   # formatted for stats profile
   def get_one_pr(self):
      return f"100m: {self.one_mark:.2f} - {self.one_points}"
   
   def get_two_pr(self):
      return f"200m: {self.two_mark:.2f} - {self.two_points}"
   
   def get_four_pr(self):
      return f"400m: {self.four_mark:.2f} - {self.four_points}"
   
   def get_eight_pr(self):
      return f"800m: {self.eight_mark:.2f} - {self.eight_points}"
   
   def get_sixteen_pr(self):
      return f"1600m: {self.sixteen_mark:.2f} - {self.sixteen_points}"
   
   def get_thirtytwo_pr(self):
      return f"3200m: {self.thirtytwo_mark:.2f} - {self.thirtytwo_points}"
   
   def get_one_h_pr(self):
      return f"100mH: {self.one_h_mark:.2f} - {self.one_h_points}"
   
   def get_four_h_pr(self):
      return f"400mH: {self.four_h_mark:.2f} - {self.four_h_points}"
   
   def get_one_r_pr(self):
      return f"4x100m: {self.one_r_mark:.2f} - {self.one_r_points}"
   
   def get_four_r_pr(self):
      return f"4x400m: {self.four_r_mark:.2f} - {self.four_r_points}"

   @classmethod
   def create(cls, name, gender, team):
      athlete = cls(name = name, gender = gender, team = team, 
                    one_mark = 0.0, one_points = 0, two_mark = 0.0, two_points = 0, \
                    four_mark = 0.0, four_points = 0, one_h_mark = 0.0, one_h_points = 0, \
                    four_h_mark = 0.0, four_h_points = 0, one_r_mark = 0.0, one_r_points = 0, \
                    four_r_mark = 0.0, four_r_points = 0, eight_mark = 0.0, eight_points = 0, \
                    sixteen_mark = 0.0, sixteen_points = 0, thirtytwo_mark = 0.0, thirtytwo_points = 0)
      return athlete