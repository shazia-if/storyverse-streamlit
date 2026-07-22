#database.py

import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABASE_URL = "sqlite:///data/storyverse.db"

engine = sa.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

Session = sessionmaker(autocommit=False,
    autoflush=False,
    bind=engine)

class Base(DeclarativeBase):
    pass


