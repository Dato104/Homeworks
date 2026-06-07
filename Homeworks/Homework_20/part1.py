import csv

import numpy as np
from datetime import datetime


csv_file = "products.csv"
log_file = "log.txt"

class Logger:
    def __init__(self, username):
        self.username = username

    def log(self,action):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        line = f'[{timestamp}] USER={self.username} | ACTION={action}\n'


        with open(log_file, 'a', encoding="utf-8") as f:
            f.write(line + "\n")


class ProductManager:


    def __init__(self,username):
        self.logger = Logger(username)
        self.ids = np.array([], dtype=np.int64)
        self.names = np.array([])
        self.prices = np.array([], dtype=np.float64)
        self.stocks = np.array([], dtype=np.int64)
        self.load()


    def load(self):
        try:
            with open(csv_file, "r", encoding="utf-8") as f:
                lines = f.read().splitlines()
            for line in lines[1:]:
                parts = line.split(",")
                self.ids = np.append(self.ids, int(parts[0]))
                self.names = np.append(self.names, parts[1])
                self.prices = np.append(self.prices, float(parts[2]))
                self.stocks = np.append(self.stocks, int(parts[3]))
        except Exception as e:
            print(e)


    def save(self):
        with open(csv_file, "w", encoding="utf-8") as f:
            f.write("id,name,price,stock\n")
            for i in range(len(self.ids)):
                f.write(f"{self.ids[i]},{self.names[i]},{self.prices[i]},{self.stocks[i]}\n")

    def show_all(self):
        self.logger.log("VIEW_ALL_PRODUCTS")
        try:
            if self.ids.size == 0:
                print("პროდუქტების სია ცარიელია")
            else:
                print(f"ID\tსახელი\tფასი\tმარაგი")
                print("-" * 40)
                for i in range(len(self.ids)):
                    print(f"{self.ids[i]}\t{self.names[i]}\t{self.prices[i]}\t\t{self.stocks[i]}")
                print("-" * 40)
        except Exception as e:
            print(e)

    def search_id(self):
        try:
            pid = int(input("შეიყვანეთ ID: "))
        except ValueError:
            print("ID უნდა იყოს მთელი რიცხვი.")
            return

        self.logger.log(f"GET_PRODUCT | PRODUCT_ID={pid}")

        i = pid - 1
        if pid in self.ids:
            print(f"ID\tსახელი\tფასი\tმარაგი")
            print("-" * 40)
            print(f"{self.ids[i]}\t{self.names[i]}\t{self.prices[i]}\t{self.stocks[i]}")
            print("-" * 40)
        else:
            print("id ვერ მოიძებნა")



    def add_product(self):

        name = input("შეიყვანეთ პროდუქტის სახელი: ").strip()


        if name in self.names:
            print("ასეთი პროდუქტი უკვე არსებობს")
        else:
            try:
                price = float(input("შეიყვანეთ პროდუქტის ფასი: "))
                stock = int(input("შეიყვანეთ პროდუქტის მარაგი: "))
            except ValueError:
                print("სწორად შეიყვანეთ ფასი და მარაგი!")
                return

            if len(self.ids) == 0:
                new_id = 1
            else:
                new_id = int(np.max(self.ids)) + 1
            self.ids = np.append(self.ids, new_id)
            self.names = np.append(self.names, name)
            self.prices = np.append(self.prices, price)
            self.stocks = np.append(self.stocks, stock)
            self.save()
            self.logger.log(f"ADD_PRODUCT | NAME={name}")
            print(f"პროდუქტი დაემატა (ID={new_id}).")

    def del_product(self):
        try:
            del_id = int(input("შეიყვანეთ id პროდუქტის წასაშლელად: "))
        except ValueError:
            print("ID უნდა იყოს მთელი რიცხვი.")
            return


        if del_id not in self.ids:
            print("ID ვერ მოიძებნა.")
        else:
            mask = self.ids != del_id
            self.ids = self.ids[mask]
            self.names = self.names[mask]
            self.prices = self.prices[mask]
            self.stocks = self.stocks[mask]
            self.save()

            self.logger.log(f"DELETE_PRODUCT | PRODUCT_ID={del_id}")
            print(f"ID={del_id} წაიშალა.")

class App:
    def __init__(self):
        username = input("Enter your name: ").strip()
        self.manager = ProductManager(username)

    def run(self):
        while True:
            print("\n1. Show all products")
            print("2. Get product by id")
            print("3. Add product")
            print("4. Delete product")
            print("5. Exit")

            choice = input("\nაირჩიეთ: ")

            if choice == "1":
                self.manager.show_all()
            elif choice == "2":
                self.manager.search_id()
            elif choice == "3":
                self.manager.add_product()
            elif choice == "4":
                self.manager.del_product()
            elif choice == "5":
                break
            else:
                print("არასწორი არჩევანი")


final = App()
final.run()
























































