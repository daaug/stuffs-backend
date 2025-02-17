import os
import pymysql

# Connects to create the DATABASE
conn = pymysql.connect(
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS"),
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
)

conn.cursor().execute('CREATE DATABASE IF NOT EXISTS stuffs')
conn.close()