from flask import Blueprint, render_template, redirect, url_for
from .stocks.show_datas import stocks

# 建立總路由
routes = Blueprint("routes", __name__)

routes.register_blueprint(stocks)

@routes.route("/index")
def index():
  return render_template("index.html")


# 捕捉所有未知路徑
@routes.route("/", defaults={"path": ""})
@routes.route("/<path:path>")
def catch_all(path):
    return redirect(url_for("routes.index"))