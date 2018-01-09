## is leap year function from stackoverflow:
## https://stackoverflow.com/questions/11621740/how-to-determine-whether-a-year-is-a-leap-year
def is_leap_year(year):
    """Determine whether a year is a leap year."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    days = 0

    if month in (1, 3, 5, 7, 8, 10, 12):
        days = 31

    elif month is not 2:
        days = 30

    elif month is 2 and is_leap_year(year):
        days = 29

    elif month is 2:
        days = 28

    return days


def next_day(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    # YOUR CODE HERE

    if day < days_in_month(year, month):
        day += 1
    # else it's the last day
    elif month < 12:
        day = 1
        month += 1
    # else it's the last day of December
    else:
        day = 1
        month = 1
        year += 1

    return year,month,day


def date_is_before(year1, month1, day1, year2, month2, day2):
     if year1 < year2:
         return True
     elif year1 == year2:
         if month1 < month2:
             return True
         elif month1 == month2 and day1 < day2:
             return True
     else:
         return False


def days_between_dates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""

    assert(not date_is_before(year2, month2, day2,
                                year1, month1, day1))

    days = 0

    while date_is_before(year1, month1, day1,
                            year2, month2, day2):
        days += 1
        year1, month1, day1 = next_day(year1, month1, day1)

    return days


def test_days_between_dates():

    # test same day
    assert(days_between_dates(2017, 12, 30,
                              2017, 12, 30) == 0)
    # test adjacent days
    assert(days_between_dates(2017, 12, 30,
                              2017, 12, 31) == 1)
    # test new year
    assert(days_between_dates(2017, 12, 30,
                              2018, 1,  1)  == 2)
    # test full year difference
    assert(days_between_dates(2012, 6, 29,
                              2013, 6, 29)  == 365)
    # test full leap year difference
    assert(days_between_dates(2015, 6, 29,
                              2016, 6, 29)  == 366)

    print("Congratulations! Your days_between_dates")
    print("function is working correctly!")

test_days_between_dates()
