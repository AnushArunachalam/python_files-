# today we look at classmethods in python
class Employee():

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        
        print(f"My name is {self.first, self.last}")
    def amount(self):
        self.pay = int(self.pay * self.raise_amount)
        return self.pay

    @classmethod # decorator(@)
    def set_raise(cls, amount):
        cls.raise_amount = amount

emp = Employee('anush', 'arunachalam', 5000)
emp.fullname()
# call amount function
print(emp.amount())
Employee.set_raise(1.5)
print(emp.amount())