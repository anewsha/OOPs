# Define class car
class Car:
    wheels = 4 # class variable 
    
    # on instantiation __new__ is run to allocate memory
    def __new__(cls, name, color, speed):
        if (isinstance(name, str) and isinstance(color, str) and isinstance(speed, int)):
            print("allocating memory")
            return super().__new__(cls)
        else:
            raise ValueError ("String string float")
        
    # assigns variables to the object created
    def __init__(self,name,color, speed): 
        self.name =name
        self.color = color
        self.speed = speed
        print("Object created")
    
    # when you say print(object); must return str
    def __repr__(self): 
        return f"Hi this is the Car {self.name}, {self.color}, {self.speed}"
    
    # invoked at ==
    def __eq__(self, other):
        if (self.name==other.name and self.color ==other.color and self.speed==other.speed):
            return True
        else: 
            return False
    # if not defined then checks __len__, if not then default is True
    def __bool__(self):
        if self.speed>0:
            return True
        else:
            return False
    # Methods 
    def change_speed(self, new_speed):
        self.speed = new_speed
    def stopcar(self):
        self.speed = 0

# -> This is my object of the class
nano = Car("nano", "yellow", 30 )
harr =Car("Harr", "red", 70)
#-> Class variable  
print("Class variable: Car.wheels = ",Car.wheels)

nano.change_speed(50)
print(nano.speed)

nano.stopcar()
print(nano.speed)

print("===Type===")
print("type(nano)",type(nano)) #class Car
print(nano) #mem

print("=== check eq ====")
car1 = Car("samecar","black",30)
car2 = Car("samecar","black",30)

print("car1==car2",car1==car2) #false: two different objects even if values are same (but i defined eq, comment it to check false)
print("car1 is car2", car1 is car2) #points to diff memrory location hence false

# add __eq__() in the class 
print("car1.__eq__(car2)", car1.__eq__(car2)) #True, since i defined it to check values
print("car1==car2",car1==car2) #True because of my __eq__ class 

# check Bool
print("==== Bool ====")
print(nano.speed)
if nano:
    print("car is On")
else:
    print("car is off")

# __call__()
class quadratic:
    def __init__(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c
        
    def eval(self,x):
        return x**2 *self.a + x*self.b + self.c
    def __add__(self,other):
        return quadratic(self.a+other.a , self.b+other.b, self.c+other.c)
    
    def __contains__(self,m): #invoked by in
        if (m==self.a or m==self.b or m==self.c):
            return True
        else:
            False
        
quad = quadratic(2,3,1)
print("quad.eval(2)", quad.eval(2))
print("=== callable ===")
print("callable", callable(quad))

print("=== add ===")
print(type(quadratic(1,2,3)+quadratic(2,3,4)))

print("=== contain ===")
print(5 not in quad) #in invokes __contain__
print("bool",bool(nano))

# ===== Inheritance ======
# put the base class in ()
# invoke the __init__ of baseclass: the sub class INHERITS the attributes and methods of superclass 
# want something restricted to baseclass? __privateAttribute (double underscore)

class SuperClass:
    def __init__(self, animal):
        self.animal = animal
        
    def name(self, name):
        self.name = "name"
    

cat = SuperClass("Cat")
# print(cat.animal)
cat.name("kittybaby")
print(cat.name)

class subclass(SuperClass):
    def __init__(self,animal, sound):
        SuperClass.animal = animal
        self.sound = sound
    def name(self, name):
        self.name = name
cat_sub = subclass("cat","meow")
print(cat_sub.animal)
print(cat_sub.sound)
cat_sub.name("blah")
print(cat_sub.name)
        