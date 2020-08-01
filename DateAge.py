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
# current_datetime = time(now.year, now.month, now.day , now.hour, now.minute)
print(f'Current time: {now} !')
print("----- " * 3)
print(now.year)
print(now.hour)

print("----- " * 3)

def fn_timestemp( part_1 , extension):
    fn_timestemp = now.strftime("%y%m%d-%H%M")
    fn_center = part_1
    fn_ext = extension
    return (f'{fn_timestemp}_{fn_center}.{fn_ext}')

fn = fn_timestemp( "RecordsFromDictio" , "rst")
print(fn)
