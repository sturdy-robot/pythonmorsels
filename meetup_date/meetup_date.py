from datetime import date, timedelta
from enum import Enum


class Weekday(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


def meetup_date(year, month, nth=4, weekday=3):
    first_day_month = date(year, month, 1)
    first_weekday = first_day_month.weekday()
    return first_day_month + get_days_until(nth, first_weekday, weekday)


def get_days_until(nth, first_weekday, weekday):
    days = timedelta((weekday - first_weekday) % 7)
    days += timedelta(weeks=nth-1) if nth > 0 else timedelta(weeks=nth)
    return days
