import re


class PhoneNumber:
    def __init__(self, number: str):
        self.number = number
        self.__prefix = None
        self.__area_code = None
        self.__line_number = None
        self.calculate_phone_number()
    
    def calculate_phone_number(self):
        phone_number_regex = re.compile(r'\(?(\d\d\d)\)?[-|.|\s]*?(\d\d\d)[-|.|\s]*?(\d\d\d\d)')
        mo = phone_number_regex.search(self.number)
        self.area_code = mo.group(1)
        self.prefix = mo.group(2)
        self.line_number = mo.group(3)

    @property
    def prefix(self):
        return self.__prefix

    @prefix.setter
    def prefix(self, value):
        self.__prefix = value
    
    @property
    def area_code(self):
        return self.__area_code
    
    @area_code.setter
    def area_code(self, value):
        self.__area_code = value

    @property
    def line_number(self):
        return self.__line_number

    @line_number.setter
    def line_number(self, value):
        self.__line_number = value
    
    def __repr__(self):
        return f"PhoneNumber('{self.area_code}{self.prefix}{self.line_number}')"
    
    def __str__(self):
        return f"{self.area_code}-{self.prefix}-{self.line_number}"
    