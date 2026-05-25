import csv
import random
from faker import Faker

fake = Faker()


def students_writer(file):
    try:
        with open(file, "w", encoding="utf-8", newline="", ) as f:
            headers = ["name", "python", "java", "ruby", "c" ]
            writer = csv.DictWriter(f, delimiter=",", fieldnames=headers)
            writer.writeheader()
            for _ in range(100):
                writer.writerow({
                    "name": fake.name(),
                    "python": random.randint(1, 100),
                    "java": random.randint(1, 100),
                    "ruby": random.randint(1, 100),
                    "c": random.randint(1, 100)
                })
            return
    except ValueError:
        print("მონაცემი არასწორია — რიცხვი უნდა იყოს ქულა")
    except Exception as e:
        print(e)

students_writer("students.csv")


def students_reader(file):
    try:
        with open(file, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f, delimiter=",")
            rows = list(reader)
            for row in rows:
                row["average"] = (float(row["python"]) + float(row["java"]) + float(row["ruby"]) + float(row["c"])) / 4
                print(f"{row["name"]} - საშუალო ქულა: {row["average"]}")

            best_student = max(rows, key=lambda x: x["average"])
            best_python = max(rows, key=lambda x: float(x["python"]))
            best_java = max(rows, key=lambda x: float(x["java"]))
            best_ruby = max(rows, key=lambda x: float(x["ruby"]))
            best_c = max(rows, key=lambda x: float(x["c"]))
        print("\n")
        print("📊 სტატისტიკა:\n--------------------------------------------------")
        print(f"საუკეთესო სტუდენტი: {best_student['name']} (საშუალო: {best_student['average']:.2f})")
        print()
        print("🏆 ლიდერები საგნების მიხედვით:")
        print(f"  Python: {best_python["name"]}   -{best_python["python"]}")
        print(f"  Java: {best_java["name"]}   -{best_java["java"]}")
        print(f"  Ruby: {best_ruby["name"]}   -{best_ruby["ruby"]}")
        print(f"  C: {best_c["name"]}   -{best_c["c"]}")

    except FileNotFoundError:
        print("ფაილი ვერ მოიძებნა")
    except Exception as e:
        print(e)

students_reader("students.csv")


