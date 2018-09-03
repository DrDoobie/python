class Employee:
        annualSalInc = 1.04

        def __init__ (self, last, first, salary):
            self.last = last
            self.first = first
            self.salary = float(salary * 1000)
            self.email = last + "-" + first + "@company.com"
            self.promotionsReceived = 0

        def pullFullName (self):
            return "{}, {}".format(self.last, self.first)

        def upgradeSalary (self):
            self.salary *= 1.04
            self.promotionsReceived += 1

# Employee light here:
emp_1 = Employee("Hendrix", "Jimi", 100)
emp_2 = Employee("Lennon", "John", 200)

# Use this function to pull all of employee's information
def pullEmpInfo (emp):
    print(emp.__dict__)

def predictRaise (emp):
    predictedSal = (emp.salary * 1.04)
    print(predictedSal)