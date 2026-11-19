class InvalidSalaryError(Exception):
    pass

def bonus(salary, rate=0.1,*extras,**options):
    total=0;
    total=salary*rate
    for num in extras:
        total+=num
    if "cap" in options:
        total=min(total,options["cap"])
        
    return total
class Employee:
    def __init__(self,name, salary):
        self.name=name
        if(salary<0):
            raise InvalidSalaryError("Invalid Salary ",salary)
        self.salary=salary
        
    def annual_salary(self):
        return self.salary*12
    def get_details(self):
        print("Name of the Employee : ",self.name)
        print("Salary of the Employee : ",self.salary)
        
class Manager(Employee):
    def __init__(self,name,salary,team_size):
        super().__init__(name,salary)
        self.team_size=team_size
        
    def get_details(self):
        super().get_details()
        print("Team size : ",self.team_size)
    
    
    
employees = [
    (1, "Arun", "Sales", 30000, "Chennai"),
    (2, "Priya", "HR", 45000, "Chennai"),
    (3, "Rahul", "IT", 60000, "Bangalore"),
    (4, "Divya", "IT", 75000, "Chennai"),
    (5, "Karthik", "Finance", 90000, "Mumbai"),
    (6, "Meena", "Sales", 52000, "Bangalore"),
    (7, "Suresh", "IT", 68000, "Chennai"),
    (8, "Anitha", "HR", 48000, "Mumbai")
]

# high_salary=[]
# for emp in employees:
#     if emp[3]>50000:
#         high_salary.append(emp[1])
high_salary = [emp[1] for emp in employees if emp[3] > 50000]
        
        
print("Persons earning more than 50000 : ",high_salary)

list_raise=list(map(lambda emp:emp[3]+(emp[3]/10),employees))

print("people after raise in salary:")
print(list_raise)

list_place=list(filter(lambda pl:pl[4]=="Chennai", employees))
print("people who are working in chennai :")
for place in list_place:
    print(place[1])

print("people salary below 85000: ")
for emp in employees:
    if emp[3]==0:
        continue
    if emp[3]>85000:
        break
    print(emp[3])
try:
    emp = Employee("Lokesh", -500)
    print("Annual Salary:", emp.annual_salary())

except InvalidSalaryError as e:
    print("Error:", e)

finally:
    print("Transaction Finished")