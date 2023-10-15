"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, type, pay, contracts = 0, commission = 0, bonus = 0):
        self.name = name
        self.type = type
        self.pay = pay
        self.contracts = contracts
        self.commission = commission
        self.bonus = bonus

    def get_pay(self):
        return self.pay

    def __str__(self):
        return self.name + f" works on a {self.type}"

class MonthlyEmployee(Employee):
    def __init__(self, name, pay, contracts = 0, commission = 0, bonus = 0):
        super().__init__(name, 'monthly', pay, contracts, commission, bonus)
        self.declare = ""

    def get_pay(self):
        amount = super().get_pay()
        self.pay = amount + (self.commission * self.contracts) + self.bonus
        return self.pay
    
    def __str__(self):
        self.get_pay
        self.declare = super().__str__() + f" salary of {self.pay}"
        if self.commission:
            self.declare += f" and receives a commission for {self.commission} contract(s) at {self.commission}/contract"
        elif self.bonus:
            self.declare += f" and receives a bonus commission of {self.bonus}"
        return self.declare + f".  Their total pay is {self.get_pay()}."
    
class ContractEmployee(Employee):
    def __init__(self, name, hours, rate, contracts = 0, commission = 0, bonus = 0):
        super().__init__(name, 'contract', 0, contracts, commission, bonus)
        self.hours = hours
        self.rate = rate
        self.declare = ""

    def get_pay(self):
        self.pay = (self.hours * self.rate) + (self.commission * self.contracts) + self.bonus
        return self.pay
    
    def __str__(self):
        self.declare = super().__str__() + f" of {self.hours} hours at {self.rate}/hour"
        if self.commission:
            self.declare += f" and receives a commission for {self.contracts} contract(s) at {self.commission}/contract"
        if self.bonus:
            self.declare += f" and receives a bonus commission of {self.bonus}"
        return self.declare + f". Their total pay is {self.get_pay()}."
    
# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = MonthlyEmployee('Billie', 4000)
print(str(billie))
# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = ContractEmployee('Charlie', 100, 25)
print(str(charlie))
# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = MonthlyEmployee('Renee', 3000, 4, 200)
print(str(renee))
# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = ContractEmployee('Jan', 150, 25, 3, 220)
print(str(jan))
# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = MonthlyEmployee('Robbie', 2000, bonus=1500)
print(str(robbie))
# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = ContractEmployee('Ariel', 120, 30, bonus=600)
print(str(ariel))