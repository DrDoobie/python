annualSalInc = 1.04

class Employee:
        def __init__ (self, last, first, salary):
            self.last = last
            self.first = first
            self.salary = float(salary * 1000)
            self.email = last + "-" + first + "@company.com"
            self.promotionsReceived = 0

        def pullFullName (self):
            return "{}, {}".format(self.last, self.first)

        def upgradeSalary (self):
            self.salary *= annualSalInc
            self.promotionsReceived += 1

# Employee list here:
emp_1 = Employee("Hendrix", "Jimi", 100)
emp_2 = Employee("Lennon", "John", 200)
emp_3 = Employee("McCartney", "Paul", 175)

# Use this function to pull all of employee's information
def pullInfo (emp):
    print(emp.__dict__)

# t = amount of years in the future
def predictSalary (emp, t):
    predictedSal = (emp.salary * annualSalInc * t)
    print(predictedSal)



