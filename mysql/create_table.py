from create_database import cursor

sql = """
CREATE TABLE IF NOT EXISTS stock_data (
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100) NOT NULL,
date DATETIME NOT NULL,
open FLOAT NOT NULL,
high FLOAT NOT NULL,
low FLOAT NOT NULL,
close FLOAT NOT NULL,
volume INT NOT NULL,
sma5 FLOAT,
sma10 FLOAT,
sma20 FLOAT,
sma60 FLOAT,
sma200 FLOAT
)
"""

cursor.execute(sql)