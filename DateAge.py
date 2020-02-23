# dates are easily constructed and formatted
from datetime import date
now = date.today()
print(now)
# now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
# dates support calendar arithmetic
birthday = date(1980, 2, 21)
age = now - birthday
print(age.days / 365)
