from dotenv import dotenv_values
import pymysql

config = dotenv_values(".env")

conn = pymysql.connect(
  host=config["DB_HOST"],
  database=config["DB_NAME"],
  user=config["DB_USER"],
  password=config["DB_PASSWORD"]
)

cursor = conn.cursor()
