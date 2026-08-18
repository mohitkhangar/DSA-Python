class Employee:
    company= "hp"
    
    def __init__(self,salary,name,bond,company):
        self.salary= salary
        self.name= name
        self.bond=bond
        self.company=company
    
    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"the salary is {self.salary} .The name of the person is {self.name} .the bond is for {self.bond} years . the company name is {self.company}")
        
e1 = Employee(34000, "john doe", 4, "tesla")
print(e1.company)
