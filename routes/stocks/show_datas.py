from pathlib import Path
import sys

root = Path(__file__).resolve().parents[2] / "mysql"
print(root)
sys.path.append(str(root))


from flask import Blueprint, render_template, request, redirect, url_for
from login_database import conn, cursor
from datetime import datetime

# 建立 stocks 相關路由
stocks = Blueprint('stocks', __name__)

# 股票查詢路由
@stocks.route("/stock/<stock_num>", methods = ["GET"])
def stock(stock_num):
  # 起始日期
  start_date = datetime(2025, 1, 1).strftime("%Y-%m-%d")

  """
  從資料庫搜尋符合的資料
  """
  sql = """
    SELECT * FROM stock_data
    WHERE name = %s AND date > %s
    """
  
  params = (stock_num, start_date)

  cursor.execute(sql, params)

  datas = cursor.fetchall()

  # 跳過 index 及 股票代碼
  datas = [(date.strftime("%Y-%m-%d"), *others) for _, _, date, *others in datas]


  stock_datas = {
    'dates' : [],
    'k_datas' : [],
    "sma5" : [],
    "sma10" : [],
    "sma20" : [],
    "sma60" : [],
    "sma200" : [],
  }

  for data in datas :

    # 將日期格式從 2025-01-01 改為 2025/01/01
    stock_datas['dates'].append(data[0].replace("-", "/"))

    stock_datas['k_datas'].append((data[1], data[4], data[3], data[2]))

    stock_datas["sma5"].append(data[6])
    stock_datas["sma10"].append(data[6])
    stock_datas["sma20"].append(data[7])
    stock_datas["sma60"].append(data[8])
    stock_datas["sma200"].append(data[9])

  return render_template("stock.html", stock_num=stock_num, datas=datas, stock_datas=stock_datas)


# 從導向到"股票查詢"路由
@stocks.route("/stock")
def stock_redirect():
  stock_num = request.args.get("stock_num")

  if stock_num :
    return redirect(url_for("routes.stocks.stock", stock_num=stock_num))
  
  else :
    return render_template("stock.html", stock_datas={})