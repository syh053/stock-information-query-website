import pymysql
from dotenv import dotenv_values
from login_database import cursor


sql = "CREATE DATABASE IF NOT EXISTS stock DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci"

cursor.execute(sql)
