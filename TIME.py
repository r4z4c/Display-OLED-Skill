
import time, datetime

class theTime:
  def __init__(self):
    self.name = "theTime"
    
  def currentTime(stringa, stringb):
    now = datetime.datetime.now()
    nowyear = now.year
    nowmonth = now.month
    nowday = now.day
    nowhour = now.hour
    nowminute = now.minute
    nowsecond = now.second
    nowTime = str(nowhour).zfill(2) + ":" + str(nowminute).zfill(2) + ":" + str(nowsecond).zfill(2)
    nowDate = str(nowday).zfill(2) + "." + str(nowmonth).zfill(2) + "." + str(nowyear)
    if stringa == "time" and stringb == "date":
      theTime = nowTime + " " + nowDate
    elif stringa == "date" and stringb == "time":
      theTime = nowDate + " " + nowTime
    elif stringa == "time" and stringb == "":
      theTime = nowTime
    elif stringa == "date" and stringb == "":
      theTime = nowDate
    else:
      theTime = now
    return theTime
    
  def
