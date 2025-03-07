# initiate a class
class Employee:
    # special method/ dunder method / magic method - constructor
    def __init__(self):
        print("Attributes are getting initiated")
        self.id = 123
        self.designation = "SDE"
        self.salary = 50000
        print("The attributes have been initiated")
    
    # method
    def travel(self, destination):
        print("Travel function is called manually")
        print(f"The Employee is travelling to {destination}")

# create an obj/instance of a class
sam = Employee()

# print the attributes
print(sam.id)
print(sam.designation)
print(sam.salary)

# calling the method
sam.travel("Bangalore")

# type
print(type(sam))