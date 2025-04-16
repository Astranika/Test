
from logging.config import fileConfig
from alembic import context
from app.models import Table, Reservation
import sys
from app.models import *

sys.path.append("/app")

from dotenv import load_dotenv
from os.path import abspath, dirname
load_dotenv()

from app.database import engine

sys.path.append(dirname(dirname(abspath(__file__))))

target_metadata = SQLModel.metadata


config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = engine

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()