from datetime import date

date1 = date(2014, 7, 2)
date2 = date(2014, 7, 20)

difference = date2 - date1

print("Number of days between the dates:", difference.days)