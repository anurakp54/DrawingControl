from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#create an engine

engine = create_engine('sqlite:///drawings.db')
Session = sessionmaker(bind=engine)
Base = declarative_base()

#Create a session

session = Session()