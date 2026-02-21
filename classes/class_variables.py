class Dog:
    species = "собачка"  # class variable

    def __init__(self, name, age):
        self.name = name  # instance variable
        self.age = age    # instance variable
d1 = Dog("Buddy", 3)
d2 = Dog("Lucy", 5)

print(d1.name)      
print(d2.age)       
print(d1.species)   
print(d2.species)  