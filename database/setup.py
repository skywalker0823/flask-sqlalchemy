import sys

from sqlalchemy import Column, Integer, String, ForeignKey

from sqlalchemy.orm import relationship, declarative_base

from sqlalchemy import create_engine

Base = declarative_base()

# Add class definitions here
class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    author = Column(String(250), nullable=False)
    genre = Column(String(250))


# Create an engine that stores data in the local directory's
engine = create_engine('sqlite:///project.db')

Base.metadata.create_all(engine)
