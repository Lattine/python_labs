# -*- coding: utf-8 -*-

# @Time    : 2019/11/25
# @Author  : Lattine

# ======================
from flask import request, render_template, flash, redirect, url_for
from app import app
from tasks import send_mail


# --------------------- URL conf ----------------------
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        data = {}
        data["email"] = request.form['email']
        data["username"] = request.form['username']
        data["message"] = request.form['message']
        duration = int(request.form['duration'])
        duration_unit = request.form['duration_unit']
        if duration_unit == "M":
            duration *= 60
        elif duration_unit == "H":
            duration *= 3600
        elif duration_unit == "D":
            duration *= 86400
        send_mail.apply_async(args=[data], countdown=duration)
        flash(f"Email will be sent to {data['email']} in {request.form['duration']} {duration_unit}")
        return redirect(url_for("index"))


if __name__ == '__main__':
    app.run(debug=True)

# -------------------------------
# 1. 启动Flask
# $ python web.py

# 2. 启动Celery
# Linux下 $ celery worker -A tasks.celery --loglevel=info
# Windows下 $ celery worker -A tasks.celery --loglevel=info -P eventlet

# 3. 启动Flower进行监测
# $ flower -A tasks.celery --port=5555
