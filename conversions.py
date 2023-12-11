# created to avoid circular imports and to have a dedicated file for conversions

# converts time from seconds to minutes
def sec_to_min(time):
   time = float(time)
   min = int(time // 60)
   sec = int(time % 60)
   if sec < 10:
      sec = "0" + str(sec)
   ms = int(round(100 * (time - int(time))))
   if ms < 10:
      ms = "0" + str(ms)
   return str(min) + ":" + str(sec) + "." + str(ms)

# converts time from minutes to seconds
def min_to_sec(time):
   time_sep = time.split(":")
   min = int(time_sep[0])
   sec = round(float(time_sep[1]), 2)
   return round((60.0 * min) + sec, 2)