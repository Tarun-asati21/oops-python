# initiate a class

class employee :
    # special method/magic method/dunder method
    def __init__(self): # constructor --> special method used for creating data or attributes
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        
    def travel(self, destination): # method
        print(f"employee is now travelling to {destination}")

# creating an instant/object of the class

SAM = employee()
# printing the attributes
print(SAM.salary)
print(SAM.id)
# calling a method
SAM.travel("London")