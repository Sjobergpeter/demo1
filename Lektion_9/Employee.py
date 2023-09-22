import datetime
class Employee():
    def __init__(self, name, salary, employment):
        self.name = name
        self.salary = salary
        self.employment = employment

    def YearsOfEmployment(self):
        CurrentYear = 2023
        YearsEmployed =  CurrentYear - self.employment['Year']
        print (self.name, "Has been working for", YearsEmployed, "Years")

EmployeePeter = Employee("Peter", 30000,{'Date': 20, 'Month': 6, 'Year': 2020})
 
EmployeePeter.YearsOfEmployment()