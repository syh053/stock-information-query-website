# Python 爬蟲程式與資料視覺化開發

  此專案是利用 [Pytorch](https://pytorch.org/) 框架來實做深度學習並利用 [Flask](https://github.com/hsuanchi/flask-template) 呈現視覺化的練習網站 

  - 使用 yfinance 奇摩股市資料工具

  - 利用 PyMySQL 將資料以關聯式資料庫形式儲存在本地端

  - 透過 Pytorch 框架針對「收盤價」和「成交量」進行股市預測
  
  - 透過 Echarts 圖形化呈現數據結果

<br>

# Python 及套件版本

### Python 版本

- Python==3.9.13

### 重點套件

- Pytorch : pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu126

- Flask==3.1.2  ( 若 flask 版本過舊，Blueprint 物件可能沒有 register_blueprint 功能 )

- python-dotenv==1.1.1

- PyMySQL==1.1.1

- scikit-learn

<br>

# 專案簡介

  ### 目前開發的路由為

  - 查詢個股「開盤價」、「最高價」、「最低價」、「收盤價」及 sma 均線等資訊

  ### 待完成路由

  - 將訓練好的 LSTM 模型導入預測路由

<br>

# 執行專案方法

### 1. 建立資料夾，並將終端機導引到該資料夾
```
cd "資料夾路徑" 
```

### 2. git clone 專案
```
git clone "請放專案路徑"
```

### 3. 建立虛擬環境
```
python -m venv .venv
```

### 4. 安裝套件
```
pip install 相關套件
```

### 5. 依下面步驟在本地端建立資料
- 建立 .env 文件作為還境變數使用(可見範例檔案.env_test)
- create_database.py
- create_table.py
- stock_table_index.py
- create_datas_to_table.py

### 6. 啟動伺服器
```
python main.py
```

<br>

# 預覽

### 以 2330 為例

![2330](https://meee.com.tw/a7ogq20.png)



