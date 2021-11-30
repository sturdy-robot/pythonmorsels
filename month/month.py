import calendar
from dataclasses import dataclass
from datetime import date


@dataclass(init=True, eq=True, order=True, frozen=True)
class Month:
    __slots__ = ['year', 'month']
    year: int
    month: int

    @property
    def first_day(self):
        return date(self.year, self.month, 1)

    @property
    def last_day(self):
        _, num_days = calendar.monthrange(self.year, self.month)
        return date(self.year, self.month, num_days)

    @classmethod
    def from_date(cls, dt: date):
        return cls(dt.year, dt.month)

    def strftime(self, args):
        pass

    def __str__(self):
        return f'{self.year}-{self.month:02d}'

    def __repr__(self):
        return f'Month({self.year}, {self.month})'
