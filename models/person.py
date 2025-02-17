from peewee import *
import os

# Connects to create the TABLES
db = MySQLDatabase(
    os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS"),
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT"))
)

class Person(Model):
    name = CharField()
    birthday = DateField()

    class Meta:
        database = db

db.connect()
db.create_tables([Person])