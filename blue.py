from flask import Blueprint, render_template



blue_print = Blueprint("blue",__name__,template_folder="templates")


from models import Todo

@blue_print.route('/')
@blue_print.route('/index')
def index():
    todo_list = Todo.query.all()
    print(todo_list)
    return render_template('index.html', todo_list=todo_list)