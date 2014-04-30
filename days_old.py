# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    ##
    # Your code here.
    ##

    #calculate year_for_days    only for a whole year
    year = year1+1 #only count whole year,   year1 is not a whole year
    days_for_years = 0

    #if the same year
    if year1==year2:
        return days_after_jan(year2,month2, day2)-days_after_jan(year1,month1, day1)

    while year< year2:
        days_for_years = days_for_years + year_days(year)
        year =year+1

    # days for a whole year + days after the whole year + days before the whole year
    return days_for_years+days_after_jan(year2,month2, day2)+(year_days(year1)-days_after_jan(year1,month1, day1))

#calculate days in a year
def year_days(year):
    if year%4 != 0:# not divisible by 4 then common year
        return 365
    # here the number can divisible by 4
    if year%100 != 0: #not divisible by 100 then leap year
        return 366
    if year%400 == 0:#year is not divisible by 100 then leap year
        return 366
    else:
        return 365

def days_after_jan(year,month,day):
    #common year
    daysOfMonths = [31,28,31,30,31,30,31,31,30,31,30,31]
    #leap yaar
    if year_days(year) == 366:
        daysOfMonths = [31,29,31,30,31,30,31,31,30,31,30,31]

    #calculate days of months       
    days_of_months = 0
    for i in range(0,month-1):
        days_of_months = days_of_months+daysOfMonths[i]
        
    return days_of_months + day

   


# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        print result #to see the difference
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()

#print year_days(1988),year_days(2000),year_days(2003)
#print days_after_jan(1,21),days_after_jan(2,1)
            
