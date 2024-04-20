from sqlalchemy import create_engine, inspect, text
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from .config import config

Base = declarative_base()
engine = create_engine(config.MYSQL_DB_URI)
DatabaseSession = sessionmaker(bind = engine)



