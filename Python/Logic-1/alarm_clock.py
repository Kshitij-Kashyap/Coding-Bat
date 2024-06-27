def alarm_clock(day, vacation):
  if vacation:
    return "off" if (day == 6 or day == 0) else "10:00"
  return "10:00" if (day == 6 or day == 0) else "7:00"
  
  
  

