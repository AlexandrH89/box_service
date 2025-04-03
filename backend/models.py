from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Базовый класс для моделей
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    nickname = Column(String)
    email = Column(String)

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', nickname='{self.nickname}', email='{self.email}')>"
    

# Подключаемся к базе данных SQLite
engine = create_engine('sqlite:///./db.sqlite')

# Создаем таблицы, если они ещё не существуют
Base.metadata.create_all(engine)

# Создаём суссию для работы с базой данных
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()