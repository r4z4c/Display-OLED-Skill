
import time, datetime

class theTime:
  def __init__(self):
    self.name = "theTime"
    
  def currentTime(self):
    now = datetime.datetime.now()
    
    nowhour = now.hour
    nowminute = now.minute
    nowsecond = now.second
    
    nowTime = str(nowhour).zfill(2) + ":" + str(nowminute).zfill(2) + ":" + str(nowsecond).zfill(2)
    
    return nowTime
    
  def currentDate(self):
    now = datetime.datetime.now()
    
    nowyear = now.year
    nowmonth = now.month
    nowday = now.day

    nowDate = str(nowday).zfill(2) + "." + str(nowmonth).zfill(2) + "." + str(nowyear)
    
    return nowDate
    
