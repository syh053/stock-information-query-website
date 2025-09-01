from login_database import conn, cursor

sql = """
ALTER TABLE stock_data
ADD UNIQUE name_date_index (name, date);
"""

cursor.execute(sql)
