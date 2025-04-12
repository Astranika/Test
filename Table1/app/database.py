from sqlmodel import SQLModel
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os
import time
from sqlalchemy.exc import OperationalError

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://test_user:your_strong_password@db:5432/restaurant_db")
engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    retries = 10
    while retries > 0:
        try:
            SQLModel.metadata.create_all(engine)
            print("Успешное подключение к БД")
            break
        except OperationalError:
            retries -= 1
            print(f"Ошибка подключения, осталось попыток: {retries}")
            time.sleep(5)
            if retries == 0:
                print("Не удалось подключиться к БД")
                raise
