from django.db import models
from conversions import sec_to_min

# Create your models here.
class Mark(models.Model):
   name = models.CharField(max_length = 50)
   gender = models.CharField(max_length = 5)
   grade = models.IntegerField(default  = 0)
   team = models.CharField(max_length = 50)
   event = models.CharField(max_length = 10)
   mark = models.FloatField(default = 0.0)
   points = models.IntegerField(default = 0)
   user = models.CharField(max_length = 30, default="admin")

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
   
   def get_grade_text(self):
      return self.grade
   
   def get_team_text(self):
      return self.team

   def get_event_text(self):
      return self.event

   def get_sd_mark_text(self):
      if self.mark < 60.0:
         return f"{self.mark:.2f}"
      else:
         return sec_to_min(self.mark)

   def get_jt_mark_text(self):
      return f"{self.mark:.2f}m"

   def get_points_text(self):
      return self.points

   def get_user_text(self):
      return self.user
   
   @classmethod
   def create(cls, name, gender, grade, team, event, mark, user):
      mark = cls(name = name, gender = gender, grade = grade, team = team, event = event, mark = mark, points = 0, user = user)
      return mark
   
class Athlete(models.Model):
   name = models.CharField(max_length = 50)
   gender = models.CharField(max_length = 50)
   grade = models.IntegerField(default = 0, verbose_name = "grade")
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
   hj_mark = models.FloatField(default = 0.0, verbose_name = "mark")
   hj_points = models.IntegerField(default = 0, verbose_name = "points")
   pv_mark = models.FloatField(default = 0.0, verbose_name = "mark")
   pv_points = models.IntegerField(default = 0, verbose_name = "points")
   lj_mark = models.FloatField(default = 0.0, verbose_name = "mark")
   lj_points = models.IntegerField(default = 0, verbose_name = "points")
   tj_mark = models.FloatField(default = 0.0, verbose_name = "mark")
   tj_points = models.IntegerField(default = 0, verbose_name = "points")
   sp_mark = models.FloatField(default = 0.0, verbose_name = "mark")
   sp_points = models.IntegerField(default = 0, verbose_name = "points")
   dt_mark = models.FloatField(default = 0.0, verbose_name = "mark")
   dt_points = models.IntegerField(default = 0, verbose_name = "points")
   user = models.CharField(max_length = 30, default="admin")

   def __str__(self):
      athlete_text = f"{self.name}, {self.team}"
      return athlete_text

   # makes each parameter accessible in html
   def get_name_text(self):
      return self.name
   
   def get_grade_text(self):
      return self.grade

   def get_team_text(self):
      return self.team

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
   
   def get_hj_pr(self):
      return f"High Jump: {self.hj_mark:.2f}m - {self.hj_points}"
   
   def get_pv_pr(self):
      return f"Pole Vault: {self.pv_mark:.2f}m - {self.pv_points}"
   
   def get_lj_pr(self):
      return f"Long Jump: {self.lj_mark:.2f}m - {self.lj_points}"
   
   def get_tj_pr(self):
      return f"Triple Jump: {self.tj_mark:.2f}m - {self.tj_points}"
   
   def get_sp_pr(self):
      return f"Shot Put: {self.sp_mark:.2f}m - {self.sp_points}"
   
   def get_dt_pr(self):
      return f"Discus Throw: {self.dt_mark:.2f}m - {self.dt_points}"

   def get_user_text(self):
      return self.user

   @classmethod
   def create(cls, name, gender, grade, team, user):
      athlete = cls(name = name, gender = gender, grade = grade, team = team, 
                    one_mark = 0.0, one_points = 0, two_mark = 0.0, two_points = 0,
                    four_mark = 0.0, four_points = 0, one_h_mark = 0.0, one_h_points = 0,
                    four_h_mark = 0.0, four_h_points = 0, one_r_mark = 0.0, one_r_points = 0,
                    four_r_mark = 0.0, four_r_points = 0, eight_mark = 0.0, eight_points = 0, 
                    sixteen_mark = 0.0, sixteen_points = 0, thirtytwo_mark = 0.0, thirtytwo_points = 0,
                    hj_mark = 0.0, hj_points = 0, pv_mark = 0.0, pv_points = 0, lj_mark = 0.0,
                    lj_points = 0, tj_mark = 0.0, tj_points = 0, sp_mark = 0.0, sp_points = 0,
                    dt_mark = 0.0, dt_points = 0, user = user)
      return athlete