from flask import Blueprint, render_template,request,redirect,url_for




delete_blueprint=Blueprint("delete",__name__,template_folder="templates")


from models import Todo
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

@delete_blueprint.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    local_object = db.session.merge(todo)
    db.session.delete(local_object)
    db.session.commit()
    return redirect(url_for("blue.index"))