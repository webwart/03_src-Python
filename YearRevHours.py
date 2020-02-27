
#  author: Rainer Warth
#  date:  25-02-2020
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
