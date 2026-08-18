class Employee:
    
    def __init__(self,salary,name,bond):
        self.salary= salary
        self.name= name
        self.bond=bond
    
    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"the salary is {self.salary} .The name of the person is {self.name} . the bond is for {self.bond} years ")
        
e1 = Employee(34000, "john doe", 4)

e1.get_info()


e2= Employee(50000, "mohit",5)

e2.get_info()