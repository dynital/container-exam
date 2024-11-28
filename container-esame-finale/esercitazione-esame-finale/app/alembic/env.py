import os
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
# Importa il modulo contenente i tuoi modelli
from models import Base  # Assicurati di importare il modulo corretto
# Carica il configuratore di logging
config = context.config
fileConfig(config.config_file_name)
# Aggiungi il tuo modello Base a target_metadata
target_metadata = Base.metadata
# Ottieni la stringa di connessione dalla variabile d'ambiente
database_url = os.getenv('DATABASE_URL')
if database_url:
    config.set_main_option('sqlalchemy.url', database_url)
def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )
        with context.begin_transaction():
            context.run_migrations()
run_migrations_online()