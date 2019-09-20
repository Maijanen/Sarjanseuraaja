from application import app, db
from flask import render_template, request, redirect, url_for
from application.series.models import Serie


@app.route("/series/", methods=["GET"])
def series_index():
    return render_template("series/list.html", series=Serie.query.all())


@app.route("/series/new/")
def series_form():
    return render_template("series/new.html")


@app.route("/series/", methods=["POST"])
def series_create():
    s = Serie(request.form.get("name"), request.form.get("year"),
              request.form.get("info"), request.form.get("link"))

    db.session().add(s)
    db.session().commit()

    return redirect(url_for("series_index"))


@app.route("/series/modify/<int:serie_id>", methods=["GET"])
def series_modify(serie_id):
    return render_template("series/modify.html",
                           serie=Serie.query.get(serie_id))


@app.route("/series/modify/", methods=["POST"])
def series_modifyid():
    serie_id = request.form.get("id")
    s = Serie.query.get(serie_id)
    s.name = request.form.get("name")
    s.year = request.form.get("year")
    s.info = request.form.get("info")
    s.link = request.form.get("link")

    db.session().commit()

    return redirect(url_for("series_index"))
