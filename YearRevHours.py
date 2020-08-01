#!/user/  .in Unix only
# -*- coding: utf-8 -*-

#  ------------------------------------
#  Porject: LEARN
#   Author: Rainer Warth
#  Version: 28-02-2020 Previous: -- First: 25-02-2020
#    Goals: Learn datetime
#      Ref: PYTHON.org Documentation. 
#      Ref: 20.5.1.7. Parsing XML with Namespaces  
#      Ref: https://docs.python.org/3/library/xml.etree.elementtree.html
#    Satus: <runs> - <bug (false output , script does not run)> - <broken (link, module, file is missing)> 
#    Satus: 
#       >N: --


#  description: calculate the total number of hours worked / year based on hours worked / week and vacation, conference, and trainng days.



NoWeekYear = 52
WeeksYear = 52
WeeksVacation = 10
HoursWeek = 33
ConferenceDays = 10
FormationDays = 15

horaireNow = ( 52 , 10 , 33 , 10 , 15)

HoursTotal = 0 

def calHoursYear(hoursDataList):
    '''
    Function returns yearly worked hour based on weekly hours and vacation days

    '''

    HoursTotal = ( NoWeekYear - WeeksVacation - ( ConferenceDays / 7 ) - ( FormationDays / 7) ) * HoursWeek
    return HoursTotal


HoursTotal = calHoursYear(HoursTotal)


print(HoursTotal)
