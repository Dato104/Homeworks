import csv


def contact_func(file ):
    try:
        with open(file, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            for i in reader:
                print(i)
    except FileNotFoundError:
        print("ფაილი ვერ მოიძებნა")
    except Exception as e:
        print(e)

contact_func("contacts.csv")


def contact_add(file, name, phone, email):
    try:
        with open(file, "a", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, ["name", "phone", "email"])
            writer.writerow({"name": name, "phone": phone, "email": email})

    except FileNotFoundError:
        print("ფაილი ვერ მოიძებნა")
    except Exception as e:
        print(e)


contact_add("contacts.csv","gocha", "555-43-56-78", "gochito@gmail.com")

def find_name(file, name):
    try:
        with open(file, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)

            for i in reader:
                if i["name"] == name:
                    print(i)

    except FileNotFoundError:
        print("ფაილი ვერ მოიძებნა")
    except Exception as e:
        print(e)


find_name("contacts.csv", "gocha")


def del_contact(file, name):
    try:
        with open(file, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            new_rows = []
            for i in rows:
                if i["name"] != name:
                    new_rows.append(i)


            if len(rows) == len(new_rows):
                print("კონტაქტი არ არსებობს")
                return


        with open(file, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=reader.fieldnames)
            writer.writeheader()
            writer.writerows(new_rows)

    except FileNotFoundError:
        print("ფაილი ვერ მოიძებნა")
    except Exception as e:
        print(e)


del_contact("contacts.csv", "John")



#
# import csv
#
#
# def contact_func(file ):
#        with open(file, "r", encoding="utf-8", newline="") as f:
#         reader = csv.DictReader(f)
#         for i in reader:
#             print(i)
#
# contact_func("contacts.csv")
#
#
# def contact_add(file, name, phone, email):
#
#     with open(file, "a", encoding="utf-8", newline="") as f:
#         writer = csv.DictWriter(f, ["name", "phone", "email"])
#         writer.writerow({"name": name, "phone": phone, "email": email})
#
#
# contact_add("contacts.csv","gocha", "555-43-56-78", "gochito@gmail.com")
#
# def find_name(file, name):
#     with open(file, "r", encoding="utf-8", newline="") as f:
#         reader = csv.DictReader(f)
#
#         for i in reader:
#             if i["name"] == name:
#                 print(i)
#
#
# find_name("contacts.csv", "gocha")
#
#
# def del_contact(file, name):
#     with open(file, "r", encoding="utf-8", newline="") as f:
#         reader = csv.DictReader(f)
#         rows = list(reader)
#         new_rows = []
#         for i in rows:
#             if i["name"] != name:
#                 new_rows.append(i)
#
#
#         if len(rows) == len(new_rows):
#             print("კონტაქტი არ არსებობს")
#             return
#
#
#     with open(file, "w", encoding="utf-8", newline="") as f:
#         writer = csv.DictWriter(f, fieldnames=reader.fieldnames)
#         writer.writeheader()
#         writer.writerows(new_rows)
#
#
# del_contact("contacts.csv", "John")
