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


class NextDate:
    def __init__(self, weekday: Weekday, after_today=False):
        self.after_today = after_today
        self.weekday = weekday
        self._today = date.today()
        self._today_weekday = self._today.weekday()
    
    @property
    def today(self):
        self._today = date.today()
        return self._today
    
    @property
    def today_weekday(self):
        self._today_weekday = self.today.weekday()
        return self._today_weekday

    def __get_days_until(self):
        if self.after_today:
            return timedelta((self.weekday.value - self.today_weekday) % 7 + 7)
        return timedelta((self.weekday.value - self.today_weekday) % 7)

    def date(self):
        return self.today + self.__get_days_until()
        
    def days_until(self):
        return self.__get_days_until().days

    def __repr__(self):
        return f"NextDay({self.weekday}, {self.after_today})"
    
    def __str__(self):
        return f"NextDay({self.weekday}, {self.after_today})"


def days_until(weekday: Weekday, after_today=False):
    today = date.today()
    if after_today:
        return timedelta((weekday.value - today.weekday() - 1) % 7 + 1).days
    return timedelta((weekday.value - today.weekday()) % 7).days


def next_date(weekday: Weekday, after_today=False):
    return date.today() + timedelta(days_until(weekday, after_today))
    

def next_tuesday(after_today=False):
    return next_date(Weekday.TUESDAY, after_today)


def days_to_tuesday(after_today=False):
    return days_until(Weekday.TUESDAY, after_today)
