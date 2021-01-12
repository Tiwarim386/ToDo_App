from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


from flask import Blueprint
#from sqlalchemy.dialects.postgresql import UUID

#import uuid

app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://mohit.tiwari:12345@localhost/finaltodo'

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/[todolist.db]'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
marsh=Marshmallow(app)

from add import add_blueprint
app.register_blueprint(add_blueprint,url_prefix="")

from blue import blue_print
app.register_blueprint(blue_print,url_prefix="")

from update import update_blueprint
app.register_blueprint(update_blueprint,url_prefix="")

from delete import delete_blueprint
app.register_blueprint(delete_blueprint,url_prefix="")









if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)