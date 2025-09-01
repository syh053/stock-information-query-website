#%%
import yfinance as yf
from datetime import datetime, timedelta
import pandas as pd
from login_database import cursor, conn
from get_all_stocks_code import get_stock_numbers

"""
取得資料後存入 table
"""

def update_datas():

  start = "2017-01-01"
  end = datetime.today() + timedelta(days=1)
  end = end.strftime('%Y-%m-%d')

  stocks = get_stock_numbers()

  sorted_datas = stocks[stocks["產業別"] == "半導體業"]

  codes = sorted_datas["代號"].to_list()

  for code in codes:

    print(code)

    datas = yf.Ticker(f"{code}.TW").history(start=start, end=end)

    datas.reset_index(inplace=True)

    # 只顯示日期，不顯示時間
    datas['Date'] = datas['Date'].dt.date

    # 選擇固定
    datas = datas[["Date", "Open", "High", "Low", "Close", "Volume"]]


    datas["sma5"] =  datas["Close"].rolling(window=5).mean()
    datas["sma10"] =  datas["Close"].rolling(window=10).mean()
    datas["sma20"] =  datas["Close"].rolling(window=20).mean()
    datas["sma60"] =  datas["Close"].rolling(window=60).mean()
    datas["sma200"] =  datas["Close"].rolling(window=200).mean()

    datas = datas[199:]
    datas.reset_index(drop=True, inplace=True)

    columns = ["Open", "High", "Low", "Close", "sma5", "sma10", "sma20", "sma60", "sma200"]

    datas[columns] = datas[columns].apply(lambda x : round(x, 2))
    datas["Volume"] = datas["Volume"].map(lambda x : round(x/1000))


    # 逐筆將資料存入 table
    for row in datas.itertuples(index=False):
      # 查詢指令
      sql = "SELECT * FROM stock_data WHERE name = %s AND date =%s"

      params = (code, row.Date)

      cursor.execute(sql, params)

      existed = cursor.fetchall()

      # 若沒有重複的資料就輸入至 table
      if not existed :
        sql = """
        INSERT INTO stock_data (name, date, open, high, low, close, volume, sma5, sma10, sma20, sma60, sma200)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        params = (code, row.Date, row.Open, row.High, row.Low, row.Close, row.Volume, row.sma5, row.sma10, row.sma20, row.sma60, row.sma200)

        cursor.execute(sql, params)

        conn.commit()

      else :
        print(f"{ code }_{ row.Date } 資料已存在!")

update_datas()
