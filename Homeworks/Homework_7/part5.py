




students = {
    "კლასი 10A": {
        "გიორგი": {
            "ასაკი": 16,
            "საშუალო_ქულა": 8.7,
            "საგნები": {
                "მათემატიკა": {"ქულა": 9, "გამოცდა": True},
                "ფიზიკა": {"ქულა": 8, "გამოცდა": False},
                "ისტორია": {"ქულა": 9, "გამოცდა": True},
                "ინგლისური": {"ქულა": 10, "გამოცდა": True}
            },
            "დასწრება": 92,
            "დამატებითი": ["ფეხბურთი", "პროგრამირება"]
        },
        "ანა": {
            "ასაკი": 15,
            "საშუალო_ქულა": 9.4,
            "საგნები": {
                "მათემატიკა": {"ქულა": 10, "გამოცდა": True},
                "ფიზიკა": {"ქულა": 9, "გამოცდა": True},
                "ისტორია": {"ქულა": 8, "გამოცდა": False},
                "ინგლისური": {"ქულა": 10, "გამოცდა": True}
            },
            "დასწრება": 98,
            "დამატებითი": ["ცეკვა"]
        },
        "დავით": {
            "ასაკი": 16,
            "საშუალო_ქულა": 7.2,
            "საგნები": {
                "მათემატიკა": {"ქულა": 6, "გამოცდა": False},
                "ფიზიკა": {"ქულა": 7, "გამოცდა": True},
                "ისტორია": {"ქულა": 8, "გამოცდა": True},
                "ინგლისური": {"ქულა": 9, "გამოცდა": False}
            },
            "დასწრება": 75,
            "დამატებითი": ["კალათბურთი", "პროგრამირება"]
        }
    },

    "კლასი 10B": {
        "მარიამ": {
            "ასაკი": 15,
            "საშუალო_ქულა": 9.1,
            "საგნები": {
                "მათემატიკა": {"ქულა": 9, "გამოცდა": True},
                "ბიოლოგია": {"ქულა": 10, "გამოცდა": True}
            },
            "დასწრება": 95,
            "დამატებითი": ["მუსიკა", "ხატვა"]
        },
        "ლევან": {
            "ასაკი": 16,
            "საშუალო_ქულა": 6.8,
            "საგნები": {
                "მათემატიკა": {"ქულა": 5, "გამოცდა": False},
                "ფიზიკა": {"ქულა": 7, "გამოცდა": False}
            },
            "დასწრება": 60,
            "დამატებითი": []
        }
    }
}




for class_name, students_in_class in students.items():
    for student_name, student_info in students_in_class.items():
        print(f"სახელი: {student_name} | საშუალო ქულა: {student_info["საშუალო_ქულა"]}")



best_student = None
best_grade = 0

for class_name, students_in_class in students.items():
    for student_name, student_info in students_in_class.items():
        if student_info["საშუალო_ქულა"] > best_grade:
            best_grade = student_info["საშუალო_ქულა"]
            best_student = student_name


print("\n", end = "")


print(f"საუკეთესო სტუდენტი: {best_student}")


print("\n", end = "")



print("სტუდენტები რომელთა დასწრება 90%-ს აჭარბებს: ")

for class_name, students_in_class in students.items():
    for student_name, student_info in students_in_class.items():
        if student_info["დასწრება"] > 90:
            print(f"სახელი: {student_name} | დასწრება: {student_info["დასწრება"]}")


print("\n", end = "")

best_class = None
most_students = 0

for class_name, students_in_class in students.items():
    if len(students_in_class) > most_students:
        most_students = len(students_in_class)
        best_class = class_name

print(f"ყველაზე მეტი სტუდენტი არის {best_class}-ში")

print("\n", end = "")

print("პროგრამირებაზე დადიან: ")

for class_name, students_in_class in students.items():
    for student_name, student_info in students_in_class.items():
        if "პროგრამირება" in student_info["დამატებითი"]:
            print(f"{student_name}")


print("\n", end = "")


total_attendance = 0
student_count = 0


for class_name, students_in_class in students.items():
    for student_name, student_info in students_in_class.items():
        total_attendance += student_info["დასწრება"]
        student_count += 1

average_attendance = total_attendance / student_count

print(f"საშუალო დასწრება მთელს სკოლაში: {average_attendance}")




print("\n", end = "")


dct = {}

print("სტუდენტები და მათი საგნების რაოდენობა: ")
for class_name, students_in_class in students.items():
    for student_name, student_info in students_in_class.items():
        dct[student_name] = len(student_info["საგნები"])


print(dct)


print("\n", end = "")

best_students = []
added_subject = 0

for class_name, students_in_class in students.items():
    for student_name, student_info in students_in_class.items():
        subject = len(student_info["დამატებითი"])
        if subject > added_subject:
            added_subject = subject
            best_students = [student_name]
        elif subject == added_subject:
            best_students.append(student_name)

print(f"საუკეთესო სტუდენტები: {best_students}")













