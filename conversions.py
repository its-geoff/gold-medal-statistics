# created to avoid circular imports and to have a dedicated file for conversions

# converts time from seconds to minutes
def sec_to_min(time):
   time = float(time)
   min = int(time // 60)
   sec = int(time % 60)
   ms = int(round(100 * (time - int(time))))
   return str(min) + ":" + str(sec) + "." + str(ms)