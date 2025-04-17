
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import text
import subprocess
import logging
from sqlmodel import SQLModel
import os
import time
from sqlalchemy.exc import OperationalError
from dotenv import load_dotenv
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
def apply_migrations():
    try:
        subprocess.run(["alembic", "upgrade", "head"], check=True)
        logger.info("Alembic миграции успешно применены")
    except subprocess.CalledProcessError as e:
        logger.error(f"Ошибка применения миграций Alembic: {e}")
        raise

def init_db():
    retries = 10
    while retries > 0:
        try:
            apply_migrations()
            print("Успешное подключение к БД + успешное применение миграций Alembic")
            break
        except OperationalError:
            retries -= 1
            print(f"Ошибка подключения, осталось попыток: {retries}")
            time.sleep(5)
            if retries == 0:
                print("Не удалось подключиться к БД")
                raise
        except Exception as other_error:
            logger.critical(f"Неизвестная ошибка при подключении к БД: {other_error}")
            raise