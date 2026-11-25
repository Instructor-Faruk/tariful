from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/training2"
#DATABASE_URL = "postgresql+psycopg2://training_rn82_user:Dw0W65kwL8h1D2iyOBYEKBWJ2su56Ibk@dpg-dc35cq9ksfps7392o240-a.oregon-postgres.render.com/training_rn82"

DATABASE_URL="postgresql+psycopg2://tarif_db_user:dKA1uuzyzTQRQbx8ajuazczKxpbYLOMo@dpg-dc380eh5efls73b4c9b0-a.oregon-postgres.render.com/tarif_db"
engine = create_engine(DATABASE_URL)
session_local = sessionmaker(autocommit = False, autoflush= False, bind=engine)
base = declarative_base()
