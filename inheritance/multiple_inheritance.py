class Person:
    def greet(self):
        print("Hello, I am a person")

class Worker:
    def work(self):
        print("I am working")

class Student(Person, Worker):
    def study(self):
        print("I am studying")
s = Student()

s.greet()   
s.work()    
s.study()   