from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config.envloaders import SQL_DIALECT, MYSQL_HOST, MYSQL_DATABASE, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD

# SQLALCHEMY_DATABASE_URL = "mysql://root:root@127.0.0.1:3306/protaige_intro"
SQLALCHEMY_DATABASE_URL = f"{SQL_DIALECT}://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def database():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()