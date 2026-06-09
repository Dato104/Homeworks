
import pandas as pd
from datetime import datetime


csv_file = "products.csv"
log_file = "log.txt"

products_df = pd.DataFrame(columns=["id", "name", "price", "stock"])


class Logger:
    def __init__(self,username):
        self.username = username

    def log(self,action):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        line = f'[{timestamp}] USER={self.username} | ACTION={action}\n'

        with open('log_file', 'a', encoding="utf-8") as f:
            f.write(line)

class ProductsManager:
    def __init__(self,username):
        self.logger = Logger(username)
        self.df = self.load()

    def load(self):
        try:
            return pd.read_csv(csv_file)
        except FileNotFoundError:
            return products_df


    def save(self):
        self.df.to_csv(csv_file, index=False)

    def show_all(self):
        self.logger.log('SHOW ALL PRODUCTS')
        if self.df.empty:
            print("პროდუქტების სია ცარიელია")
        else:
            print(f"\n""ID""\tname""\tprice""\tstock")
            print("-" * 40)
            for index, row in self.df.iterrows():
                print(f"{int(row['id'])}\t{row['name']}\t{row['price']}\t{int(row['stock'])}")
            print("-" * 40)

    def search_id(self):

        try:
            pid = int(input("შეიყვანეთ ID პროდუქტის მოსაძებნად: "))
        except ValueError:
            print("ID უნდა იყოს მტელი რიცხვი")
            return

        self.logger.log(f"GET_PRODUCT | PRODUCT_ID={pid}")

        result = self.df[self.df["id"] == pid]
        if result.empty:
            print("ID ვერ მოიძებნა")
        else:
            print(f"\n""\t""ID""\tname""\tprice""\tstock")
            print("-" * 40)
            for index, row in result.iterrows():
                print(f"{int(row['id'])}\t{row['name']}\t{row['price']}\t{int(row['stock'])}")
            print("-" * 40)

    def add_product(self):
        p_name = input("შეიყვანეთ პროდუქტის სახელი მის დასამატებლად: ").strip()


        if p_name in self.df["name"].values:
            print("ასეთი პროდუქტი უკვე არსებობს")
            return
        try:
            price = float(input("შეიყვანეთ პროდუქტის ფასი: "))
            stock = int(input("შეიყვანეთ პროდუქტის მარაგი: "))
        except ValueError:
            print("სწორად შეიყვანეთ ფასი და მარაგი!")
            return

        new_id = len(self.df) + 1
        self.df.loc[len(self.df)] = [new_id, p_name, price, stock]
        self.save()

        self.logger.log(f"ADD_PRODUCT | NAME={p_name}")
        print(f"პროდუქტი დაემატა (ID={new_id}).")


    def del_product(self):
        try:
            del_id = int(input("შეიყვანეთ ID პროდუქტის წაშაშლელად: "))
        except ValueError:
            print("ID უნდა იყოს მთელი რიცხვი.")
            return

        if del_id not in self.df["id"].values:
            print("ID ვერ მოიძებნა")

        else:
            self.df = self.df[self.df["id"] != del_id]
            self.save()
            self.logger.log(f"DELETE_PRODUCT | PRODUCT_ID={del_id}")
            print(f"ID={del_id} წაიშალა.")


class App:
    def __init__(self):
        username = input("შეიყვანეთ თქვენი სახელი: ").strip()
        self.manager = ProductsManager(username)

    def run(self):
        while True:
            print("\n1. Show all products")
            print("2. Get product by id")
            print("3. Add product")
            print("4. Delete product")
            print("5. Exit")

            choice = input("\n აირჩიეთ: ")

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




























































