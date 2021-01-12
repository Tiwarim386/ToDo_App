from flask import Blueprint, render_template,request,redirect,url_for,session




update_blueprint=Blueprint("update",__name__,template_folder="templates")


from models import Todo
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()



@update_blueprint.route("/update/<int:todo_id>")
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    #local_object = db.session.merge(todo)
    #db.session.add(local_object)
    #db.session.save-update()
    db.session.commit()
    return redirect(url_for("blue.index"),code=301)