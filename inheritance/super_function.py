class Person:
    def __init__(self, name):
        self.name = name

    def get_info(self):
        return f"Name: {self.name}"


class Student(Person):
    def __init__(self, name, university):
        super().__init__(name)   # вызываем родительский __init__
        self.university = university

    def get_info(self):
        parent_info = super().get_info()  # вызываем метод родителя
        return f"{parent_info}, University: {self.university}"


s = Student("John", "Harvard")

print(s.get_info())