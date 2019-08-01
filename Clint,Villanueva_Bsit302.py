Employees = []
class Employee:
    def __init__(self,name,department,position,rate):
        self.name = name
        self.department = department
        self.position = position
        self.rate = rate
    def getsalary(self,hourly):
        return self.rate * hourly
while True:
    print("Employee Management System by Clint")
    print("[1] Add New Employee")
    print("[2] Enter Hourly of Employee")
    print("[3] Show Employee Information")
    print("[4] Exit")

    str = int(input("Enter Option:"))

    if str == 1:
        name = (input("Enter name: "))
        
        department = (input("Enter Department: "))
     
        position = (input("Enter Position: "))
        
        rate = (input("Enter rate"))

        emp = Employee(name, department, position, rate)
        Employees.append(emp)
       
    elif str ==2:
        e = (int(input("Employee Number: ")))
        ee = Employees[e]
        f = (int(input("Enter Hours: ")))
        print(ee.getsalary(f))
        Employees.append(f)
    elif str == 3:
        for e in Employees:
            print("Employee Id: " ,Employees.index(e))
            print("Employee Name: " ,e.name)
            print("Employee Department " , e.department)
            print("Employee Position: " , e.position)
            print("Employee rate: ", e.rate)
            print("***************************")
    elif str == 4:
        exit(1)

