import re
from dataclasses import dataclass, field


@dataclass(frozen=True)
class PhoneNumber:
    number: str
    area_code: int = field(init=False)
    prefix: int = field(init=False)
    phone_number: str = field(init=False, hash=True, compare=True)
    line_number: int = field(init=False)

    def __post_init__(self):
        phone_number_regex = re.compile(r'\(?(\d\d\d)\)?[-|\.|\s]*?(\d\d\d)[-|\.|\s]*?(\d\d\d\d)')
        mo = phone_number_regex.fullmatch(str(self.number))

        if mo is None:
            raise ValueError

        super(PhoneNumber, self).__setattr__('area_code', mo[1])
        super(PhoneNumber, self).__setattr__('prefix', mo[2])
        super(PhoneNumber, self).__setattr__('line_number', mo[3])
        super(PhoneNumber, self).__setattr__('phone_number', f'{self.area_code}{self.prefix}{self.line_number}')

    def __eq__(self, other):
        if isinstance(other, PhoneNumber):
            return self.phone_number == other.phone_number
        return NotImplemented

    def __hash__(self):
        return hash(self.phone_number)

    def __repr__(self):
        return f"PhoneNumber('{self.area_code}{self.prefix}{self.line_number}')"
    
    def __str__(self):
        return f"{self.area_code}-{self.prefix}-{self.line_number}"
