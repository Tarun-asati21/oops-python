# simple inheritance

class Animal :
    def __init__(self):
        self.name = "Shero"
        
    def speak(self) :
        print(f"{self.name} makes a sound")
        
class Dog(Animal) :
    def __init__(self, breed):
        super().__init__() # to handle constructor overloading
        self.breed = breed
        
    def speak(self) : 
        super().speak() # call the base class method, to handle method overriding using super keyword
        print(f"{self.name} barks. It is a {self.breed}.") 
        
# animal = Animal("generic animal")
# animal.speak() # generic animal makes a sound

puppy = Dog("Golden Retreiver")
puppy.speak() # Shero makes a bark sound