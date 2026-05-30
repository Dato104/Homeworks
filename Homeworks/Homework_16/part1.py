


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def introduce(self):
        return f"Person: {self.first_name} {self.last_name}"


class Student(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)

    def introduce(self):
        return f"Student: {self.first_name} {self.last_name}"


class Lecturer(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)

    def introduce(self):
        return f"Lecturer: {self.first_name} {self.last_name}"


person_1 = Person("John", "Doe")
print(person_1.introduce())

person_2 = Student("John", "Doe")
print(person_2.introduce())

person_3 = Lecturer("John", "Doe")
print(person_3.introduce())




























