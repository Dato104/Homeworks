from sqlalchemy import create_engine, text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker


engine = create_engine('postgresql+psycopg2://postgres:datobase003@localhost/homework')


class Base(DeclarativeBase):
    pass

class Books(Base):
    __tablename__ = 'books'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    author: Mapped[str]
    publish_year: Mapped[int]


Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()


book_1 = Books(
    title='ვეფხისტყაოსანი',
    author='შოთა რუსთაველი',
    publish_year=1220,
)

book_2 = Books(
    title='დათა თუთაშხია',
    author='ჭაბუა ამირეჯიბი',
    publish_year=1975,
)

book_3 = Books(
    title='1984',
    author='ჯორჯ ორუელი',
    publish_year=1949,
)

book_4 = Books(
    title='ჯამბაზი',
    author='გურამ დოჩანაშვილი',
    publish_year=1972,
)

book_5 = Books(
    title='პროექტ ჰეილ მერი',
    author='ენდი ვეირი',
    publish_year=2021,
)

books = [book_1, book_2, book_3, book_4, book_5]

session.add_all(books)

session.commit()


all_books = session.query(Books).all()
for book in all_books:
    print(f"ID: {book.id} || Title: {book.title} || Author: {book.author} || Publish Year: {book.publish_year}")


book = session.query(Books).filter(Books.id == 1).first()
print(f"ID: {book.id} || Title: {book.title} || Author: {book.author} || Publish Year: {book.publish_year}")


filtered_books = session.query(Books).filter(Books.publish_year > 2015).all()
for filtered_book in filtered_books:
    print(f"ID: {filtered_book.id} || Title: {filtered_book.title} || Author: {filtered_book.author} || Publish Year: {filtered_book.publish_year}")




the_book = session.query(Books).filter_by(id=3).first()
print(f"ID: {the_book.id} || Title: {the_book.title} || Author: {the_book.author} || Publish Year: {the_book.publish_year}")

the_book.author = "ილია ჟავჟავაძე"

session.commit()



session.delete(the_book)

session.commit()


session.close()

