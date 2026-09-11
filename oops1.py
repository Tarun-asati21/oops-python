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
# # printing the attributes
# print(SAM.salary)
# print(SAM.id)
# # calling a method
# SAM.travel("London")

SHAKTIMAAN = employee()
# different objects, will have different id (memory location)
print(id(SAM))
print(id(SHAKTIMAAN)) # id is an inbuilt function in python which points to the memory location where object is stored in RAM

# we can create additional attribute in some object, outside the class also
SAM.name = "sam kumar"
print(SAM.name)