from logging.config import fileConfig
from sqlalchemy import pool
from alembic import context
from sqlmodel import SQLModel
import sys

# Добавляем путь к проекту
sys.path.append("/app")

# Импортируем все модели
from app.models import Table, Reservation  # Укажите все ваши модели
from app.database import engine

# Используем метаданные из SQLModel
target_metadata = SQLModel.metadata

# Конфигурация логов (оставляем как есть)
config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
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
    """Run migrations in 'online' mode."""
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