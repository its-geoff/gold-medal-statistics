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

# converts distance from meters to feet and inches
def met_to_imp(distance):
   imp = round(distance * 3.281, 3)
   feet = int(imp // 1)
   in_dec = round(imp % 1, 3)
   inches = int((12 * in_dec) // 1)
   offset = round((12 * in_dec) % 0.25, 3)
   dec = round(100 * ((12 * in_dec) % 1 - offset))
   return str(feet) + "' " + str(inches) + "." + str(dec) + "\""

# converts distance from feet and inches to meters
def imp_to_met(distance):
   in_dis = distance.split("'")
   feet = float(in_dis[0])
   # isalnum() adds character to string if it's a number and discards if not
   inches = float("".join(i for i in in_dis[1] if i.isalnum()))
   met = round((feet + (inches / 12)) * 0.3048, 3)
   return met