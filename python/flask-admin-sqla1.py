# http://127.0.0.1:8000/admin/
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config.update( SQLALCHEMY_DATABASE_URI = 'sqlite:///' , SECRET_KEY = 's' )
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(128))

if __name__ == '__main__':
    admin = Admin(app)
    admin.add_view(ModelView(User, db.session))
    db.create_all()
    app.run('0.0.0.0', 8000)
