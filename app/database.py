from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import databases, sqlalchemy

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost/test_db"
database = databases.Database(SQLALCHEMY_DATABASE_URL)

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_size=3)

 
metadata = sqlalchemy.MetaData()
