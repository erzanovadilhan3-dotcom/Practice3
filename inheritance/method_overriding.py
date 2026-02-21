class Animal:
    def speak(self):
        print("The animal makes a sound")
class Dog(Animal):
    def speak(self):   # overriding
        print("The dog says woof")
a = Animal()
d = Dog()

a.speak()
d.speak()