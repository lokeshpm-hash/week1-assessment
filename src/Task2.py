import csv
import json

with open("Test1/employees.csv","r", newline="") as file:
    dict_reader=csv.DictReader(file)   
    count=0
    employees=list(dict_reader)
    
    
with open("employees.json","w") as file:
    json.dump(employees,file, indent=4)
    
    
high_earner =[
    emp for emp in employees
    if int(emp["salary"])>50000 
            
]
    
         
with open("high_earners.csv","w", newline="") as file:
    fieldnames = employees[0].keys()
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(high_earner)

print(f"Rows read: {len(employees)} | High earners: {len(high_earner)}")
  
