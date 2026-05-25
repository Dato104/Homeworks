
import csv

def min_price():
    try:
        price = input("შეიყვანეთ მინიმალური ფასი: ")
        price = float(price)
        with open("products.csv", "r", encoding="utf-8",newline="") as f:
            reader = csv.DictReader(f,  delimiter=",")

            with open("filtered_products.csv", "w", encoding="utf-8",newline="") as nf:
                writer = csv.DictWriter(nf, fieldnames=reader.fieldnames)
                writer.writeheader()

                for i in reader:
                    if float(i["price"]) > price:
                        writer.writerow(i)
    except FileNotFoundError:
        print("ფაილი ვერ მოიძებნა")
    except ValueError:
        print("ფასი უნდა იყოს რიცხვი")
    except Exception as e:
        print(e)

min_price()

































































