import os
from dotenv import load_dotenv

from alembic import context
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Build paths inside the project like this: BASE_DIR / 'subdir'.
file = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(os.path.dirname(file))
load_dotenv(os.path.join(BASE_DIR, '../.env'))


def get_db_uri():
    _driver = os.getenv("DB_DRIVER")
    _user = os.getenv("POSTGRES_USER")
    _password = os.getenv("POSTGRES_PASSWORD")
    _host = os.getenv("POSTGRES_HOST")
    _database = os.getenv("POSTGRES_DB")
    return f'{_driver}://{_user}:{_password}@{_host}/{_database}'


DB_URI = get_db_uri()
engine = create_engine(DB_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
