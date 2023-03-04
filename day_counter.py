import datetime

print("\nHi, I'm a day counter. Give me two dates and I'll tell you the number of days between them.\n")

year1 = int(input('\nWhat is the first year? (YYYY)\n'))
month1 = int(input('What is the first month? (MM)\n'))
day1 = int(input('What is the first day? (DD)\n'))
date1 = datetime.date(year1, month1, day1)

year2 = int(input('\nWhat is the second year? (YYYY)\n'))
month2 = int(input('What is the second month? (MM)\n'))
day2 = int(input('What is the second day? (DD)\n'))
date2 = datetime.date(year2, month2, day2)

print('\n\nThe difference between the two dates is ' + str(date2-date1)+'\n')
