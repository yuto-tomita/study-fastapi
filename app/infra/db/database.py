import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASSWORD')
DB_SERVER = os.environ.get('DB_SERVER')
DB_PORT = os.environ.get('DB_PORT')
DB_NAME = os.environ.get('DB_NAME')

SQLALCHEMY_DB_URL = "postgresql://{0}:{1}@{2}:{3}/{4}".format(
	DB_USER, DB_PASS, DB_SERVER, DB_PORT, DB_NAME
)

engine = create_engine(
	SQLALCHEMY_DB_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
