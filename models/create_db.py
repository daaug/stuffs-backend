import os
import pymysql
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import product

# This file serves only for automation and learning purposes
# In the ideal world, the database must be created by "hand"

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# PYMYSQL
# Only connects to create the DATABASE
conn = pymysql.connect(
    user=DB_USER,
    password=DB_PASS,
    host=DB_HOST,
    port=int(DB_PORT),
)

conn.cursor().execute(f'CREATE DATABASE IF NOT EXISTS {DB_NAME}')
conn.close()

# SQLALCHEMY
# dialect+driver://username:password@host:port/database
engine = create_engine(f'mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Create the tables
product.create_table(engine=engine)

# Inserting data
new_product = product.Product(name="Pastel", price=7.90)

session.add(new_product)
session.commit()