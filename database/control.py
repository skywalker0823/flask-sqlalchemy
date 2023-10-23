from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.setup import Base, Book

engine = create_engine('sqlite:///project.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()


# Create
# bookOne = Book(title="The Hobbit", author="J.R.R. Tolkien", genre="Fantasy")
# session.add(bookOne)
# session.commit()
class BookController():
    def Create(self, title, author, genre):
        book = Book(title=title, author=author, genre=genre)
        session.add(book)
        session.commit()
        return book

    def Read_all(self):
        return session.query(Book).all()

    def Read_one_by_id(self, id):
        return session.query(Book).filter_by(id=id).first()

    def Read_one_by_title(self, title):
        return session.query(Book).filter_by(title=title).first()
    
    def Update(self, id, title, author, genre):
        book = session.query(Book).filter_by(id=id).first()
        book.title = title
        book.author = author
        book.genre = genre
        session.commit()
        return book
    
    def Delete(self, id):
        book = session.query(Book).filter_by(id=id).first()
        session.delete(book)
        session.commit()
        return book

