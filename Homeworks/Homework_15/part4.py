
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade



class Classroom:
    def __init__(self):
        self.students = []


    def add_student(self, student):
        self.students.append(student)

    def average(self):
        total = 0
        for student in self.students:
            total += student.grade
        return total / len(self.students)

    def top_student(self):
        best_student = max(self.students, key=lambda x: x.grade)
        return best_student.name

classroom = Classroom()
classroom.add_student(Student(name="Ana", grade=10))
classroom.add_student(Student(name="Gocha", grade=2))
classroom.add_student(Student(name="nika", grade=7))
classroom.add_student(Student(name="anita", grade=8))

print(classroom.average())
print(classroom.top_student())



