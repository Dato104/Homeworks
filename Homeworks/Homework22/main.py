import json
import os
from dataclasses import dataclass, asdict



@dataclass
class Book:
    id: int
    title: str
    author: str
    year: int
    available: bool

def save_books(books):
    with open('books.json', 'w', encoding="utf-8") as f:
        json.dump([asdict(b) for b in books], f, ensure_ascii=False, indent=2)

def load_books():
    if os.path.exists("books.json"):
        with open("books.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Book(**item) for item in data]
    return []


def book_add(books):
    try:
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        year = int(input("Enter book year: "))
        new_id = max((b.id for b in books), default=0) + 1
        books.append(Book(new_id, title, author, year, True))
    except ValueError:
        print("Invalid input")
        return
    print("✅ წიგნი დაემატა!")


def show_all():
    all_books = load_books()
    if not all_books:
        print("წიგნები არ არის")
    else:
        for book in all_books:
            status = "ხელმისაწვდომი" if book.available else "გაცემული"
            print(f"ID: {book.id} | {book.title} | {book.author} | {book.year} | {status}")


def search_by_name():
    all_books = load_books()
    search = input("Enter book name: ")
    found = False
    for book in all_books:
        if search.lower() in book.title.lower():
            status = "ხელმისაწვდომი" if book.available else "გაცემული"
            print(f"ID: {book.id} | {book.title} | {book.author} | {book.year} | {status}")
            found = True
    if not found:
        print("წიგნი ვერ მოიძებნა")


def get_book():
    all_books = load_books()
    bid = int(input("Enter book ID: "))
    for book in all_books:
        if bid == book.id:
            if book.available:
                book.available = False
                print("წიგნი წარმატებით გაიცა")
            else:
                print("წიგნი უკვე გაცემულია")
            return
    print("წიგნი ვერ მოიძებნა")

def return_book():
    all_books = load_books()
    bid = int(input("Enter book ID: "))
    for book in all_books:
        if bid == book.id:
            book.available = True
            print("წიგნი დაბრუნდა")
            return
    print("წიგნი ვერ მოიძებნა")

def statistics():
    all_books = load_books()
    total = len(all_books)
    available = sum(1 for b in all_books if b.available)
    print(f"სულ წიგნები: {total}")
    print(f"ხელმისაწვდომი: {available}")
    print(f"გაცემული: {total - available}")

def main():
    books = load_books()

    while True:
        print("\n1. წიგნის დამატება")
        print("2. ყველა წიგნის ნახვა")
        print("3. წიგნის ძებნა")
        print("4. წიგნის გატანა")
        print("5. წიგნის დაბრუნება")
        print("6. სტატისტიკა")
        print("7. მონაცემების შენახვა")
        print("8. გამოსვლა")

        try:
            choice = int(input("შეიყვანეთ ციფრი მოქმედების შესასრულებლად: "))

        except ValueError:
            print("უნდა შეიყვანოთ მთელი ციფრი")
            continue


        if choice == 1:
            book_add(books)
        elif choice == 2:
            show_all()
        elif choice == 3:
            search_by_name()
        elif choice == 4:
            get_book()
        elif choice == 5:
            return_book()
        elif choice == 6:
            statistics()
        elif choice == 7:
            save_books(books)
            print("მონაცემები შენახულია")
        elif choice == 8:
            break
        else:
            print("არასწორი არჩევანი!")


if __name__ == "__main__":
    main()

























































