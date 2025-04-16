
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import text
import os
import time
from sqlalchemy.exc import OperationalError
from dotenv import load_dotenv
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    retries = 10
    while retries > 0:
        try:
            #SQLModel.metadata.create_all(engine)
            with engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            print("Успешное подключение к БД")
            break
        except OperationalError:
            retries -= 1
            print(f"Ошибка подключения, осталось попыток: {retries}")
            time.sleep(5)
            if retries == 0:
                print("Не удалось подключиться к БД")
                raise
