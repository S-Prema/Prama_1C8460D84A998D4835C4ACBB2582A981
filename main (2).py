   if (year%4==0 and year%100!=0) or year%400==0:
     return True
   else:
     return Flase
year=2012
if isleapyear(year):
    print('{} is a leap year.'.format(year))
else:
    Print('is not a leap year.'.format (year)) 