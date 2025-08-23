from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/index")
def index():
  return render_template("index.html")

# 若 url 都不匹配，自動導向首頁
@app.route("/")
def home():
  return redirect(url_for("index"))


if __name__ == "__main__":
  app.run(debug=True)
