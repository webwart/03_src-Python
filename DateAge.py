#!/user/  .in Unix only

#  ------------------------------------
#  Porject: LEARN
#   Author: Rainer Warth
#  Version: 31-07-2020
#    Goals: learn usage of dates, time, datetime
#      Ref: https://realpython.com/python-datetime/
#    Satus: <runs> - <bug (false output , script does not run)> - <broken (link, module, file is missing)> 
#    Satus: runs
#       >N: --
#  ------------------------------------ 
 

# dates are easily constructed and formatted
from datetime import date, time, datetime
today = date.today()
print(f'With data.today I get the day: {today} !')

# now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
# dates support calendar arithmetic
birthday = date(1964, 11, 27)
age = today - birthday
print(age.days / 365)
print("----- " * 3)
now = datetime.now()
current_time = time(now.hour, now.minute, now.second)
print(f'Current time: {current_time} !')
print("----- " * 3)
print(now.year)


