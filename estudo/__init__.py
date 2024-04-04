from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.bd'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'a874boan733rb9wfbw83rbfwb983wpibf'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from estudo.views import index
from estudo.models import Contato 
