from sqlalchemy import Column, ForeignKey, Integer, String, create_engine, Table
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
from settings import api_config

#engine = create_engine('postgresql://habrpguser:pgpwd4habr@localhost:5432/habrdb', echo=True)
engine = create_engine(f'postgresql://{api_config.user_sql}:{api_config.password_sql}@localhost:5432/{api_config.db_sql}', echo=True)
# echo=True вывод в консоли все запросы, которые делаем к БД







Base = declarative_base()

association_teble= Table(
    'association_teble', Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("book_id", Integer, ForeignKey("books.id"))
)



class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String(60), nullable=False) # nullable не могут быть пустыми
    author =Column(String(100), nullable=False)
    reviews = relationship('Reviews', backref='book', lazy=True)
    # с помощью функции relationship мы связываем нашу таблицу book c reviews
    readers = relationship('User', secondary=association_teble, back_populates='books', lazy=True)


    def __repr__(self):
        return self.title

class Reviews(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    text = Column(String(200), nullable=False)
    book_id = Column(Integer, ForeignKey('books.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f'От {self.reviews}'

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    reviews = relationship('Reviews', backref='reviews', lazy=True)
    books = relationship("Book", secondary=association_teble, back_populates="readers", lazy=True)

    def  __repr__(self):
        return self.name

class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    children = relationship('Child', back_populates="parent")

class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey("parent.id"))
    parent = relationship("Parent", back_populates="children")

    def __repr__(self):
        return f'От {self.name}'

Session = sessionmaker(bind=engine)
session = Session()
# Прокидывем соедиенение в sessionmaker
session.add(Book(title='Робинзон Крузо', author="Даниэль Дэфо")) #Создаем книгу 1


Base.metadata.create_all(engine)
# проверка таблиц


# book1 = session.query(Book).filter_by(title="Робинзон Крузо").first()
# user1 = session.query(User).filter_by(name="user1").first()
# book1.readers.append(user1)
# book1 = session.query(Book).filter_by(title="Робинзон Крузо").first()
# session.commit()
#
# user = session.query(User).filter(User.username == 'susan').first()
# query = select(User).where(User.username == 'susan')
# results = session.execute(query)
