import uuid


class BankAccount:
    accounts = []
    def __init__(self, balance=0):
        self.number = uuid.uuid4()
        if balance >= 0:
            self._balance = balance
        else:
            raise ValueError("Cannot open account with -10 balance")
        BankAccount.accounts.append(self)
    
    @property
    def balance(self):
        return self._balance

    def deposit(self, value):
        if value > 0:
            self._balance += value
        else:
            raise ValueError("Can't deposit ", value)
    
    def withdraw(self, value):
        if value > 0 and self._balance > 0 and self._balance >= value:
            self._balance -= value
        else:
            raise ValueError("Can't withdraw ", value)
    
    def transfer(self, acc, value):
        if self._balance > 0 and value > 0 and self._balance >= value:
            self._balance -= value
            acc.deposit(value)
        else:
            raise ValueError("Can't transfer ", value)
    
    def __str__(self):
        return f"BankAccount(balance={self._balance})"
    
    def __repr__(self):
        return f"BankAccount(balance={self._balance})"
