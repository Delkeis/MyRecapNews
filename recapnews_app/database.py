from flask_sqlalchemy import SQLAlchemy
from .views import app

db = SQLAlchemy(app)

db.create_all()