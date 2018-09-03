annualSalInc = 1.04

class Employee:
        def __init__ (self, last, first, yearsWorked):
            import random
            self.last = last
            self.first = first
            self.yearsWorked = yearsWorked
            self.id = random.randint(0, 100)
            self.salary = (random.randint(0 ,100) * yearsWorked)
            self.email = last + "-" + first + "@company.com"
            self.promotionsReceived = 0

        def pullFullName (self):
            return "{}, {}".format(self.last, self.first)

        def upgradeSalary (self):
            if self.yearsWorked > 0:
                self.salary *= (annualSalInc * self.yearsWorked)
            else:
                self.salary *= (annualSalInc)

            self.promotionsReceived += 1

# Employee list here:
emp_1 = Employee("Hendrix", "Jimi", 2)
emp_2 = Employee("Lennon", "John", 3)
emp_3 = Employee("McCartney", "Paul", 5)

# Use this function to pull all of employee's information
def pullInfo (emp):
    print(emp.__dict__)

# t = amount of years in the future
def predictSalary (emp, t):
    predictedSal = (emp.salary * annualSalInc * t)
    print('$', float(predictedSal), "- Predicted salary in", float(t), "years. Current Salary: ", "$", float(emp.salary))

pullInfo(emp_1)
predictSalary(emp_1, 3.5)

pullInfo(emp_2)
predictSalary(emp_2, 2)

pullInfo(emp_3)
predictSalary(emp_3, 5)