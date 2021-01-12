from flask import Blueprint, render_template,request,redirect,url_for
import uuid



add_blueprint=Blueprint("add",__name__,template_folder="templates")


from models import Todo
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


@add_blueprint.route('/')
@add_blueprint.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    desc = request.form.get("desc")
    asdate = request.form.get("asdate")
    priority = request.form.get("priority")
    assignto = request.form.get("assignto")
    new_todo = Todo(title=title, complete=False, desc=desc, asdate=asdate, priority=priority, assignto=assignto)
    local_object = db.session.merge(new_todo)
    db.session.add(local_object)

    db.session.commit()
    return redirect(url_for("blue.index"))