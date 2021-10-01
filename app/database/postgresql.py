import os
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv
load_dotenv()

uri = os.getenv('POSTGRESQL_URI')

engine = create_engine(uri)

Session = sessionmaker(bind=engine)

session = Session()

Base = declarative_base()
